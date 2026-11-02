#!/usr/bin/env python3
"""Independent ideal enumeration for the Lie algebra of a star graph over prime fields."""
from itertools import product,combinations
from collections import Counter

def gb(n,k,q):
    if k<0 or k>n:return 0
    num=1;den=1
    for i in range(k):num*=q**(n-i)-1;den*=q**(k-i)-1
    return num//den

def predicted(n,q):
    d=2*n+1; hist=Counter()
    for k in range(n+1):
        hist[n+k+1]+=gb(n,k,q)*q**(n-k)
        for j in range(k,n+1):
            hist[k+j]+=gb(n,k,q)*gb(n-k,j-k,q)*q**(k*(n-j))
    return tuple(hist[t] for t in range(d+1))

def bases(d,k,q):
    # canonical row-reduced echelon matrices spanning all k-subspaces
    for pivots in combinations(range(d),k):
        slots=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,d) if j not in pivots]
        for vals in product(range(q),repeat=len(slots)):
            rows=[[0]*d for _ in range(k)]
            for i,p in enumerate(pivots):rows[i][p]=1
            for (i,j),x in zip(slots,vals): rows[i][j]=x
            yield rows,pivots

def in_span(v,rows,pivots,q):
    w=list(v)
    for row,p in zip(rows,pivots):
        a=w[p]%q
        if a:
            w=[(x-a*y)%q for x,y in zip(w,row)]
    return not any(w)

def bracket(a,b,n,q):
    # basis indices h=0; leaves 1..n; centers n+1..2n
    out=[0]*(2*n+1)
    for i in range(n):out[n+1+i]=(a[0]*b[1+i]-b[0]*a[1+i])%q
    return out

def observed(n,q):
    d=2*n+1; hist=Counter()
    std=[[int(i==j) for j in range(d)] for i in range(d)]
    for k in range(d+1):
      for rows,piv in bases(d,k,q):
        good=True
        for x in rows:
          for y in std:
            if not in_span(bracket(x,y,n,q),rows,piv,q):good=False;break
          if not good:break
        if good:hist[k]+=1
    return tuple(hist[t] for t in range(d+1))

if __name__=='__main__':
    for n,q in [(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)]:
        a=observed(n,q);b=predicted(n,q)
        assert a==b,(n,q,a,b)
        print('CASE',n,q,'HIST',a,'SUM',sum(a))
    for n,q in [(4,257),(5,257),(6,257),(7,257)]:
        h=predicted(n,q); total=sum(h)
        target=[n] if n%2==0 else [n-1,n,n+1]
        mass=sum(h[d] for d in target)
        assert 0 < total-mass < total//20,(n,q,h)
        if n%2: assert max(h[d] for d in target)-min(h[d] for d in target)<total//20
        print('HIGH_FIELD',n,q,'IN_TARGET',str(mass)+'/'+str(total))
    print('VERIFY_OK')
