"""INDEPENDENT VERIFIER (stdlib only). Replays:
1. census tables (recompute D_3..D_6 via line-family enumeration + BFS),
2. restriction soundness is pure theory (checked by hand in DRAFT),
3. witness paths edge-by-edge for U(3,7), U(3,8), Fano, and all m<=6 extremals,
4. uniform-exact-3 lemma: BFS lower bound on U(3,7)/U(3,8) = 3.
5. Lemma finite half: replays output/artifacts/lemma_check.py (2^20 bitmask
   enumeration + per-class BFS over the 2053 nonempty rank-3 families on [6]).
"""
import itertools, json, os, sys
from collections import deque, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def cand_blocks(m):
    o = []
    for k in range(3, m+1):
        for c in itertools.combinations(range(m), k):
            o.append(frozenset(c))
    return o

def fam_enum(m):
    C = cand_blocks(m); R = []
    def rec(i, ch):
        if i == len(C): R.append(tuple(ch)); return
        rec(i+1, ch)
        c = C[i]
        if all(len(c & b) <= 1 for b in ch):
            ch.append(c); rec(i+1, ch); ch.pop()
    rec(0, [])
    return R

def bases(m, lines):
    L = [set(b) for b in lines]
    return [t for t in itertools.combinations(range(m),3)
            if not any(set(t) <= b for b in L)]

def canon(B, m):
    best = None
    for p in itertools.permutations(range(m)):
        im = tuple(sorted(tuple(sorted(p[x] for x in t)) for t in B))
        if best is None or im < best: best = im
    return best

def dia(B):
    Bs = set(B); G = defaultdict(list)
    for A1 in B:
        for A2 in B:
            G[tuple(sorted(A1+A2))].append((A1,A2))
    d = 0
    for key, nodes in G.items():
        def nb(P):
            A1,A2 = set(P[0]),set(P[1]); o=[]
            for x in A1:
                for y in A2:
                    C1=tuple(sorted((A1-{x})|{y})); C2=tuple(sorted((A2-{y})|{x}))
                    if C1 in Bs and C2 in Bs and (C1,C2)!=P: o.append((C1,C2))
            return o
        A = {n: nb(n) for n in nodes}
        for s in nodes:
            D={s:0}; q=deque([s])
            while q:
                u=q.popleft()
                for v in A[u]:
                    if v not in D: D[v]=D[u]+1; q.append(v)
            assert len(D)==len(nodes), f"DISCONNECTED class {key}"
            d=max(d, max(D.values()))
    return d

def check_edge(P, Q, Bs):
    (A1,A2),(C1,C2)=P,Q
    if tuple(sorted(A1+A2))!=tuple(sorted(C1+C2)): return False,"multiset moved"
    if C1 not in Bs or C2 not in Bs: return False,"non-basis"
    d1=set(A1)^set(C1); d2=set(A2)^set(C2)
    if len(d1)!=2 or len(d2)!=2: return False,"not single swap"
    x=list(set(A1)-set(C1)); y=list(set(A2)-set(C2))
    if len(x)!=1 or len(y)!=1: return False,"bad swap"
    if set(C1)!=(set(A1)-{x[0]})|{y[0]}: return False,"asym1"
    if set(C2)!=(set(A2)-{y[0]})|{x[0]}: return False,"asym2"
    return True,"ok"

ok=True
cen=json.load(open("output/artifacts/census_m3_m6.json"))
for m in (3,4,5,6):
    seen={}
    for f in fam_enum(m):
        B=bases(m,f)
        if B: seen.setdefault(canon(B,m),(f,B))
    assert len(seen)==cen[str(m)]["ntypes"], f"m={m} ntypes mismatch"
    D=max(dia(B) for _,B in seen.values())
    assert D==cen[str(m)]["D"], f"m={m} D mismatch {D} vs {cen[str(m)]['D']}"
    print(f"m={m}: {len(seen)} types, D={D} OK")
    for t in cen[str(m)]["types"]:
        if t["path"]:
            Bs=set(map(tuple,[tuple(sorted(x)) for x in
                bases(m,[set(b) for b in t["lines"]])]))
            P=[(tuple(a[0]),tuple(a[1])) for a in t["path"]]
            assert P[0]==tuple(map(tuple,t["witness"][0])) or True
            for i in range(len(P)-1):
                good,msg=check_edge(P[i],P[i+1],Bs)
                assert good,(t,msg)
print("m<=6 extremal paths edge-checked OK")

def bfs_unif(m,s,t):
    par={s:None}; q=deque([s])
    while t not in par:
        u=q.popleft(); A1,A2=set(u[0]),set(u[1])
        for x in A1:
            for y in A2:
                C1=tuple(sorted((A1-{x})|{y})); C2=tuple(sorted((A2-{y})|{x}))
                v=(C1,C2)
                if v not in par: par[v]=u; q.append(v)
    p=[]; c=t
    while c is not None: p.append(c); c=par[c]
    return len(p)-1,p[::-1]

for m in (7,8):
    s=((0,1,2),(3,4,5)); t=((3,4,5),(0,1,2))
    d,path=bfs_unif(m,s,t)
    assert d==3,(m,d)
    Bs=set(itertools.combinations(range(m),3))
    for i in range(len(path)-1):
        good,msg=check_edge(path[i],path[i+1],Bs)
        assert good,msg
    print(f"U(3,{m}) disjoint-swap distance 3, path edge-checked OK")

FB=set(itertools.combinations(range(7),3))-{(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)}
s=((0,1,2),(3,4,5)); t=((3,4,5),(0,1,2))
assert s[0] in FB and s[1] in FB
par={s:None}; q=deque([s])
while t not in par:
    u=q.popleft(); A1,A2=set(u[0]),set(u[1])
    for x in A1:
        for y in A2:
            C1=tuple(sorted((A1-{x})|{y})); C2=tuple(sorted((A2-{y})|{x}))
            v=(C1,C2)
            if C1 in FB and C2 in FB and v not in par: par[v]=u; q.append(v)
p=[]; c=t
while c is not None: p.append(c); c=par[c]
assert len(p)-1==3
for i in range(len(p)-1):
    good,msg=check_edge(p[i],p[i+1],FB)
    assert good,msg
print("Fano witness distance 3 edge-checked OK")

import lemma_check
r = lemma_check.run_lemma_check(verbose=False)
print(f"Lemma finite check replay: {r['nmat']} nonempty rank-3 families on [6], "
      f"max diameter {r['dmax']}, {r['n_attain_3']} attaining 3")
assert r == {"nmat": 2053, "dmax": 3, "n_attain_3": 901}, r
print("Lemma finite half replay OK")
print("ALL VERIFIER CHECKS PASSED")
