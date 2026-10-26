"""Exact tests of cyclic-point/terminal-count formulas in uniform random mappings."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, comb, sqrt, exp, pi

def cyclic_count(f):
    n=len(f)
    marked=[False]*n
    cyc=set()
    for i in range(n):
        if marked[i]:continue
        seq=[]; pos={};j=i
        while not marked[j] and j not in pos:
            pos[j]=len(seq);seq.append(j);j=f[j]
        if j in pos:cyc.update(seq[pos[j]:])
        for v in seq:marked[v]=True
    return len(cyc)

def falling(n,r):
    z=1
    for j in range(r):z*=n-j
    return z

def theoretical_factorial(n,k,r):
    s=n-k
    if r>s:return Fraction(0)
    if r==0:return Fraction(1)
    return Fraction(falling(s,r)*(n-r)**(s-1),n**(s-1)) if s else Fraction(0)

def exact_test():
    num=0
    for n in range(2,8):
        d=Counter();marg=Counter()
        for f in product(range(n),repeat=n):
            ind=[0]*n
            for t in f:ind[t]+=1
            z=ind.count(0);k=cyclic_count(f)
            d[(k,z)]+=1;marg[k]+=1
        assert sum(marg.values())==n**n
        for k in range(1,n+1):
            p=Fraction(marg[k],n**n)
            expected=Fraction(falling(n,k)*k,n**(k+1))
            assert p==expected,(n,k,p,expected)
            for r in range(n-k+1):
                true=Fraction(sum(cnt*falling(z,r) for (kk,z),cnt in d.items() if kk==k),marg[k])
                theo=theoretical_factorial(n,k,r)
                assert true==theo,(n,k,r,true,theo)
                num+=1
        az=Fraction(sum(z*count for (k,z),count in d.items()),n**n)
        ak=Fraction(sum(k*count for (k,z),count in d.items()),n**n)
        cross=Fraction(sum(z*k*count for (k,z),count in d.items()),n**n)
        prev=sum(Fraction(falling(n-1,r),(n-1)**r) for r in range(1,n))
        expectedcov=n*Fraction((n-1)**n,n**n)*(prev-ak)
        assert cross-az*ak==expectedcov
        assert cross-az*ak<0
        print('EXACT_ENUMERATION_PASS',n,n**n,len(d),num)

def asymptotic_test():
    mu=sqrt(pi/2)
    q=exp(-1)-2*exp(-2)
    for n in [200,1000,10000,60000]:
        # Distribution of cyclic count by recurrence, avoiding factorial overflow.
        masses=[];weight=1.0
        for k in range(1,n+1):
            weight *= (n-k+1)/n
            pk=(k/n)*weight
            masses.append(pk)
            if weight<1e-35: break
        norm=sum(masses)
        ec=sum((i+1)*p for i,p in enumerate(masses))
        ec2=sum((i+1)**2*p for i,p in enumerate(masses))
        fmeans=[]
        ezc=0.0
        for j,p in enumerate(masses,1):
            v=(n-j)*exp((n-j-1)*__import__('math').log1p(-1/n)) if j<n else 0.0
            ezc+=p*j*v
            fmeans.append(v)
        ez=n*exp(n*__import__('math').log1p(-1/n))
        cov=ezc-ec*ez
        varc=ec2-ec**2
        varz=n*exp(n*__import__('math').log1p(-1/n))*(1-exp(n*__import__('math').log1p(-1/n)))
        varz+=n*(n-1)*(exp(n*__import__('math').log1p(-2/n))-exp(2*n*__import__('math').log1p(-1/n)))
        corr=cov/sqrt(varc*varz)
        print('ASYMPTOTIC_DIAGNOSTIC',n,round(cov/sqrt(n),7),round(corr*sqrt(n),7),round(norm,9))
    print('EXPECTED_LIMIT',-mu/(2*exp(1)),-mu/(2*exp(1)*sqrt((2-pi/2)*q)))

if __name__=='__main__':
    exact_test()
    asymptotic_test()
    print('VERIFY_OK')
