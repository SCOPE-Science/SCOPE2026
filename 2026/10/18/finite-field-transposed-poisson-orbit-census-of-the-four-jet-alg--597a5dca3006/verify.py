#!/usr/bin/env python3
"""Independent finite-field checks of transposed-Poisson four-jet orbit census."""
from itertools import product
from collections import defaultdict, Counter

def mul(x,y,p):
    z=[0]*4
    for i in range(4):
        for j in range(4-i):z[i+j]=(z[i+j]+x[i]*y[j])%p
    return tuple(z)

def add(x,y,p):return tuple((a+b)%p for a,b in zip(x,y))
def sub(x,y,p):return tuple((a-b)%p for a,b in zip(x,y))
def scale(x,a,p):return tuple((a*u)%p for u in x)
def power(x,n,p):
    z=(1,0,0,0)
    for _ in range(n):z=mul(z,x,p)
    return z

def subst(x,f,p):
    powers=[power(f,n,p) for n in range(4)]
    r=(0,0,0,0)
    for a,v in zip(x,powers):r=add(r,scale(v,a,p),p)
    return r

def deriv(x,abc,p):
    f=(0,)+abc
    der=(0,0,0,0)
    for j,a in enumerate(x):
        if j: der=add(der,scale(mul(power((0,1,0,0),j-1,p),f,p),j*a,p),p)
    return der

def bracket(x,y,d,p):return sub(mul(x,deriv(y,d,p),p),mul(y,deriv(x,d,p),p),p)

def composition_inv(phi,p):
    # inverse of phi(t)=ut+vt^2+wt^3 as a truncated series
    u,v,w=phi[1:];ui=pow(u,-1,p)
    return (0,ui,(-v*pow(ui,3,p))%p, (2*v*v*pow(ui,5,p)-w*pow(ui,4,p))%p)

def conjugate_direct(abc,phi,p):
    inv=composition_inv(phi,p)
    assert subst(inv,phi,p)==(0,1,0,0)
    # Action is phi * D * phi^-1 on the algebra generators
    return subst(deriv(inv,abc,p),phi,p)[1:]

def conjugate_formula(abc,phi,p):
    a,b,c=abc;u,v,w=phi[1:];ui=pow(u,-1,p)
    return (a,(u*b-a*v*ui)%p,(u*u*c+2*a*((v*v*ui*ui-w*ui)%p))%p)

def normal_form(abc,p):
    a,b,c=abc
    if a:return ('linear',a)
    if b:return ('quadratic',(c*pow(b,-2,p))%p)
    if c:
        sq={x*x%p for x in range(1,p)}
        return ('cubic','square' if c in sq else 'nonsquare')
    return ('zero',0)

def run(p):
    uvals=range(1,p)
    autos=[(0,u,v,w) for u in uvals for v in range(p) for w in range(p)]
    ds=list(product(range(p),repeat=3))
    assert len(autos)==(p-1)*p*p
    orbits=defaultdict(list)
    for abc in ds:orbits[normal_form(abc,p)].append(abc)
    assert len(orbits)==2*p+2
    for abc in ds:
        # numeric formula is independently compared with polynomial conjugation
        for phi in autos:
            d1=conjugate_direct(abc,phi,p)
            d2=conjugate_formula(abc,phi,p)
            assert d1==d2,(p,abc,phi,d1,d2)
            assert normal_form(abc,p)==normal_form(d1,p)
    for rep, els in orbits.items():
        a=els[0]
        reached={conjugate_direct(a,phi,p) for phi in autos}
        assert reached==set(els),(p,rep, len(reached),len(els))
        typ=rep[0]
        expected={'linear':p*p,'quadratic':p-1,'cubic':(p-1)//2,'zero':1}[typ]
        assert len(els)==expected,(p,rep,len(els),expected)
    # Check Lie Jacobi and transposed-Leibniz conditions on basis vectors
    basis=[tuple(int(i==j) for i in range(4)) for j in range(4)]
    for abc in ds:
        for x,y,z in product(basis,repeat=3):
            if p<=5 or abc in [(0,0,0),(1,2,3),(0,1,1),(0,0,1)]:
                xy=bracket(x,y,abc,p)
                jac=add(add(bracket(x,bracket(y,z,abc,p),abc,p),bracket(y,bracket(z,x,abc,p),abc,p),p),bracket(z,xy,abc,p),p)
                assert jac==(0,0,0,0),(p,abc,'Jacobi')
                tp=sub(scale(mul(z,xy,p),2,p),add(bracket(mul(z,x,p),y,abc,p),bracket(x,mul(z,y,p),abc,p),p),p)
                assert tp==(0,0,0,0),(p,abc,'TP')
    sizes=Counter((k[0],len(v)) for k,v in orbits.items())
    print('PASS',p,'brackets',len(ds),'automorphisms',len(autos),'orbits',len(orbits),'orbit_sizes',dict(sizes))

if __name__=='__main__':
    for p in (3,5,7):run(p)
    print('ALL_TRANSPOSED_POISSON_JET_CHECKS_PASSED')
