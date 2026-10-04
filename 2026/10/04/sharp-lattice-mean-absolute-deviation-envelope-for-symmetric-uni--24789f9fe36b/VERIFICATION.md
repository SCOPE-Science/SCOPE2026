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

The proof is analytic. The accompanying checker uses exact rational arithmetic
for all finite identities.

It verifies the centered discrete-uniform formulas
\[
v_m=\frac{m(m+1)}3,
\qquad
d_m=\frac{m(m+1)}{2m+1},
\]
checks strict decrease of the consecutive secant slopes, and confirms exact
attainment of the upper chord by every tested rational variance phase.

For many random rational mixtures of centered discrete uniforms, the checker
computes the variance and mean absolute deviation exactly and verifies the
sharp upper envelope. It also checks the explicit same-variance sequence
\[
(1-v/v_R)U_0+(v/v_R)U_R
\]
whose mean absolute deviation is \(3v/(2R+1)\).

Representative large-cell phase sequences are compared with the asymptotic
coefficient
\[
\frac{\sqrt3}{48}\bigl(1+4\theta(1-\theta)\bigr).
\]

Finite replay does not replace the strict-concavity proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK moment_checks=2002 slope_checks=999 equality_checks=21000 random_mix_checks=30000 low_sequence_checks=20 phase_checks=20`.
