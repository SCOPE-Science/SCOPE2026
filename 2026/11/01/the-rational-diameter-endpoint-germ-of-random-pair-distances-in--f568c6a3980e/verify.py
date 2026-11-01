#!/usr/bin/env python3
"""Exact coefficient arithmetic and seeded cone-integration diagnostics.
No symbolic or finite computation substitutes for the analytic tail proof.
"""
import math
from collections import defaultdict
from fractions import Fraction as F
import numpy as np

def columns(d):
    i,j=0,1
    cols=[]
    for k in range(d+1):
        if k==i: continue
        w=2 if k==j else 1
        v=[F(0)]*(d+1);v[k]=F(1,w);v[i]=F(-1,w);cols.append(v)
    for k in range(d+1):
        if k==j:continue
        w=2 if k==i else 1
        v=[F(0)]*(d+1);v[j]=F(1,w);v[k]=F(-1,w);cols.append(v)
    return cols

def exact(d):
    cols=columns(d);m=2*d
    sq=sum(sum(x*x for x in c) for c in cols)
    tot=[sum(c[j] for c in cols) for j in range(d+1)]
    norm2=sum(x*x for x in tot)
    qavg=(sq+norm2)/F(4*d*(2*d+1))
    beta=4*d*qavg-d
    coeff=F(d*(d+1)*2**(2*d-2)*math.factorial(d)**2,math.factorial(2*d))
    assert len(cols)==m
    assert sq==4*d-3,(d,sq)
    assert norm2==2*d*d,(d,norm2)
    assert beta==F(3*(d-1),2*d+1)
    assert coeff>0
    return coeff,beta

def exact_q_moments(d,order=2):
    """Integrate powers of the rational quadratic form over Dirichlet(1^m)."""
    cs=columns(d); m=2*d
    terms={}
    for i in range(m):
        for j in range(i,m):
            dot=sum(x*y for x,y in zip(cs[i],cs[j]))
            if dot:
                e=[0]*m
                e[i]+=1
                e[j]+=1
                terms[tuple(e)]=dot if i<j else dot/2
    poly={(0,)*m:F(1)}
    out=[]
    for k in range(order+1):
        deg=2*k
        mom=F(0)
        scale=F(math.factorial(m-1),math.factorial(m+deg-1))
        for powers, coefficient in poly.items():
            prod=math.prod(math.factorial(z) for z in powers)
            mom+=coefficient*scale*prod
        out.append(mom)
        if k<order:
            nxt=defaultdict(F)
            for powers, coefficient in poly.items():
                for e,v in terms.items():
                    nxt[tuple(a+b for a,b in zip(powers,e))]+=coefficient*v
            poly=nxt
    return out

def lagrange_identity_test():
    """Compare independent Catalan-root expansion against Lagrange formula."""
    m=8; order=5; q=F(1,7)
    # r(s)=s + q*s*s + 2*q*q*s*s*s +... , check r(s)^m.
    def mul(a,b):
        c=[F(0)]*(len(a))
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if i+j<len(c): c[i+j]+=x*y
        return c
    n=m+order+1
    root=[F(0)]*n
    for k in range(1,n):
        root[k]=F(math.comb(2*k-2,k-1),k)*q**(k-1)
    result=[F(0)]*n
    result[0]=F(1)
    for _ in range(m): result=mul(result,root)
    for k in range(order+1):
        required=F(m,m+k)*math.comb(m+2*k-1,k)*q**k
        assert result[m+k]==required,(m,k,result[m+k],required)

def simulate(d,t,seed=7313,n=130000):
    rng=np.random.default_rng(seed+d)
    m=2*d
    th=rng.dirichlet(np.ones(m),size=n)
    col=np.asarray([[float(x) for x in c] for c in columns(d)])
    v=th@col
    q=(v*v).sum(axis=1)/2
    s=2*t-t*t
    # The near-zero root of r-q*r*r=s: numerically stable formula.
    rad=1-4*q*s
    assert np.min(rad)>0
    r=2*s/(1+np.sqrt(rad))
    # Single ordered pair probability is (d!)²/(4(2d)!) E[r**(2d)].
    p=(d*(d+1)*math.factorial(d)**2/(4*math.factorial(2*d)))*np.mean(r**m)
    leading,beta=exact(d)
    quotient=p/(float(leading)*t**(2*d))
    return quotient,float(beta),p

def main():
    for d in range(2,17):
        coeff,beta=exact(d)
        print('exact',d,str(coeff),str(beta))
    assert exact(4)==(F(128,7), F(1))
    qmom=exact_q_moments(4,2)
    assert qmom==[F(1),F(5,16),F(533,5280)], qmom
    m=8
    gamma=F(m*(m-1),8) -m*(m+1)*qmom[1] +4*F(m,m+2)*math.comb(m+3,2)*qmom[2]
    assert gamma==F(34,15), gamma
    lagrange_identity_test()
    print('quartic-Dirichlet moment and second relative coefficient:',qmom, gamma)
    for d in (4,5,7):
        vals=[]
        for t in (0.004,0.002,0.001):
            q,b,p=simulate(d,t)
            vals.append((q-1)/t)
            assert abs((q-1)/t-b)<0.04,(d,t,q,b)
        print('cone_quadrature',d,'estimated slopes',vals,'target',b)
    print('VERIFICATION PASSED')
if __name__=='__main__':main()
