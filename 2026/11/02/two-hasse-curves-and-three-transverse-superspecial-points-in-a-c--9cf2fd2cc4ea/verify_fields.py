"""Independent exact GF(7), GF(49) census from sextic coefficients.

Uses the field F7[w]/(w*w+1), irreducible as -1=6 nonsquare in F7.
"""
from collections import Counter

def add(x,y): return ((x[0]+y[0])%7,(x[1]+y[1])%7)
def mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%7,(x[0]*y[1]+x[1]*y[0])%7)
def neg(x):return((-x[0])%7,(-x[1])%7)
def sub(x,y):return add(x,neg(y))
def power(x,n):
    r=(1,0)
    for _ in range(n):r=mul(r,x)
    return r
zero=(0,0); one=(1,0); three=(3,0); four=(4,0)
def coeffs(a,b):
    # Generate power 3 of 1+b*x^2+a*x^4+x^6 and independently
    # read the x^6 and x^12 coefficients.
    f=[zero]*7
    for i,v in ((0,one),(2,b),(4,a),(6,one)):f[i]=v
    r=[one]
    for _ in range(3):
        t=[zero]*(len(r)+len(f)-1)
        for i,v in enumerate(r):
            if v==zero:continue
            for j,w in enumerate(f):
                if w!=zero:t[i+j]=add(t[i+j],mul(v,w))
        r=t
    return r[6],r[12]
def disc(a,b):
    # a*a*b*b-4*a^3-4*b^3-27+18*a*b modulo seven
    ab=mul(a,b)
    return add(add(mul(ab,ab),mul(three,add(power(a,3),power(b,3)))),add(mul(four,ab),one))
def verify(n):
    field=[(x,y) for x in range(7) for y in range(7)] if n==2 else [(x,0) for x in range(7)]
    q=len(field); counts=Counter(); D0=set(); repeated=set()
    for a in field:
      for b in field:
        if disc(a,b)==zero:
          counts['singular']+=1;D0.add((a,b));continue
        x,y=coeffs(a,b)
        counts[(x!=zero)+(y!=zero)]+=1
    for r in field:
      if r==zero:continue
      rinv=power(r,q-2)
      a=sub(power(rinv,2),mul((2,0),r))
      b=sub(power(r,2),mul((2,0),rinv))
      repeated.add((a,b))
    assert D0==repeated
    assert counts['singular']==q-1
    assert counts[0]==3
    assert counts[1]==2*(q-7)
    assert counts[2]==q*q-3*q+12
    print('GF%d_EXACT_INDEPENDENT_CARTIER_CENSUS_OK %s'%(q,dict(counts)))
verify(1)
verify(2)
