#!/usr/bin/env python3
import itertools, json, sys
from collections import Counter, deque


def pair_data(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return pairs,{p:k for k,p in enumerate(pairs)}


def permute_mask(mask, perm, pairs, pindex):
    out=0
    for k,(i,j) in enumerate(pairs):
        a,b=(i,j) if ((mask>>k)&1) else (j,i)
        a2,b2=perm[a],perm[b]
        lo,hi=(a2,b2) if a2<b2 else (b2,a2)
        kk=pindex[(lo,hi)]
        if a2==lo:
            out |= 1<<kk
    return out


def orbit_representatives(n):
    pairs,pindex=pair_data(n)
    perms=list(itertools.permutations(range(n)))
    seen=set(); rows=[]
    for mask in range(1<<len(pairs)):
        if mask in seen:
            continue
        orb={permute_mask(mask,p,pairs,pindex) for p in perms}
        rep=min(orb)
        if rep != mask:
            raise AssertionError('first unseen mask was not canonical minimum')
        seen.update(orb)
        aut=len(perms)//len(orb)
        rows.append((rep,len(orb),aut))
    return rows,pairs,perms


def out_neighbors(mask,n,pairs):
    outs=[set() for _ in range(n)]
    indeg=[0]*n
    for k,(i,j) in enumerate(pairs):
        if (mask>>k)&1:
            outs[i].add(j); indeg[j]+=1
        else:
            outs[j].add(i); indeg[i]+=1
    return outs,indeg


def neighborhood_faces(mask,n,pairs):
    outs,indeg=out_neighbors(mask,n,pairs)
    faces=set()
    for O in outs:
        L=sorted(O)
        for r in range(1,len(L)+1):
            faces.update(itertools.combinations(L,r))
    # Definition 4.1 vertex set is indegree-positive vertices; this is automatic here:
    used={v for f in faces for v in f}
    assert used == {v for v,d in enumerate(indeg) if d>0}
    return faces,outs


def components(faces):
    verts=sorted({v for f in faces for v in f})
    adj={v:set() for v in verts}
    for f in faces:
        for a,b in itertools.combinations(f,2):
            adj[a].add(b); adj[b].add(a)
    comps=[]; seen=set()
    for s in verts:
        if s in seen: continue
        q=[s]; seen.add(s); c=[]
        while q:
            v=q.pop(); c.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w); q.append(w)
        comps.append(tuple(sorted(c)))
    return tuple(sorted(comps))


def lex_matching(faces,order):
    unmatched=set(faces); pairs=[]
    for v in order:
        for f in sorted([x for x in unmatched if v not in x],key=lambda x:(len(x),x)):
            up=tuple(sorted(f+(v,)))
            if f in unmatched and up in unmatched and up in faces:
                unmatched.remove(f); unmatched.remove(up); pairs.append((f,up))
    return pairs,unmatched


def verify_acyclic(faces,matching):
    # Hasse orientation: unmatched cover arrows from higher to lower; matched cover reversed.
    matched={(lo,hi) for lo,hi in matching}
    succ={f:[] for f in faces}; indeg={f:0 for f in faces}
    for hi in faces:
        if len(hi)<=1: continue
        for k in range(len(hi)):
            lo=hi[:k]+hi[k+1:]
            if lo not in faces: continue
            if (lo,hi) in matched:
                a,b=lo,hi
            else:
                a,b=hi,lo
            succ[a].append(b); indeg[b]+=1
    q=deque([f for f,d in indeg.items() if d==0]); count=0
    while q:
        a=q.popleft(); count+=1
        for b in succ[a]:
            indeg[b]-=1
            if indeg[b]==0:q.append(b)
    return count==len(faces)


def find_certificate(faces,n):
    comps=components(faces); c=len(comps)
    for order in itertools.permutations(range(n)):
        matching,crit=lex_matching(faces,order)
        if any(len(f)>2 for f in crit):
            continue
        c0=sum(len(f)==1 for f in crit); c1=sum(len(f)==2 for f in crit)
        if c0!=c:
            continue
        if not verify_acyclic(faces,matching):
            raise AssertionError('stagewise matching unexpectedly cyclic')
        # Critical edges must lie in a component with its unique critical vertex.
        return order,matching,crit,c0,c1
    raise AssertionError('no graph-dimensional matching found')


def homotopy_label(c0,c1):
    if c0==1:
        if c1==0:return 'point'
        if c1==1:return 'S1'
        return f'wedge_{c1}_S1'
    if c0==2 and c1==0:return 'two_points'
    if c0==2 and c1==1:return 'S1_disjoint_point'
    return f'graph_components_{c0}_cycle_rank_{c1}'


def census(n):
    orbits,pairs,perms=orbit_representatives(n)
    rows=[]
    for rep,orb,aut in orbits:
        faces,outs=neighborhood_faces(rep,n,pairs)
        order,matching,crit,c0,c1=find_certificate(faces,n)
        deg=sorted((len(x) for x in outs),reverse=True)
        rows.append({
            'canonical_mask':rep,
            'orbit_size':orb,
            'automorphism_group_order':aut,
            'outdegree_sequence':deg,
            'face_count':len(faces),
            'morse_vertex_order':list(order),
            'critical_vertices':[list(f) for f in sorted(x for x in crit if len(x)==1)],
            'critical_edges':[list(f) for f in sorted(x for x in crit if len(x)==2)],
            'homotopy_type':homotopy_label(c0,c1)
        })
    return rows


def main():
    rows6=census(6)
    assert len(rows6)==56
    assert sum(r['orbit_size'] for r in rows6)==32768
    distribution=Counter(r['homotopy_type'] for r in rows6)
    expected={
      'point':34,'S1':11,'wedge_2_S1':4,'wedge_3_S1':2,
      'wedge_4_S1':1,'two_points':3,'S1_disjoint_point':1
    }
    assert dict(distribution)==expected, (distribution,expected)
    maxrows=[r for r in rows6 if len(r['critical_edges'])==4 and len(r['critical_vertices'])==1]
    assert len(maxrows)==1
    m=maxrows[0]
    assert m['canonical_mask']==1332
    assert m['outdegree_sequence']==[3,3,3,2,2,2]
    assert m['automorphism_group_order']==3 and m['orbit_size']==240
    # Adjacency of the unique beta_1=4 representative, in 0-based labels.
    pairs,_=pair_data(6)
    _,outs=neighborhood_faces(1332,6,pairs)
    expected_out=[{3,5},{0,2,5},{0,4},{1,2},{0,1,3},{2,3,4}]
    assert outs==expected_out

    # Independent regression against the published 5-vertex Table 1 homology ranks.
    rows5=census(5)
    assert len(rows5)==12 and sum(r['orbit_size'] for r in rows5)==1024
    d5=Counter((len(r['critical_vertices'])-1,len(r['critical_edges'])) for r in rows5)
    assert d5==Counter({(0,0):8,(0,1):2,(1,0):1,(1,2):1})

    if len(sys.argv)>1:
        with open(sys.argv[1],encoding='utf-8') as fh:
            archived=json.load(fh)
        assert archived['schema_version']==1
        assert archived['n']==6
        assert archived['distribution']==expected
        assert archived['rows']==rows6
    print('T6_ISOMORPHISM_CLASSES=56')
    print('T6_DISTRIBUTION='+json.dumps(expected,sort_keys=True))
    print('UNIQUE_MAX_BETA1_MASK=1332')
    print('UNIQUE_MAX_BETA1=4')
    print('T5_TABLE1_REGRESSION=OK')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
