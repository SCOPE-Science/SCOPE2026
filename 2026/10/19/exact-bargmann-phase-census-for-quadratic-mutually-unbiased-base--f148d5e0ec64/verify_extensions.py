"""Exact-field-model numerical cross-check for the odd-extension MUB triple phase census.

Uses the explicit quotient F_9 = F_3[u]/(u^2+1), not external packages.
This exhaustive finite test is supplemental to the uniform algebraic proof.
"""
from itertools import permutations, product
from collections import Counter
import cmath
import math

p=3
q=9

def unpack(x): return (x%3,x//3)
def add(x,y):
    a,b=unpack(x);c,d=unpack(y)
    return (a+c)%3+3*((b+d)%3)
def neg(x):
    a,b=unpack(x)
    return (-a)%3+3*((-b)%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b=unpack(x);c,d=unpack(y)
    return ((a*c-b*d)%3)+3*((a*d+b*c)%3)
def pw(x,n):
    r=1
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
def inv(x):
    assert x!=0
    return pw(x,q-2)
def trace(x):
    return (2*(x%3))%3
def chi(x):
    return 0 if x==0 else (1 if pw(x,4)==1 else -1)
def psi(x):
    return cmath.exp(2j*math.pi*trace(x)/3)
def dot(v,w):
    return sum(a.conjugate()*b for a,b in zip(v,w))

def basis_vector(a,b):
    if a==9:
        return [1.+0j if x==b else 0j for x in range(9)]
    return [psi(add(mul(a,mul(x,x)),mul(b,x)))/3 for x in range(9)]

def prediction(a,b,c,i,j,k):
    # Normalized oriented Bargmann invariant for pairwise distinct bases.
    while a!=9 and (a==9 or b==9 or c==9):
        a,b,c=b,c,a
        i,j,k=j,k,i
    if a==9:
        A=sub(c,b)
        s=add(i,mul(sub(k,j),inv(mul(2,A))))
        z=neg(mul(A,mul(s,s)))
        return chi(A)*psi(z),z
    A=sub(b,a)
    B=sub(c,b)
    K=mul(mul(A,B),add(A,B))
    t=sub(mul(B,sub(j,i)),mul(A,sub(k,j)))
    z=neg(mul(mul(t,t),inv(mul(4%3,K))))
    return chi(K)*psi(z),z

def check():
    assert all(add(x,neg(x))==0 for x in range(q))
    assert all(mul(x,inv(x))==1 for x in range(1,q))
    assert sum(chi(x) for x in range(1,q))==0
    zeta=cmath.exp(2j*math.pi/3)
    vec={(a,i):basis_vector(a,i) for a in range(10) for i in range(9)}
    ip={(a,i,b,j):dot(vec[a,i],vec[b,j])
        for a in range(10) for b in range(10) if a!=b
        for i in range(9) for j in range(9)}
    counts=Counter(); tested=0
    for a,b,c in permutations(range(10),3):
        for i,j,k in product(range(9),repeat=3):
            w=27*ip[a,i,b,j]*ip[b,j,c,k]*ip[c,k,a,i]
            expect,z=prediction(a,b,c,i,j,k)
            assert abs(w-expect)<3e-8, (a,b,c,i,j,k,w,expect)
            candidates=[(sgn,t) for sgn in (-1,1) for t in range(3)]
            tags=[tag for tag in candidates if abs(w-tag[0]*(zeta**tag[1]))<3e-8]
            assert len(tags)==1, (w,tags)
            counts[tags[0]]+=1
            tested+=1
    B=10*9*8
    M=lambda s,t:sum(1 for z in range(1,q) if chi(z)==s and trace(z)==t)
    for s in (-1,1):
        for t in range(3):
            expected=B*q*q*M(s,t)+(B*q*q//2 if t==0 else 0)
            assert counts[s,t]==expected,(s,t,counts[s,t],expected)
    assert len(counts)==6 and tested==B*q**3
    # Extension-field trace/Gauss sum formulas, even extension degree r=2.
    S=[sum(chi(z) for z in range(q) if trace(z)==t) for t in range(3)]
    assert S==[2,-1,-1],S
    print('VERIFY_OK extension_field=F9 exhaustive_bargmann_triples=',tested,'phases=',dict(sorted(counts.items())))

if __name__=='__main__': check()
