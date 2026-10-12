---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The exact elimination identity is checked coefficient-by-coefficient in `verify.py` using integer polynomial arithmetic. The same script evaluates the critical polynomial with exact rational arithmetic at two adjacent decimal rationals and confirms
\[
0.6589251988439<\theta_*<0.6589251988440.
\]
It also checks representative signs of the nonsymmetric discriminant factor on both sides of the bracket using high-precision decimal arithmetic.

The all-parameter proof does not rely on those samples. Its decisive steps are: every zero of the discriminant factor lies below \(3^{-1/4}\); the exact elimination maps such a zero to the polynomial \(P\); and \(P'\) is strictly positive on \((0,1)\) by the analytic bound in `RESULT.md`.

Unproved limits: no claim is made about non-translation-invariant Gibbs measures, extremality, arbitrary Cayley-tree order, or the uniqueness of analogous thresholds for other compatibility graphs.
