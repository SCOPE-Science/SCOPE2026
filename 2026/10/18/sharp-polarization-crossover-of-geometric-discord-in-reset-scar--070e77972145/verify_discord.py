"""Reproducibility checks for two-site collective-phase-reset geometric discord.

Requires numpy, sympy. Run: python verify_discord.py
Finite tests supplement, and do not replace, the analytic proof in RESULT.md.
"""
import numpy as np
import sympy as sp
from math import sqrt

NTESTS=0

def assert_close(a,b,atol=2e-10):
    global NTESTS
    assert np.allclose(a,b,atol=atol,rtol=atol), (a,b)
    NTESTS+=1

def assert_ok(val):
    global NTESTS
    assert bool(val)
    NTESTS+=1

X=sp.symbols('X',positive=True)
U=sp.Matrix([1/(1+X**2), X/(1+X**2)])
T=sp.Matrix([[(1+1/(1+4*X**2))/2, X/(1+4*X**2)], [X/(1+4*X**2),(1-1/(1+4*X**2))/2]])
K=sp.simplify(U*U.T+T*T)
tr_expected=(2*X**4+7*X**2+2)/((X**2+1)*(4*X**2+1))
det_expected=X**4*(X**4+6*X**2+2)/((X**2+1)**2*(4*X**2+1)**2)
assert_ok(sp.simplify(sp.trace(K)-tr_expected)==0)
assert_ok(sp.simplify(K.det()-det_expected)==0)
disc_expected=(X**4+12*X**2+4)/((1+X**2)**2*(1+4*X**2))
assert_ok(sp.simplify(sp.trace(K)**2-4*K.det()-disc_expected)==0)
D=(tr_expected-sp.sqrt(disc_expected))/8
assert_ok(sp.simplify(sp.limit(D, X, sp.oo)-sp.Rational(1,16))==0)
assert_ok(sp.simplify(sp.limit(D/X**4,X,0)-sp.Rational(1,4))==0)
assert_ok(sp.simplify(sp.limit((D-sp.Rational(1,4)*X**4)/X**6,X,0)+sp.Rational(11,8))==0)

sigma=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),np.array([[1,0],[0,-1]],dtype=complex)]
identity=np.eye(2)
def exact_density(x,z):
    # q=(1-z)/2 population of the |1> state; Bloch transverse s=sqrt(1-z²).
    s=sqrt(1-z*z)
    def moment(k):return 1/(1-1j*k*x)
    # v(phi) = (s cos phi, s sin phi,z), E(exp(i k phi))=1/(1-i k x).
    c=moment(1).real;sn=moment(1).imag; c2=moment(2).real; s2=moment(2).imag
    u=np.array([s*c,s*sn,z])
    T=np.array([[s*s*(1+c2)/2,s*s*s2/2,s*z*c],
                [s*s*s2/2,s*s*(1-c2)/2,s*z*sn],
                [s*z*c,s*z*sn,z*z]],float)
    rho=np.kron(identity,identity).astype(complex)
    for j in range(3):rho+=u[j]*(np.kron(sigma[j],identity)+np.kron(identity,sigma[j]))
    for j in range(3):
        for k in range(3):rho+=T[j,k]*np.kron(sigma[j],sigma[k])
    return rho/4,u,T

def quadrature(x,z,count=20000):
    # Exponentially distributed phase age using midpoint quantiles.
    s=sqrt(1-z*z);total=np.zeros((4,4),complex)
    for i in range(count):
        tau=-np.log1p(-(i+0.5)/count);theta=x*tau
        q=np.array([sqrt((1+z)/2),sqrt((1-z)/2)*np.exp(1j*theta)])
        rho=np.outer(q,q.conj())
        total+=np.kron(rho,rho)
    return total/count

for x in [.1,.5,1,2,10]:
    for z in [-.85,-.3,0,.2,.77]:
        rho,u,T0=exact_density(x,z)
        assert_close(rho,rho.conj().T)
        assert_close(np.trace(rho),1)
        assert_ok(np.linalg.eigvalsh(rho).min()>-1e-12)
        assert_close(np.trace(rho@np.kron(sigma[0],identity)).real,u[0])
        assert_close(np.trace(rho@np.kron(sigma[1],sigma[1])).real,T0[1,1])
        # Partial transpose on B for separability (also follows from explicit product mixture).
        pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
        assert_ok(np.linalg.eigvalsh(pt).min()>-1e-11)
        assert_ok(np.linalg.matrix_rank(T0,tol=1e-10)>=2)
        if z==0:
            Knum=np.outer(u,u)+T0@T0.T
            eigen=np.linalg.eigvalsh(Knum)
            assert_close((np.trace(Knum)-eigen[-1])/4,float(D.subs(X,x)),atol=1e-9)
    rho,*_=exact_density(x,0)
    assert_close(rho,quadrature(x,0,6000),atol=.0004)

z2=sp.symbols('z2',nonnegative=True)
tstar=(2*sp.sqrt(3)-3)/3
k=(1-z2)**2/4; h=z2+z2**2
assert_ok(sp.simplify(k.subs(z2,tstar)-h.subs(z2,tstar))==0)
assert_ok(sp.simplify(k.subs(z2,tstar)/2-(2-sp.sqrt(3))/3)==0)
assert_ok(sp.simplify(sp.diff((k+h)/4,z2)-(1+5*z2)/8)==0)
assert_ok(sp.simplify(sp.diff(k/2,z2)-(z2-1)/4)==0)
for z2v in np.linspace(0,1,101):
    zz=sqrt(z2v)
    # Sparse reset uniform phase law: transverse first moment 0;
    # T=diag((1-z²)/2,(1-z²)/2,z²).
    uv=np.array([0.,0.,zz]);Tv=np.diag([(1-z2v)/2]*2+[z2v]);K0=np.outer(uv,uv)+Tv@Tv.T
    direct=(np.trace(K0)-np.linalg.eigvalsh(K0)[-1])/4
    formula=(float(k.subs(z2,z2v))+float(h.subs(z2,z2v)))/4 if z2v<=float(tstar) else float(k.subs(z2,z2v))/2
    assert_close(direct,formula)
    # Non-equatorial finite reset approximates the uniform phase limit continuously.
    if z2v not in (0,1):
        rstate,u,T0=exact_density(3000,zz)
        Knum=np.outer(u,u)+T0@T0.T
        assert_close((np.trace(Knum)-np.linalg.eigvalsh(Knum)[-1])/4,direct,atol=.0003)

print(f'PASS {NTESTS} analytic and numerical assertions')
