"""Exact arithmetic checks for rational floor-rotated lattice inverse multiplicities.

Requires Python 3.9+ standard library only. Finite diagnostics, not an infinite proof.
"""
from collections import Counter
from math import gcd, isqrt, cos, sin, pi, floor, sqrt


def primitive_triples(max_m=16):
    for m in range(2, max_m + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            q = m * m + n * n
            a, b = m * m - n * n, 2 * m * n
            for x, y in ((a, b), (b, a)):
                yield x, y, q


def modular_counts(a, b, q):
    assert a*a+b*b == q*q and gcd(a, q) == gcd(b, q) == 1
    h = b * pow(a, -1, q) % q
    assert (h*h+1) % q == 0
    H = sum((h*r) % q < q-b for r in range(q-a))
    V = sum((h*r) % q < q-a for r in range(b, q))
    return H, V, h


def source_period_counts(a,b,q):
    horiz = vert = 0
    for X in range(q):
        for Y in range(q):
            r = (a*X-b*Y)%q
            t = (b*X+a*Y)%q
            horiz += (r < q-a and t < q-b)
            vert += (r >= b and t < q-a)
    return horiz, vert


def finite_target_counts(a,b,q,M):
    # If both transformed coordinates have absolute value <= M+1,
    # the original source coordinates are bounded by sqrt(2)*(M+1).
    bound = (3*(M+2))//2+3
    targets = Counter()
    for X in range(-bound,bound+1):
        for Y in range(-bound,bound+1):
            U = (a*X-b*Y)//q
            V = (b*X+a*Y)//q
            if -M <= U <= M and -M <= V <= M:
                targets[U,V] += 1
    cnt=Counter(targets.values())
    cnt[0]=(2*M+1)**2-len(targets)
    assert all(k in (0,1,2) for k in cnt)
    assert sum(cnt.values())==(2*M+1)**2
    return cnt


def irrational_window(theta,M):
    c, s = cos(theta), sin(theta)
    bound=int(1.5*(M+2))+3
    hits=Counter()
    for X in range(-bound,bound+1):
        for Y in range(-bound,bound+1):
            U=floor(c*X-s*Y)
            V=floor(s*X+c*Y)
            if -M<=U<=M and -M<=V<=M:
                hits[U,V]+=1
    return ((2*M+1)**2-len(hits))/(2*M+1)**2


def main():
    tests=0
    for a,b,q in primitive_triples():
        H,V,h=modular_counts(a,b,q)
        assert H==V+1, (a,b,q,H,V)
        assert source_period_counts(a,b,q)==(q*H,q*V)
        D=(2*H-1)/q
        benchmark=2*(q-a)*(q-b)/q**2
        assert abs(D-benchmark)<=4*sqrt(2/q)+4/q
        assert 0 < D < 0.5
        tests+=1
    assert tests>=100
    for a,b,q in ((3,4,5),(4,3,5),(5,12,13),(8,15,17)):
        H,V,h=modular_counts(a,b,q)
        expected=(2*H-1)/q
        for M in (20,60):
            cnt=finite_target_counts(a,b,q,M)
            observed=cnt[2]/(2*M+1)**2
            assert abs(observed-expected)<0.04, (a,b,q,M,expected,observed)
            assert abs(cnt[0]-cnt[2])<=25*M
    assert modular_counts(3,4,5)[:2]==(1,0)
    for theta in (pi/4,pi/8):
        c,s=cos(theta),sin(theta)
        for M in (60,120):
            observed=irrational_window(theta,M)
            expected=(c+s-1)**2
            assert abs(observed-expected)<0.02,(theta,M,observed,expected)
    print(f'PASS: {tests} ordered primitive triples, exact modular-period counts,')
    print('exact finite target counts, discrepancy bounds, and irrational diagnostics.')


if __name__=='__main__':
    main()
