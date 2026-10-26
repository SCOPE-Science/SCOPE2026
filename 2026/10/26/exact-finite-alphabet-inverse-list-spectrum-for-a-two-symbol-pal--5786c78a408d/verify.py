#!/usr/bin/env python3
"""Independent finite tests for the q-ary PAL-2 inverse-list census."""
from collections import Counter
from itertools import product
from fractions import Fraction
from math import comb

def add(a,b,scale=1):
    out=a.copy()
    for k,v in b.items():
        out[k]=out.get(k,0)+scale*v
    return {k:v for k,v in out.items() if v}
def shift(a,d):return {k+d:v for k,v in a.items()}

def polynomial_coefficients(q,Nmax):
    # [z^N] of H(z,t) G(z,t)=q(z-(t-1)z^3+(t-1)z^4-(t-1)^2 z^6).
    C=[{} for _ in range(Nmax+1)]
    delta={1:1,0:-1}
    for n in range(1,Nmax+1):
        p={}
        if n>=1:p=add(p,C[n-1],q)
        for lag,sgn in ((2,1),(3,-1),(4,q-1)):
            if n>=lag:
                for exponent,coeff in C[n-lag].items():
                    p=add(p,shift(delta,exponent),sgn*coeff)
        if n==1:p=add(p,{0:q})
        if n==3:p=add(p,delta,-q)
        if n==4:p=add(p,delta,q)
        if n==6:p=add(p,{2:1,1:-2,0:1},-q)
        C[n]=p
    return C

def brute(q,N):
    hist=Counter()
    for y in product(range(q),repeat=N):
        parents=set()
        run_lens=[]; colors=[]
        for a in y:
            if not colors or colors[-1]!=a:
                colors.append(a);run_lens.append(1)
            else:run_lens[-1]+=1
        structural=sum(x>=4 for x in run_lens)
        structural+=sum(run_lens[i]==2 and colors[i-1]==colors[i+1]
                        for i in range(1,len(run_lens)-1))
        for i in range(N-3):
            if y[i]==y[i+3] and y[i+1]==y[i+2]:
                parents.add(y[:i+2]+y[i+4:])
        assert len(parents)==structural, (q,N,y,len(parents),structural)
        hist[len(parents)]+=1
    return hist

total=0
for q,top in ((2,12),(3,9),(4,8),(5,7)):
    C=polynomial_coefficients(q,top)
    for N in range(4,top+1):
        hist=brute(q,N)
        total+=q**N
        assert dict(hist)==C[N], (q,N,dict(hist),C[N])
        assert max(hist)==(N-2)//2,(q,N,'max',max(hist))
        if N>=6 and N%2==0:
            assert hist[(N-2)//2]==q*(q-1),(q,N,'maximizers')
        numerator=sum(v*k for k,v in hist.items())
        formula=Fraction((q*q-1)*N-3*q*q+4,q**4)
        assert Fraction(numerator,q**N)==formula,(q,N,'mean')
    print('q=%d up to length %d: passed'% (q,top))
print('WORDS_CHECKED',total)
print('VERIFY_OK')
