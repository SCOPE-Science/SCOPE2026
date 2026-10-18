#!/usr/bin/env python3
"""Exact finite verification of two rational homology characters for the Nauru independence complex.
Requires Python >=3.9, standard library only. All finite sets are enumerated from definitions.
"""
import collections
import itertools
from collections import deque
from functools import lru_cache

ORDER = (22, 23, 10, 14, 13, 9, 19, 3, 6, 20, 4, 0, 15, 21, 8, 17, 7, 18, 2, 5, 12, 16, 11, 1)
GP_TO_CAYLEY = (0, 6, 12, 18, 4, 10, 16, 22, 3, 9, 15, 21, 14, 19, 2, 7, 17, 20, 5, 8, 13, 23, 1, 11)
EXPECTED_LEFSCHETZ = {
 ((1,1,1,1),(1,1,1)):-3, ((1,1,1,1),(2,1)):5, ((1,1,1,1),(3,)):-3,
 ((2,1,1),(1,1,1)):1, ((2,1,1),(2,1)):-3, ((2,1,1),(3,)):1,
 ((2,2),(1,1,1)):1, ((2,2),(2,1)):1, ((2,2),(3,)):1,
 ((3,1),(1,1,1)):0, ((3,1),(2,1)):2, ((3,1),(3,)):0,
 ((4,),(1,1,1)):-1, ((4,),(2,1)):-1, ((4,),(3,)):-1,
}
# S4 irreducibles: trivial, sign, 3-standard, 3-sign-standard, 2-dimensional.
CHAR4 = {
 (1,1,1,1):(1,1,3,3,2), (2,1,1):(1,-1,1,-1,0),
 (2,2):(1,1,-1,-1,2), (3,1):(1,1,0,0,-1), (4,):(1,-1,-1,1,0),
}
# S3 irreducibles: trivial, sign, 2-standard.
CHAR3 = {(1,1,1):(1,1,2), (2,1):(1,-1,0), (3,):(1,1,-1)}


def graph():
    adj = [0]*24
    edges = set()
    for i in range(12):
        for j in ((i+1)%12, i+12):
            e=tuple(sorted((i,j)));edges.add(e)
        edges.add(tuple(sorted((i+12,(i+5)%12+12))))
    assert len(edges)==36
    for i,j in edges: adj[i]|=1<<j;adj[j]|=1<<i
    assert all(a.bit_count()==3 for a in adj)
    return edges,adj


def independent_faces(adj):
    faces=[0]
    for i in range(24):
        original=tuple(faces)
        faces.extend(f|1<<i for f in original if not f&adj[i])
    assert len(faces)==35219
    assert tuple(collections.Counter(f.bit_count()-1 for f in faces)[k] for k in range(-1,12)) == (
      1,24,240,1304,4212,8328,10036,7176,2964,752,156,24,2)
    return set(faces)


def morse_certificate(faces):
    available=set(faces);up={};pairs=[]
    for v in ORDER:
        choose=[(f,f|(1<<v)) for f in tuple(available)
                if (not f&(1<<v)) and (f|(1<<v)) in available]
        for f,t in choose:
            assert f in available and t in available
            available.remove(f);available.remove(t);up[f]=t;pairs.append((f,t))
    dimensions=collections.Counter(f.bit_count()-1 for f in available)
    assert dimensions=={5:4,6:1},dimensions
    assert len(pairs)==17607 and 0 not in available
    # The directed Hasse graph points down except that matched incidences point up.
    indegree={f:0 for f in faces}
    outgoing={f:[] for f in faces}
    incidence_count=0
    for t in faces:
        bits=t
        while bits:
            lowbit=bits&-bits;bits^=lowbit
            f=t^lowbit
            if up.get(f)==t: src,dst=f,t
            else: src,dst=t,f
            outgoing[src].append(dst); indegree[dst]+=1;incidence_count+=1
    assert incidence_count==205680
    queue=deque(f for f in faces if indegree[f]==0)
    done=0
    while queue:
        f=queue.popleft();done+=1
        for h in outgoing[f]:
            indegree[h]-=1
            if indegree[h]==0:queue.append(h)
    assert done==len(faces),(done,len(faces))
    # Compute the integral Morse boundary C_6 -> C_5 by exact gradient paths.
    upper_matched=set(up.values())
    critical5=sorted(f for f in available if f.bit_count()==6)
    critical6=sorted(f for f in available if f.bit_count()==7)
    assert len(critical5)==4 and len(critical6)==1
    def boundary(t):
        return [(t^(1<<v),(-1)**i) for i,v in enumerate(k for k in range(24) if t>>k&1)]
    pending=set()
    @lru_cache(None)
    def projection(f):
        if f in pending:raise ValueError("closed gradient path")
        if f in available:return {f:1}
        if f in upper_matched:return {}
        assert f in up and up[f].bit_count()==7
        t=up[f]
        bd=dict(boundary(t));pivot=bd[f]
        assert abs(pivot)==1
        pending.add(f)
        result={}
        for other,coeff in bd.items():
            if other==f:continue
            for c,value in projection(other).items():
                result[c]=result.get(c,0)-coeff*value//pivot
        pending.remove(f)
        return {k:v for k,v in result.items() if v}
    morse_columns=[]
    for t in critical6:
        result={}
        for f,coeff in boundary(t):
            for c,value in projection(f).items():
                result[c]=result.get(c,0)+coeff*value
        morse_columns.append(tuple(result.get(c,0) for c in critical5))
    assert morse_columns==[(0,0,0,0)],morse_columns
    # All integral Morse differentials vanish: C_5=Z^4 and C_6=Z.
    return dimensions


def mul(a,b):
    return tuple(a[b[i]] for i in range(4))


def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def cycle_type(p):
    seen=set();result=[]
    for i in range(len(p)):
        if i in seen:continue
        x=i;k=0
        while x not in seen:
            seen.add(x);k+=1;x=p[x]
        result.append(k)
    return tuple(sorted(result,reverse=True))


def cayley_action(gp_edges):
    perms=list(itertools.permutations(range(4)))
    idx={p:i for i,p in enumerate(perms)}
    trans=[]
    for i in (1,2,3):
        s=list(range(4));s[0],s[i]=s[i],s[0];trans.append(tuple(s))
    star_edges=set()
    for p in perms:
        for s in trans:
            a=idx[p];b=idx[mul(p,s)]
            star_edges.add(tuple(sorted((a,b))))
    assert len(star_edges)==36
    permuted_gp={tuple(sorted((GP_TO_CAYLEY[a],GP_TO_CAYLEY[b]))) for a,b in gp_edges}
    assert permuted_gp==star_edges
    # Full group: S4 acts on the left and the S3 fixing 0 acts on the right.
    group=[]
    for a in perms:
        for b in (p for p in perms if p[0]==0):
            action=tuple(idx[mul(mul(a,p),inverse(b))] for p in perms)
            assert {tuple(sorted((action[x],action[y]))) for x,y in star_edges}==star_edges
            bsmall=tuple(b[i]-1 for i in range(1,4))
            group.append((cycle_type(a),cycle_type(bsmall),action))
    assert len(group)==len(set(p for _,_,p in group))==144
    # The pointwise stabilizer of one vertex and its three neighbors is trivial:
    # distinguish these four vertices, then repeatedly refine by neighboring colors.
    neighbors=[set() for _ in range(24)]
    for x,y in star_edges:neighbors[x].add(y);neighbors[y].add(x)
    root=idx[(0,1,2,3)]
    colors=[0]*24;colors[root]=1
    for number,v in enumerate(sorted(neighbors[root]),2):colors[v]=number
    refinement_counts=[]
    for _ in range(5):
        signature=[(colors[v],tuple(sorted(colors[u] for u in neighbors[v]))) for v in range(24)]
        palette={c:i for i,c in enumerate(sorted(set(signature)))}
        colors=[palette[s] for s in signature]
        refinement_counts.append(len(set(colors)))
    assert refinement_counts==[8,14,20,23,24]
    assert len(set(colors))==24
    # Hence a rooted-neighborhood pointwise stabilizer is trivial.
    # Since every vertex image has at most 3! neighbor images, |Aut| <=24*6=144.
    return star_edges,group


def fixed_lefschetz(action,adj):
    # All invariant independent sets are unions of full vertex-permutation cycles.
    # A union of k selected cycles contributes (-1)^(k-1), including the empty set.
    seen=set();eligible=[]
    for i in range(24):
        if i in seen:continue
        cyc=[];j=i
        while j not in seen:
            seen.add(j);cyc.append(j);j=action[j]
        bits=sum(1<<v for v in cyc)
        if all(not adj[v]&bits for v in cyc):eligible.append(bits)
    choices=[(0,1)]
    for cyc in eligible:
        choices.extend((mask|cyc,-coeff) for mask,coeff in list(choices)
                       if all(not adj[v]&mask for v in range(24) if cyc>>v&1))
    return -sum(coeff for _,coeff in choices)


def direct_lefschetz(action,faces):
    out=0
    for face in faces:
        vertices=[i for i in range(24) if face>>i&1]
        targets=[action[v] for v in vertices]
        if sum(1<<v for v in targets)!=face:continue
        inv=sum(targets[i]>targets[j] for i in range(len(targets)) for j in range(i+1,len(targets)))
        out+=(-1 if ((len(vertices)-1+inv)%2) else 1)
    return out


def character_checks(group,adj,faces):
    # Validate the small symmetric-group character tables and their completeness.
    for degree,chars in ((4,CHAR4),(3,CHAR3)):
        permutations=list(itertools.permutations(range(degree)))
        n_irr=len(next(iter(chars.values())))
        sizes=collections.Counter(cycle_type(p) for p in permutations)
        assert set(sizes)==set(chars)
        for i,j in itertools.product(range(n_irr),repeat=2):
            scalar=sum(sizes[k]*chars[k][i]*chars[k][j] for k in sizes)
            assert scalar==(len(permutations) if i==j else 0)
        identity=tuple([1]*degree)
        assert sum(d*d for d in chars[identity])==len(permutations)
    table=collections.defaultdict(list)
    representative={}
    for a,b,action in group:
        val=fixed_lefschetz(action,adj)
        table[(a,b)].append(val);representative.setdefault((a,b),action)
    assert len(table)==15
    for key,values in table.items():
        assert len(set(values))==1
        assert values[0]==EXPECTED_LEFSCHETZ[key]
        assert direct_lefschetz(representative[key],faces)==values[0]
    assert sum(len(v) for v in table.values())==144
    multiplicities={}
    for candidate4,candidate3 in itertools.product(range(2),repeat=2):
        co={}
        for i,j in itertools.product(range(5),range(3)):
            numerator=sum(len(vals)*(
                CHAR4[a][candidate4]*CHAR3[b][candidate3]-vals[0]
                )*CHAR4[a][i]*CHAR3[b][j] for (a,b),vals in table.items())
            assert numerator%144==0
            co[(i,j)]=numerator//144
        multiplicities[(candidate4,candidate3)]=co
    assert [(a,b) for (a,b),coeffs in multiplicities.items()
            if all(v>=0 for v in coeffs.values())]==[(1,0)]
    assert {key:val for key,val in multiplicities[(1,0)].items() if val} == {(1,1):1,(3,1):1}
    # H6 is sign(S4) tensor trivial(S3); H5 is sign(S4)sign(S3) tensor Perm4.
    for (a,b),vals in table.items():
        sign4=CHAR4[a][1];sign3=CHAR3[b][1]
        h6=sign4
        h5=sign4*sign3*(1+CHAR4[a][2])
        assert h6-h5==vals[0]
    return {str(k):(len(v),v[0]) for k,v in sorted(table.items())}


def main():
    gp_edges,gp_adj=graph()
    faces=independent_faces(gp_adj)
    critical=morse_certificate(faces)
    star_edges,group=cayley_action(gp_edges)
    star_adj=[0]*24
    for i,j in star_edges:star_adj[i]|=1<<j;star_adj[j]|=1<<i
    cayley_faces={sum(1<<GP_TO_CAYLEY[v] for v in range(24) if f>>v&1) for f in faces}
    table=character_checks(group,star_adj,cayley_faces)
    print('NAURU_EQUIVARIANT_VERIFY_OK', 'faces',len(faces),'matched',17607,
          'critical',dict(critical),'automorphisms',len(group),'classes',len(table))
    for x,y in table.items():print(x,y)

if __name__=='__main__':main()
