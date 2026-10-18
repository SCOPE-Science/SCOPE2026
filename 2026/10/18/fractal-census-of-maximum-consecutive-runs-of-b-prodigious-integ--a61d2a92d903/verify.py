"""Exact finite checks for maximal b-prodigious intervals and digit-shell counts.

All checks use integer arithmetic; asymptotic claims are proved separately.
"""
from math import gcd, lcm


def setup(b):
    L = lcm(*range(1,b))
    M = L // gcd(L,b*b)
    M0, M1 = 1, M
    for p in range(2,b+1):
        if b%p==0 and all(p%q for q in range(2,int(p**0.5)+1)):
            while M1%p==0:
                M1//=p
                M0*=p
    r=0
    while M0 and b**r % M0:
        r+=1
    ell=next(j for j in range(1,b+1) if b%j)
    return L,M,M0,M1,r,ell


def bit_c(c,b):
    if c < 1: return False
    while c:
        if c%b > 1: return False
        c//=b
    return True


def formula(b,m):
    L,M,M0,M1,r,ell=setup(b)
    if m<=r: return 0
    n=m-r-1
    cnt=0
    for mask in range(1<<n):
        c=b**(m-1)
        for j in range(n):
            if mask & (1<<j): c+=b**(r+j)
        if c%M==0: cnt+=1
    return cnt


def direct_shell(b,m):
    L,M,M0,M1,r,ell=setup(b)
    cnt=0
    for mask in range(1<<(m-1)):
        c=b**(m-1)
        for j in range(m-1):
            if mask>>j&1: c+=b**j
        if c%M==0: cnt+=1
    assert cnt==formula(b,m)
    return cnt


def verify_all():
    shells=0
    for b in range(3,13):
        L,M,M0,M1,r,ell=setup(b)
        assert M==M0*M1
        assert gcd(M1,b)==1
        for m in range(1,9):
            exact=direct_shell(b,m)
            shells+=1
            if m>=r+2 and M1>1:
                from math import cos,pi
                err=abs(exact-2**(m-r-1)/M1)
                bound=(M1-1)/M1*(2*cos(pi/M1))**(m-r-1)+1e-9
                assert err <= bound, (b,m,exact,bound)
        N = min(300000, b**8)
        prod=[1]*(N+1)
        for n in range(1,N+1):
            d=n%b
            prod[n]=prod[n//b]*(d if d else 1)
        good=[False]*(N+1)
        for n in range(1,N+1):
            good[n]=(n%prod[n]==0)
        s=0
        run=0
        for n in range(1,N+1):
            if good[n]:
                if not run: s=n
                run+=1
            else:
                if run==b+ell and s+run<N:
                    assert s%(b*b)==0,(b,s,run)
                    c=s//(b*b)
                    assert bit_c(c,b) and c%M==0,(b,s,c,L,M)
                run=0
        # Every predicted maximal run safely interior to test interval occurs.
        for c in range(1,(N-b-ell)//(b*b)+1):
            if bit_c(c,b) and c%M==0:
                s=c*b*b
                assert all(good[s+i] for i in range(b+ell)),(b,s,c)
                assert not good[s-1] and not good[s+b+ell],(b,s,c)
        print('PASS',b,'ell',ell,'M',M,'M0',M0,'M1',M1,'r',r,'N',N)
    print('VERIFIED 80 shell counts, 10 bases, direct consecutive runs in finite ranges')

if __name__ == '__main__':verify_all()
