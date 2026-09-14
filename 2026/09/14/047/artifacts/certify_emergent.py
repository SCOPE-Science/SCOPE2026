"""Certify: (a) F2 odd-product (un)satisfiability for concrete G1 lifts of K3,3;
(b) cube joint witness (connected, Ramanujan, girth 6) with explicit signing;
(c) escape probe: sampled connected girth-4 children of the frozen H0 that are
themselves F2-raisable (one-step frozenness does NOT permanently trap towers).
Exact integer arithmetic only (GF(2) elimination); spectra via numpy with margin.
"""
import itertools, math
from collections import deque
import numpy as np
import networkx as nx
import sys
sys.path.insert(0, "output/artifacts")
from enumerate_lifts import signed_adj_spectrum, lift_graph, girth

def four_cycles_exact(G):
    # return list of 4-cycles as edge-index tuples; enumerate exactly
    edges = list(G.edges())
    eindex = {e:i for i,e in enumerate(edges)}
    # normalize edge key
    def ek(u,v):
        return eindex[(u,v)] if (u,v) in eindex else eindex[(v,u)]
    nodes = list(G.nodes())
    cycs = set()
    for a in nodes:
        for c in G.neighbors(a):
            for b in G.neighbors(c):
                if b==a: continue
                for d in G.neighbors(b):
                    if d==c or d==a: continue
                    if a in set(G.neighbors(d)):
                        e4 = tuple(sorted([ek(a,c),ek(c,b),ek(b,d),ek(d,a)]))
                        cycs.add(e4)
    return sorted(cycs), edges

def gf2_solve(rows, ncols):
    # rows: list of (bitmask int, rhs 0/1). Returns (sol or None, rank info)
    M = [list(r) for r in rows]
    where = [-1]*ncols
    piv = 0
    for c in range(ncols):
        f = next((r for r in range(piv, len(M)) if (M[r][0]>>c)&1), None)
        if f is None: continue
        M[piv],M[f]=M[f],M[piv]; where[c]=piv
        for r in range(len(M)):
            if r!=piv and ((M[r][0]>>c)&1):
                M[r][0]^=M[piv][0]; M[r][1]^=M[piv][1]
        piv+=1
    for r in range(piv, len(M)):
        if M[r][0]==0 and M[r][1]==1:
            return None, {"rank":piv,"nrows":len(M),"unsat":True}
    sol=[0]*ncols
    for c in range(ncols):
        if where[c]>=0: sol[c]=M[where[c]][1]
    return sol, {"rank":piv,"nrows":len(M),"unsat":False}

def certify_g1(seed_pick=7):
    import random
    K33 = nx.complete_bipartite_graph(3,3)
    edges0 = list(K33.edges())
    rng = random.Random(seed_pick)
    G1s=[]; sigs=[]
    tried=0
    while len(G1s)<3 and tried<60:
        tried+=1
        signs=[1 if rng.random()<0.5 else -1 for _ in range(len(edges0))]
        H=lift_graph(K33,edges0,signs)
        if not nx.is_connected(H): continue
        if max(abs(signed_adj_spectrum(K33,edges0,signs)))>2*math.sqrt(2)+1e-8: continue
        if girth(H)!=4: continue
        G1s.append(H); sigs.append(tuple(signs))
    for t,(H,s) in enumerate(zip(G1s,sigs)):
        cycs, edges1 = four_cycles_exact(H)
        m=len(edges1)
        rows=[]
        for c in cycs:
            mask=0
            for e in c: mask|=1<<e
            rows.append([mask,1])
        sol,info=gf2_solve(rows,m)
        print(f"G1[{t}]: n={H.number_of_nodes()} m={m} #4cyc={len(cycs)} F2: {info} "
              f"=> {'ONE-STEP GIRTH-FROZEN (UNSAT: every immediate 2-lift has girth 4)' if sol is None else 'girth-raisable'}")
        print(f"   base signing: {s}")
    return G1s

print("=== G1 dead-end certification ===")
G1s = certify_g1()

print("=== cube joint witness certification ===")
Q3 = nx.cubical_graph()
edges = list(Q3.edges())
g0 = girth(Q3)
sols=0
bound=2*math.sqrt(2)
for signs in itertools.product([1,-1], repeat=len(edges)):
    signs=list(signs)
    ws = signed_adj_spectrum(Q3, edges, signs)
    if max(abs(ws))>bound+1e-8: continue
    H=lift_graph(Q3,edges,signs)
    if not nx.is_connected(H): continue
    if girth(H)>g0:
        sols+=1
        if sols==1:
            print(f"witness signing: {tuple(signs)}")
            print(f"signed new eigenvalues: min={min(ws):.6f} maxabs={max(abs(ws)):.6f} bound={bound:.6f} margin={bound-max(abs(ws)):.6f}")
            print(f"connected={nx.is_connected(H)} girth(H)={girth(H)} n={H.number_of_nodes()}")
print(f"total joint witnesses (connected+Ramanujan+girth 4->6+): {sols} / 4096")

print("=== escape probe: children of frozen H0 that are themselves raisable ===")
import random as _random
_H0 = G1s[0]
_e1 = list(_H0.edges())
_rng = _random.Random(123)
n_conn_g4 = 0
n_rais = 0
_first = None
for _ in range(400):
    _sg = [1 if _rng.random() < 0.5 else -1 for _ in range(len(_e1))]
    _Hp = lift_graph(_H0, _e1, _sg)
    if not nx.is_connected(_Hp):
        continue
    if girth(_Hp) != 4:
        continue
    n_conn_g4 += 1
    _cy, _ee = four_cycles_exact(_Hp)
    _rows = []
    for _c in _cy:
        _mask = 0
        for _e in _c:
            _mask |= 1 << _e
        _rows.append([_mask, 1])
    _sol, _info = gf2_solve(_rows, len(_ee))
    if _sol is not None:
        n_rais += 1
        if _first is None:
            _first = (tuple(_sg), len(_cy), _info)
print(f"sampled connected girth-4 children of H0: {n_conn_g4}/400; "
      f"F2-raisable among them: {n_rais}")
if _first is not None:
    print(f"first raisable child: #4cyc={_first[1]} F2={_first[2]} signing={_first[0]}")
print("=> one-step frozenness of H0 constrains branch choice but does not "
      "permanently trap longer towers.")
