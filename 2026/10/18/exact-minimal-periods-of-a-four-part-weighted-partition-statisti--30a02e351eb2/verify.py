#!/usr/bin/env python3
"""Standalone exact checks for weighted four-part partition periods (stdlib only)."""
from math import comb, gcd

def add(*polys):
    out=[0]*max(map(len,polys))
    for p in polys:
        for i,x in enumerate(p):out[i]+=x
    return trim(out)
def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def mul(*polys):
    res=[1]
    for p in polys:
        q=[0]*(len(res)+len(p)-1)
        for i,x in enumerate(res):
            for j,y in enumerate(p):q[i+j]+=x*y
        res=q
    return trim(res)
def powpoly(p,n):
    res=[1]
    for _ in range(n):res=mul(res,p)
    return res
def scale(p,n,shift=0):return [0]*shift+[n*x for x in p]
def exact_coeffs(N,D,size):
    a=[]
    for n in range(size):
        a.append((N[n] if n<len(N) else 0)-sum(D[j]*a[n-j] for j in range(1,min(n,len(D)-1)+1)))
    return a
def mod_coeffs(N,D,size,m):
    a=[]
    for n in range(size):
        a.append(((N[n] if n<len(N) else 0)-sum(D[j]*a[n-j] for j in range(1,min(n,len(D)-1)+1)))%m)
    return a

def build():
    P=[6,15,34,57,95,121,146,126,106,72,50,25,11]
    N=[0]*4+P
    f1=[-1,1]; f2=[1,1]; f3=[1,1,1]; f4=[1,0,1]
    D=mul(powpoly(f1,6),powpoly(f2,4),powpoly(f3,3),powpoly(f4,3))
    B=[]
    for i in range(1,5):
        b=[0]*(i+1);b[0]=1;b[i]=-1;B.append(b)
    base=mul(*(powpoly(b,2) for b in B))
    raw=[0]
    raw=add(raw,scale(base,6,4))
    for i in range(1,5):
        fs=[powpoly(B[j],2 if j!=i-1 else 1) for j in range(4)]
        raw=add(raw,scale(mul(*fs),3*i,4+i))
    for i in range(1,5):
        for j in range(i+1,5):
            fs=[powpoly(B[k],1 if k in [i-1,j-1] else 2) for k in range(4)]
            raw=add(raw,scale(mul(*fs),i*(j-1),4+i+j))
    for i in range(1,5):
        fs=[powpoly(B[j],0 if j==i-1 else 2) for j in range(4)]
        one_plus=[0]*(i+1);one_plus[0]=1;one_plus[i]=1
        raw=add(raw,scale(mul(one_plus,*fs),comb(i,2),4+i))
    assert raw==mul(N,powpoly(f1,6),powpoly(f2,2)),(raw[:20],mul(N,powpoly(f1,6),powpoly(f2,2))[:20])
    assert D[0]==1 and len(N)==17 and len(D)==23
    print('EXACT_RATIONAL_GENERATING_IDENTITY_OK; numerator_degree=16 denominator_degree=22')
    return N,D

def brute(limit):
    out=[0]*(limit+1)
    for y4 in range((limit-4)//4+1):
      for y3 in range((limit-4-4*y4)//3+1):
       for y2 in range((limit-4-4*y4-3*y3)//2+1):
        for y1 in range(limit-3-4*y4-3*y3-2*y2):
         n=4+y1+2*y2+3*y3+4*y4
         parts=[1+y1+y2+y3+y4,1+y2+y3+y4,1+y3+y4,1+y4]
         e2=sum(parts[i]*parts[j] for i in range(4) for j in range(i+1,4))
         out[n]+=e2
    return out

def divisors(n):return [d for d in range(1,n+1) if n%d==0]
def expected(m):
    assert gcd(m,6)==1 and m>1
    return 60*m if m%5==0 else 12*m

def main():
    N,D=build()
    a=exact_coeffs(N,D,75)
    b=brute(74)
    assert a==b,[(n,x,y) for n,(x,y) in enumerate(zip(a,b)) if x!=y][:4]
    print('INDEPENDENT_FOUR_PART_ENUMERATION_OK 75 coefficients')
    for m in [5,7,11,13,17,25,35,49,77,125]:
        T=expected(m)
        q=mod_coeffs(N,D,2*T+31,m)
        assert all(q[n]==q[n+T] for n in range(T+31)),(m,T,'not period')
        smaller=[d for d in divisors(T) if d<T and all(q[n]==q[n+d] for n in range(T))]
        assert not smaller,(m,T,'unexpected divisor period',smaller)
        print(f'MODULAR_PERIOD_CHECK_OK modulus={m} minimal_candidate={T} tested_terms={2*T+31}')
    print('VERIFIED')
if __name__=='__main__':main()
