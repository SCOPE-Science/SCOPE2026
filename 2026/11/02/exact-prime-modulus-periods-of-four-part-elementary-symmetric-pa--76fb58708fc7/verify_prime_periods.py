#!/usr/bin/env python3
"""Exact checks for the four-part elementary-symmetric partition period theorem.
Requires Python 3 and SymPy; no external data or network access.
"""
import sympy as s
from itertools import combinations
q=s.symbols('q')
B=s.Matrix([[1,0,0,0],[1,1,0,0],[1,1,1,0],[1,1,1,1]])
w=[4,3,2,1]
E=(s.Matrix(w)*s.Matrix(w).T-B.T*B)/2
h=[q**4/(1-q**4),1/(1-q**3),1/(1-q**2),1/(1-q)]
J=[s.cancel(q*s.diff(h[i],q)/w[i]) for i in range(4)]
K=[s.cancel(q*s.diff(J[i],q)/w[i]) for i in range(4)]
F=0
for i in range(4):
    for j in range(4):
        term=E[i,j]*(K[i] if i==j else J[i]*J[j])
        for k in range(4):
            if k!=i and k!=j: term*=h[k]
        F+=term
N=q**4*(11*q**12+25*q**11+50*q**10+72*q**9+106*q**8+126*q**7+146*q**6+121*q**5+95*q**4+57*q**3+34*q**2+15*q+6)
D=(1-q)**6*(1+q)**4*(1+q**2)**3*(1+q+q**2)**3
assert s.cancel(F-N/D)==0, 'symbolic series identity'
res=[s.resultant(N,f,q) for f in [q-1,q+1,q**2+1,q**2+q+1]]
assert res==[864,32,144,36],res
P=s.Poly(D,q);Q=s.Poly(N,q)
d=list(reversed([int(c) for c in P.all_coeffs()]))
a=[0]*801
for n in range(801):
    a[n]=(int(Q.nth(n)) if n<=Q.degree() else 0)-sum(d[k]*a[n-k] for k in range(1,min(len(d),n+1)))
# Independent partition enumeration: positive weakly increasing parts x<=y<=z<=w.
for n in range(4,72):
    direct=0
    for x in range(1,n//4+1):
        for y in range(x,(n-x)//3+1):
            for z in range(y,(n-x-y)//2+1):
                w4=n-x-y-z
                if w4>=z:
                    v=(x,y,z,w4)
                    direct+=sum(v[i]*v[j] for i,j in combinations(range(4),2))
    assert direct==a[n],(n,direct,a[n])
for p in [5,7,11,13,17,19,31,41]:
    period=300 if p==5 else 12*p
    assert all((a[n+period]-a[n])%p==0 for n in range(0,min(801-period,300))),(p,'not a period')
    assert all(any((a[n+h]-a[n])%p for n in range(min(801-h,period))) for h in range(1,period) if period%h==0),(p,'not least')
print('VERIFY_OK: exact generating function; resultants',res,'; independent 68 partition sizes; prime periods 5,7,11,13,17,19,31,41')
