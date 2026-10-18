#!/usr/bin/env python3
"""Exact finite certificate for consecutive quartic-cyclotomic LCM quotient."""
from math import lcm

EXPECTED_RESULTANTS = (
    153, 73728, 46584153, 4421910528, 154497425625
)
EXPECTED_FACTORS = (
    {3:2,17:1}, {2:13,3:2}, {3:4,7:2,11:2,97:1},
    {2:16,3:4,7:2,17:1}, {3:6,5:4,23:2,641:1}
)
ROOTS={17:(2,8,9,15),97:(33,47,50,64),641:(256,318,323,385)}
PERIODS=(17,34,1649,3298,1057009)


def bareiss(matrix):
    a=[list(row) for row in matrix]
    m=len(a); prev=1; sign=1
    for i in range(m-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,m) if a[j][i]),None)
            assert j is not None
            a[i],a[j]=a[j],a[i]; sign=-sign
        pivot=a[i][i]
        for j in range(i+1,m):
            for h in range(i+1,m):
                z=a[j][h]*pivot-a[j][i]*a[i][h]
                assert z%prev==0
                a[j][h]=z//prev
            a[j][i]=0
        prev=pivot
    return sign*a[-1][-1]


def resultant(h):
    f=[1,0,0,0,1] # leading-first coefficients of x^4+1
    shifted=[1,4*h,6*h*h,4*h**3,h**4+1]
    sylvester=[]
    for j in range(4):
        sylvester.append([0]*j+f+[0]*(3-j))
    for j in range(4):
        sylvester.append([0]*j+shifted+[0]*(3-j))
    return bareiss(sylvester)


def isprime(n):
    if n<2:return False
    d=2
    while d*d<=n:
        if n%d==0:return False
        d+=1
    return True


def allowed(k,n):
    e=((n%17) in ({(8-j)%17 for j in range(k)} |
                      ({(15-j)%17 for j in range(k-3)} if k>=4 else set())))
    t=(k>=3 and n%97 in {(47-j)%97 for j in range(k-2)})
    u=(k>=5 and n%641==318)
    n_odd=sum((n+j)%2 for j in range(k+1))
    return (2**(n_odd-1))*(17 if e else 1)*(97 if t else 1)*(641 if u else 1)


def direct(k,n):
    vals=[(n+j)**4+1 for j in range(k+1)]
    product=1; unit_lcm=1
    for t in vals:
        product*=t
        unit_lcm=lcm(unit_lcm,t)
    return product//unit_lcm


def run():
    for h in range(1,6):
        r=resultant(h)
        assert r==EXPECTED_RESULTANTS[h-1],(h,r)
        fac=EXPECTED_FACTORS[h-1]; prod=1
        for p,e in fac.items():
            assert isprime(p)
            prod*=p**e
        assert prod==r
        for p in fac:
            if p%8==1:
                roots=[x for x in range(p) if (pow(x,4,p)+1)%p==0]
                assert roots==list(ROOTS[p]),(p,roots)
        print('resultant',h,r,fac)
    for p,rr in ROOTS.items():
        pairs=[(a,h) for a in rr for h in range(1,6) if (a+h)%p in rr]
        assert pairs=={17:[(8,1),(15,4)],97:[(47,3)],641:[(318,5)]}[p],(p,pairs)
        print('rootpairs',p,pairs)
    # Direct independent integer lcm/product testing in multiple full small periods
    # plus a far range catching every 641 residue class repeatedly.
    for k in range(1,6):
        limit=60000 if k==5 else 25000
        for n in range(1,limit+1):
            a=allowed(k,n)
            b=direct(k,n)
            assert a==b,(k,n,a,b)
        print('direct_checks',k,limit)
    # Check exact entire period distribution at k=5 via independent CRT counting.
    cnt={}
    for n in range(1,PERIODS[4]+1):
        val=allowed(5,n)
        cnt[val]=cnt.get(val,0)+1
    assert cnt=={4:601600,68:421120,388:19200,6596:13440,
                 2564:940,43588:658,248708:30,4228036:21},cnt
    assert sum(cnt.values())==PERIODS[4]
    print('k5_distribution',dict(sorted(cnt.items())))
    # verify period minimality via explicit prime-support witnesses and parity
    assert PERiODS_CHECK()
    print('VERIFY_OK')


def PERiODS_CHECK():
    for k,T in enumerate(PERIODS,start=1):
        factors={p for p in (2,17,97,641) if T%p==0}
        product=1
        for p in factors: product*=p
        assert product==T,(k,T,factors)
        for p in factors:
            smaller=T//p
            # Any proper divisor-period implies a T/p period for some p|T.
            witness=next((n for n in range(1,3001)
                          if allowed(k,n)!=allowed(k,n+smaller)),None)
            assert witness is not None,(k,p,smaller)
            print('minimal_period_witness',k,p,smaller,witness)
    return True

if __name__=='__main__':
    run()
