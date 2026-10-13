#!/usr/bin/env python3
"""Reproduce exact special-case identities and sampled equilibrium residuals.

The infinite-domain threshold statements follow from the analytic derivative
argument in RESULT.md; finite sampling here is a consistency check, not a proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def D(a, b=1):
    return Decimal(a) / Decimal(b)


def ck(condition, note):
    if not condition:
        raise AssertionError(note)


with localcontext() as ctx:
    ctx.prec = 85
    eps = Decimal('1e-65')
    L = D(3).ln()
    d, p, delta = D(1, 4), D(3, 4), D(1, 4)
    beta, b, w, mu = D(1), D(1), D(0), D(0)
    I = L
    t = (-I).exp()
    S = I / (D(3) * (D(1) - t))
    U = S + w*I
    r = D(3,4)*D(3).sqrt()
    barS = (r / d).ln() / b
    ck(abs(t-D(1,3)) < eps, 'exact exponential endpoint')
    ck(abs(S-L/D(2)) < eps, 'exact susceptible at crossing')
    ck(abs(S+I-barS) < eps, 'population equality at crossing')
    S_next = r*U*(-b*U).exp() + p*S*(-beta*I).exp()
    I_next = p*S*(D(1)-(-beta*I).exp()) + p*(D(1)-mu)*I
    ck(abs(S_next-S) < eps and abs(I_next-I) < eps, 'fixed-point residuals')
    # Quadratic from the exact exponential equation, factored at rational roots.
    for t0 in [Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2)]:
        ck(3*t0*t0-4*t0+1 == (1-t0)*(1-3*t0), 'polynomial factorization')
    trace = (D(7)-L)/D(4)
    det = D(3,4) - D(3,32)*L - D(3,64)*L*L
    jur1 = D(1)-det
    jur2 = D(1)-trace+det
    jur3 = D(1)+trace+det
    ck(D(1)<L<D(2), 'elementary logarithm bracket')
    ck(jur1 >0 and jur2 >0 and jur3>0, 'strict Schur stability')
    ck(abs(jur2-L*(D(10)-D(3)*L)/D(64))<eps, 'Schur symbolic identity')
    ck(abs(jur3-(D(224)-D(22)*L-D(3)*L*L)/D(64))<eps, 'Schur symbolic identity')
    ck(abs(jur1-(D(16)+D(6)*L+D(3)*L*L)/D(64))<eps, 'Schur symbolic identity')
    # Crossings on both sides of exact threshold are checked against both
    # the original equilibrium equations and the analytic population criterion.
    cases = [
      (D(1,4),D(0),D(0),D(1),D(1)),
      (D(1,2),D(1,2),D(3,10),D(1),D(4,5)),
      (D(1,5),D(0),D(9,10),D(1,10),D(1,2)),
      (D(3,5),D(3,4),D(1),D(3,10),D(1,4)),
      (D(1,3),D(0),D(1),D(1,5),D(1,3)),
    ]
    for d,mu,w,beta,b in cases:
        p=D(1)-d
        delta=d+p*mu
        c=delta/d
        a=p/delta
        for I in [D(1,50),D(1,5),D(1),D(3),D(10)]:
            q=(-beta*I).exp()
            S=delta*I/(p*(D(1)-q))
            z=I/S
            U=S+w*I
            r=d*(D(1)+c*z)/(D(1)+w*z)*(b*U).exp()
            Snext=r*U*(-b*U).exp()+p*S*q
            Inext=p*S*(D(1)-q)+p*(D(1)-mu)*I
            ck(abs(Snext-S) < eps*D(1000), 'susceptible equilibrium residual')
            ck(abs(Inext-I) < eps*D(1000), 'infected equilibrium residual')
            diseasefree=(r/d).ln()/b
            hydradifference=S+I-diseasefree
            scalar=(D(1)-w)*I - (D(1)+c*z).ln()/b+(D(1)+w*z).ln()/b
            ck(abs(hydradifference-scalar)<eps*D(1000), 'hydra sign identity')
            ck(abs(z-a*(D(1)-q))<eps*D(1000), 'infected ratio identity')
    print('VERIFY_OK')
    print('closed_form_r_H = 3*sqrt(3)/4 =',r if False else D(3,4)*D(3).sqrt())
    print('schur_criteria =',jur1,jur2,jur3)
