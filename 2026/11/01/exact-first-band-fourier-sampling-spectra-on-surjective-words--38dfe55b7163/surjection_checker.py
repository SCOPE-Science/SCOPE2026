"""Exact pair-moment and Gram-sector checks for onto-word Fourier sampling.
Run: python surjection_checker.py
Requires Python 3.9+, standard library only.
"""
from itertools import product
from fractions import Fraction

def stirling(n,k):
    if k < 0 or k > n: return 0
    if n == k == 0: return 1
    v=[0]*(k+1);v[0]=1
    for i in range(1,n+1):
        w=[0]*(k+1)
        for j in range(1,min(i,k)+1): w[j]=j*v[j]+v[j-1]
        v=w
    return v[k]

def check(n,q):
    onto=[x for x in product(range(q),repeat=n) if len(set(x))==q]
    N=len(onto); S=stirling(n,q)
    assert N==math_factorial(q)*S,(n,q,N,S)
    theta=Fraction(stirling(n-1,q-1),(q-1)*S)
    pairs=0
    for i in range(n):
        for j in range(n):
            for a in range(q):
                for b in range(q):
                    count=sum((w[i]==a and w[j]==b) for w in onto)
                    found=Fraction(count,N)
                    if i==j:
                        predicted=Fraction(int(a==b),q)
                    elif a==b:
                        predicted=Fraction(stirling(n-1,q),q*S)
                    else:
                        predicted=Fraction(S-stirling(n-1,q),q*(q-1)*S)
                    assert found==predicted, (n,q,i,j,a,b,found,predicted)
                    pairs+=1
    Llow=1-(n-1)*theta;Lhigh=1+theta
    assert Lhigh>1 and (Llow==0 if n==q else Llow>0)
    assert (n==q+1)==(Llow==Fraction(1,q+1) and Lhigh==Fraction(q+2,q+1)) if n>=q+1 else True
    return N,pairs,str(theta),str(Llow),str(Lhigh)

def math_factorial(k):
    p=1
    for i in range(2,k+1): p*=i
    return p

if __name__=='__main__':
    total=0
    for q in range(2,5):
        for n in range(q,min(q+4,9)):
            N,pairs,t,low,high=check(n,q)
            total+=pairs
            print(f'q={q} n={n} onto={N} pair_tests={pairs} theta={t} low={low} high={high}')
    print(f'PASS exact moment checks={total}')
