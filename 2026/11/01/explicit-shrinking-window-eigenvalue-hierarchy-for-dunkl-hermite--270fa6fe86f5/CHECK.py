"""Reproducibility checks for the finite-band small-window spectral law.

The argument establishing all orders is analytical and is given in RESULT.md;
these checks test determinant constants, matrix identities and asymptotics.
Requires mpmath and sympy.
"""
from math import factorial
import mpmath as mp
import sympy as sp

mp.mp.dps = 95
checks = 0

def test(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

def selberg(k, a, b):
    # S_k(a,b,1), normalized with S_0=1.
    return mp.fprod(mp.gamma(a+j)*mp.gamma(b+j)*mp.gamma(j+2)/mp.gamma(a+b+k+j-1)
                    for j in range(k))

def hankel_det(m, alpha, kind, beta=0):
    if kind == 'laguerre':
        return mp.fprod(mp.factorial(j)*mp.gamma(alpha+j+1) for j in range(m))
    return selberg(m, alpha+1, beta+1)/mp.factorial(m)

def D(m, k, alpha, kind, beta=0):
    return (hankel_det(m-k, alpha+2*k, kind, beta)/hankel_det(m,alpha,kind,beta)
            *selberg(k,alpha+1,1)/mp.factorial(k))

def gram(m, alpha, kind, beta, b):
    H=mp.matrix(m); G=mp.matrix(m)
    for i in range(m):
        for j in range(m):
            s=alpha+i+j+1
            if kind=='laguerre':
                H[i,j]=mp.gamma(s)
                G[i,j]=mp.gammainc(s,0,b)
            else:
                H[i,j]=mp.beta(s,beta+1)
                G[i,j]=mp.betainc(s,beta+1,0,b,regularized=False)
    return H,G

def eigvals(H,G):
    L=mp.cholesky(H)
    Linv=L**-1
    E=Linv*G*Linv.T
    return sorted([v for v in mp.eigsy(E,eigvals_only=True)],reverse=True)

def char_coeffs(vals):
    e=[mp.mpf(1)]
    for x in vals:
        e=[e[0]] + [e[j] + e[j-1]*x for j in range(1,len(e))] + [e[-1]*x]
    return e

# Hankel determinants: direct determinant vs product (fully checked at all sizes).
for kind in ['laguerre','jacobi']:
    for alpha,beta in [(mp.mpf('-0.5'),mp.mpf('0.5')),(mp.mpf(0),mp.mpf(0)),(mp.mpf('0.5'),mp.mpf(2))]:
        for m in range(1,6):
            H,_=gram(m,alpha,kind,beta,mp.mpf('.1'))
            target=hankel_det(m,alpha,kind,beta)
            test(abs(mp.det(H)/target-1)<mp.mpf('1e-65'), ('H',kind,alpha,beta,m))

# All elementary symmetric leading terms and ordered eigenvalue constants.
for kind in ['laguerre','jacobi']:
    for alpha,beta in [(mp.mpf('-0.5'),mp.mpf('0.5')),(mp.mpf(0),mp.mpf(0)),(mp.mpf('0.5'),mp.mpf(1))]:
        for m in range(1,5):
            errs=[]
            for b in map(mp.mpf,['0.02','0.01','0.005']):
                H,G=gram(m,alpha,kind,beta,b)
                eig=eigvals(H,G)
                test(all(x>0 for x in eig), ('positive',kind,alpha,m,b))
                ecoeff=char_coeffs(eig)
                errors=[]
                for k in range(1,m+1):
                    leading=D(m,k,alpha,kind,beta)
                    ratio=ecoeff[k]/(leading*b**(k*(alpha+k)))
                    test(abs(ratio-1)<mp.mpf('0.28'), ('e',kind,alpha,beta,m,k,b,ratio))
                    c=leading/D(m,k-1,alpha,kind,beta)
                    spectral=eig[k-1]/(c*b**(alpha+2*k-1))
                    test(abs(spectral-1)<mp.mpf('0.35'), ('lambda',kind,alpha,beta,m,k,b,spectral))
                    errors.append(abs(spectral-1))
                errs.append(errors)
            for k in range(m):
                test(errs[2][k] <= errs[0][k]+mp.mpf("1e-70"),('convergence',kind,alpha,beta,m,k,errs))

# An exact symbolic independent test for the m=3, alpha=0 Laguerre Hankel minors.
b=sp.symbols('b')
m=3
H=sp.Matrix([[sp.factorial(i+j) for j in range(m)] for i in range(m)])
G=sp.Matrix([[sp.integrate(sp.Symbol('y')**(i+j)*sp.exp(-sp.Symbol('y')), (sp.Symbol('y'),0,b)) for j in range(m)] for i in range(m)])
Q=H.inv()*G
poly=sp.Poly((sp.eye(m)+sp.Symbol('t')*Q).det(),sp.Symbol('t'))
for k in (1,2,3):
    expr=sp.series(poly.coeff_monomial(sp.Symbol('t')**k), b,0,k*k+2).removeO().expand()
    leading=sp.simplify(expr.coeff(b,k*k))
    target=[None,sp.Integer(3),sp.Rational(1,2),sp.Rational(1,8640)][k]
    test(sp.simplify(leading-target)==0,('symbolic-leading',k,leading,target))

print('CHECK_OK',checks)
