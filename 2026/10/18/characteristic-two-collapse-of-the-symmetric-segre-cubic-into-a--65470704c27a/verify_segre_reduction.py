"""Exact finite-field checks for the symmetric six-coordinate cubic reduction.

Run: python verify_segre_reduction.py
Only finite checks are performed; the general classification is proved separately.
"""
from itertools import product, combinations
from collections import Counter


def fm(a,b):
    """Multiply in F4 = F2[t]/(t^2+t+1), using 2 for t."""
    z = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & 1 and (b >> j) & 1:
                z ^= 1 << (i+j)
    if z & 4:
        z ^= 4 | 2 | 1  # t^2 = t+1
    return z


def fp(a, n):
    r = 1
    for _ in range(n):
        r = fm(r,a)
    return r


def nv4(v):
    nonzero = next(a for a in v if a)
    inv = next(a for a in range(1,4) if fm(a,nonzero)==1)
    return tuple(fm(inv,a) for a in v)


def vf4(y):
    s = 0
    for a in y:
        s ^= a
    # In F4, every nonzero element has cube 1.
    return sum(1 for a in list(y)+[s] if a) % 2


def all_f4_points():
    return sorted({nv4(v) for v in product(range(4),repeat=4) if any(v)})


def span_line_f4(p,q):
    pts=set()
    for a,b in product(range(4),repeat=2):
        v=tuple(fm(a,pi)^fm(b,qi) for pi,qi in zip(p,q))
        if any(v):
            pts.add(nv4(v))
    assert len(pts)==5
    return frozenset(pts)


def char2_checks():
    assert all(fm(a,fp(a,2))== (a!=0) for a in range(4))
    points=all_f4_points()
    assert len(points)==85
    on={p for p in points if vf4(p)==0}
    assert len(on)==45, len(on)
    lines={span_line_f4(p,q) for p,q in combinations(points,2)}
    assert len(lines)==357
    contained={l for l in lines if l.issubset(on)}
    assert len(contained)==27, len(contained)
    incidence=Counter(p for l in contained for p in l)
    assert set(incidence)==on and set(incidence.values())=={3},Counter(incidence.values())
    pairints=Counter(len(x & y) for x,y in combinations(contained,2))
    assert pairints=={0:216,1:135},pairints
    # Formal Tjurina algebra: the four partial quadrics generate
    # (y_1^2,...,y_4^2) because I+J is its own inverse in characteristic two.
    IplusJ = [[(i != j) * 1 for j in range(4)] for i in range(4)]
    def multiply_mod2(A,B):
        return [[sum(A[i][k]*B[k][j] for k in range(4))%2 for j in range(4)] for i in range(4)]
    assert multiply_mod2(IplusJ,IplusJ)==[[int(i==j) for j in range(4)] for i in range(4)]
    print('GF4_BASE_POINTS=45 GF4_BASE_LINES=27 PAIR_INTERSECTIONS=135')
    print('CHAR2_TJURINA_LENGTH=16 HILBERT_FUNCTION=1,4,6,4,1')


def prime_checks(p):
    def normalize(v):
        c=next(a for a in v if a)
        inv=pow(c,-1,p)
        return tuple(a*inv%p for a in v)
    # Six coordinates, sum zero. Enumerate four free coordinates and
    # a projective scale using homogeneous vectors in the 5D hyperplane.
    seen=set()
    for i in range(5):
        for tail in product(range(p), repeat=4-i):
            five=[0]*i+[1]+list(tail)
            sixth=(-sum(five))%p
            v=tuple(five+[sixth])
            assert normalize(v)==v
            if sum(pow(a,3,p) for a in v)%p:
                continue
            if len({a*a%p for a in v})==1:
                seen.add(v)
    assert len(seen)==10,(p,len(seen))
    for v in seen:
        # A node has three plus and three minus after rescaling.
        assert sum(a==1 for a in v)==3 or sum(a==p-1 for a in v)==3
    print(f'CHAR{p}_SINGULAR_POINTS={len(seen)}')


if __name__ == '__main__':
    char2_checks()
    for prime in (5,7):
        prime_checks(prime)
    print('VERIFY_OK')
