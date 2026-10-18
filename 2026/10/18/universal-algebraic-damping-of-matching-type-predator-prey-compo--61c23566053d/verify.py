#!/usr/bin/env python3
"""Symbolic consistency checks and finite trajectory diagnostics for the rate law.

The infinite-time limit is established analytically in RESULT.md, not by
these computations. Run using Python 3, SymPy and SciPy.
"""
import sympy as sp
from scipy.integrate import solve_ivp

n, h, c, gamma, p, rho = sp.symbols('n h c gamma p rho', positive=True)
N, H, x, y = sp.symbols('N H x y', real=True)
a, beta = sp.symbols('a beta', real=True)
n0 = N*(1+x)/2
n1 = N*(1-x)/2
h0 = H*(1+y)/2
h1 = H*(1-y)/2
v0 = n0*(a-c*N-p*h0)
v1 = n1*(a-c*N-p*h1)
w0 = h0*(beta-gamma*H+rho*n0)
w1 = h1*(beta-gamma*H+rho*n1)
Ndot = sp.expand(v0+v1)
Hdot = sp.expand(w0+w1)
xdot = sp.simplify(((v0-v1)*N-(n0-n1)*Ndot)/N**2)
ydot = sp.simplify(((w0-w1)*H-(h0-h1)*Hdot)/H**2)
assert sp.simplify(Ndot-N*(a-c*N-p*H*(1+x*y)/2)) == 0
assert sp.simplify(Hdot-H*(beta-gamma*H+rho*N*(1+x*y)/2)) == 0
assert sp.simplify(xdot+p*H*y*(1-x*x)/2) == 0
assert sp.simplify(ydot-rho*N*x*(1-y*y)/2) == 0

omega = sp.sqrt(p*rho*n*h)
A = sp.Matrix([[-2*c*n,-p*n],[rho*h,-2*gamma*h]])
q = sp.Matrix([-2*p*n*h/omega,2*rho*n*h/omega])
# If P_2 = alpha*(X^2-Y^2)/2 + b*X*Y, the quadratic
# center-manifold invariance equation gives these two vectors.
alpha = -2*omega*(A*A+4*omega**2*sp.eye(2)).inv()*q
b = -A*(A*A+4*omega**2*sp.eye(2)).inv()*q
assert all(sp.simplify(z) == 0 for z in (2*omega*b-A*alpha))
assert all(sp.simplify(z) == 0 for z in (-2*omega*alpha-A*b-q))

kappa = sp.factor(-omega*(b[0]/n-b[1]/h)/8)
numerator = (4*c*gamma+p*rho)*(c*rho*n**2+gamma*p*h**2) + \
            4*p*rho*n*h*(c*p+gamma*rho)
denominator = 2*(n*h*(4*c*gamma-3*p*rho)**2 +
                 16*p*rho*(c*n+gamma*h)**2)
assert sp.simplify(kappa-numerator/denominator) == 0
kappa_dissipation = (rho*c*(alpha[0]**2+b[0]**2) +
                     p*gamma*(alpha[1]**2+b[1]**2))/8
assert sp.simplify(kappa-kappa_dissipation) == 0
assert sp.simplify(kappa.subs({n:1,h:1,c:1,gamma:1,p:1,rho:1})-sp.Rational(9,65)) == 0
print('Exact reduction, quadratic invariance and positive damping coefficient: PASS')
print('Normalized example: kappa = 9/65; limiting t-energy = 65/9')

# Diagnostics use positive initial data; their trend is not a proof.
for nn, hh, cc, gg, pp, rr in [(1.,1.,1.,1.,1.,1.),(1.,2.,1.,4.,2.,3.)]:
    aa=2*cc*nn+pp*hh
    bb=2*gg*hh-rr*nn
    vals={n:nn,h:hh,c:cc,gamma:gg,p:pp,rho:rr}
    kk=float(kappa.subs(vals))
    def rhs(t,z):
        n0,n1,h0,h1=z
        total_n=n0+n1
        total_h=h0+h1
        return [n0*(aa-cc*total_n-pp*h0),n1*(aa-cc*total_n-pp*h1),
                h0*(bb-gg*total_h+rr*n0),h1*(bb-gg*total_h+rr*n1)]
    sol=solve_ivp(rhs,(0,3000),[1.1*nn,.9*nn,1.07*hh,.93*hh],
                  rtol=3e-8,atol=1e-10,method='DOP853',dense_output=True)
    assert sol.success
    observed=[]
    for t in [500,1500,3000]:
        z=sol.sol(t)
        xn=(z[0]-z[1])/(z[0]+z[1])
        yh=(z[2]-z[3])/(z[2]+z[3])
        observed.append(t*(rr*nn*xn*xn+pp*hh*yh*yh))
    assert observed[0]<observed[1]<observed[2]<1/kk
    assert abs(1/kk-observed[2])/(1/kk)<.19
    print('Parameters', (nn,hh,cc,gg,pp,rr),
          't-energy at 500/1500/3000:', [round(z,6) for z in observed],
          'predicted limit:',round(1/kk,6))
print('Finite trajectory diagnostics: PASS')
