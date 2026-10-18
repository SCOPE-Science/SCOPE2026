#!/usr/bin/env python3
"""Exact integer and rational certificates for rarefaction-richness variance."""
from itertools import combinations
from fractions import Fraction
from math import comb, factorial


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for head in range(min(n, maximum), 0, -1):
        for tail in partitions(n-head, head):
            yield (head,) + tail


def balancing_neighbors(profile):
    out = set()
    for i, x in enumerate(profile):
        for j, y in enumerate(profile):
            if i == j or x < y + 2:
                continue
            b = list(profile)
            b[i] -= 1
            b[j] += 1
            out.add(tuple(sorted(b, reverse=True)))
    return sorted(out, reverse=True)


def choose(n, m):
    return comb(n, m) if 0 <= m <= n else 0


def raw_variance_numerator(a, m):
    """Returns binom(N,m)^2 * Var(number of species represented)."""
    N = sum(a)
    D = choose(N, m)
    q = [choose(N-x, m) for x in a]
    total = sum(x*(D-x) for x in q)
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            total += 2*(D*choose(N-a[i]-a[j], m)-q[i]*q[j])
    return total


def variance(a, m):
    D = choose(sum(a), m)
    return Fraction(raw_variance_numerator(a, m), D*D)


def mean(a, m):
    N = sum(a)
    D = choose(N, m)
    return Fraction(sum(D-choose(N-x,m) for x in a), D)


def direct_moments(a,m):
    labels = tuple(j for j, size in enumerate(a) for _ in range(size))
    values = [len({labels[i] for i in subset}) for subset in combinations(range(len(labels)), m)]
    den = len(values)
    mu = Fraction(sum(values),den)
    var = Fraction(sum(v*v for v in values),den)-mu*mu
    return mu,var


def signs(a,b):
    return [(m, (raw_variance_numerator(b,m)>raw_variance_numerator(a,m))
                  -(raw_variance_numerator(b,m)<raw_variance_numerator(a,m)))
            for m in range(1,sum(a))]


def changes(signs_with_sample):
    nonzero = [z for _,z in signs_with_sample if z]
    return sum(nonzero[i]!=nonzero[i-1] for i in range(1,len(nonzero)))

# Exact lower-bound census, including two-species communities.
observed = []
for N in range(2,9):
    profiles = list(partitions(N))
    tested = 0
    double = []
    for a in profiles:
        for b in balancing_neighbors(a):
            tested += 1
            pattern = signs(a,b)
            if changes(pattern)>=2:
                double.append((a,b,pattern))
    expected_counts = {2:(2,0),3:(3,0),4:(5,1),5:(7,2),6:(11,5),7:(15,9),8:(22,17)}
    assert (len(profiles),tested)==expected_counts[N], (N,len(profiles),tested)
    if N<8:
        assert not double
    else:
        assert len(double)==1 and double[0][:2]==((4,3,1),(4,2,2)),double
    observed.append((N,len(profiles),tested,len(double)))
print('Exact exhaustive census: N, abundance partitions, one-unit transfers, two-reversal pairs')
for row in observed:
    print(*row)

A=(4,3,1); B=(4,2,2)
print('Eight-individual witness: m, expected richness change, variance change')
assert signs(A,B)==[(1,0),(2,-1),(3,1),(4,1),(5,-1),(6,-1),(7,-1)]
for m in range(1,8):
    da=direct_moments(A,m)
    db=direct_moments(B,m)
    assert da==(mean(A,m),variance(A,m)),(m,da)
    assert db==(mean(B,m),variance(B,m)),(m,db)
    print(m,db[0]-da[0],db[1]-da[1])

# Polynomial arithmetic, in t=k-1. A_k=(4k,3k,k), B_k=(4k,3k-1,k+1).
# Each binom(linear(t), m) is the falling-factorial polynomial divided by m!.
zero = (Fraction(0),)

def norm(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return tuple(p)

def padd(a,b):
    return norm([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def pscale(a,s):
    return norm([s*x for x in a])

def psub(a,b):
    return padd(a,pscale(b,-1))

def pmul(a,b):
    c=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return norm(c)

def choose_poly(linear,m):
    ans=(Fraction(1),)
    for j in range(m):
        ans=pmul(ans,psub(linear,(Fraction(j),)))
    return pscale(ans,Fraction(1,factorial(m)))

def vpoly(a,m):
    N=(Fraction(8),Fraction(8))
    D=choose_poly(N,m)
    q=[choose_poly(psub(N,x),m) for x in a]
    s=zero
    for x in q:
        s=padd(s,pmul(x,psub(D,x)))
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            u=choose_poly(psub(psub(N,a[i]),a[j]),m)
            s=padd(s,pscale(psub(pmul(D,u),pmul(q[i],q[j])),2))
    return s

Apolys=((Fraction(4),Fraction(4)),(Fraction(3),Fraction(3)),(Fraction(1),Fraction(1)))
Bpolys=((Fraction(4),Fraction(4)),(Fraction(2),Fraction(3)),(Fraction(2),Fraction(1)))
for m,sgn in [(2,-1),(3,1),(7,-1)]:
    difference=psub(vpoly(Bpolys,m),vpoly(Apolys,m))
    assert all(sgn*x>0 for x in difference), (m,difference)
    assert len(difference)<=2*m+1
    for k in [1,2,3,10,100,1000]:
        t=k-1
        evaluation=sum(c*t**j for j,c in enumerate(difference))
        x=(4*k,3*k,k); y=(4*k,3*k-1,k+1)
        assert evaluation==raw_variance_numerator(y,m)-raw_variance_numerator(x,m),(k,m)
    print('All-size family polynomial m =',m,'degree=',len(difference)-1)
    print('coefficients low-to-high in t=k-1:',','.join(str(v) for v in difference))
    print('sign=', '+' if sgn>0 else '-', 'for every integer k>=1')

print('ALL CERTIFICATES PASS')
