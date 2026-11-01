#!/usr/bin/env python3
"""Exact rational checks for a piecewise-affine first-entry theorem.

Finite rational partition checks support, but do not replace, the proof.
"""
from fractions import Fraction as F
from math import exp, log


def cells(p,m,b):
    B=sum(m**j for j in range(p))
    R=sum(m**j for j in range(p-1))
    assert 1/B < b < 1/R
    d=(m*R+1)*b/m-1/m
    a0=(1-b)/m
    a1=b*R
    assert d==a1-a0 and d>0
    C=[]
    for j in range(p):
        lo=b*sum(m**i for i in range(j))
        hi=(1-b*sum(m**i for i in range(p-j-1)))/m**(p-j-1)
        C.append((lo,hi))
    U=[]
    for s in range(p-1):
        j=p-1-s
        lo=(1-b*sum(m**i for i in range(p-j)))/m**(p-j)
        hi=b*sum(m**i for i in range(j))
        U.append((lo,hi))
    # C0,U_(p-2),C1,...,U0,C(p-1) partition the interval.
    ordered=[]
    for j in range(p):
        ordered.append(('C',j,C[j]))
        if j<p-1: ordered.append(('U',p-2-j,U[p-2-j]))
    assert ordered[0][2][0]==0 and ordered[-1][2][1]==1
    assert all(ordered[i][2][1]==ordered[i+1][2][0]
               for i in range(len(ordered)-1))
    A=sum(m**-s for s in range(p-1))
    q=A*d
    assert all(U[s][1]-U[s][0]==d/m**s for s in range(p-1))
    assert all(C[j][1]-C[j][0]==(1-q)*m**j/B for j in range(p))
    return ordered,U,C,d,q


def verify(p,m,b,nmax):
    m,b=F(m),F(b)
    ordered,U,C,delta,q=cells(p,m,b)
    A=sum(m**-s for s in range(p-1))
    v=[m**-s/A for s in range(p-1)]
    c=1-q
    B=sum(m**j for j in range(p))
    # exact rational coefficients of c/(1-q sum_s v_s z^(s+1))
    predicted=[c]
    for n in range(1,nmax+1):
        predicted.append(q*sum(v[s]*predicted[n-s-1]
                               for s in range(min(p-2,n-1)+1)))
    hits=[C[j][1]-C[j][0] for j in range(p)]
    assert sum(hits)==predicted[0]
    # Survivors: tuples (original interval endpoints, slope, offset, current cell index).
    alive=[(U[s][0],U[s][1],F(1),F(0),s) for s in range(p-1)]
    assert sum(hi-lo for lo,hi,_,_,_ in alive)==q
    verified=1
    for n in range(1,nmax+1):
        fresh=[]
        hits=[F(0) for _ in range(p)]
        for lo,hi,aa,bb,s in alive:
            if s>0:
                # On U_-s the original map uses the increasing first arm.
                a2,b2=m*aa,m*bb+b
                assert sorted((a2*lo+b2,a2*hi+b2))==list(U[s-1])
                fresh.append((lo,hi,a2,b2,s-1))
                continue
            # U0 is the decreasing middle branch, onto [0,1].
            a2,b2=-aa/delta,-(bb-C[-1][0])/delta
            assert {a2*lo+b2,a2*hi+b2}=={F(0),F(1)}
            for typ,j,(tl,th) in ordered:
                x=(tl-b2)/a2
                y=(th-b2)/a2
                left,right=sorted((x,y))
                assert lo<=left<right<=hi
                if typ=='C':
                    hits[j]+=right-left
                else:
                    fresh.append((left,right,a2,b2,j))
        mass=sum(hits)
        assert mass==predicted[n], (p,m,b,n,mass,predicted[n])
        assert all(hits[j]==mass*m**j/B for j in range(p))
        # Survival probability = 1 - P(T <= n), starting from uniform on [0,1].
        assert sum(hi-lo for lo,hi,_,_,_ in fresh)==1-sum(predicted[:n+1])
        verified+=len(alive)+len(fresh)+len(ordered)
        alive=fresh
    # First-return inverse similarities phi_s from U0 to disjoint subintervals of U0.
    branches=[]
    u0lo,u0hi=U[0]
    x1=C[-1][0]
    for s in range(p-1):
        S_s=sum(m**j for j in range(s))
        r=delta/m**s
        # phi_s(w)=x1-delta*(w-b*S_s)/m**s
        offset=x1+delta*b*S_s/m**s
        z0=offset-r*u0hi
        z1=offset-r*u0lo
        assert u0lo<z0<z1<u0hi
        assert z1-z0==r*(u0hi-u0lo)
        # The first iterate reaches U_-s, then s increasing-arm iterates reach U0.
        for z,w in ((z0,u0hi),(z1,u0lo)):
            y=(x1-z)/delta
            assert U[s][0]<=y<=U[s][1]
            assert m**s*y+b*S_s==w
        branches.append((z0,z1))
    branches.sort()
    assert all(branches[i][1]<branches[i+1][0]
               for i in range(len(branches)-1))
    # Numerical root sanity only; analytically the dimension is the Moran root.
    r=[float(delta/m**s) for s in range(p-1)]
    lo,hi=0.0,1.0
    assert sum(r)>0 and sum(r)<1 and len(r)>=2
    for _ in range(90):
        mid=(lo+hi)/2
        if sum(a**mid for a in r)>1: lo=mid
        else: hi=mid
    dimension=(lo+hi)/2
    assert 0<dimension<1 and abs(sum(a**dimension for a in r)-1)<1e-13
    mu=sum(F(s+1)*v[s] for s in range(p-1))
    second=sum(F((s+1)**2)*v[s] for s in range(p-1))
    mean=q*mu/c
    variance=q*(second-mu*mu)/c+q*mu*mu/(c*c)
    assert mean>=0 and variance>=0
    print('PASS',{'p':p,'m':str(m),'b':str(b),'nmax':nmax,
                  'first_hit_checks':nmax+1,'final_surviving_cells':len(alive),
                  'exact_mean':str(mean),'exact_variance':str(variance),
                  'exact_survival_at_nmax':str(sum(a1-a0 for a0,a1,_,_,_ in alive)),
                  'partition_arithmetic_checks':verified, 'moran_dimension_approx':format(dimension,'.12f')})


def main():
    verify(3,F(2),F(1,5),9)
    verify(4,F(3,2),F(1,7),7)
    verify(5,F(2),F(1,20),6)
    print('PASS exact-rational first-entry and independent phase checks')

if __name__=='__main__':
    main()
