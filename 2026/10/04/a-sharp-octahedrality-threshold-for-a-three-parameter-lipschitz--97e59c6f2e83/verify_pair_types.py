from fractions import Fraction
from itertools import product


def valid(a, b, c):
    return a > 0 and b > 0 and c > 0 and a <= 2*b and abs(a-b) <= c <= a+b


def dist(p, q, a, b, c):
    if p == q:
        return Fraction(0)
    if {p, q} == {"o", "z"}:
        return c
    if "z" in (p, q):
        return b
    return a


def obstruction(a, b, c):
    q_xx = (a+b)/(a+c)
    q_zx = a/(b+c)
    return max(q_xx, q_zx)


def enumerate_obstruction(a, b, c):
    pts = ["o", "z", "x0", "x1", "x2"]
    best = Fraction(0)
    for u in pts:
        for v in pts:
            if u == v:
                continue
            q1 = (dist("o",u,a,b,c)+dist("z",v,a,b,c))/(c+dist(u,v,a,b,c))
            q2 = (dist("z",u,a,b,c)+dist("o",v,a,b,c))/(c+dist(u,v,a,b,c))
            best = max(best, min(q1,q2))
    return best


def verify_exact_witness(a, b, c):
    N = ["o", "z", "x0", "x1", "x2"]
    u, v = "x3", "x4"
    for x in N:
        for y in N:
            assert dist(x,y,a,b,c)+dist(u,v,a,b,c) <= dist(x,u,a,b,c)+dist(y,v,a,b,c)


vals = [Fraction(k,4) for k in range(1, 17)]
checked = 0
for a, b, c in product(vals, repeat=3):
    if not valid(a,b,c):
        continue
    checked += 1
    assert enumerate_obstruction(a,b,c) == obstruction(a,b,c)
    if c <= b:
        verify_exact_witness(a,b,c)
    else:
        assert obstruction(a,b,c) < 1
print(f"verified {checked} rational parameter triples")
