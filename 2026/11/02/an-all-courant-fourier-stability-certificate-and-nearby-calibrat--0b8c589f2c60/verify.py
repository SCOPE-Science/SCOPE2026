#!/usr/bin/env python3
"""Exact-rational Fourier certificate for a 5-stage blended RK transport method.
Only the Python standard library is needed. All polynomial coefficients are exact.
"""
from fractions import Fraction as Q
from math import comb

# Sparse polynomials in the variables c,T, keyed by (degree_c,degree_T).
def mon(i=0,j=0,a=1):
    return {(i,j):Q(a)} if a else {}
def add(*polys):
    d={}
    for p in polys:
        for ij,v in p.items(): d[ij]=d.get(ij,Q(0))+v
    return {ij:v for ij,v in d.items() if v}
def mul(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items(): out[(i+k,j+l)]=out.get((i+k,j+l),Q(0))+x*y
    return {ij:v for ij,v in out.items() if v}
def scale(a,v): return {ij:x*Q(v) for ij,x in a.items() if x*v}
def power(a,n):
    v=mon()
    for _ in range(n):v=mul(v,a)
    return v

one=mon();c=mon(1);T=mon(0,1)
# Fifth-order face stencil has Fourier symbol q:
# Re(q)=16T^3/15, Im(q)^2 = 4T(1-T)(8T^2+10T+15)^2/225.
A=scale(power(T,3),Q(16,15))
S=add(scale(power(T,2),8),scale(T,10),scale(one,15))
B2=scale(mul(mul(T,add(one,scale(T,-1))),power(S,2)),Q(4,225))
# z=-c*q; let u=Re(z), v2=Im(z)^2.
u=scale(mul(c,A),-1)
v2=mul(power(c,2),B2)
R=add(one,u,scale(add(power(u,2),scale(v2,-1)),Q(1,2)),
      scale(add(power(u,3),scale(mul(u,v2),-3)),Q(1,6)))
Ibr=add(one,u,scale(power(u,2),Q(1,2)),scale(v2,Q(-1,6)))
F=add(one,scale(add(power(R,2),mul(v2,power(Ibr,2))),-1))
assert all(i>=1 and j>=2 for (i,j) in F), 'factor c*T^2 failed'
H={(i-1,j-2):v for (i,j),v in F.items()}
assert max(i for i,j in H)==5 and max(j for i,j in H)==13
# We certify H>=0 for 0<=c<=10/7, 0<=T<=1 by two rectangular
# Bernstein expansions, split once at T=1/2.
N=13; M=5
powers=[[Q(0) for j in range(M+1)] for i in range(N+1)]
for (ic,it),v in H.items(): powers[it][ic]=v*Q(10,7)**ic
bern=[[sum(powers[a][d]*Q(comb(i,a),comb(N,a))*Q(comb(j,d),comb(M,d))
           for a in range(i+1) for d in range(j+1))
       for j in range(M+1)] for i in range(N+1)]
# de Casteljau split of degree-13 Bernstein polynomial at midpoint.
lo=[[Q(0) for j in range(M+1)] for i in range(N+1)]
hi=[[Q(0) for j in range(M+1)] for i in range(N+1)]
for j in range(M+1):
    work=[bern[i][j] for i in range(N+1)]
    lo[0][j]=work[0];hi[N][j]=work[-1]
    for k in range(1,N+1):
        work=[(work[i]+work[i+1])/2 for i in range(len(work)-1)]
        lo[k][j]=work[0];hi[N-k][j]=work[-1]
for name,coef in [('T in [0,1/2]',lo),('T in [1/2,1]',hi)]:
    flat=[v for row in coef for v in row]
    assert len(flat)==84 and min(flat)>=0, name
    print(name,'coefficients=',len(flat),'zeros=',sum(x==0 for x in flat),
          'minimum=',min(flat),'minimum_positive=',min(x for x in flat if x>0))
# Exact crossing at the Fourier phase xi=pi/2 when high-C calibration
# coefficient gamma is lowered from 7/10 to 69/100.
a=Q(100,69); v2=(a*Q(22,15))**2; u=-a*Q(2,15)
real=1+u+(u*u-v2)/2+(u**3-3*u*v2)/6
imagbr=1+u+u*u/2-v2/6
excess=real*real+v2*imagbr*imagbr-1
assert excess==Q(14399294983760,708051067974441) and excess>0
print('calibration 0.69 limiting |R|^2-1=',excess)
# Numerically independent checks of the tableau factorization, and of q.
import cmath
import random
rng=random.Random(20261026)
stencil={2:-1/20,1:1/2,0:1/3,-1:-1,-2:1/4,-3:-1/30}
Arows=[[0]*5 for _ in range(5)]
for _ in range(1000):
    theta=rng.random();C=0.1+100*rng.random();xi=2*3.141592653589793*rng.random()
    qmode=sum(w*cmath.exp(1j*k*xi) for k,w in stencil.items())
    Tx=(1-cmath.cos(xi).real)/2
    assert abs(qmode.real-16*Tx**3/15)<1e-12
    assert abs(qmode.imag-(cmath.sin(xi).real)*(8*Tx**2+10*Tx+15)/15)<1e-12
    z=-C*qmode
    Arows[1][0]=theta/2
    Arows[2][0]=theta/2;Arows[2][1]=1-theta
    Arows[3][0]=theta/2;Arows[3][1]=Arows[3][2]=(1-theta)/4
    Arows[4][0]=theta/2;Arows[4][1]=Arows[4][2]=(1-theta)/6
    Arows[4][3]=2*(1-theta)/3;Arows[4][4]=theta/2
    stages=[]
    for i in range(5):
        stages.append((1+z*sum(Arows[i][j]*stages[j] for j in range(i)))/(1-z*Arows[i][i]))
    zz=(1-theta)*z
    fact=(1+theta*z/2)/(1-theta*z/2)*(1+zz+zz**2/2+zz**3/6)
    assert abs(stages[-1]-fact)<3e-9
print('1000 tableau-factorization checks passed')
print('All exact certificates and auxiliary numerical comparisons PASSED')
