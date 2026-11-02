"""Deterministic numerical spot checks for the Hermite small-window theorem.

This is corroboration of finite examples, not a proof for all ranks.
Requires mpmath and numpy; no external file dependencies.
"""
import mpmath as mp
import numpy as np
mp.mp.dps = 55
checks = 0

def h(n, x):
    return mp.hermite(n,x)*mp.exp(-x*x/2)/mp.sqrt(2**n*mp.factorial(n)*mp.sqrt(mp.pi))

def coefficients(N,x):
    v=[h(j,x) for j in range(N)]
    vp=[mp.sqrt(2*j)*v[j-1]-x*v[j] if j else -x*v[0] for j in range(N)]
    v2=[(x*x-(2*j+1))*v[j] for j in range(N)]
    v3=[2*x*v[j]+(x*x-(2*j+1))*vp[j] for j in range(N)]
    v4=[2*v[j]+4*x*vp[j]+(x*x-(2*j+1))*v2[j] for j in range(N)]
    dot=lambda a,b:sum(s*t for s,t in zip(a,b))
    R=dot(v,v);P=dot(v,vp);A=dot(v,v2);B=dot(v,v3);C=dot(v,v4)
    m1=(A+P*P/R)/3
    w=[v2[j]+2*P/R*vp[j]-(A/R+2*P*P/R**2)*v[j] for j in range(N)]
    m2=C/60+P*B/(15*R)+A*A/(20*R)+dot(w,w)/36
    return R,m1,m2

def strict_close(u,v,tol=mp.mpf('1e-30')):
    global checks
    assert abs(u-v)<tol,(u,v)
    checks+=1

for N in range(1,13):
    roots=np.polynomial.hermite.hermroots([0]*N+[1]);rts=sorted(float(r.real) for r in roots if abs(r.imag)<1e-10 and r.real>1e-7)
    candidates=([mp.mpf('0')] if N%2 else [])+[mp.findroot(lambda t:mp.hermite(N,t),(z-mp.mpf('.01'),z+mp.mpf('.01'))) for z in rts]
    for x in candidates:
        R,M1,M2=coefficients(N,x)
        strict_close(mp.diff(lambda t:coefficients(N,t)[0],x),0)
        strict_close(mp.diff(lambda t:coefficients(N,t)[0],x,2),-2*R)
        strict_close(mp.diff(lambda t:coefficients(N,t)[1],x),0)
        strict_close(mp.diff(lambda t:coefficients(N,t)[2],x),-x*R/45)
    if N>=2:
        x=candidates[0]
        if N%2: strict_close(x,0)
        else: assert x>0;checks+=1
# Compare the leading Gram-matrix eigenvalue against the asymptotic coefficients.
for N in range(1,9):
    roots=np.polynomial.hermite.hermroots([0]*N+[1]); rts=sorted(float(r.real) for r in roots if abs(r.imag)<1e-10 and r.real>1e-7)
    a=mp.mpf('0') if N%2 else mp.findroot(lambda t:mp.hermite(N,t), (rts[0]-.01,rts[0]+.01))
    R,M1,M2=coefficients(N,a)
    for L in [mp.mpf('.02'),mp.mpf('.01')]:
        # Direct high-precision quadrature on the short interval.
        def integrand(i,j):return lambda s:h(i,a+s)*h(j,a+s)
        mat=mp.matrix([[mp.quad(integrand(i,j),[-L,L])/(2*L) for j in range(N)] for i in range(N)])
        eig=sorted(mp.eigsy(mat,eigvals_only=True))[-1]
        approximate=R+L*L*M1+L**4*M2
        assert abs(eig-approximate)<mp.mpf('20')*L**6,(N,a,L,eig,approximate)
        checks+=1
print('PASS',checks,'deterministic assertions; maximum rank 12, mpmath precision',mp.mp.dps)
