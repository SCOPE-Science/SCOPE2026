#!/usr/bin/env python3
"""Exact algebraic certificate and independent face-by-face checks for box-surface chord dispersion.
Uses only the Python standard library. Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product
from random import Random

Z=(0,0,0)
def const(n): return {Z:F(n)}
def var(i):
    t=[0,0,0];t[i]=1
    return {tuple(t):F(1)}
def add(*ps):
    out={}
    for p in ps:
        for m,v in p.items():out[m]=out.get(m,F(0))+v
    return {m:v for m,v in out.items() if v}
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
    out={}
    for x,ux in p.items():
        for y,uy in q.items():
            z=tuple(t+s for t,s in zip(x,y))
            out[z]=out.get(z,F(0))+ux*uy
    return {m:v for m,v in out.items() if v}
def power(p,k):
    out=const(1)
    for _ in range(k):out=mul(out,p)
    return out
def formula(a,b,c):
    H=add(mul(a,b),mul(a,c),mul(b,c))
    B=mul(mul(a,b),c)
    T=add(a,b,c)
    A2=add(power(a,2),power(b,2),power(c,2))
    A3=add(power(a,3),power(b,3),power(c,3))
    A4=add(power(a,4),power(b,4),power(c,4))
    Q=add(mul(A2,H),scale(mul(B,T),2))
    W=add(scale(mul(power(A2,2),power(H,2)),5),
          scale(mul(A4,power(H,2)),14),
          scale(mul(mul(A3,B),H),56),
          scale(mul(mul(mul(A2,T),B),H),20),
          scale(mul(A2,power(B,2)),40))
    return Q,W

def moments_from_formula(A):
    a,b,c=map(F,A);H=a*b+b*c+a*c;B=a*b*c
    S=a*a+b*b+c*c;T=a+b+c;A3=a**3+b**3+c**3;A4=a**4+b**4+c**4
    Q=S*H+2*B*T
    W=5*S*S*H*H+14*A4*H*H+56*A3*B*H+20*S*T*B*H+40*S*B*B
    m2=2*Q/(3*H)
    m4=2*(5*Q*Q+W)/(45*H*H)
    return m2,m4

def moments_facewise(A):
    a=list(map(F,A));H=a[0]*a[1]+a[0]*a[2]+a[1]*a[2]
    p=[a[(i+1)%3]*a[(i+2)%3]/(2*H) for i in range(3)]
    faces=[(i,sgn) for i in range(3) for sgn in [-1,1]]
    total2=F(0);total4=F(0)
    for i,si in faces:
        for j,sj in faces:
            t2=[];t4=[]
            for k in range(3):
                def raw(i,si,k,pow):
                    if i==k:return (si*a[k])**pow
                    if pow%2:return F(0)
                    return a[k]**pow/F(pow+1)
                X=[F(1)]+[raw(i,si,k,q) for q in range(1,5)]
                Y=[F(1)]+[raw(j,sj,k,q) for q in range(1,5)]
                t2.append(X[2]+Y[2]-2*X[1]*Y[1])
                t4.append(X[4]+Y[4]+6*X[2]*Y[2]-4*X[3]*Y[1]-4*X[1]*Y[3])
            d2=sum(t2)
            d4=sum(t4)+2*sum(t2[k]*t2[m] for k in range(3) for m in range(k+1,3))
            weight=p[i]*p[j]
            total2+=weight*d2;total4+=weight*d4
    return total2,total4

def sample(A,N,seed):
    rng=Random(seed);a=list(map(float,A));H=a[0]*a[1]+a[0]*a[2]+a[1]*a[2]
    p=[a[(i+1)%3]*a[(i+2)%3]/H for i in range(3)]
    def point():
        r=rng.random();i=next(k for k in range(3) if r<sum(p[:k+1]))
        x=[rng.uniform(-v,v) for v in a]
        x[i]=a[i] if rng.random()<0.5 else -a[i]
        return x
    m2=m4=0.
    for _ in range(N):
        X=point();Y=point();d2=sum((x-y)**2 for x,y in zip(X,Y))
        m2+=d2;m4+=d2*d2
    return m2/N,m4/N

if __name__=='__main__':
    a,b,c=(var(i) for i in range(3))
    Q,W=formula(a,b,c)
    Q2=power(Q,2)
    lo=scale(add(scale(W,75),scale(Q2,-649)),F(1,4))
    hi=scale(add(scale(Q2,19),scale(W,-1)),F(1,4))
    # Universal upper certificate: every monomial has positive coefficient.
    assert len(hi)==15 and all(v>0 and v.denominator==1 for v in hi.values())
    # Universal lower certificate: by symmetry order a >= b >= c > 0,
    # substitute a=w+v+u, b=w+v, c=w, with u,v>=0 and w>0.
    u,v,w=(var(i) for i in range(3))
    aa=add(u,v,w);bb=add(v,w);cc=w
    Qa,Wa=formula(aa,bb,cc)
    low_ordered=scale(add(scale(Wa,75),scale(power(Qa,2),-649)),F(1,4))
    assert len(low_ordered)==39
    assert all(z>0 and z.denominator==1 for z in low_ordered.values())
    assert not any(i==0 and j==0 for (i,j,k) in low_ordered)
    assert any(k==6 and i==2 and j==0 for (i,j,k) in low_ordered)
    # Confirm both certificates exactly match the normalized moment ratio.
    assert all((75*W.get(k,F(0))-649*Q2.get(k,F(0)))==4*lo.get(k,F(0)) for k in set(W)|set(Q2)|set(lo))
    assert all((19*Q2.get(k,F(0))-W.get(k,F(0)))==4*hi.get(k,F(0)) for k in set(W)|set(Q2)|set(hi))
    # Independent exact face-pair conditioning, not using covariance shortcuts.
    cases=[[1,1,1],[1,2,3],[2,7,8],[1,1,100],[F(5,4),F(10,3),1]]
    for side in cases:
        assert moments_from_formula(side)==moments_facewise(side),(side,moments_from_formula(side),moments_facewise(side))
    m2,m4=moments_from_formula([1,1,1])
    assert m4/(m2*m2)==F(512,375)
    for sides in cases:
        m2,m4=moments_from_formula(sides)
        assert F(512,375)<=m4/(m2*m2)<F(12,5)
    # Sharp unattained upper bound: for a=t,b=c=1, Q has leading 2t^3
    # and W has leading 76t^6. Therefore K tends (5*4+76)/(10*4)=12/5.
    q_large,w_large=formula(add(var(0),const(1)),const(1),const(1))
    def top(poly):return max(i for (i,j,k),val in poly.items() if val)
    assert top(q_large)==3 and top(w_large)==6
    assert q_large.get((3,0,0))==2 and w_large.get((6,0,0))==76
    for idx,sides in enumerate([[1,1,1],[2,1,1],[2,3,5]]):
        true2,true4=map(float,moments_from_formula(sides))
        est2,est4=sample(sides,80000,20261031+idx)
        assert abs(est2/true2-1)<0.035 and abs(est4/true4-1)<0.045,(sides,est2,est4,true2,true4)
    print('VERIFY_OK upper_monomials=%d lower_ordered_monomials=%d exact_face_pair_cases=%d seeded_pairs=%d' % (len(hi),len(low_ordered),len(cases),3*80000))
