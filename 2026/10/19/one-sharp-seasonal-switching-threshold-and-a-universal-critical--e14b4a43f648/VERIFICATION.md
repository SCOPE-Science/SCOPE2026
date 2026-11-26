---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

With E=exp((T/2)A_+), the monodromy is E^T E. Its normalized determinant is one, and half the trace of exp(dT)E^T E is half the squared Frobenius norm of exp((T/2)(A_++dI)), namely 1+2 cosh(h)^2 sinh(rT/2)^2. Its larger eigenvalue gives the stated Floquet exponent. For C=cosh(h)>1, g(z)=asinh(C sinh z) has g(0)=0 and g''(z)=C(1-C^2)sinh(z)/(1+C^2 sinh(z)^2)^(3/2)<0 for z>0. Thus g(z)/z strictly decreases from C to 1, yielding exactly the threshold regime, including persistence at d=r and extinction at d=rC for every finite T. If X=Phi(t)u(0), exact division by H=1+kappa times the integral of the total of X solves the nonlinear equation; positivity guarantees H>=1 globally. The positive monodromy gives X(nT+s)=Phi(s)[a mu^n v+O(nu^n)] with a>0 including for axis initial states and 0<nu<mu. For mu<1 the numerator gives uniform exponential decay. For mu>1 the Poincare map has the unique positive fixed point (mu-1)v/(kappa I) and summing the Perron geometric series in H proves phase-uniform attraction to the stated orbit. For mu=1 the complete periods contribute kappa a n I+O(1) to H and the partial period is uniformly bounded, while the numerator tends uniformly to a Phi(s)v. Multiplication by nT+s cancels a and gives the claimed strictly positive universal coefficient, confirming algebraic rather than exponential decay. The example matches the Gram-matrix eigenvalue and the threshold equation.

## originality

PASS

The supported distinction is the exact strictly monotone threshold for a two-patch transpose switch together with the full nonlinear trichotomy and its phase-resolved all-extinction coefficient. Switching-induced growth, the scalar-density transform, and the general phenomenon of universal periodic critical profiles are not independently novel. The inspected prior statements do not provide this combined model-specific conclusion.

## value

PASS

The transpose switch is a minimal explicit cooperative model where individually stable seasons can sustain persistence. Exact monotonicity determines when switching speed can reverse extinction and supplies a sharp unique boundary rather than a sufficient condition. At that boundary the positive phase profile gives the actual asymptotic abundance and composition independently of the initial population, distinguishing the critical regime from exponential extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
