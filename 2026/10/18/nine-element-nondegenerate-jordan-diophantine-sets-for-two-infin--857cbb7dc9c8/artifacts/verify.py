#!/usr/bin/env python3
"""Exact arithmetic verifier for two base Jordan-D(N) nine-tuples and scaling."""
from itertools import combinations
from math import isqrt
Q=(1,3,8,120)

def sq(x):
    a,b,d=x
    return (a*a,b*(a+d),d*d)

def jordan(x,y):
    a,b,d=x; e,f,g=y
    v=b*(e+g)+f*(a+d)
    assert v%2==0
    return (a*e,v//2,d*g)

def root(z):
    a,b,d=z
    v=isqrt(a); w=isqrt(d)
    assert v*v==a and w*w==d,(a,b,d)
    for x in (v,-v):
      for y in (w,-w):
        if x+y and b%(x+y)==0:
          return (x,b//(x+y),y)
        if x+y==0 and b==0:
          return (x,0,y)
    raise AssertionError(('no square root',z))

def nine(B,R):
    v=[(a,2*B,0) for a in Q]+[(0,2*B,a) for a in Q]+[(0,2*B,0)]
    n=(1,R,1)
    return v,n

def check(V,N):
    assert len(V)==9 and len(set(V))==9 and all(v!=(0,0,0) for v in V)
    for i,j in combinations(range(len(V)),2):
        product=jordan(V[i],V[j]); assert product!=(0,0,0),(i,j)
        target=tuple(x+y for x,y in zip(product,N))
        s=root(target)
        assert sq(s)==target,(i,j,target,s)
    return 36

def scale(V,N,t,degree):
    if degree==1:
        return ([(a,t*b,d) for a,b,d in V], (N[0],t*N[1],N[2]))
    return ([(2*a,t*b,2*d) for a,b,d in V], (4,2*t*N[1],4))

if __name__=='__main__':
    total=0
    for B,R in [(18,6),(10,10)]:
        V,N=nine(B,R);total+=check(V,N)
        for t in [-11,-3,-1,1,2,3,11]:
            for degree in [1,2]:
                S,T=scale(V,N,t,degree);total+=check(S,T)
        print('PASS base',B,R,'and signed scale tests')
    print('PASS total certified pairs',total)
    for x,y in combinations(Q,2):
        h=isqrt(x*y+1); assert h*h==x*y+1
        cs=[]
        for B,R in ((18,6),(10,10)):
            u=B*(x+y)+R
            cs.append((u,[(sgn,denom) for sgn,denom in [(1,h+1),(-1,h-1)] if denom and u%denom==0]))
            assert cs[-1][1]
        print('D1 pair',x,y,'h',h,'details',cs)
