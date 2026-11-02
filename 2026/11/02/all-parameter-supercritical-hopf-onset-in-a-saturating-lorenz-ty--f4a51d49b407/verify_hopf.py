#!/usr/bin/env python3
"""Exact symbolic checks for the cubic Hopf coefficient of a saturating Lorenz-type flow.

Requires Python 3 and SymPy. No numerical integrator or external data are needed.
Run: python3 verify_hopf.py
"""
import sympy as s


def generic_identity():
    sigma, delta, epsilon = s.symbols('sigma delta epsilon', positive=True)
    kappa = delta + epsilon
    omega = -1 / s.sqrt(delta)
    phi1 = 2 * kappa * omega / (1 + epsilon * omega**2)**2
    phi2half = kappa * (1 - 3 * epsilon * omega**2) / (1 + epsilon * omega**2)**3
    a = sigma / (2 * (sigma + s.I * omega))
    norm_a2 = s.simplify(a * s.conjugate(a))
    assert s.simplify(norm_a2 - sigma**2/(4*(sigma**2+1/delta))) == 0
    h11 = -2*phi1*norm_a2/sigma
    C = phi1+s.I
    A = C*a
    B = C*s.conjugate(a)
    raw = C*h11 + 2*phi2half*norm_a2
    induced = -A*B/(s.I*omega) + B*s.conjugate(-B/(s.I*omega))
    # Independently check the real part of near-identity normal-form correction.
    nu = s.simplify(s.re(s.expand_complex(raw+induced)))
    expected = -sigma*delta**3*(sigma*(kappa+4*epsilon)+4*delta) / (2*kappa**2*(1+sigma**2*delta))
    assert s.simplify(nu-expected) == 0, s.factor(nu-expected)
    crossing = s.simplify(-phi1/sigma)
    assert s.simplify(crossing - 2*delta**s.Rational(3,2)/(kappa*sigma)) == 0
    return 'generic identity and crossing: PASS'


def independent_multilinear(sigma,kappa,epsilon):
    """Kuznetsov real 3D multilinear formula, not the center-manifold algebra."""
    delta=kappa-epsilon
    assert delta>0 and epsilon>0 and sigma>0
    omega=-1/s.sqrt(delta)
    Omega=-omega
    c=2*kappa*omega/(1+epsilon*omega**2)**2
    d=kappa*(1-3*epsilon*omega**2)/(1+epsilon*omega**2)**3
    J=s.Matrix([[-sigma,sigma,0],[0,0,-omega],[0,omega,0]])
    v=s.Matrix([sigma/(sigma+s.I*Omega),1,s.I])
    vc=s.conjugate(v)
    ell=s.Matrix([[0,s.Rational(1,2),-s.I/2]])
    assert s.simplify(J*v-s.I*Omega*v)==s.zeros(3,1)
    assert s.simplify(ell*J-s.I*Omega*ell)==s.zeros(1,3)
    assert s.simplify((ell*v)[0]-1)==0
    def B(u,z):
        return s.Matrix([0,
          c*(u[0]*z[1]+u[1]*z[0])-(u[0]*z[2]+u[2]*z[0]),
          (u[0]*z[1]+u[1]*z[0])+c*(u[0]*z[2]+u[2]*z[0])])
    def T(u,z,h):
        return s.Matrix([0,
          2*d*(u[0]*z[0]*h[1]+u[0]*z[1]*h[0]+u[1]*z[0]*h[0]),
          2*d*(u[0]*z[0]*h[2]+u[0]*z[2]*h[0]+u[2]*z[0]*h[0])])
    g21=s.simplify((ell*(T(v,v,vc) - 2*B(v,J.inv()*B(v,vc))
       +B(vc,(2*s.I*Omega*s.eye(3)-J).inv()*B(v,v))))[0])
    # Real modal state w*v+conj(w)*conj(v) has physical y+i*z=2*conj(w).
    # The normal form for w has coefficient g21/2, hence physical coefficient g21/8.
    nu=s.simplify(s.re(g21)/8)
    expected = -sigma*delta**3*(sigma*(kappa+4*epsilon)+4*delta)/(2*kappa**2*(1+sigma**2*delta))
    assert s.simplify(nu-expected)==0, (nu,expected)
    return (sigma,kappa,epsilon,s.factor(nu))


if __name__=='__main__':
    print(generic_identity())
    examples=[(s.Rational(10),s.Rational(5,4),s.Rational(1,4)),
      (s.Rational(3),s.Rational(1,2),s.Rational(1,4)),
      (s.Rational(5,2),s.Rational(10,9),s.Rational(1,9))]
    for sig,kap,eps in examples:
        print('independent multilinear check:',independent_multilinear(sig,kap,eps),'PASS')
    print('ALL CHECKS PASS')
