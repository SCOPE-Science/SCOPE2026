"""Exact-algebra and finite-dimensional numerical cross-checks for a noisy two-qubit reset model.

Run: python checker.py
Dependencies: numpy, sympy (Python 3).
"""
import math
import numpy as np
import sympy as sp

checks = 0

def verify(ok, msg="check"):
    global checks
    if not ok:
        raise AssertionError(msg)
    checks += 1

r, a, b, j = sp.symbols("r a b j", positive=True)
s = a + b
d1 = (r + 2*a)**2 + 4*j*j
d2 = (r + 2*b)**2 + 4*j*j
A = r/(r+2*s)
B1 = r*(r+2*a)/d1
B2 = r*(r+2*b)/d2
S1 = 2*j*r/d1
S2 = 2*j*r/d2
P = ((a*b-j*j)*r**4 + 4*s*(a*b-j*j)*r**3
     + 2*s*s*(3*a*b-j*j)*r**2
     + 4*s**3*(a*b+j*j)*r
     + 4*s*s*(a*a+j*j)*(b*b+j*j))
verify(sp.cancel((S1+S2)**2+(B1-B2)**2-(1-A)**2 +
                 16*P/((r+2*s)**2*d1*d2)) == 0, "exact PPT polynomial identity")
verify(sp.Poly(P,r).coeff_monomial(r**4) == a*b-j*j, "leading coefficient")
verify(sp.factor(sp.Poly(P,r).coeff_monomial(r**3)-4*s*(a*b-j*j)) == 0, "cubic coefficient")
verify(sp.factor(sp.Poly(P,r).coeff_monomial(r**2)-2*s*s*(3*a*b-j*j)) == 0, "quadratic coefficient")
verify(sp.factor(sp.Poly(P,r).coeff_monomial(r)-4*s**3*(a*b+j*j)) == 0, "linear coefficient")
verify(sp.factor(P.subs(r,0)-4*s*s*(a*a+j*j)*(b*b+j*j)) == 0, "constant coefficient")

I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]],complex)
Y = np.array([[0,-1j],[1j,0]],complex)
XX = np.kron(X,X)
X1 = np.kron(X,I)
X2 = np.kron(I,X)
YY = np.kron(Y,Y)
rho0 = np.zeros((4,4),complex)
rho0[0,0] = 1

def explicit(rr,jj,aa,bb):
    dr = [((rr+2*g)**2+4*jj*jj) for g in (aa,bb)]
    bs = [rr*(rr+2*g)/d for g,d in zip((aa,bb),dr)]
    ss = [2*jj*rr/d for d in dr]
    u = rr/(rr+2*(aa+bb))
    rho = np.zeros((4,4),complex)
    rho[0,0] = (1+u+bs[0]+bs[1])/4
    rho[3,3] = (1+u-bs[0]-bs[1])/4
    rho[1,1] = (1-u+bs[0]-bs[1])/4
    rho[2,2] = (1-u-bs[0]+bs[1])/4
    rho[0,3] = 1j*(ss[0]+ss[1])/4
    rho[3,0] = rho[0,3].conjugate()
    rho[1,2] = 1j*(ss[0]-ss[1])/4
    rho[2,1] = rho[1,2].conjugate()
    return rho

def steady_liouvillian(rr,jj,aa,bb):
    H = jj*XX
    def L(Q):
        return (-1j*(H@Q-Q@H)+aa*(X1@Q@X1-Q)+bb*(X2@Q@X2-Q))
    # Column-wise vectorization; independent basis-by-basis construction.
    M = np.zeros((16,16), complex)
    for column in range(16):
        E = np.zeros((4,4),complex)
        E[column%4,column//4] = 1
        M[:,column] = L(E).reshape(16,order='F')
    vec = np.linalg.solve(rr*np.eye(16)-M, rr*rho0.reshape(16,order='F'))
    return vec.reshape((4,4),order='F')

def concurrence(rho):
    spin = YY@rho.conj()@YY
    vals = np.linalg.eigvals(rho@spin)
    roots = sorted(np.sqrt(np.maximum(np.real(vals),0)),reverse=True)
    return max(0.,float(roots[0]-sum(roots[1:])))

def x_concurrence(rho):
    return max(0.,2*(abs(rho[0,3])-math.sqrt(max(0.,rho[1,1].real*rho[2,2].real))),
               2*(abs(rho[1,2])-math.sqrt(max(0.,rho[0,0].real*rho[3,3].real))))

def poly(rr,jj,aa,bb):
    ss=aa+bb
    return ((aa*bb-jj*jj)*rr**4+4*ss*(aa*bb-jj*jj)*rr**3
           +2*ss**2*(3*aa*bb-jj*jj)*rr**2+4*ss**3*(aa*bb+jj*jj)*rr
           +4*ss**2*(aa*aa+jj*jj)*(bb*bb+jj*jj))

rng=np.random.default_rng(710421)
for t in range(350):
    rr,jj,aa,bb=10**rng.uniform(-1.1,1.3,size=4)
    exact=explicit(rr,jj,aa,bb)
    direct=steady_liouvillian(rr,jj,aa,bb)
    verify(np.max(np.abs(exact-direct))<2e-11,f"steady matrix {t}")
    verify(abs(np.trace(exact)-1)<1e-11,f"trace {t}")
    verify(np.min(np.linalg.eigvalsh(exact))>-3e-12,f"PSD {t}")
    C1=concurrence(exact);C2=x_concurrence(exact)
    verify(abs(C1-C2)<1e-8,f"concurrence {t}")
    verify(abs(exact[1,2])**2 <= exact[0,0].real*exact[3,3].real+1e-12,f"inactive PPT branch {t}")
    # Away from a numerical zero, the quartic supplies the exact concurrence sign.
    p=poly(rr,jj,aa,bb)
    if abs(p)>1e-7:
        verify((C1>1e-9) == (p<0),f"quartic sign {t}")
    else:
        verify(True,"near threshold skip sign")

for t in range(250):
    jj,aa,bb=10**rng.uniform(-1,1.2,size=3)
    co=[aa*bb-jj*jj,4*(aa+bb)*(aa*bb-jj*jj),
        2*(aa+bb)**2*(3*aa*bb-jj*jj),
        4*(aa+bb)**3*(aa*bb+jj*jj),
        4*(aa+bb)**2*(aa*aa+jj*jj)*(bb*bb+jj*jj)]
    if jj*jj<=aa*bb:
        verify(all(c>=-1e-12 for c in co),f"nonnegative coefficients {t}")
        for rr in np.logspace(-3,3,5):
            verify(concurrence(explicit(rr,jj,aa,bb))<1e-9,"below-noise-threshold")
    else:
        signs=[1 if c>0 else -1 for c in co]
        changes=sum(signs[k]!=signs[k+1] for k in range(4))
        verify(changes==1,f"Descartes one sign change {t}")
        roots=np.roots(co)
        positive=[float(v.real) for v in roots if abs(v.imag)<1e-6*max(1,abs(v.real)) and v.real>0]
        verify(len(positive)==1,f"unique real positive root {t}")
        rc=positive[0]
        verify(poly(rc*0.7,jj,aa,bb)>0 and poly(rc*1.3,jj,aa,bb)<0,f"root direction {t}")
        verify(concurrence(explicit(rc*0.7,jj,aa,bb))<1e-9,"separable before reset threshold")
        verify(concurrence(explicit(rc*1.3,jj,aa,bb))>0,"entangled after reset threshold")

# The symmetric-noise special case agrees with an independent quadratic threshold.
for gg in np.logspace(-3,-0.03,80):
    jj=1.; aa=bb=gg
    rc=2*(math.sqrt(gg*(1+gg)/(1-gg))-gg)
    verify(abs(poly(rc,jj,aa,bb))<2e-7*max(1,rc**4),"symmetric noise boundary")
    verify(concurrence(explicit(rc*1.1,jj,aa,bb))>0,"symmetric noise above boundary")

# Demonstrate that arbitrarily asymmetric noise can preserve stationary entanglement.
for gg1,gg2 in ((0.005,100.),(0.0001,5000.),(0.5,1.),(5.,0.1)):
    jj=1.
    assert gg1*gg2<jj*jj
    rr=1e6*max(jj,gg1,gg2)
    verify(concurrence(explicit(rr,jj,gg1,gg2))>1e-14,"asymmetric rescue")

print(f"PASS {checks} algebraic and finite-dimensional checks")
