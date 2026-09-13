"""Verify the two combinatorial lemmas disproving SF6's droplet clause (d=6, torus).

Lemma 1: the only forward-closed subsets of T_n^d are empty and full
  (forward steps generate the whole group). Hence no proper "cube" is forward-closed.
Lemma 2 (sterility): a side-s cube C (s<n) on T_n^d generates ZERO new infections
  under the forward-2 rule: every x outside C has <=1 forward neighbour in C.
  Hence [C]=C: no layer-by-layer expansion, let alone covering the torus.
"""
import itertools

def add_mod(x, e, n):
    y = list(x); y[e] = (y[e] + 1) % n; return tuple(y)

def forward_reachable(start, d, n):
    seen = {start}; stack = [start]
    while stack:
        x = stack.pop()
        for i in range(d):
            y = add_mod(x, i, n)
            if y not in seen:
                seen.add(y); stack.append(y)
    return seen

def in_cube(x, corner, s, n):
    # cube = product of intervals [c_i, c_i+s) mod n; require s<=n
    for i, (xi, ci) in enumerate(zip(x, corner)):
        if (xi - ci) % n >= s:
            return False
    return True

def check(d, n, s, corner):
    N = n ** d
    # Lemma 1: forward orbit of origin is the whole torus
    orb = forward_reachable(tuple([0]*d), d, n)
    assert len(orb) == N, (d, n, len(orb), N)
    # Lemma 2: sterility of the cube
    allpts = itertools.product(range(n), repeat=d)
    cube = {x for x in allpts if in_cube(x, corner, s, n)}
    assert len(cube) == s ** d, (len(cube), s ** d)
    worst = 0; growers = []
    for x in itertools.product(range(n), repeat=d):
        if x in cube:
            continue
        c = sum(1 for i in range(d) if add_mod(x, i, n) in cube)
        worst = max(worst, c)
        if c >= 2:
            growers.append(x)
    return N, len(cube), worst, growers

for (d, n, s, corner) in [(6, 5, 3, (0,0,0,0,0,0)),
                          (6, 5, 3, (4,4,4,4,4,4)),  # wrapped corner cube
                          (6, 4, 2, (1,2,0,3,1,2)),
                          (6, 3, 1, (0,0,0,0,0,0)),  # singleton
                          (2, 6, 2, (5,5))]:
    N, nc, worst, growers = check(d, n, s, corner)
    print(f"d={d} n={n} s={s} corner={corner}: |T|={N} |C|={nc} "
          f"max_forward_nbrs_outside={worst} growers={len(growers)}")
    assert worst <= 1 and not growers

# side-length vs torus: s(n)=floor(F log n) < n eventually for any fixed F
import math
for F in [0.5, 1.0, 5.0]:
    ns = [n for n in range(2, 200) if math.floor(F*math.log(n)) >= n]
    print(f"F={F}: n with s(n)>=n (small-n only): {ns}")
print("ALL CHECKS PASSED: forward orbit = full torus; cubes sterile (0 growers).")
