#!/usr/bin/env python3
"""Check finite-field ranks of left exterior multiplication by 2-vectors."""
from itertools import combinations,product
from math import comb
from collections import Counter

def rank_mod(M,p):
    if not M:return 0
    a=[row[:] for row in M];nr=len(a);nc=len(a[0]);row=0
    for c in range(nc):
        t=next((i for i in range(row,nr) if a[i][c]%p),None)
        if t is None:continue
        a[row],a[t]=a[t],a[row]
        z=pow(a[row][c]%p,-1,p);a[row]=[(x*z)%p for x in a[row]]
        for i in range(row+1,nr):
            fac=a[i][c]%p
            if fac:a[i]=[(x-fac*y)%p for x,y in zip(a[i],a[row])]
        row+=1
        if row==nr:break
    return row

def gf_ranks_by_degree(c,p):
    total=0
    for j in range(c):
        dom=list(combinations(range(c),j));cod=list(combinations(range(c),j+1));
        m=[[int(set(a).issubset(b)) for a in dom] for b in cod]
        total+=rank_mod(m,p)
    return total

def formula(n,r,p):
    f=[]
    for c in range(r+1):
        f_c=0
        for j in range(c):
            a=min(j,c-j-1)
            f_c+=sum((comb(c,i)-(comb(c,i-1) if i else 0)) for i in range(a+1) if (a+1-i)%p)
        f.append(f_c)
    return (1<<(n-2*r))*sum(comb(r,s)*(1<<s)*f[r-s] for s in range(r+1))

def direct_form(n,p,coeff):
    d=1<<n;M=[[0]*d for _ in range(d)];pairs=list(combinations(range(n),2))
    for s in range(d):
        for a,(i,j) in zip(coeff,pairs):
            if a==0 or ((s>>i)&1) or ((s>>j)&1):continue
            # sign from putting (i,j) in front of sorted monomial s
            sign = -1 if ((s & ((1<<j)-(1<<(i+1)))).bit_count()%2) else 1
            # actually i,j wedge in front of old S: to sort, crossings from each i,j with S less than those -> #s <i + #s<j.
            crossings=(s & ((1<<i)-1)).bit_count()+(s & ((1<<j)-1)).bit_count()
            sign= -1 if crossings%2 else 1
            M[s|(1<<i)|(1<<j)][s]=(M[s|(1<<i)|(1<<j)][s]+sign*a)%p
    return rank_mod(M,p)

def alt_rank(n,p,coeff):
    pairs=list(combinations(range(n),2));A=[[0]*n for _ in range(n)]
    for a,(i,j) in zip(coeff,pairs):A[i][j]=a;A[j][i]=-a
    return rank_mod(A,p)

def canonical_coeff(n,r):
    pairs=list(combinations(range(n),2)); return [1 if (i,j) in [(2*k,2*k+1) for k in range(r)] else 0 for i,j in pairs]

def gauss(n,k,q):
    if k<0 or k>n:return 0
    z=1
    for i in range(k):z=z*(q**(n-i)-1)//(q**(i+1)-1) if False else z
    from functools import reduce
    a=1;b=1
    for i in range(k):a*=q**(n-i)-1;b*=q**(k-i)-1
    return a//b

def multiplicity(n,r,q):
    return gauss(n,2*r,q)* q**(r*(r-1))*__import__('math').prod(q**(2*i-1)-1 for i in range(1,r+1))

def main():
    for p in [2,3,5,7]:
      for n in range(1,9):
       vals=[]
       for r in range(n//2+1):
        expected=formula(n,r,p)
        if n<=7:
         actual=direct_form(n,p,canonical_coeff(n,r))
         assert actual==expected,(p,n,r,actual,expected)
        vals.append(expected)
       assert len(set(vals))==len(vals),(p,n,vals)
       assert sum(multiplicity(n,r,p) for r in range(n//2+1))==p**comb(n,2),(p,n)
       if p==2:
        assert all(formula(n,r,p)==(2**(n-1)*(1-2**(-r))) for r in range(n//2+1))
    for n,p in [(3,2),(4,2),(4,3),(5,2)]:
      d={};pairs=list(combinations(range(n),2));
      for coeff in product(range(p),repeat=len(pairs)):
       ar=alt_rank(n,p,coeff);assert ar%2==0
       dr=direct_form(n,p,coeff)
       assert dr==formula(n,ar//2,p),(n,p,coeff,ar,dr,formula(n,ar//2,p))
       d[ar//2]=d.get(ar//2,0)+1
      assert all(d.get(r,0)==multiplicity(n,r,p) for r in range(n//2+1)),(n,p,d)
      print('EXHAUSTIVE_OK',n,p,len(pairs),len(d),d)
    for n in [2,4,6,8,10]:
      vals=[formula(n,r,2) for r in range(n//2+1)]
      print('CHAR2_SPECTRUM',n,vals)
    print('VERIFY_OK_EXTERIOR_WEDGE')

if __name__=='__main__':main()
