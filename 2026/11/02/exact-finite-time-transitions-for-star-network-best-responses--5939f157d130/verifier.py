"""Reproduce exact sweep cutoffs for the star network best-response model.
Only uses the Python standard library. Run: python verifier.py
"""
from fractions import Fraction as F
from itertools import product, permutations
from math import ceil, factorial, isclose, log, sqrt


def update(c, leaves, delta):
    leaves = [max(F(0), F(1)-delta*c) for _ in leaves]
    c = max(F(0), F(1)-delta*sum(leaves))
    return c, leaves


def iterate_formula(c, s, d, k):
    a = F(1)-d*s
    b = d*d*s
    if b == 1:
        return max(F(0), c + k*a)
    y = b**k * c + a * ((b**k-F(1))/(b-F(1)))
    return max(F(0), y)


def exact_cutoff(s, d):
    assert F(1,s)<d<F(1)
    c=F(1)
    for r in range(1,1500):
        c=max(F(0),F(1)-d*s+d*d*s*c)
        if not c:
            return r
    raise AssertionError('long cutoff')


def check():
    ntests=0
    maxr=0
    one_sweep=0
    for s in range(2,31):
        for q in range(2,81):
            for p in range(1,q):
                d=F(p,q)
                if not F(1,s)<d<F(1):
                    continue
                r=exact_cutoff(s,d)
                maxr=max(maxr,r)
                c=F(1)
                leaves=[F(1,3)]*s
                for j in range(r):
                    c,leaves=update(c,leaves,d)
                    assert c==iterate_formula(F(1),s,d,j+1), (s,d,j)
                    assert c>0 if j+1<r else c==0
                c,leaves=update(c,leaves,d)
                assert c==0 and leaves==[F(1)]*s
                assert (r==1)==(s*d*(F(1)-d)>=1)
                if r==1:
                    one_sweep+=1
                b=float(d*d*s)
                Q=float((d*s-1)/(d*s*(1-d)))
                if abs(b-1)>1e-12:
                    rr=log(Q)/log(b)
                    if abs(rr-round(rr))>1e-9:
                        assert ceil(rr)==r,(s,d,r,rr)
                else:
                    assert r==ceil(1/float(d*s-1))
                # Every permissible initial center is dominated by the full-center start.
                for c0 in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
                    assert iterate_formula(c0,s,d,r)==0
                ntests+=1
    # At the lower boundary exact convergence is absent for the center-one cycle.
    for s in range(2,31):
        d=F(1,s)
        c=F(1)
        leaves=[F(0)]*s
        for i in range(15):
            c,leaves=update(c,leaves,d)
            assert c==d**(i+1) and c>0
    # With less than critical externality, center-one orbit never reaches its interior fixed point.
    for s in range(2,15):
        for q in range(2,36):
            for p in range(1,q):
                d=F(p,q)
                if d>=F(1,s):
                    continue
                b=d*d*s
                cstar=(1-d*s)/(1-b)
                c=F(1)
                leaves=[F(0)]*s
                for k in range(1,9):
                    c,leaves=update(c,leaves,d)
                    assert c!=cstar and c-cstar==b**k*(1-cstar)
    # A random schedule's prescribed good block is a valid deterministic certificate.
    for s in range(2,11):
        for d in (F(1,2),F(3,4),F(9,10)):
            if d<=F(1,s):
                continue
            r=exact_cutoff(s,d)
            for c0 in (F(0),F(1,3),F(1)):
                c=c0
                leaves=[F(2,7)]*s
                for _ in range(r):
                    c,leaves=update(c,leaves,d)
                assert c==0
                c,leaves=update(c,leaves,d)
                assert c==0 and all(x==1 for x in leaves)
    permutation_trials=0
    for s in range(2,8):
        for d in (F(1,3),F(1,2),F(2,3),F(3,4),F(9,10)):
            if not F(1,s)<d<F(1):
                continue
            count=0
            for perm in permutations(range(s+1)):
                c=F(1)
                leaves=[F(0)]*s
                for ix in perm:
                    if ix==0:
                        c=max(F(0),F(1)-d*sum(leaves))
                    else:
                        leaves[ix-1]=max(F(0),F(1)-d*c)
                count+=(c==0)
            cutoff=F(1)/(d*(1-d))
            kmin=(cutoff.numerator+cutoff.denominator-1)//cutoff.denominator
            assert count==max(0,s-kmin+1)*factorial(s), (s,d,count)
            permutation_trials+=1
    print('permutation deactivation PASS', permutation_trials, 'parameter/order exhaustions')
    print('PASS', ntests, 'rational parameter cases;', 'maximum cutoff',maxr,';', one_sweep,'one-sweep cases;', 'lower/upper boundary checks PASS')


if __name__=='__main__':
    check()
