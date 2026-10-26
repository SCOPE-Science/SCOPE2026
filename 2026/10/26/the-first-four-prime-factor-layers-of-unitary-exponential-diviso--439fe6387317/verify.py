"""Finite checks for unitary/exponential divisor-sum equality at low Omega.
All universal claims are proved separately; these tests are finite diagnostics.
"""
from math import isqrt

LIMIT = 1_000_000

def spf_sieve(n):
    spf=list(range(n+1))
    for p in range(2,isqrt(n)+1):
        if spf[p]==p:
            for k in range(p*p,n+1,p):
                if spf[k]==k:spf[k]=p
    return spf

def factors(n,spf):
    fs=[]
    while n>1:
        p=spf[n]; a=0
        while n%p==0:
            n//=p; a+=1
        fs.append((p,a))
    return fs

def sigmas(fs):
    unitary=exponential=1
    for p,a in fs:
        unitary *= 1+p**a
        exponential *= sum(p**d for d in range(1,a+1) if a%d==0)
    return unitary,exponential

def main():
    spf=spf_sieve(LIMIT)
    eq=[]
    low=0
    triples=0
    for n in range(1,LIMIT+1):
        fs=factors(n,spf)
        omega=sum(a for _,a in fs)
        if omega<=4:
            low+=1
            u,e=sigmas(fs)
            if u==e:eq.append(n)
            if len(fs)==3 and sorted(a for _,a in fs)==[1,1,2]:
                triples+=1
                assert u!=e, (n,fs)
    assert eq==[1,20,45],eq
    for n in eq:
        print(n, factors(n,spf), sigmas(factors(n,spf)))
    for p in [2,3,5,7,11,31,71,127]:
        if p>2:
            half=(p*p+1)//2
            assert (p*p+1)==2*half
            assert (p*p+1)%(p-1)!=0 or p in (2,3)
    print(f'VERIFY_OK: n<= {LIMIT}; omega<=4 tested={low}; p^2*q*r instances={triples}; matches={eq}')

if __name__=='__main__': main()
