#!/usr/bin/env python3
"""Direct numerical cross-checks of the stated Fourier/Wigner formulas.
All dimensions here are illustrative; the general proof is analytic.
"""
import cmath
import itertools
import math
import random


def add(a,b,p): return tuple((x+y)%p for x,y in zip(a,b))
def mid(a,b,p): return tuple(((x+y)*pow(2,-1,p))%p for x,y in zip(a,b))
def dot(a,b,p): return sum(x*y for x,y in zip(a,b))%p

def sidon(S,p):
    sums=[add(S[i],S[j],p) for i in range(len(S)) for j in range(i,len(S))]
    return len(sums)==len(set(sums))

def direct(S,coeff,p):
    d=len(S[0]);G=list(itertools.product(range(p),repeat=d)); n=len(G)
    psi={x:a for x,a in zip(S,coeff)}
    W=[]
    inv2=pow(2,-1,p)
    for q in G:
        for k in G:
            v=0j
            for s in G:
                u=tuple((q[i]+inv2*s[i])%p for i in range(d))
                w=tuple((q[i]-inv2*s[i])%p for i in range(d))
                v+=psi.get(u,0)*psi.get(w,0).conjugate()*cmath.exp(-2j*math.pi*dot(k,s,p)/p)
            assert abs((v/n).imag)<1e-10,(p,q,k,v)
            W.append((v/n).real)
    assert abs(sum(W)-1)<1e-9
    assert abs(sum(x*x for x in W)-1/n)<1e-9
    return sum(abs(x) for x in W),W

def formula(coeff,p):
    C=1/math.sin(math.pi/(2*p)); ans=1.
    for i in range(len(coeff)):
        for j in range(i+1,len(coeff)):
            a,b=coeff[i],coeff[j]
            angle=cmath.phase(a*b.conjugate());delta=abs(((angle+math.pi/(2*p))%(math.pi/p))-math.pi/(2*p))
            ans+=2*C/p*abs(a*b)*math.cos(delta)
    return ans

def test(p,S):
    assert sidon(S,p)
    m=len(S)
    B=1+(m-1)/(p*math.sin(math.pi/(2*p)))
    # Equal-amplitude quantized phases must attain bound.
    coeff=[cmath.exp(1j*math.pi*(2*i+1)/p)/math.sqrt(m) for i in range(m)]
    observed,_=direct(S,coeff,p)
    assert abs(observed-B)<1e-9,(p,S,observed,B)
    assert abs(formula(coeff,p)-B)<1e-9
    rng=random.Random(17042026+p)
    for trial in range(5):
        raw=[rng.random()*cmath.exp(1j*2*math.pi*rng.random()) for _ in S]
        norm=math.sqrt(sum(abs(x)**2 for x in raw));a=[x/norm for x in raw]
        obs,_=direct(S,a,p)
        calc=formula(a,p)
        assert abs(obs-calc)<1e-9,(p,S,trial,obs,calc)
        assert obs<=B+1e-9
    print('PASS',p,S,'bound',repr(B),'equal',repr(observed),'random tests 5')

if __name__=='__main__':
    test(7,[(0,),(1,),(3,)])
    test(5,[(0,),(1,)])
    test(3,[(0,0),(1,0),(0,1)])
    test(5,[(x,(x*x)%5) for x in range(5)])
    print('PASS all checks')
