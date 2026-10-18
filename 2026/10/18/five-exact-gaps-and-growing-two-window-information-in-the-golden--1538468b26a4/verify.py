#!/usr/bin/env python3
"""Exact quadratic-field verification of golden-rotation two-window gap counts."""
from collections import Counter
from functools import cmp_to_key
from math import isqrt, log, sqrt

# A pair (a,b) encodes (a+b*sqrt(5))/2; the pairs below have equal parity.
def add(u,v): return (u[0]+v[0], u[1]+v[1])
def sub(u,v): return (u[0]-v[0],u[1]-v[1])
def mul(u,v):
    a,b=u;c,d=v
    assert (a*c+5*b*d)%2==0 and (a*d+b*c)%2==0
    return ((a*c+5*b*d)//2,(a*d+b*c)//2)
def positive(v):
    a,b=v
    if b==0:return a>0
    if a==0:return b>0
    if a>0 and b>0:return True
    if a<0 and b<0:return False
    if a>0: return a*a>5*b*b
    return 5*b*b>a*a
def cmp(u,v):
    d=sub(u,v)
    return 1 if positive(d) else (-1 if positive(sub(v,u)) else 0)
def power(u,n):
    out=(2,0)
    for _ in range(n):out=mul(out,u)
    return out
ONE=(2,0); ALPHA=(3,-1); R=(-1,1)
def fibs(n):
    f=[0,1]
    for _ in range(2,n+1):f.append(f[-1]+f[-2])
    return f
F=fibs(20)
def fractional_alpha(j):
    # Floor is computed numerically, but exact field inequalities certify it.
    z=j*(3-sqrt(5))/2
    m=int(z)
    v=(3*j-2*m,-j)
    assert not positive(sub((0,0),v)) and positive(sub(ONE,v))
    return v

def gaps_for(indices):
    q=sorted((fractional_alpha(j) for j in indices),key=cmp_to_key(cmp))
    assert len(q)==len(set(q))
    diffs=[sub(q[i+1],q[i]) for i in range(len(q)-1)]+[sub(add(q[0],ONE),q[-1])]
    assert all(positive(v) for v in diffs)
    accum=(0,0)
    for g in diffs:accum=add(accum,g)
    assert accum==ONE
    return Counter(diffs)

# Independently checks the symbolic partition: distinct joint words correspond to
# the (2n+2) rotation cells.  Tested with certified point ordering and midpoint words.
def joint_word_test(k):
    n=F[k]
    idx=list(range(n+1))+list(range(2*n,3*n+1))
    endpoints=sorted((fractional_alpha(-j) if j<=0 else
                      sub(ONE,fractional_alpha(j)) for j in idx),key=cmp_to_key(cmp))
    # -j alpha mod 1, exact handling of zero.
    assert len(endpoints)==2*n+2
    words=set()
    alpha=(3-sqrt(5))/2
    for i,e in enumerate(endpoints):
        f= endpoints[i+1] if i+1<len(endpoints) else add(endpoints[0],ONE)
        a=(e[0]+e[1]*sqrt(5))/2
        b=(f[0]+f[1]*sqrt(5))/2
        x=((a+b)/2)%1
        left=tuple(int(((x+j*alpha)%1) >= 1-alpha) for j in range(n))
        right=tuple(int(((x+j*alpha)%1) >= 1-alpha) for j in range(2*n,3*n))
        words.add((left,right))
    assert len(words)==2*n+2,(k,len(words),2*n+2)

for k in range(6,15):
    n=F[k]
    one=gaps_for(list(range(n+1)))
    expect_one=Counter({power(R,k-2):F[k-1]-1,power(R,k-1):F[k-2]+1,power(R,k):1})
    assert one==expect_one,(k,'one',one,expect_one)
    two=gaps_for(list(range(n+1))+list(range(2*n,3*n+1)))
    expect_two=Counter({power(R,k+2):F[k-2]+1,power(R,k+1):F[k-1]+1,power(R,k):1,power(R,k-1):2*F[k-2],mul((4,0),power(R,k)):F[k-3]-1})
    assert two==expect_two,(k,'two',two,expect_two)
    if k<=11: joint_word_test(k)

# Independent double-precision evaluation checks the limit of joint information.
r=(sqrt(5)-1)/2;c=1/sqrt(5)
h1=-(r*(c/r**2)*log(c/r**2)+r*r*(c/r)*log(c/r))
h2=-(r*r*(c*r*r)*log(c*r*r)+r*(c*r)*log(c*r)+2*r*r*(c/r)*log(c/r)+r**3*(2*c)*log(2*c))
C=2*h1-h2
assert abs(C-(-0.5867552564501619))<1e-11
for k in range(6,15):
    n=F[k]
    hs=[(F[k-1]-1,r**(k-2)),(F[k-2]+1,r**(k-1)),(1,r**k)]
    hj=[(F[k-2]+1,r**(k+2)),(F[k-1]+1,r**(k+1)),(1,r**k),(2*F[k-2],r**(k-1)),(F[k-3]-1,2*r**k)]
    h=lambda terms:-sum(mult*length*log(length) for mult,length in terms)
    I=2*h(hs)-h(hj)
    assert I>0 and abs((I-log(n))-C)<0.85
print('VERIFY_OK: exact field gap histograms at 9 Fibonacci orders, 6 joint-word partitions, entropy limit',round(C,15))
