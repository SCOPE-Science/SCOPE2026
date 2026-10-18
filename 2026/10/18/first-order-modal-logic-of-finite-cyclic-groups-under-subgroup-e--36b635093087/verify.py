"""Finite consistency checks for a divisibility-frame modal classification.
The infinite proof uses a Smith-normal-form/Baur–Monk argument and is not
certified by these finite tests.
"""
from itertools import product
from math import gcd


def positive_primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**0.5)+1))]


def valuation(n,p):
    z=0
    while n%p==0:
        n//=p
        z+=1
    return z


def box(values,up,i):
    return all(values[j] for j in up[i])


def diamond(values,up,i):
    return any(values[j] for j in up[i])


def check_grz_dot2(points, le):
    up=[[j for j in range(len(points)) if le(points[i],points[j])]
        for i in range(len(points))]
    assert all(up[i] for i in range(len(points)))
    assert all(any(k in up[i] and k in up[j] for k in range(len(points)))
               for i in range(len(points)) for j in range(len(points)))
    for bits in product((False,True),repeat=len(points)):
        p=list(bits)
        bp=[box(p,up,i) for i in range(len(points))]
        guard=[(not p[i]) or bp[i] for i in range(len(points))]
        bg=[box(guard,up,i) for i in range(len(points))]
        inner=[(not bg[i]) or p[i] for i in range(len(points))]
        grz=[(not box(inner,up,i)) or p[i] for i in range(len(points))]
        assert all(grz), (points,p)
        dp=[diamond(p,up,i) for i in range(len(points))]
        dbp=[diamond(bp,up,i) for i in range(len(points))]
        bdp=[box(dp,up,i) for i in range(len(points))]
        assert all((not dbp[i]) or bdp[i] for i in range(len(points)))


def test_boolean_quotient():
    primes=[2,3,5]
    for n in range(1,151):
        state=frozenset(i for i,p in enumerate(primes) if n%p==0)
        for target_bits in product((False,True),repeat=3):
            target=frozenset(i for i,on in enumerate(target_bits) if on)
            if not state<=target:
                continue
            witness=n
            for i in target-state:
                witness*=primes[i]
            assert witness%n==0
            assert frozenset(i for i,p in enumerate(primes) if witness%p==0)==target
    for r in range(0,4):
        cube=list(product((0,1),repeat=r))
        check_grz_dot2(cube,lambda a,b:all(x<=y for x,y in zip(a,b)))


def test_finite_profile_quotient():
    # Prototype: small exceptional orders plus truncated p-valuations.
    N=8
    primes=[2,3,5,7]
    thresholds=[3,2,1,1]
    def profile(n):
        return tuple(min(valuation(n,p),t) for p,t in zip(primes,thresholds))
    def image(n):
        return ('s',n) if n<=N else ('l',profile(n))
    def order(a,b):
        if a[0]=='l' and b[0]=='s':
            return False
        if a[0]=='s' and b[0]=='s':
            return b[1]%a[1]==0
        va=profile(a[1]) if a[0]=='s' else a[1]
        vb=profile(b[1]) if b[0]=='s' else b[1]
        return all(x<=y for x,y in zip(va,vb))
    large=list(product(*[range(t+1) for t in thresholds]))
    states=[('s',n) for n in range(1,N+1)]+[('l',p) for p in large]
    assert all(order(a,a) for a in states)
    assert all(not(order(a,b) and order(b,a)) or a==b for a in states for b in states)
    assert all(not(order(a,b) and order(b,c)) or order(a,c)
               for a in states for b in states for c in states)
    def lift(n,target):
        if target[0]=='s':
            return target[1]
        y=n
        for p,t,desired in zip(primes,thresholds,target[1]):
            present=min(valuation(y,p),t)
            if desired>present:
                y*=p**(desired-present)
        if y<=N:
            y*=11
        return y
    for n in range(1,131):
        for target in states:
            if not order(image(n),target):
                continue
            y=lift(n,target)
            assert y%n==0 and image(y)==target,(n,target,y)
    for n in range(1,131):
        for m in range(1,131):
            if m%n==0:
                assert order(image(n),image(m))


def check_pp_ratios():
    # Check two explicit pp-pairs against direct subgroup enumeration.
    for n in range(1,91):
        for p in [2,3,5,7]:
            carrier=range(n)
            phi={x for x in carrier if any((p*y-x)%n==0 for y in carrier)}
            psi={x for x in carrier if (p*x)%n==0}
            intersection=phi&psi
            assert len(intersection)>0
            quotient=len(phi)//len(intersection)
            # pG has n/gcd(n,p) elements, p-torsion gcd(n,p).
            assert len(phi)==n//gcd(n,p)
            assert len(psi)==gcd(n,p)
            assert len(phi)%len(intersection)==0
            assert quotient>=1

if __name__=='__main__':
    test_boolean_quotient()
    test_finite_profile_quotient()
    check_pp_ratios()
    print('VERIFY_OK: Boolean cubes; finite quotient p-morphism; pp subgroup examples')
