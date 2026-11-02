#!/usr/bin/env python3
"""Exact integer transfer certificate for optimal singleton 3-rainbow functions on cycle prisms."""
from itertools import product, combinations
from collections import Counter

COLS = [c for c in product(range(4), repeat=2) if c != (0, 0)]
PAIRS = [(a, b) for a in COLS for b in COLS]
INDEX = {s: i for i, s in enumerate(PAIRS)}
SIZE = len(PAIRS)


def constraint(prev, cur, nxt):
    return all(cur[r] != 0 or sorted((prev[r], cur[1-r], nxt[r])) == [1,2,3]
               for r in (0,1))


def transition():
    a, b = ([{} for _ in range(SIZE)] for _ in range(2))
    for i, (prev, cur) in enumerate(PAIRS):
        for nxt in COLS:
            if constraint(prev, cur, nxt):
                (a if 0 in nxt else b)[i][INDEX[(cur, nxt)]] = 1
    return a, b


def eye():
    return [{i: 1} for i in range(SIZE)]


def multiply(a, b):
    out = [{} for _ in range(SIZE)]
    for i, row in enumerate(a):
        dest = out[i]
        for j, x in row.items():
            for k, y in b[j].items():
                dest[k] = dest.get(k, 0) + x*y
    return out


def trace(a):
    return sum(row.get(i, 0) for i, row in enumerate(a))


def numerator_certificate():
    a, b = transition()
    power = [eye()]
    for i in range(1,15):
        power.append(multiply(power[-1], a))
    assert power[8] == power[2], 'periodic single-column transfer identity'
    # P(t) = (1-t^6)(I-t A)^{-1}: coefficient t^j as a polynomial in A.
    p = [{j:1} for j in range(8)]
    p[6][0] = -1
    p[7][1] = -1
    pp = [{} for _ in range(15)]
    for k, c in enumerate(p):
        for j, e in enumerate(p):
            for x, v in c.items():
                for y, w in e.items():
                    pp[k+j][x+y] = pp[k+j].get(x+y, 0) + v*w
    n0 = {j: sum(v*trace(power[k]) for k,v in cj.items()) for j,cj in enumerate(p)}
    abtr = [trace(multiply(power[i], b)) for i in range(15)]
    n1 = {j+1: sum(v*abtr[k] for k,v in cj.items()) for j,cj in enumerate(pp)}
    xb = [multiply(power[i], b) for i in range(15)]
    ht = {}
    for i in range(15):
        for j in range(8):
            ht[i,j] = sum(v * xb[j][k].get(row, 0)
                          for row, line in enumerate(xb[i]) for k,v in line.items())
    n2 = {}
    for k, dk in enumerate(pp):
        for j, pj in enumerate(p):
            term = sum(c*e*ht[v,w] for v,c in dk.items() for w,e in pj.items())
            n2[k+j+2] = n2.get(k+j+2, 0) + term
    clean = lambda d: {k:v for k,v in d.items() if v}
    return tuple(map(clean,(n0,n1,n2)))

EXPECTED = (
    {0:225, 6:-213},
    {1:9, 3:36, 5:60, 6:216, 7:66, 9:36, 11:12, 13:-3},
    {2:81,3:324,4:792,5:1260,6:2592,7:2772,8:2493,9:3888,
     10:2844,11:3744,12:5184,13:2448,14:1359,15:972,16:252,
     17:180,19:-36,20:-45},
)


def trace_coefficient(num, h, n):
    # Denominator (1-t^6)^(h+1), use exact positive-binomial expansion.
    return sum(v*__import__('math').comb((n-k)//6+h, h)
               for k,v in num.items() if k<=n and (n-k)%6==0)


def predicted(n):
    if n%6==0: return n, 12
    if n%2: return n+1, 12*n
    if n%6==2: return n+2, 18*n*(3*n-5)
    return n+2, 18*n*(3*n-1)


def supported_sets(n, h):
    # Independent vertices are omitted (uncolored). At most one per rung.
    for holes_tuple in combinations(range(n), h):
        holes = set(holes_tuple)
        if not holes:
            if n%2 == 0:
                for row in (0,1):
                    yield frozenset(2*i+((i+row)%2) for i in range(n))
            continue
        starts = [i for i in range(n) if i not in holes and (i-1)%n in holes]
        for choices in product((0,1), repeat=len(starts)):
            seed = dict(zip(starts,choices)); rows = {}
            for z in range(n):
                i = (min(holes)+1+z)%n
                if i in holes: continue
                rows[i] = seed[i] if i in seed else 1-rows[(i-1)%n]
            yield frozenset(2*i+rows[i] for i in rows)


def direct_colorings(n, uncolored):
    colored = [v for v in range(2*n) if v not in uncolored]
    adj = {v:set() for v in colored}
    for v in uncolored:
        i,r = divmod(v,2)
        neigh = [2*((i-1)%n)+r, 2*((i+1)%n)+r, 2*i+(1-r)]
        if any(w in uncolored for w in neigh): return 0
        for x,y in combinations(neigh,2):
            adj[x].add(y); adj[y].add(x)
    cmap={}; result=0
    def rec():
        nonlocal result
        if len(cmap)==len(colored):
            result+=1;return
        v=max((v for v in colored if v not in cmap),
              key=lambda z:(len({cmap[j] for j in adj[z] if j in cmap}),len(adj[z])))
        forbidden={cmap[j] for j in adj[v] if j in cmap}
        for color in range(3):
            if color not in forbidden:
                cmap[v]=color;rec();del cmap[v]
    rec()
    return result




def full_assignment_check():
    for m in range(3,6):
        neighbors = [(2*((i-1)%m)+r, 2*((i+1)%m)+r, 2*i+(1-r))
                     for i in range(m) for r in (0,1)]
        best, count = 2*m+1, 0
        for labels in product(range(4), repeat=2*m):
            if any(labels[v] == 0 and sorted(labels[u] for u in neighbors[v]) != [1,2,3]
                   for v in range(2*m)):
                continue
            weight = sum(x != 0 for x in labels)
            if weight < best: best, count = weight, 1
            elif weight == best: count += 1
        assert (best, count) == predicted(m), (m,best,count)

def main():
    n0,n1,n2=numerator_certificate()
    assert (n0,n1,n2)==EXPECTED, 'all finite matrix coefficient identities'
    for m in range(3,100):
        arr = [trace_coefficient(x,h,m) for h,x in enumerate(EXPECTED)]
        w, c = predicted(m)
        assert arr[w-m]==c and all(x==0 for x in arr[:w-m]), (m,arr,w,c)
    full_assignment_check()
    count=0
    for m in range(3,13):
        for h in range(3):
            v=sum(direct_colorings(m,U) for U in supported_sets(m,h))
            assert v==trace_coefficient(EXPECTED[h],h,m), (m,h,v)
            count+=1
    print('VERIFY_OK matrix_dimension=225 A8_eq_A2=True exact_numerators=3 '
          'symbolic_residue_classes=6 full_label_lengths=3..5 independent_support_checks=%d lengths=3..12' % count)

if __name__=='__main__': main()
