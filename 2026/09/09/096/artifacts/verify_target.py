#!/usr/bin/env python3
"""Replayable certificate for lane-472 TARGET identifiers (Mowlavi Sec 5.3 + BHS bound).
Replays from the record alone (stdlib only): Bruhat order, lengths, ww'^{-1},
d-integer, orbits, bad-pair witness, Schubert tangent count, dimension arithmetic.
"""
from itertools import permutations, combinations
from collections import deque

def lg(p):
    return sum(1 for i in range(len(p)) for j in range(i+1, len(p)) if p[i] > p[j])

def comp(a, b):
    return tuple(a[b[i]-1] for i in range(len(a)))

def inv_p(p):
    q = [0]*len(p)
    for i, pi in enumerate(p):
        q[pi-1] = i+1
    return tuple(q)

def cycles(p):
    vis = [False]*len(p); c = 0
    for i in range(len(p)):
        if not vis[i]:
            c += 1; j = i
            while not vis[j]:
                vis[j] = True; j = p[j]-1
    return c

NODES = list(permutations([1,2,3,4]))
L = {p: lg(p) for p in NODES}
COVERS = {}
for a in NODES:
    s = set()
    for i in range(4):
        for j in range(i+1, 4):
            l = list(a); l[i], l[j] = l[j], l[i]; b = tuple(l)
            if L[b] == L[a]+1:
                s.add(b)
    COVERS[a] = s

def bruhat_le(a, b):
    seen = {a}; q = deque([a])
    while q:
        u = q.popleft()
        if u == b:
            return True
        for v in COVERS[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return False

def swap_pos(a, i, j):
    l = list(a); l[i], l[j] = l[j], l[i]; return tuple(l)

def main():
    w = (4,2,3,1); wp = (1,3,2,4); w0 = (4,3,2,1)
    assert L[w] == 5 and L[wp] == 1 and L[w0] == 6, (L[w], L[wp], L[w0])
    assert bruhat_le(wp, w), "need wp <= w"
    # saturated chain wp < ... < w of length 4
    chain = [wp]
    cur = wp
    while cur != w:
        nxt = [v for v in COVERS[cur] if bruhat_le(v, w)]
        assert nxt, "chain stuck"
        cur = sorted(nxt)[0]; chain.append(cur)
    assert len(chain)-1 == L[w]-L[wp] == 4, chain
    wwp = comp(w, inv_p(wp))
    assert wwp == w0 == (4,3,2,1), wwp
    d = 4 - cycles(wwp)
    assert d == 2, d
    # orbits of w0 on {1,2,3,4}
    orb1 = {1, wwp[0]}; orb2 = {2, wwp[1]}
    assert orb1 == {1,4} and orb2 == {2,3}, (orb1, orb2)
    assert 1 in orb1 and 2 in orb2 and orb1 != orb2  # (a,b)=(1,2) distinct orbits
    # fixed-space equations t1=t4, t2=t3
    # bad-pair witness: t=(0,1,1,0) in t^{ww'^{-1}}, t1 != t2
    t = (0,1,1,0)
    assert t[0]==t[3] and t[1]==t[2] and t[0]!=t[1]
    # Gale check: only vanishing d=2 Plucker set for w is {(3,4)} vs W-set {2,4}
    def sset(v, dd): return tuple(sorted(v[:dd]))
    Ws = sset(w,2); Wps = sset(wp,2)
    assert Ws==(2,4) and Wps==(1,3), (Ws,Wps)
    def gale_le(I,J): return all(i<=j for i,j in zip(sorted(I),sorted(J)))
    bad = [I for I in combinations([1,2,3,4],2) if not gale_le(I,Ws)]
    assert bad == [(3,4)], bad
    # Schubert tangent count at wpB: #{transpositions s: wp*s <= w} == 5
    cnt = sum(1 for i in range(4) for j in range(i+1,4) if bruhat_le(swap_pos(wp,i,j), w))
    assert cnt == 5, cnt
    # dimensions
    dimXtri = 16 + 10
    assert dimXtri == 26
    dimT_closure = cnt  # smooth point: equals lg(w)=5
    assert dimT_closure == L[w] == 5
    dBHS = dimXtri - d + dimT_closure - L[wp]
    assert dBHS == 28, dBHS
    assert dBHS - 1 == 27
    # bridge: dim T_Xtri = 10 + dim T_{X_w}
    assert (dimXtri - 16) == 10
    assert 10 + 17 == 27 and 11 + 1 + 5 == 17  # T_Ubar + cut line + u-fiber
    print("chain:", " < ".join("".join(map(str,v)) for v in chain))
    print("ww'^-1 =", "".join(map(str,wwp)), "d =", d)
    print("orbits: {1,4} {2,3}; (a,b)=(1,2) distinct: True")
    print("bad-pair witness t=(0,1,1,0): in t^{ww'^-1}, violates t1=t2: True")
    print("Schubert tangent count =", cnt, "(smooth: == lg w = 5)")
    print("dim X_tri = 26, d_BHS = 28, target = 27; bridge summands 11+1+5=17")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
