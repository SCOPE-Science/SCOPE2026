#!/usr/bin/env python3
from collections import deque, Counter
from itertools import combinations

G6 = [
    "K?ABE`Ke@WEO",
    "K?ABCfCU@WF?",
    "K?ABAdgi?wQ_",
    "K?AB?tos@WP_",
    "K?`@EaKX?sEO",
]
EXPECTED = [
    {
        "diameter": 3,
        "orders": {1:list(range(12)),2:list(range(12)),3:list(range(12))},
        "r": {
            1:{"faces":31,"fvec":[12,18,1],"hasse":39,"pairs":12,"critical":{0:1,1:6}},
            2:{"faces":189,"fvec":[12,47,73,45,11,1],"hasse":554,"pairs":93,"critical":{0:1,2:2}},
            3:{"faces":4095,"fvec":[12,66,220,495,792,924,792,495,220,66,12,1],"hasse":24564,"pairs":2047,"critical":{0:1}},
        },
    },
    {
        "diameter": 4,
        "orders": {1:list(range(12)),2:list(range(12)),3:list(range(12))},
        "r": {
            1:{"faces":31,"fvec":[12,18,1],"hasse":39,"pairs":12,"critical":{0:1,1:6}},
            2:{"faces":186,"fvec":[12,47,74,45,8],"hasse":536,"pairs":92,"critical":{0:1,2:1}},
            3:{"faces":3071,"fvec":[12,65,210,450,672,714,540,285,100,21,2],"hasse":17396,"pairs":1535,"critical":{0:1}},
        },
    },
    {
        "diameter": 4,
        "orders": {1:list(reversed(range(12))),2:list(range(12)),3:list(range(12))},
        "r": {
            1:{"faces":32,"fvec":[12,18,2],"hasse":42,"pairs":13,"critical":{0:1,1:5}},
            2:{"faces":142,"fvec":[12,42,55,28,5],"hasse":386,"pairs":70,"critical":{0:1,2:1}},
            3:{"faces":1535,"fvec":[12,62,182,336,406,322,162,47,6],"hasse":7540,"pairs":767,"critical":{0:1}},
        },
    },
    {
        "diameter": 4,
        "orders": {1:list(range(12)),2:list(range(12)),3:list(range(12))},
        "r": {
            1:{"faces":31,"fvec":[12,18,1],"hasse":39,"pairs":12,"critical":{0:1,1:6}},
            2:{"faces":186,"fvec":[12,45,67,45,15,2],"hasse":558,"pairs":92,"critical":{0:1,2:1}},
            3:{"faces":3071,"fvec":[12,65,210,450,672,714,540,285,100,21,2],"hasse":17396,"pairs":1535,"critical":{0:1}},
        },
    },
    {
        "diameter": 4,
        "orders": {1:list(range(12)),2:list(range(12)),3:list(range(12))},
        "r": {
            1:{"faces":33,"fvec":[12,18,3],"hasse":45,"pairs":14,"critical":{0:1,1:4}},
            2:{"faces":150,"fvec":[12,43,58,31,6],"hasse":414,"pairs":74,"critical":{0:1,2:1}},
            3:{"faces":2303,"fvec":[12,64,200,406,560,532,344,145,36,4],"hasse":12276,"pairs":1151,"critical":{0:1}},
        },
    },
]

def decode_graph6(s):
    vals=[ord(c)-63 for c in s]
    if not (0 <= vals[0] <= 62):
        raise ValueError("only short graph6 headers are supported")
    n=vals[0]
    bits=[]
    for x in vals[1:]:
        bits.extend((x>>k)&1 for k in (5,4,3,2,1,0))
    A=[set() for _ in range(n)]
    p=0
    for j in range(1,n):
        for i in range(j):
            if bits[p]:
                A[i].add(j); A[j].add(i)
            p+=1
    return A

def connected(A):
    q=[0]; seen={0}
    while q:
        v=q.pop()
        for w in A[v]:
            if w not in seen:
                seen.add(w); q.append(w)
    return len(seen)==len(A)

def distances(A):
    n=len(A); D=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; q=deque([s])
        while q:
            v=q.popleft()
            for w in A[v]:
                if d[w]<0:
                    d[w]=d[v]+1; q.append(w)
        D.append(d)
    return D

def hamiltonian_cycle(A):
    n=len(A); path=[0]; used={0}
    def rec(v):
        if len(path)==n:
            return 0 in A[v]
        for w in sorted(A[v]):
            if w not in used:
                used.add(w); path.append(w)
                if rec(w): return True
                path.pop(); used.remove(w)
        return False
    if rec(0): return path+[0]
    return None

def iso_count(A,B,stop_after=None):
    n=len(A)
    if len(B)!=n or sorted(map(len,A))!=sorted(map(len,B)): return 0
    degA=[len(x) for x in A]; degB=[len(x) for x in B]
    mapping={}; used=set(); count=0
    def choose_u():
        U=[u for u in range(n) if u not in mapping]
        return max(U,key=lambda u:(sum(v in mapping for v in A[u]),degA[u],-u))
    def rec():
        nonlocal count
        if len(mapping)==n:
            count+=1; return stop_after is not None and count>=stop_after
        u=choose_u()
        for v in range(n):
            if v in used or degB[v]!=degA[u]: continue
            ok=True
            for u2,v2 in mapping.items():
                if ((u2 in A[u]) != (v2 in B[v])):
                    ok=False; break
            if not ok: continue
            mapping[u]=v; used.add(v)
            if rec(): return True
            used.remove(v); del mapping[u]
        return False
    rec(); return count

def rips_faces(D,r):
    n=len(D); out=[]
    for m in range(1,1<<n):
        verts=[i for i in range(n) if (m>>i)&1]
        good=True
        for a,b in combinations(verts,2):
            if D[a][b]>r:
                good=False; break
        if good: out.append(m)
    return out

def f_vector(faces):
    c=Counter(m.bit_count() for m in faces)
    return [c[k] for k in range(1,max(c)+1)]

def staged_toggle_matching(faces,order):
    U=set(faces); pairs=[]
    for v in order:
        b=1<<v
        lows=sorted(m for m in U if not (m&b) and (m|b) in U)
        for lo in lows:
            hi=lo|b
            if lo in U and hi in U:
                pairs.append((lo,hi)); U.remove(lo); U.remove(hi)
    return pairs,sorted(U)

def critical_by_dim(crit):
    c=Counter(m.bit_count()-1 for m in crit)
    return dict(sorted(c.items()))

def hasse_and_acyclic(faces,pairs):
    F=set(faces); P=set(pairs)
    indeg={m:0 for m in F}; out={m:[] for m in F}; covers=0
    for hi in F:
        t=hi
        while t:
            b=t & -t; t-=b; lo=hi^b
            if lo==0 or lo not in F: continue
            covers+=1
            # Forman orientation: matched cover low -> high; unmatched high -> low.
            a,z=(lo,hi) if (lo,hi) in P else (hi,lo)
            out[a].append(z); indeg[z]+=1
    q=deque([m for m,d in indeg.items() if d==0]); seen=0
    while q:
        x=q.popleft(); seen+=1
        for y in out[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    return covers, seen==len(F)

graphs=[decode_graph6(s) for s in G6]
for i,A in enumerate(graphs):
    assert len(A)==12
    assert connected(A)
    assert all(len(x)==3 for x in A)
    assert sum(map(len,A))//2==18
    cyc=hamiltonian_cycle(A); assert cyc is not None
    assert iso_count(A,A)==1, (i,"not asymmetric")
    D=distances(A); diam=max(map(max,D)); assert diam==EXPECTED[i]["diameter"]
    for j in range(i): assert iso_count(A,graphs[j],stop_after=1)==0
    for r in (1,2,3):
        faces=rips_faces(D,r); ex=EXPECTED[i]["r"][r]
        assert len(faces)==ex["faces"]
        assert f_vector(faces)==ex["fvec"]
        pairs,crit=staged_toggle_matching(faces,EXPECTED[i]["orders"][r])
        assert len(pairs)==ex["pairs"]
        assert critical_by_dim(crit)==ex["critical"]
        covers,acyc=hasse_and_acyclic(faces,pairs)
        assert covers==ex["hasse"] and acyc
        for lo,hi in pairs:
            assert lo in faces and hi in faces
            assert lo.bit_count()+1==hi.bit_count()
            assert lo & hi == lo
    print(f"G{i+1} {G6[i]}: diameter={diam}; Hamiltonian_cycle={cyc}")
    for r in (1,2,3):
        ex=EXPECTED[i]["r"][r]
        print(f"  r={r}: faces={ex['faces']} f={ex['fvec']} covers={ex['hasse']} pairs={ex['pairs']} critical={ex['critical']}")
print("all five graphs are pairwise nonisomorphic, cubic, Hamiltonian, and asymmetric")
print("all stated Rips Morse certificates are exhaustive and acyclic")
print("VERIFY_OK")
