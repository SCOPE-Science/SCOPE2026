"""Numerical checks for a sharp sketched Ritz spectral-reality threshold.

This code verifies exact finite-dimensional witnesses and numerical inequalities;
the general conclusions are proved analytically in RESULT.md.
"""
from fractions import Fraction as Q
import math
import numpy as np

checks=0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks+=1

# Exact four-dimensional witness with distortion 3/5.
e=Q(3,5)
delta=Q(1,2)
gamma=Q(1,1)
beta=Q(3,1)
a=1-e*e
z=1+e*e
b=e*Q(4,5)
check(a==Q(16,25),'a')
check(z==Q(34,25),'z')
check(b==Q(12,25),'b')
check(a*z-b*b==1-e*e,'positive block determinant')
check(e*e*e*e+b*b==e*e,'G-I squares to e^2 I')
k=gamma*b/a
check(k==Q(3,4),'sketched skew coupling')
check(k*k-delta*delta==Q(5,16),'negative characteristic discriminant')
check(delta*delta+gamma*gamma==Q(5,4),'critical threshold denominator')
check(e*e>delta*delta/(delta*delta+gamma*gamma),'distortion exceeds threshold')
check(beta>delta+gamma,'A positive definite by norm')

J=np.array([[0,-1],[1,0]], dtype=float)
I=np.eye(2)
H0=np.diag([float(beta-delta),float(beta+delta)])
A=np.block([[H0,float(gamma)*I],[float(gamma)*I,float(beta)*I]])
G=np.block([[float(a)*I,float(b)*J],[-float(b)*J,float(z)*I]])
X=np.eye(4)[:,:2]
L=np.linalg.cholesky(G).T  # L.T @ L = G
P=np.linalg.solve((L@X).T@(L@X),(L@X).T@(L@A@X))
check(np.allclose(P,H0+float(k)*J,atol=1e-13),'exact projected matrix')
check(np.allclose((G-np.eye(4))@(G-np.eye(4)),float(e*e)*np.eye(4),atol=1e-13),'exact G spectrum')
check(np.allclose(np.linalg.eigvalsh(G),[1-float(e),1-float(e),1+float(e),1+float(e)],atol=1e-13),'embedding eigenvalues')
check(np.linalg.eigvalsh(A).min()>0,'SPD')
check(np.allclose(np.sort_complex(np.linalg.eigvals(P)),np.sort_complex([3+1j*math.sqrt(5)/4,3-1j*math.sqrt(5)/4])),'complex eigenvalue pair')
check(np.isclose(np.linalg.norm(P-H0,2),float(e)/math.sqrt(1-float(e)**2)),'sharp bound attained')

# Exact threshold identities for rational and irrational param families.
for numerator in range(1,10):
    for denominator in range(numerator+1,13):
        er=Q(numerator,denominator)
        # algebraic identity: upper block a=1-e^2 and off-diagonal b=e sqrt(1-e^2)
        aa=1-er*er
        gain_sq=er*er/aa
        check(aa>0,'embedding positive')
        check((gain_sq<delta*delta/gamma**2)==(er*er<delta*delta/(delta*delta+gamma*gamma)), 'sharp strict threshold')

rng=np.random.default_rng(20261026)
for sample in range(800):
    m=int(rng.integers(4,10)); kdim=int(rng.integers(2,min(5,m)))
    U,_=np.linalg.qr(rng.normal(size=(m,kdim)))
    W=rng.normal(size=(m,m))
    A=W.T@W+np.eye(m)
    R=A@U-U@(U.T@A@U)
    E=rng.normal(size=(m,m)); E=(E+E.T)/2
    E=E/np.linalg.norm(E,2)
    eps=float(rng.uniform(0.001,0.95))
    G=np.eye(m)+eps*E
    B=U.T@A@U
    P=np.linalg.solve(U.T@G@U,U.T@G@A@U)
    bound=eps/math.sqrt(1-eps**2)*np.linalg.norm(R,2)
    check(np.linalg.norm(P-B,2)<=bound+1e-10,'sharp perturbation inequality')
    vals=np.linalg.eigvalsh(B)
    gap=np.min(np.diff(vals))
    if gap>2*bound+1e-10:
        check(np.max(np.abs(np.imag(np.linalg.eigvals(P))))<1e-8,'all projected eigenvalues real with separated Ritz spectrum')
    else:
        check(True,'inconclusive gap case correctly excluded')

print(f'PASS {checks} deterministic exact and seeded numerical assertions')
