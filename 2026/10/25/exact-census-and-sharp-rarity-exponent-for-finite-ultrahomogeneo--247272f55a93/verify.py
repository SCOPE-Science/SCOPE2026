from fractions import Fraction
from math import factorial
from collections import defaultdict
from itertools import product

def types(N):
    for k in range(1,N+1):
      def rec(levels, bs):
        Q=sum(levels)
        if k*Q>N:return
        a=k
        for j,b in enumerate(bs):
          a*=factorial(b)**(k*levels[j])
        yield (k*Q,a,k,tuple(bs))
        bmax=(N//k-Q)//levels[-1]
        for b in range(1,bmax+1):
          yield from rec(levels+[levels[-1]*b],bs+[b])
      yield from rec([1],[])

def poly_exp_monom(N, s, a):
    c={0:Fraction(1)}
    if s<=N:
      den=1
      for m in range(1,N//s+1):
        den*=a*m
        c[s*m]=Fraction(1,den)
    return c

def poly_mul(A,B,N):
    D=defaultdict(Fraction)
    for i,a in A.items():
      for j,b in B.items():
        if i+j<=N:D[i+j]+=a*b
    return dict(D)

def exact_coeff(N):
    types_by_k=defaultdict(list)
    for s,a,k,bs in types(N): types_by_k[k].append((s,a,bs))
    A={0:Fraction(1)}
    for k in range(1,N+1):
      B=defaultdict(Fraction);B[0]=1
      for s,a,bs in types_by_k[k]:
        term=poly_exp_monom(N,s,a)
        for i,c in term.items():
          if i:B[i]+=c
      A=poly_mul(A,B,N)
    return [int(A.get(i,0)*factorial(i)) for i in range(N+1)],types_by_k

def uh(f):
    n=len(f); indeg=[0]*n
    for j in f:indeg[j]+=1
    counts={}
    for i in range(n):
      pos={};x=i;k=0
      while x not in pos:
        pos[x]=k;k+=1;x=f[x]
      key=(k-pos[x],pos[x])
      if key in counts and counts[key]!=indeg[i]:return False
      counts[key]=indeg[i]
    return True

if __name__=='__main__':
    N=12
    c,byk=exact_coeff(N)
    print('EGF counts',c)
    for n in range(1,7):
      total=sum(uh(f) for f in product(range(n),repeat=n))
      assert total==c[n],(n,total,c[n])
      print('n',n,'count',total,'fraction',Fraction(total,n**n))
    print('UH_ENUMERATION_OK')
