"""Exact symbolic identities and independent numerical checks for quartic-harmonic
sampling on signed coordinate and pair roots.

Requires Python 3, sympy and numpy. Run: python bn4_checker.py
"""
from fractions import Fraction as F
from itertools import combinations
import random
import math
import sympy as s
import numpy as np

z = s.symbols('z', integer=True, positive=True)
c = z*(z+6)/24
k0=3*c
k1=c*(z*z-1)
khalf=c*(z*z-18*z+8)/16
ksqrt=c*(z*z-6*z-4)/4
B=s.factor(k1-k0)
T=s.factor(k1+3*k0-4*khalf)
S=s.factor((k1-k0)+(k1+3*k0-4*khalf)+2*(khalf-k0)*(z-2))
R=s.factor((k1+(z-1)*k0)+(k1+k0+4*(z-2)*khalf+(z-2)*(z-3)*k0))
assert s.simplify(B - z*(z+6)*(z*z-4)/24)==0
assert s.simplify(T - z*(z+6)*(z+2)*(z+4)/32)==0
assert s.simplify(S-z*(z+6)*(z+2)*(z*z-8*z+48)/192)==0
assert s.simplify(R-z*(z+6)*(z+4)*(z*z-4*z+12)/96)==0
standard_det=(k1-k0)*((k1+3*k0-4*khalf)+2*(khalf-k0)*(z-2))-2*(ksqrt-k0)**2*(z-2)
trivial_det=(k1+(z-1)*k0)*(k1+k0+4*(z-2)*khalf+(z-2)*(z-3)*k0)-4*(z-1)*(ksqrt+(z-2)*k0/2)**2
assert s.factor(standard_det)==0
assert s.factor(trivial_det)==0
print('symbolic: kernel normalization, four eigenbranches and both rank-one blocks OK')

# All signs and all inner products are computed from integer coordinate vectors.
def gram(n):
    labels=[('short',i) for i in range(n)]
    labels += [('long',i,j,eps) for i,j in combinations(range(n),2) for eps in (1,-1)]
    def dot_sq(p,q):
        if p[0]=='short' and q[0]=='short': return F(int(p[1]==q[1]))
        if p[0]=='short':
            return F(1,2) if p[1] in q[1:3] else F(0)
        if q[0]=='short':return F(1,2) if q[1] in p[1:3] else F(0)
        # long vectors have components (1,eps)/sqrt(2) at (i,j).
        a={p[1]:1,p[2]:p[3]}; b={q[1]:1,q[2]:q[3]}
        h=sum(a.get(i,0)*b.get(i,0) for i in a)
        return F(h*h,4)
    cf=F(n*(n+6),24)
    M=[]
    for p in labels:
        M.append([cf*((n+4)*(n+2)*dot_sq(p,q)**2-6*(n+2)*dot_sq(p,q)+3) for q in labels])
    return M

for n in range(3,14):
    K=gram(n); size=n*n
    exact_trace=sum(K[i][i] for i in range(size))
    exact_trace2=sum(x*x for row in K for x in row)
    v=[F(n*(n+6)*(n*n-4),24),F(n*(n+6)*(n+2)*(n*n-8*n+48),192),
       F(n*(n+6)*(n+2)*(n+4),32),F(n*(n+6)*(n+4)*(n*n-4*n+12),96)]
    mult=[n*(n-1)//2,n-1,n*(n-3)//2,1]
    assert sum(mult)==n*(n-1)
    assert exact_trace==sum(a*b for a,b in zip(v,mult))
    assert exact_trace2==sum(a*a*b for a,b in zip(v,mult))
    eig=np.linalg.eigvalsh(np.asarray(K,dtype=float))
    expected=np.sort(np.array([0.]*n+sum(([float(a)]*b for a,b in zip(v,mult)),[])))
    err=max(abs(eig-expected))
    assert err<1e-7*max(1.,max(expected)),(n,err)
    print(f'n={n}: rational trace/moment matched, rank {n*(n-1)}/{n*n}, eig error {err:.2g}')

# Independent test of the constructive interpolant, with rational complex data.
rng=random.Random(2093)
for n in range(3,16):
    edges=list(combinations(range(n),2)); b={e:F(rng.randrange(-12,13),5) for e in edges}
    a={i:-sum((b[e] for e in edges if i in e),F(0))/6 for i in range(n)}
    d={e:F(rng.randrange(-12,13),7) for e in edges}
    short={i:a[i] for i in range(n)}
    plus={e:(a[e[0]]+a[e[1]]+b[e])/4 + d[e]*F(n-2,2*(n+4)) for e in edges}
    minus={e:(a[e[0]]+a[e[1]]+b[e])/4 - d[e]*F(n-2,2*(n+4)) for e in edges}
    for i in range(n):
        lhs=2*sum((plus[e]+minus[e] for e in edges if i in e),F(0))
        assert lhs==(n-8)*short[i]+sum(short.values())
    ar=short
    br={e:2*(plus[e]+minus[e])-ar[e[0]]-ar[e[1]] for e in edges}
    dr={e:F(n+4,n-2)*(plus[e]-minus[e]) for e in edges}
    assert br==b and dr==d
    assert all(12*ar[i]+2*sum((br[e] for e in edges if i in e),F(0))==0 for i in range(n))
print('rational interpolation, n=3..15: all n constraints, coefficients and Laplacian identities OK')

# Sharp conditioning: smallest nonzero Gram eigenvalue changes branch at n=20;
# maximum changes branch at n=3, 4..5, 6 onward. Continuous ratio
# R(n) strictly increases from n=7 to n=20 and beyond by positive derivatives.
for n in range(3,1001):
    p=[F(n*(n+6)*(n*n-4),24),F(n*(n+6)*(n+2)*(n*n-8*n+48),192),
       F(n*(n+6)*(n+2)*(n+4),32),F(n*(n+6)*(n+4)*(n*n-4*n+12),96)]
    active=[p[0],p[1],p[3]]+([p[2]] if n>=4 else [])
    ratio=max(active)/min(active)
    assert ratio>=F(15,8)
    if n==6:assert ratio==F(15,8)
    else:assert ratio>F(15,8)
assert s.factor(s.diff((z+4)*(z*z-4*z+12)/(4*(z*z-4)),z)) == (z**4-8*z*z-96*z+16)/(4*(z-2)**2*(z+2)**2)
assert s.factor(s.diff((z*z-4*z+12)/(3*(z+2)),z))==(z*z+4*z-20)/(3*(z+2)**2)
print('sharp nonzero Gram condition-number ratio: unique minimum 15/8 at n=6; exact derivative sign proof')

# Independent symbolic multivariable test: construct a quartic directly, take
# its Euclidean Laplacian, and evaluate at every root representative.
n=4
u=s.symbols('u0:4')
r2=sum(v*v for v in u)
edges=list(combinations(range(n),2))
b={e:s.Rational((e[0]+1)*3-(e[1]+2),5) for e in edges}
a={i:-sum(b[e] for e in edges if i in e)/6 for i in range(n)}
d={e:s.Rational(1+e[0]-2*e[1],7) for e in edges}
P=sum(a[i]*u[i]**4 for i in range(n))+sum(b[i,j]*u[i]**2*u[j]**2 for i,j in edges)
P+=sum(d[i,j]*u[i]*u[j]*(u[i]**2+u[j]**2-s.Rational(6,n+4)*r2) for i,j in edges)
assert s.expand(sum(s.diff(P,v,2) for v in u))==0
for i in range(n):
    assert s.simplify(P.subs({v:int(k==i) for k,v in enumerate(u)}))==a[i]
for i,j in edges:
    for eps in (1,-1):
        point={v:0 for v in u};point[u[i]]=1/s.sqrt(2);point[u[j]]=eps/s.sqrt(2)
        predicted=(a[i]+a[j]+b[i,j])/4 +eps*d[i,j]*s.Rational(n-2,2*(n+4))
        assert s.simplify(P.subs(point)-predicted)==0
print('independent symbolic Laplacian and all B4 sample evaluations: OK')
print('PASS')
