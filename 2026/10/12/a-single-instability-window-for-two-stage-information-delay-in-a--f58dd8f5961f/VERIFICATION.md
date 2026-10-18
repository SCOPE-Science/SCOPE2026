---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed the source’s five equations and Jacobian, eliminating the stable -mu recovered eigenvalue; the feedback factor is (lambda²+A lambda+C)(lambda+b)(1+tau lambda)+D, with A,C,D>0. Independently recomputed all quartic coefficients and Hurwitz determinants symbolically: Delta2>0 and Delta3=A(Ab+C+b²)(1+b tau)(1+A tau+C tau²)-D[1+(A+b)tau]². When Delta3<0 the Routh first column has exactly two sign changes, and positive coefficients preclude positive real roots, so precisely one unstable conjugate pair. Equality factors an imaginary pair plus a stable quadratic. The log derivative K'/K has cubic numerator H=Cb(A+b)tau³+3Cb tau²+(2C-A²-b²)tau-(A+b), with exactly one positive root by Descartes, negative initial and positive leading signs. The rational witness exactly solves every equilibrium equation with (A,b,C,D)=(1,1,1,5/2), Delta3=(6tau³-8tau²-8tau+1)/2; exact sign brackets and tau=0,1,3 match. Independent checks do not replace universal Routh/Descartes proof. At equality only spectral neutrality is asserted, not nonlinear stability.

## originality

PASS

Best-of-knowledge PASS: read the author-accessible complete text of Fang–Liu–Du’s actual paper. It specifies vaccination acting on susceptible stock and a two-stage exponential information filter; its §3 local stability criterion uses reduced tau=0 cubic, and §4 treats heteroclinic persistence for sufficiently small tau. Its conclusion identifies Hopf studies as future work; no all-delay quartic criterion or one-minimum theorem. A 2007 one-filter birth-vaccination model already shows reentrant stability, so only the source-specific sharp two-stage map is novel. Other 2018 saturated-treatment information models may exhibit multiple switches but do not imply the exact same transfer polynomial.

## value

PASS

A complete local stability regime map for a contemporary two-filter disease-information model resolves an explicit uncertainty left in that model’s source: which positive information delays destabilize and restabilize the endemic state. The all-parameter at-most-one-window theorem, exact threshold and feasible witness are mathematically useful; no claim is made to new qualitative reentrance in general or nonlinear periodic orbit existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
