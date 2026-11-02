---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The four Gaussian overlap integrals give the exact strictly positive prefactor times e^(-i phi)+r²e^(i phi)+2rc cosh u, with c=e^(-a²/sigma²), u=aT/sigma², phi=2pi a nu. For r=1 zeros obey cos v=c cosh u, |u|<=arcosh(1/c); the implicit gradient never vanishes and the level-set Hessian is -c cosh(u) I, proving smooth closed strict convexity. The exact integral I(c)=int_0^arcosh(1/c) arccos(c cosh u) du satisfies I′(c)=-pi/(2c), I(1)=0, hence I=pi/2 log(1/c), and the physical Jacobian yields area exactly 1. Independent quadrature checked c=0.1,0.4,0.8 to ~1e-15. For r≠1 imaginary part (r²-1) sin phi=0 forces odd phi pi; the positive cosh equation has exactly two solutions at ±arcosh((r+r^-1)/(2c)) and the nonzero Jacobian changes sign between them. All real T,nu and positive parameters covered analytically.

## originality

PASS

PASS best of knowledge. Mathematical statements and implication directions were compared to inspected primary literature, not merely titles or identical parameter names; residual risks explicitly retained.

## value

PASS

The real two-Gaussian pulse/cat state is a natural ambiguity-function benchmark. A parameter-independent one-area law for all zero ovals and a complete topology change under any positive amplitude imbalance are precise global geometric invariants, contrasting with the established short-chord blind-spot approximation. The theorem distinguishes exact remote zeros from practically small signals without claiming more general Gaussian multiplets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
