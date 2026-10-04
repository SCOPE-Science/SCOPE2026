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
# Verification

The printed vector field was transcribed independently and differentiated directly. The equilibrium proof uses only the factorization
\[
F(y)=y(a_1y^2-a_2y-a_3)
\]
and the exhaustive alternative forced by
\[
x(a_6y+a_7x)=0.
\]
No numerical search is used to establish completeness.

A fresh computer-algebra replay expanded \(\det(\lambda I-J)\) at a generic line point to
\[
\lambda\bigl(\lambda^2+a_5zF'(r)\bigr)
\]
and simplified the vector field to zero at each symbolic isolated-root formula. The replay used SymPy 1.14.0 from its installed package path. These computations check algebra already proved in closed form; they are not used as substitutes for the proof.

At the article's numerical parameters, exact substitution gives
\[
r_\pm=5\pm\sqrt{35},\qquad
s_\pm=-120\pm\sqrt{14410}.
\]
The article's displayed nonzero-line radicand becomes \(-3/5\), while the actual quadratic discriminant is \(7/5\).

Limits: this verification covers the equilibrium set and linear spectra of the printed positive-parameter system only. It does not certify nonlinear stability, global boundedness, chaoticity, or any control/communication construction.
