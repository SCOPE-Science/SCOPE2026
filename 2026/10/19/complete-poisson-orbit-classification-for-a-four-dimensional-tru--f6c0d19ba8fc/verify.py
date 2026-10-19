#!/usr/bin/env python3
"""Standalone finite-field verification of Poisson brackets on a short complete intersection.
Requires Python 3 standard library only; independent direct quotient-ring operations.
"""
from itertools import product

def field(q):
    assert q in (2, 4)
    def mul(a,b):
        if q==2: return a & b
        out=0
        while b:
            if b&1:out ^=a
            b >>=1
            a <<=1
            if a&4:a ^=7 # t^2+t+1
        return out
    def inv(a):
        if not a:raise ZeroDivisionError
        return next(z for z in range(1,q) if mul(a,z)==1)
    return mul,inv

def run(q):
    mul,inv=field(q)
    xor=lambda *args:__import__('functools').reduce(int.__xor__, args,0)
    Z=(0,0,0,0)
    def times(a,b):
        return (mul(a[0],b[0]), xor(mul(a[0],b[1]),mul(a[1],b[0])),
                xor(mul(a[0],b[2]),mul(a[2],b[0])),
                xor(mul(a[0],b[3]),mul(a[3],b[0]),mul(a[1],b[2]),mul(a[2],b[1])))
    def add(a,b): return tuple(x^y for x,y in zip(a,b))
    def scale(c,p):return tuple(mul(c,v) for v in p)
    def dx(p):return (p[1],0,p[3],0)
    def dy(p):return (p[2],p[3],0,0)
    all_h=list(product(range(q),repeat=4))
    perms=[]
    for a,b,d,e in product(range(q),repeat=4):
        det=mul(a,e)^mul(b,d)
        if not det:continue
        for c,f in product(range(q),repeat=2):
            X=(0,a,b,c);Y=(0,d,e,f)
            jac=add(times(dx(X),dy(Y)),times(dy(X),dx(Y)))
            assert jac[0]==det and jac[3]==0
            # In char. 2 the nilpotent part of Jacobian squares to 0.
            dinv=inv(det)
            one=(1,0,0,0)
            jacinv=scale(dinv,add(one,scale(dinv,add(jac,(det,0,0,0)))))
            assert times(jac,jacinv)==one
            perms.append((X,Y,jacinv))
    assert len(perms)==q*q*(q*q-1)*(q*q-q)
    def image(h,p):
        X,Y,jacinv=p
        sub=add((h[0],0,0,0),add(scale(h[1],X),add(scale(h[2],Y),scale(h[3],times(X,Y)))))
        return times(sub,jacinv)
    # Verify alternation and the Jacobi identity on the algebra basis for every h.
    basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    for h in all_h:
        def bracket(v,w):
            return times(h,add(times(dx(v),dy(w)),times(dy(v),dx(w))))
        for v in basis:
            assert bracket(v,v)==Z
        for v,w,t in product(basis,repeat=3):
            jac=add(bracket(v,bracket(w,t)),
                    add(bracket(w,bracket(t,v)),bracket(t,bracket(v,w))))
            assert jac==Z
    # Check all isomorphisms respect the socle coefficient and orbit fibers.
    for h in all_h:
        orbit={image(h,p) for p in perms}
        assert all(t[3]==h[3] for t in orbit)
        target=(1 if h[0]==h[1]==h[2]==0 else (q*q-1 if h[0]==0 else (q-1)*q*q))
        assert len(orbit)==target,(q,h,target,len(orbit))
        # The orbit is exactly the corresponding elementary stratum.
        assert all((t[0]==0)==(h[0]==0) for t in orbit)
        assert all(((t[1],t[2])==(0,0)) == ((h[1],h[2])==(0,0)) for t in orbit) if h[0]==0 else True
    print('FIELD_OK',q,'brackets',len(all_h),'automorphisms',len(perms),'classes',3*q,
          'orbit_sizes',[1,q*q-1,(q-1)*q*q])

if __name__=='__main__':
    for q in (2,4):run(q)
    print('VERIFY_OK')

def run_odd(q):
    assert q in (3,5,7)
    add=lambda a,b:(a+b)%q
    mul=lambda a,b:(a*b)%q
    neg=lambda a:(-a)%q
    def times(a,b):
        return ((a[0]*b[0])%q,
                (a[0]*b[1]+a[1]*b[0])%q,
                (a[0]*b[2]+a[2]*b[0])%q,
                (a[0]*b[3]+a[3]*b[0]+a[1]*b[2]+a[2]*b[1])%q)
    def scale(t,a):return tuple(t*x%q for x in a)
    def deriv_x(a):return (a[1],0,a[3],0)
    def deriv_y(a):return (a[2],a[3],0,0)
    def minus(a,b):return tuple((x-y)%q for x,y in zip(a,b))
    perms=[]
    for a,b,d,e in product(range(q),repeat=4):
        det=(a*e-b*d)%q
        if not det or a*b%q or d*e%q:continue
        for c,f in product(range(q),repeat=2):
            X=(0,a,b,c);Y=(0,d,e,f)
            assert times(X,X)==(0,0,0,0)
            assert times(Y,Y)==(0,0,0,0)
            J=minus(times(deriv_x(X),deriv_y(Y)),times(deriv_y(X),deriv_x(Y)))
            assert J[0]==det
            perms.append((X,Y,pow(det,-1,q)))
    assert len(perms)==2*(q-1)**2*q*q
    basis=[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
    for z in range(q):
        h=(0,0,0,z)
        def bracket(v,w):
            return times(h, minus(times(deriv_x(v),deriv_y(w)),
                                   times(deriv_y(v),deriv_x(w))))
        for v in basis: assert bracket(v,v)==(0,0,0,0)
        for v,w,t in product(basis,repeat=3):
            a=bracket(v,bracket(w,t));b=bracket(w,bracket(t,v));c=bracket(t,bracket(v,w))
            assert all((a[i]+b[i]+c[i])%q==0 for i in range(4))
    classes=[]
    for z in range(q):
        images={scale(dinv,times(X,times(Y,(z,0,0,0))))[3] for X,Y,dinv in perms}
        assert images=={z,(-z)%q}
        if z not in {v for orbit in classes for v in orbit}:classes.append(images)
    assert len(classes)==(q+1)//2
    print('FIELD_ODD_OK',q,'brackets',q,'automorphisms',len(perms),'classes',len(classes),
          'orbit_sizes',[len(c) for c in classes])

if __name__=='__main__':
    for q in (3,5,7):run_odd(q)
    print('VERIFY_ALL_OK')
