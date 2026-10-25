#!/usr/bin/env python3
"""Independent shortest-path checks of a three-generator semigroup formula.

Uses only Python's standard library. Exhaustive residue shortest paths are
independent of the symbolic greedy Apéry construction in the accompanying proof.
"""
import heapq
import math


def shortest_residues(a, generators):
    infinity = 10**100
    dist = [infinity] * a
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        x, r = heapq.heappop(queue)
        if x != dist[r]:
            continue
        for v in generators[1:]:
            t = (r + v) % a
            if x + v < dist[t]:
                dist[t] = x + v
                heapq.heappush(queue, (dist[t], t))
    return dist


def predicted(h, a, d):
    B = h * h - h + 1
    q, s = divmod(a, B)
    assert h >= 3 and q >= h - 1 and math.gcd(a, d) == 1 and d >= 1
    vals = [0] * a
    for r in range(a):
        u, v = divmod(r, B)
        vals[(d * r) % a] = a * (h * h * u + h * v) + d * r
    genus = (B*h*h*q*(q-1) + q*h*B*(B-1)
             + 2*s*h*h*q + h*s*(s-1) + (d-1)*(a-1)) // 2
    c = a * (h*h*(q-1) + h*(B-1)) + d*(q*B-1) - a
    if s:
        e = a * (h*h*q + h*(s-1)) + d*(a-1) - a
        pf = sorted((c, e))
    else:
        pf = [c]
    return vals, genus, pf


def one_case(h, a, d):
    B = h*h - h + 1
    gen = (a, h*a+d, h*h*a+B*d)
    dist = shortest_residues(a, gen)
    expected, g, pf = predicted(h, a, d)
    assert dist == expected, ('residues', h, a, d)
    assert (sum(dist) - a*(a-1)//2) // a == g, ('genus', h, a, d)
    assert max(dist) - a == max(pf), ('Frobenius', h, a, d)
    actual_pf = sorted(
        w - a for r,w in enumerate(dist)
        if all(w + gen_i != dist[(r + gen_i) % a]
               for gen_i in gen[1:])
    )
    assert actual_pf == pf, ('pseudo-Frobenius', h, a, d, actual_pf, pf)
    # A genuine gap must lie below its Apéry representative.
    if a <= 100 and d <= 50:
        actual_by_gaps = [n for n in range(1, max(pf)+1)
                          if n < dist[n % a] and all(
                              n + z >= dist[(n + z) % a] for z in gen)]
        assert actual_by_gaps == pf, ('gap check', h, a, d)


def main():
    count = 0
    for h in range(3, 13):
        B = h*h-h+1
        aa = list(range((h-1)*B, (h-1)*B + min(3*B, 31)))
        aa += [(h+1)*B+5]
        for a in aa:
            for d in (1,2,3,5,7,17,a+1,2*a+1,10*a+1):
                if math.gcd(a,d) == 1:
                    one_case(h,a,d)
                    count += 1
    for h,a,d in ((3,14,1), (3,15,1), (3,18,19),
                  (4,39,1), (4,40,1), (5,105,211)):
        one_case(h,a,d)
        count += 1
    print(f"PASS: {count} independent shortest-path checks with exact Apéry, "
          "genus, Frobenius and pseudo-Frobenius comparisons")

if __name__ == '__main__':
    main()
