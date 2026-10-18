#!/usr/bin/env python3
"""Exact-rational checks of the three-particle Fleming--Viot current expansion.

Requires Python 3 and SymPy. Run: python check_fv_quintic.py
All assertions use integer/rational arithmetic, without numerical tolerance.
"""
from itertools import product
from sympy import Matrix, Rational, eye, zeros, ones, symbols


def matrices(n):
    eps = symbols('epsilon')
    k = (1-eps, 1, 1+eps)
    states = [(a,b,n-a-b) for a in range(n+1) for b in range(n-a+1)]
    others = [(a,b,n-1-a-b) for a in range(n) for b in range(n-a)]
    tags = list(product(range(3), others))
    cidx = {c:i for i,c in enumerate(states)}
    hidx = {x:i for i,x in enumerate(tags)}
    l = zeros(len(states))
    t = zeros(len(tags))
    for c in states:
        row = cidx[c]
        for a in range(3):
            if not c[a]:
                continue
            for b in range(3):
                if a == b:
                    continue
                dest = list(c); dest[a]-=1; dest[b]+=1
                rate = c[a]+Rational(c[a]*c[b],n-1)*k[a]
                l[row,cidx[tuple(dest)]]+=rate
                l[row,row]-=rate
    def jump(r, target, rate):
        t[r,hidx[target]]+=rate
        t[r,r]-=rate
    for i,d in tags:
        r = hidx[(i,d)]
        for j in range(3):
            if j!=i:
                jump(r,(j,d),1)
        for a in range(3):
            if d[a]==0:
                continue
            for b in range(3):
                if a==b:
                    continue
                dd=list(d);dd[a]-=1;dd[b]+=1
                jump(r,(i,tuple(dd)),d[a])
        t[r,r]-=k[i]
        for a in range(3):
            if d[a]==0:
                continue
            dd=list(d);dd[a]-=1;dd[i]+=1
            t[r,hidx[(i,tuple(dd))]]+=Rational(2*d[a],n-1)*k[a]
            for b in range(3):
                multiplicity=d[b]-(1 if a==b else 0)
                if multiplicity==0:
                    continue
                dd=list(d);dd[a]-=1;dd[b]+=1
                t[r,hidx[(i,tuple(dd))]]+=Rational(d[a]*multiplicity,n-1)*k[a]
            t[r,r]-=d[a]*k[a]
    return states, tags, cidx, hidx, l.subs(eps,0), l.diff(eps), t.subs(eps,0), t.diff(eps)


def current_coefficients(n, through):
    (states, tags, cidx, hidx, L0,L1,T0,T1)=matrices(n)
    a=L0.T.copy(); a[-1,:]=ones(1,len(states))
    anchor=hidx[(0,(n-1,0,0))]
    b=T0.copy(); b[anchor,:]=zeros(1,len(tags));b[anchor,anchor]=1
    inva=a.inv();invb=b.inv()
    p=[];h=[];coeff=[]
    for r in range(through+1):
        yp=zeros(len(states),1) if r==0 else -L1.T*p[-1]
        yp[-1]=1 if r==0 else 0
        yr=zeros(len(tags),1) if r==0 else -T1*h[-1]
        yr[anchor]=Rational(1,n) if r==0 else 0
        pr=inva*yp;hr=invb*yr
        assert L0.T*pr+(zeros(len(states),1) if r==0 else L1.T*p[-1])==zeros(len(states),1)
        assert T0*hr+(zeros(len(tags),1) if r==0 else T1*h[-1])==zeros(len(tags),1)
        assert sum(pr)==(1 if r==0 else 0)
        assert hr[anchor]==(Rational(1,n) if r==0 else 0)
        p.append(pr);h.append(hr)
        z=Rational(0)
        for j in range(r+1):
            for c in states:
                if c[0]:
                    dd=list(c);dd[0]-=1
                    z+=c[0]*p[j][cidx[c]]*h[r-j][hidx[(2,tuple(dd))]]
                if c[2]:
                    dd=list(c);dd[2]-=1
                    z-=c[2]*p[j][cidx[c]]*h[r-j][hidx[(0,tuple(dd))]]
        coeff.append(z)
    return coeff


def colored_absorption_current(k):
    """Independent check: two-color absorbing-chain Dirichlet equation."""
    n=3
    states=[(a,b,3-a-b) for a in range(4) for b in range(4-a)]
    ci={c:i for i,c in enumerate(states)}
    all_s=[(a,b,c,d,e,3-a-b-c-d-e)
           for a in range(4) for b in range(4-a)
           for c in range(4-a-b) for d in range(4-a-b-c)
           for e in range(4-a-b-c-d)]
    mixed=[z for z in all_s if 0<sum(z[:3])<3]
    mi={z:i for i,z in enumerate(mixed)}
    Q=zeros(len(mixed));target=zeros(len(mixed),1)
    for z in mixed:
        row=mi[z]
        for a in range(6):
            if not z[a]:
                continue
            for b in range(6):
                if a==b:
                    continue
                rate=Rational(z[a]*z[b],2)*k[a%3]
                if a//3==b//3 and a%3!=b%3:
                    rate+=z[a]
                if not rate:
                    continue
                zz=list(z);zz[a]-=1;zz[b]+=1;zz=tuple(zz)
                Q[row,row]-=rate
                if sum(zz[:3])==3:
                    target[row]+=rate
                elif sum(zz[:3])!=0:
                    Q[row,mi[zz]]+=rate
    h=Q.inv()*(-target)
    L=zeros(len(states))
    for c in states:
        row=ci[c]
        for a in range(3):
            if not c[a]:
                continue
            for b in range(3):
                if a==b:
                    continue
                rate=c[a]+Rational(c[a]*c[b],2)*k[a]
                dd=list(c);dd[a]-=1;dd[b]+=1
                L[row,row]-=rate
                L[row,ci[tuple(dd)]]+=rate
    B=L.T;B[-1,:]=ones(1,len(states))
    rhs=zeros(len(states),1);rhs[-1]=1
    p=B.inv()*rhs
    def founder(i,d):
        z=[0,0,0]+list(d);z[i]+=1
        return h[mi[tuple(z)]]
    flux=Rational(0)
    for c in states:
        if c[0]:
            dd=list(c);dd[0]-=1
            flux+=p[ci[c]]*c[0]*founder(2,dd)
        if c[2]:
            dd=list(c);dd[2]-=1
            flux-=p[ci[c]]*c[2]*founder(0,dd)
    return flux


if __name__=='__main__':
    coeff=current_coefficients(3,7)
    assert coeff[:5]==[0]*5
    assert coeff[5]==Rational(89,56010528)
    assert coeff[6]==0
    assert coeff[7]==Rational(-410017,1524382530048)
    print('N=3 Taylor coefficients r=0..7:', coeff)
    assert colored_absorption_current((1,2,4))==Rational(421413160,139117744582101)
    print('Independent two-color absorption calculation matches published N=3 benchmark.')
    for eps in (Rational(1,2),Rational(1,3)):
        exact=colored_absorption_current((1-eps,1,1+eps))
        assert exact>0
        print('N=3 exact current at epsilon =',eps,':',exact)
    coeff4=current_coefficients(4,3)
    assert coeff4[:3]==[0]*3
    assert coeff4[3]==-Rational(1,157300)
    print('N=4 cubic coefficient:',coeff4[3])
    print('All exact-rational checks passed.')
