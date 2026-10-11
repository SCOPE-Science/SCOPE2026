#!/usr/bin/env python3
from itertools import product
from collections import Counter, defaultdict, deque
from functools import lru_cache
import hashlib, json

# Three-rung ladder L_3 = P_3 square K_2.
VERTICES=list(range(6))
EDGES=[(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)]
PRIMITIVES=[]
for ei,(u,v) in enumerate(EDGES):
    PRIMITIVES.append((u,v,ei))
    PRIMITIVES.append((v,u,ei))
N=len(PRIMITIVES)
TOGGLE_ORDER=[12,10,3,5,13,4,1,11,6,0,2,9,7,8]
EXPECTED_CRITICAL=[586,677,4096,8468,8530]


def acyclic_arrows(out):
    for start in out:
        x=start; seen=set()
        while x in out:
            if x in seen:
                return False
            seen.add(x); x=out[x]
    return True


def valid_mask(mask):
    tails=set(); used_edges=set(); out={}
    for i,(tail,head,ei) in enumerate(PRIMITIVES):
        if not ((mask>>i)&1):
            continue
        if tail in tails or ei in used_edges:
            return False
        tails.add(tail); used_edges.add(ei); out[tail]=head
    return acyclic_arrows(out)


def enumerate_faces_by_masks():
    faces=set(); counts=Counter()
    for mask in range(1,1<<N):
        if valid_mask(mask):
            faces.add(mask); counts[mask.bit_count()-1]+=1
    return faces,counts


def enumerate_faces_by_edge_states():
    # Independent representation: each undirected graph edge is unused or receives one of two orientations.
    faces=set()
    for states in product((0,1,2),repeat=len(EDGES)):
        tails=set(); out={}; mask=0; ok=True
        for ei,(state,(u,v)) in enumerate(zip(states,EDGES)):
            if state==0: continue
            if state==1: tail,head,pid=u,v,2*ei
            else: tail,head,pid=v,u,2*ei+1
            if tail in tails:
                ok=False; break
            tails.add(tail); out[tail]=head; mask |= 1<<pid
        if ok and mask and acyclic_arrows(out):
            faces.add(mask)
    return faces


def toggle_matching(faces):
    unmatched=set(faces); pairs=[]
    for v in TOGGLE_ORDER:
        bit=1<<v
        lows=sorted((m for m in unmatched if not(m&bit) and (m|bit) in unmatched),
                    key=lambda m:(m.bit_count(),m))
        for low in lows:
            high=low|bit
            if low in unmatched and high in unmatched:
                unmatched.remove(low); unmatched.remove(high)
                pairs.append((low,high,v))
    return pairs,unmatched


def hasse_acyclic(faces,pairs):
    matched={(a,b) for a,b,_ in pairs}
    used=set()
    for a,b,v in pairs:
        assert a in faces and b in faces
        assert b == a | (1<<v)
        assert b.bit_count()==a.bit_count()+1
        assert a not in used and b not in used
        used.add(a); used.add(b)
    indeg={m:0 for m in faces}; adj={m:[] for m in faces}; covers=0
    for high in faces:
        for v in range(N):
            if high&(1<<v):
                low=high^(1<<v)
                if low not in faces: continue
                covers+=1
                if (low,high) in matched:
                    a,b=low,high
                else:
                    a,b=high,low
                adj[a].append(b); indeg[b]+=1
    q=deque(sorted(m for m,d in indeg.items() if d==0)); seen=0
    while q:
        u=q.popleft(); seen+=1
        for w in adj[u]:
            indeg[w]-=1
            if indeg[w]==0: q.append(w)
    return seen==len(faces),covers


def incidence(high,low):
    verts=[i for i in range(N) if (high>>i)&1]
    diff=[v for v in verts if not ((low>>v)&1)]
    assert len(diff)==1 and high.bit_count()==low.bit_count()+1
    return -1 if verts.index(diff[0])%2 else 1


def morse_d4(faces,pairs,critical):
    # Compute the integral Morse differential from critical 4-cells to critical 3-cells.
    # Projection follows gradient paths: a matched 3-cell alpha paired upward with beta is
    # replaced using d(beta)=eps*alpha+sum c_gamma gamma.
    low_to_high={a:b for a,b,_ in pairs if a.bit_count()==4 and b.bit_count()==5}
    crit3=sorted(m for m in critical if m.bit_count()==4)
    crit4=sorted(m for m in critical if m.bit_count()==5)

    visiting=set()
    @lru_cache(None)
    def project3(cell):
        if cell in crit3:
            return ((cell,1),)
        if cell not in low_to_high:
            return tuple()
        if cell in visiting:
            raise AssertionError('gradient cycle in projection')
        visiting.add(cell)
        upper=low_to_high[cell]; eps=incidence(upper,cell)
        out=defaultdict(int)
        for v in range(N):
            if not ((upper>>v)&1): continue
            sub=upper^(1<<v)
            if sub==cell or sub not in faces: continue
            c=incidence(upper,sub)
            for k,a in project3(sub):
                out[k] += -eps*c*a
        visiting.remove(cell)
        return tuple(sorted((k,a) for k,a in out.items() if a))

    matrix=[]
    for top in crit4:
        row={c:0 for c in crit3}
        for v in range(N):
            if not ((top>>v)&1): continue
            sub=top^(1<<v)
            if sub not in faces: continue
            c=incidence(top,sub)
            for k,a in project3(sub): row[k]+=c*a
        matrix.append([row[c] for c in crit3])
    return crit3,crit4,matrix


def rank_mod_p(mat,p):
    if not mat or not mat[0]: return 0
    A=[[x%p for x in row] for row in mat]; m=len(A); n=len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p); A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                a=A[i][c]; A[i]=[(x-a*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r


def homology_mod_p(faces,p):
    bydim=defaultdict(list)
    for m in faces: bydim[m.bit_count()-1].append(m)
    for k in bydim: bydim[k].sort()
    ranks={}
    for k in range(1,max(bydim)+1):
        rows=bydim[k-1]; cols=bydim[k]; ri={m:i for i,m in enumerate(rows)}
        M=[[0]*len(cols) for _ in rows]
        for j,m in enumerate(cols):
            verts=[v for v in range(N) if (m>>v)&1]
            for pos,v in enumerate(verts):
                sub=m^(1<<v); M[ri[sub]][j]=(-1 if pos%2 else 1)%p
        ranks[k]=rank_mod_p(M,p)
    betti=[]
    for k in range(max(bydim)+1):
        betti.append(len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0))
    return betti,ranks


def dominant_pairs():
    nbr={v:set() for v in VERTICES}
    for u,v in EDGES: nbr[u].add(v); nbr[v].add(u)
    ans=[]; V=set(VERTICES)
    for u,v in EDGES:
        if nbr[u]|nbr[v] != V: continue
        A=nbr[u]-nbr[v]; B=nbr[v]-nbr[u]
        if all(y in nbr[x] for x in A for y in B): ans.append((u,v))
    return ans


def mask_info(m):
    return [{"primitive_index":i,"tail":PRIMITIVES[i][0],"head":PRIMITIVES[i][1],
             "edge":list(EDGES[PRIMITIVES[i][2]])}
            for i in range(N) if (m>>i)&1]


def main():
    faces,counts=enumerate_faces_by_masks()
    independent=enumerate_faces_by_edge_states()
    assert faces==independent
    fvec=[counts[k] for k in range(max(counts)+1)]
    assert len(faces)==575
    assert fvec==[14,74,184,213,90],fvec
    assert sum(((-1)**i)*x for i,x in enumerate(fvec))==1

    pairs,critical=toggle_matching(faces)
    assert len(pairs)==285
    assert sorted(critical)==EXPECTED_CRITICAL
    profile=Counter(m.bit_count()-1 for m in critical)
    assert profile==Counter({0:1,3:2,4:2}),profile
    ok,covers=hasse_acyclic(faces,pairs)
    assert ok and covers==2002,(ok,covers)

    crit3,crit4,d4=morse_d4(faces,pairs,critical)
    assert d4==[[0,0],[0,0]],d4

    modp={}
    for p in (2,3,5):
        b,r=homology_mod_p(faces,p)
        assert b==[1,0,0,2,2],(p,b,r)
        modp[str(p)]={"betti":b,"boundary_ranks":{str(k):r[k] for k in sorted(r)}}

    dom=dominant_pairs(); assert dom==[]
    serial=[{"low":a,"high":b,"toggle":v} for a,b,v in sorted(pairs)]
    cert={
      "graph":{"name":"three-rung ladder","vertices":VERTICES,"edges":[list(e) for e in EDGES]},
      "primitive_vector_fields":[{"index":i,"tail":a,"head":b,"edge":list(EDGES[ei])}
                                  for i,(a,b,ei) in enumerate(PRIMITIVES)],
      "independent_enumerations_agree":True,
      "nonempty_face_count":len(faces),"f_vector":fvec,"euler_characteristic":1,
      "hasse_cover_count":covers,"toggle_order":TOGGLE_ORDER,
      "matching_pair_count":len(pairs),"matching_pairs":serial,
      "critical_faces":[{"mask":m,"dimension":m.bit_count()-1,"primitives":mask_info(m)}
                        for m in sorted(critical)],
      "critical_profile":{"0":1,"3":2,"4":2},
      "critical_3_masks":crit3,"critical_4_masks":crit4,
      "integral_morse_boundary_d4":d4,
      "homology_mod_p":modp,
      "symmetric_digraph_dominant_pairs":[],
      "matching_sha256":hashlib.sha256(json.dumps(serial,separators=(',',':'),sort_keys=True).encode()).hexdigest()
    }
    with open('/mnt/data/ladder_morse_certificate.json','w',encoding='utf-8') as f:
        json.dump(cert,f,ensure_ascii=False,indent=2,sort_keys=True); f.write('\n')
    print('LADDER_MORSE_VERIFY_OK')
    print('nonempty_faces',len(faces))
    print('f_vector',fvec)
    print('hasse_covers',covers)
    print('matching_pairs',len(pairs))
    print('critical_profile',dict(sorted(profile.items())))
    print('critical_masks',sorted(critical))
    print('integral_morse_boundary_d4',d4)
    for p in (2,3,5): print('betti_F'+str(p),modp[str(p)]['betti'])
    print('symmetric_digraph_dominant_pairs',dom)
    print('matching_sha256',cert['matching_sha256'])

if __name__=='__main__': main()
