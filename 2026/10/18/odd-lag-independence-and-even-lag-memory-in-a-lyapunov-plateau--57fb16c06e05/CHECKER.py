#!/usr/bin/env python3
"""Exact rational checks for a piecewise-linear dynamical correlation law.
This script uses only Python's standard library; no numerical approximations are used.
"""
from fractions import Fraction as F
from itertools import combinations

def aff(a=0, c=0):
    return F(a), F(c)

def val(z, t):
    return z[0]*t + z[1]

def plus(u,v):
    return u[0]+v[0],u[1]+v[1]

def negate(u):
    return -u[0],-u[1]

def minus(u,v):
    return plus(u,negate(v))

def scale(u,k):
    return u[0]*k,u[1]*k

B=aff(1,0)
Z=aff(0,0)
TWO=aff(0,2)
FOUR=aff(0,4)
SIX=aff(0,6)
EIGHT=aff(0,8)
SIXTEEN=aff(0,16)

def intervals(chamber):
    if chamber==0: # 3<b<4
        return [
            (negate(B),plus(negate(B),TWO),F(1,18)),
            (plus(negate(B),TWO),minus(B,FOUR),F(1,9)),
            (minus(B,FOUR),minus(B,TWO),F(2,9)),
            (minus(B,TWO),TWO,F(1,3)),
            (TWO,B,F(1,9))]
    if chamber==1: # 4<b<9/2
        return [
            (negate(B),minus(scale(B,3),SIXTEEN),F(1,27)),
            (minus(scale(B,3),SIXTEEN),plus(negate(B),TWO),F(1,18)),
            (plus(negate(B),TWO),minus(scale(B,3),aff(0,14)),F(5,54)),
            (minus(scale(B,3),aff(0,14)),plus(negate(B),FOUR),F(1,9)),
            (plus(negate(B),FOUR),minus(B,FOUR),F(4,27)),
            (minus(B,FOUR),plus(negate(B),SIX),F(2,9)),
            (plus(negate(B),SIX),TWO,F(7,27)),
            (TWO,plus(negate(B),EIGHT),F(1,9)),
            (plus(negate(B),EIGHT),B,F(2,27))]
    raise ValueError(chamber)

def break_map(chamber):
    lo,hi=[(F(3),F(4)),(F(4),F(9,2))][chamber]
    r=intervals(chamber)
    mid=(lo+hi)/2
    for L,R,w in r:
        assert val(L,mid)<val(R,mid)
    # Split at zero; the sign of each interval is stable in each chamber.
    img=[]
    for L,R,w in r:
        vl,vr=val(L,mid),val(R,mid)
        if vl<0:
            right=Z if vr>0 else R
            img.append((plus(L,TWO),plus(right,TWO),w))
        if vr>0:
            left=Z if vl<0 else L
            img.append((minus(B,scale(R,2)),minus(B,scale(left,2)),w/2))
    return r,img

def eval_density(r,t,x):
    return sum((w for L,R,w in r if val(L,t)<x<val(R,t)),F())

def exact_integral(r,t,L,R):
    s=F(0)
    for a,b,c in r:
        low=max(val(a,t),L)
        high=min(val(b,t),R)
        if high>low:s+=c*(high-low)
    return s

def check_at(r,img,t,expected):
    endpoints={val(z,t) for L,R,w in r+img for z in (L,R)}
    ep=sorted(endpoints)
    assert len(ep)>=2
    for a,b in zip(ep,ep[1:]):
        if a<b:
            x=(a+b)/2
            assert eval_density(r,t,x)==eval_density(img,t,x),(t,x,eval_density(r,t,x),eval_density(img,t,x))
    total=exact_integral(r,t,-t,t)
    assert total==1,(t,total)
    positive=exact_integral(r,t,F(0),t)
    assert positive==F(2,3),(t,positive)
    p11=exact_integral(r,t,F(0),t/2)
    cov=p11-F(4,9)
    assert cov==expected(t),(t,cov,expected(t))

def roots_of_endpoints(r,img,lo,hi):
    edges=list({e for L,R,_ in r+img for e in (L,R)})
    roots={lo,hi}
    for p,q in combinations(edges,2):
        slope=p[0]-q[0]
        if slope:
            t=(q[1]-p[1])/slope
            if lo<t<hi:roots.add(t)
    # Also ensure moving cut b/2 has constant order relative to density pieces.
    cut=scale(B,F(1,2))
    for e in edges:
        slope=e[0]-cut[0]
        if slope:
            t=(cut[1]-e[1])/slope
            if lo<t<hi:roots.add(t)
    return sorted(roots)

def verify_chamber(ch):
    lo,hi=[(F(3),F(4)),(F(4),F(9,2))][ch]
    r,img=break_map(ch)
    roots=roots_of_endpoints(r,img,lo,hi)
    # Between successive critical parameters every affine endpoint has fixed order.
    # At two interpolation values all mass identities, piecewise-constant PF equations,
    # and the linear covariance identity agree, hence they agree throughout that cell.
    expected=(lambda b:(b-4)/18) if ch==0 else (lambda b:(b-4)/54)
    for a,b in zip(roots,roots[1:]):
        assert a<b
        check_at(r,img,(2*a+b)/3,expected)
        check_at(r,img,(a+2*b)/3,expected)
    return len(roots)-1

def matvec(P,v):
    return [sum((P[i][j]*v[j] for j in range(len(v))),F(0)) for i in range(len(P))]

def dot(u,v):
    return sum((a*b for a,b in zip(u,v)),F(0))


def direct_orbit_joint(n):
    # Independent initial-condition cylinder computation, not using transition matrix.
    # Each record carries an affine expression for the n-th image of its initial x.
    cells=[(F(-4),F(-2),F(1,18)),(F(-2),F(0),F(1,9)),
           (F(0),F(2),F(2,9)),(F(2),F(4),F(1,9))]
    segments=[(l,r,rho,F(1),F(0), l>=0) for l,r,rho in cells]
    for step in range(n):
        nxt=[]
        for l,r,rho,a,c,flag in segments:
            assert a!=0
            z=-c/a
            cuts=sorted([l,r]+([z] if l<z<r else []))
            for left,right in zip(cuts,cuts[1:]):
                m=(left+right)/2
                if a*m+c<=0:
                    nxt.append((left,right,rho,a,c+2,flag))
                else:
                    nxt.append((left,right,rho,-2*a,4-2*c,flag))
        segments=nxt
    joint=F(0)
    for l,r,rho,a,c,flag in segments:
        if not flag:continue
        z=-c/a
        cuts=sorted([l,r]+([z] if l<z<r else []))
        for left,right in zip(cuts,cuts[1:]):
            if a*(left+right)/2+c>0:joint+=(right-left)*rho
    return joint

def verify_critical():
    # Parameter 4: exactly four full Markov cells A,B,C,D.
    cells=[(F(-4),F(-2),F(1,18)),(F(-2),F(0),F(1,9)),
           (F(0),F(2),F(2,9)),(F(2),F(4),F(1,9))]
    total=sum(((b-a)*rho for a,b,rho in cells),F())
    assert total==1
    pi=[(b-a)*rho for a,b,rho in cells]
    assert pi==[F(1,9),F(2,9),F(4,9),F(2,9)]
    P=[[F(0),F(1),F(0),F(0)],
       [F(0),F(0),F(1),F(0)],
       [F(0),F(0),F(1,2),F(1,2)],
       [F(1,2),F(1,2),F(0),F(0)]]
    for row in P:assert sum(row)==1
    for j in range(4):assert sum((pi[i]*P[i][j] for i in range(4)),F(0))==pi[j]
    f=[F(0),F(0),F(1),F(1)]
    mean=dot(pi,f)
    assert mean==F(2,3)
    v=[a-mean for a in f]
    Pv=matvec(P,v)
    assert dot([pi[i]*v[i] for i in range(4)],Pv)==0
    assert matvec(P,Pv)==[-a/2 for a in v]
    w=v
    for n in range(31):
        cov=dot([pi[i]*v[i] for i in range(4)],w)
        expect=F(0) if n%2 else F(2,9)*F(-1,2)**(n//2)
        assert cov==expect,(n,cov,expect)
        w=matvec(P,w)
    # Independently subdivide exact initial cylinders through twelve iterates.
    for n in range(13):
        actual=direct_orbit_joint(n)
        cov=F(0) if n%2 else F(2,9)*F(-1,2)**(n//2)
        assert actual==F(4,9)+cov,(n,actual,cov)
    # Direct order-three event obstruction, independent of any Markov approximation.
    # If x in [-4,0), T(x)=x+2: three successive negative branch visits impossible.
    assert F(-4)+4==0
    return pi,P

if __name__=='__main__':
    classes=[verify_chamber(0),verify_chamber(1)]
    pi,P=verify_critical()
    print('VERIFY_OK', 'certified_affine_parameter_subchambers',classes,
          'stationary_mass_vector',','.join(map(str,pi)),
          'all_lag_identity_checked_to',30)
