"""Exact rational verification of source-count and two-cycle covariance for p-mappings.

Run: python check_mapping_dependence.py
No external packages are needed.
"""
from fractions import Fraction as Q
from itertools import product


def theoretical(p):
    n = len(p)
    s2 = sum(x*x for x in p)
    W = sum(x*(1-x)**(n-2) for x in p)
    V = sum(x*x*(1-x)**(n-2) for x in p)
    mu_z = sum((1-x)**n for x in p)
    mu_t = (1-s2)/2
    cov = ((1+s2)*V-2*s2*W)/2
    bound = -s2*(1-s2)*W/2
    return mu_z, mu_t, cov, bound, W, V, s2


def enumerate_mapping(p):
    n = len(p)
    ez = et = ef = ezt = ezf = Q(0)
    mass = Q(0)
    count = 0
    for f in product(range(n), repeat=n):
        w = Q(1)
        for j in f:
            w *= p[j]
        if not w:
            continue
        images = set(f)
        z = n-len(images)
        t = sum(1 for i in range(n) for j in range(i+1,n)
                if f[i] == j and f[j] == i)
        fix = sum(1 for i in range(n) if f[i] == i)
        mass += w
        ez += z*w
        et += t*w
        ef += fix*w
        ezt += z*t*w
        ezf += z*fix*w
        count += 1
    assert mass == 1
    return ez, et, ezt-ez*et, ezf-ez*ef, count


def main():
    validations = 0
    enumerated = 0
    families = []
    for n in range(2,7):
        fams = [[Q(1,n)]*n,
                [Q(i+1, n*(n+1)//2) for i in range(n)],
                [Q(2**i, 2**n-1) for i in range(n)],
                [Q(0)]*(n-2)+[Q(1,3), Q(2,3)],
                [Q(1,2),Q(1,2)]+[Q(0)]*(n-2)]
        if n == 2:
            fams.append([Q(1,5),Q(4,5)])
        for p in fams:
            mu_z,mu_t,cov,bound,W,V,s2=theoretical(p)
            ez,et,cov0,covfix,seen=enumerate_mapping(p)
            enumerated += seen
            for assertion in [ez==mu_z,et==mu_t,cov0==cov,covfix==0,
                              cov<=bound,cov<0,mu_t>0,W>0]:
                assert assertion,(n,p,cov,bound,cov0)
                validations+=1
            should_equal=n==2 or len(set(x for x in p if x>0))==1
            assert (cov==bound)==should_equal,(n,p,cov,bound)
            validations+=1
            families.append((n,len(set(p))))
    # Additional large-dimensional exact polynomial checks, not exhaustive mapping enumeration.
    for n in range(7,21):
        for p in ([Q(1,n)]*n,
                  [Q(i+1,n*(n+1)//2) for i in range(n)],
                  [Q(2**i,2**n-1) for i in range(n)]):
            _,_,cov,bound,W,V,s2=theoretical(p)
            assert cov<=bound<0
            assert V<=s2*W
            validations+=2
    print('PASS', 'exact assertions:',validations,
          'positive-mass mappings enumerated:',enumerated,
          'families enumerated:',len(families))

if __name__=='__main__':
    main()
