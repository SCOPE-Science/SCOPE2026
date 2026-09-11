"""Enumerate planar Brugalle-Mikhalkin floor diagrams for F2 (n=2), genus 0,
classes aB+bF with a=2 floors. Conventions: arXiv:0812.3354 Def 3.1-3.8.

Polygon Delta_{2,a,b}: vertices (0,0),(2a+b,0),(b,a),(0,a).
  d_- = 2a+b (bottom, weight-1 incoming leaves)
  d_+ = b (top, weight-1 outgoing leaves)
  dl = {0^a}, dr = {2^a}: every floor vertex has div=2.
Genus 0 => floor-adjacency tree: exactly a-1=1 internal elevator.
s = Card(partial Delta)+g-1 = 4a+2b-1 (g=0).

Diagram data for a=2: (L1,L2,U1,U2,x):
  L1+L2 = 2a+b, U1+U2 = b, x>=1 internal weight,
  L1-U1-x = 2, L2+x-U2 = 2.
Markings: linear extensions of poset modulo leaf permutations.
Multiplicities: mu_C = prod w^2; mu_r^R per Def 3.8.
  Note: all floor divs = 2 (even) => o_r = 0 always => sign +1.
"""
import itertools
from functools import lru_cache

def diagrams_F2(a, b):
    n = 2
    dm = n*a + b
    dp = b
    out = []
    # distributions: L1 in 0..dm, U1 in 0..dp, x>=1
    for L1 in range(dm+1):
        for U1 in range(dp+1):
            for x in range(1, 2*a+b+2):
                L2 = dm - L1
                U2 = dp - U1
                if L1 - U1 - x == 2 and L2 + x - U2 == 2:
                    out.append((L1, L2, U1, U2, x))
    return out

def count_markings(L1, L2, U1, U2):
    """Count inequivalent markings = linear extensions / leaf symmetries.
    Poset elements:
      VL, VU vertices; e internal (VL<e<VU);
      dL[i] < VL; dU[j] < VU; VL? vs dU: incomparable; VU vs dL: incomparable except via VU>VL.
      Actually VL<VU (via e). dL[i]<VL<VU, so dL[i]<VU too. dU[j]<VU, incomparable with VL,e.
      uL[k] > VL, incomparable with VU,e? uL[k]>VL; VL<e<VU so uL vs e,VU incomparable.
      uU[l] > VU.
    Brute force topological sorts over distinguishable leaves, then divide by factorials.
    For small sizes only.
    """
    import math
    # build element list
    els = ['VL', 'VU', 'e']
    dL = [f'dL{i}' for i in range(L1)]
    dU = [f'dU{i}' for i in range(L2)]
    uL = [f'uL{i}' for i in range(U1)]
    uU = [f'uU{i}' for i in range(U2)]
    els += dL + dU + uL + uU
    idx = {e: i for i, e in enumerate(els)}
    # predecessors
    pred = {e: set() for e in els}
    def add(a, b):  # a < b
        pred[b].add(a)
    add('VL', 'VU')  # via e path, but add direct too (transitive ok)
    add('VL', 'e'); add('e', 'VU')
    for d in dL: add(d, 'VL')
    for d in dU: add(d, 'VU')
    for u in uL: add('VL', u)
    for u in uU: add('VU', u)
    N = len(els)
    # backtrack count linear extensions
    count = 0
    # use iterative DFS with bitmask (N<=11 ok: 2^11 states)
    from functools import lru_cache
    predmask = {}
    for e in els:
        m = 0
        for p in pred[e]:
            m |= 1 << idx[p]
        predmask[e] = m
    order = els
    @lru_cache(maxsize=None)
    def dp(mask):
        # mask = set of placed elements
        if mask == (1 << N) - 1:
            return 1
        t = 0
        for e in order:
            i = idx[e]
            if mask >> i & 1: continue
            if predmask[e] & ~mask == 0:
                t += dp(mask | (1 << i))
        return t
    total = dp(0)
    sym = math.factorial(L1)*math.factorial(L2)*math.factorial(U1)*math.factorial(U2)
    assert total % sym == 0, (total, sym)
    return total, total//sym

def all_diagrams(a, b):
    res = []
    for (L1, L2, U1, U2, x) in diagrams_F2(a, b):
        tot, ineq = count_markings(L1, L2, U1, U2)
        muC = x*x  # only internal edge has weight>1 possibly
        # r=0 real: 1 iff all weights odd
        mu0 = 1 if (x % 2 == 1) else 0
        res.append(dict(L1=L1, L2=L2, U1=U1, U2=U2, x=x,
                        lin_ext=tot, markings=ineq, muC=muC, mu0=mu0,
                        complex_total=ineq*muC, real0_total=ineq*mu0))
    return res

for (a,b) in [(2,0),(2,1),(2,2),(1,0),(1,1),(1,2)]:
    print(f"=== F2 class a={a}, b={b} ===")
    if a == 2:
        res = all_diagrams(a,b)
        ct = sum(r['complex_total'] for r in res)
        rt = sum(r['real0_total'] for r in res)
        for r in res:
            print(r)
        print(f"TOTAL complex N={ct}, real W(r=0)={rt}")
    else:
        # a=1: single floor, d_-=2+b, d_+=b, s=4+2b-1
        dm = 2*a+b; dp=b; s=4*a+2*b-1
        print(f"single floor: dm={dm} dp={dp} s={s} edges={dm+dp} vert=1 tot={1+dm+dp} (should equal s)")
        print("muC=1 mu0=1 markings=1(up to leaf sym) => N=1 W=1")
    print()
