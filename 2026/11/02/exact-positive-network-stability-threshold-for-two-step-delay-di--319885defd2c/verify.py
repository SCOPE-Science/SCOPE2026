"""Supplementary checks for positive-network IMEX delay stability.

Requires Python 3, sympy, numpy. Execute: python verify.py.
Finite numerical instances are evidence checks, not a substitute for the theorem.
"""
import numpy as np
import sympy as sp

z, beta, h = sp.symbols('z beta h')
rho = z*z + 2*(beta-1)*z + 1-2*beta
sigma = z*z + (beta-1)*z + beta
rev = lambda f: sp.expand(z*z*f.subs(z,1/z))
assert sp.simplify((rho*rev(sigma)+rev(rho)*sigma)/2 - (1-beta)*(z-1)**4/2) == 0
assert sp.factor(rho) == (z-1)*(z+2*beta-1)
assert sigma.subs(z,1) == 2*beta
assert rho.subs(z,1) == 0
print('EXACT: boundary positive-real identity and endpoint values')

# Determinant for a cyclic adjacency with arbitrary positive gains.
a = [1,2,4]
b = [4,sp.Rational(1,4),1]
for m in (1,2,3):
    T = sp.diag(*[z**m*(rho+h*ai*sigma) for ai in a])
    for j in range(3):
        T[j,(j+1)%3] -= h*b[j]*sigma
    identity = z**(3*m)*sp.prod(rho+h*ai*sigma for ai in a)-h**3*sigma**3*sp.prod(b)
    assert sp.expand(T.det()-identity) == 0
print('EXACT: directed-cycle characteristic determinants (3 delays)')

# Weighted numerical range witness for the all-exponent certificate gap.
t = sp.symbols('t', positive=True)
c = [4*t, t/8, 1/(4*t*t)]
C=sp.Matrix([[0,c[0],0],[0,0,c[1]],[c[2],0,0]])
H=(C+C.T)/2
S=sp.factor(sum(x*x for x in c))
la=sp.symbols('la')
assert sp.simplify(H.charpoly(la).as_expr() - (la**3-S*la/4-sp.Rational(1,32))) == 0
assert sp.simplify(S - (sp.Rational(1025,64)*t*t+sp.Rational(1,16)/t**4)) == 0
K=sp.Rational(1025,64)
assert K>16
assert (sp.Rational(27,64)*K*K)>64
print('EXACT: numerical-range witness and strict all-exponent bound')

# Synthetic finite checks for general nonnegative irreducible and reducible B.
def roots_for(D,B,bb,hh,mm):
    # determinant via symbolic matrix polynomials (n<=3 cases only)
    zsy=sp.symbols('u')
    rq=zsy*zsy+2*(sp.Rational(str(bb))-1)*zsy+1-2*sp.Rational(str(bb))
    sq=zsy*zsy+(sp.Rational(str(bb))-1)*zsy+sp.Rational(str(bb))
    n=len(D); V=sp.zeros(n)
    for j in range(n):
        for k in range(n):
            V[j,k]=-sp.Rational(str(hh))*sp.Rational(str(B[j][k]))*sq
        V[j,j]+=zsy**mm*(rq+sp.Rational(str(hh))*sp.Rational(str(D[j]))*sq)
    poly=sp.Poly(V.det(),zsy)
    ar=np.array([float(x) for x in poly.all_coeffs()]); ar/=max(abs(ar))
    return np.roots(ar)

cases=0
for D,B,base in [
    ([1.,2.,4.],[[0,4,0],[0,0,.25],[1,0,0]],.5),
    ([1.,1.,1.],[[0,.2,.1],[.1,0,.2],[.3,.1,0]],.95),
    ([1.,2.,3.],[[0,0,0],[.1,0,.2],[0,0,.5]],.8),
]:
    for bb in (.15,.5,.85):
        for hh in (.2,1.,4.):
            for mm in (1,2):
                rad = max(abs(v) for v in roots_for(D,B,bb,hh,mm))
                M=np.diag(1/np.array(D))@np.array(B)
                control=max(abs(v) for v in np.linalg.eigvals(M))
                assert control<1 and rad<1+2e-7, (D,B,control,rad,bb,hh,mm)
                cases+=1
print(f'NUMERICAL: {cases} finite strictly stable network examples')

# Boundary and real-instability checks for the same directed 3-cycle.
for bb in (.2, .6, .9):
    for hh in (.25, 2.):
        for mm in (1, 2):
            for b3,expected in ((8.,'boundary'),(16.,'unstable')):
                gains=[[0.,4.,0.],[0.,0.,.25],[b3,0.,0.]]
                eig=roots_for([1.,2.,4.],gains,bb,hh,mm)
                if expected=='boundary':
                    assert min(abs(zv-1) for zv in eig) < 1e-5
                else:
                    assert any(abs(zv.imag)<1e-6 and zv.real>1+1e-5 for zv in eig)
print('NUMERICAL: 24 threshold/instability checks')
print('ALL CHECKS PASSED')
