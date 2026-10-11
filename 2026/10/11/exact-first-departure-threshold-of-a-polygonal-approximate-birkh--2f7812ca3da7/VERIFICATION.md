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
The analytic proof reduces the improving-pair region to two affine cells already isolated by the focal paper. On each surviving cell, monotonicity in \(u\) puts the maximum on an explicit boundary, and a one-variable derivative sign gives the global cell maximum. The mixed-cell boundary value is
\[
D_* = \frac{18910336411}{19465125400},
\qquad
1-D_* = \frac{554788989}{19465125400}.
\]
A strict-feasibility perturbation of the boundary point approaches \(D_*\), so the value is a supremum of actual improving pairs rather than merely a formal boundary upper bound.

`activation_threshold_check.py` replays the rational arithmetic with Python's standard-library `Fraction`. It checks the branch endpoints, the derivative-sign tests on both cells, the strict comparison between the two cell maxima, the cutoff identity, and one exact rational point in the sharpness family. Its SHA-256 digest is `2861b4e3c591a6dc2287a398df59da8ca9d7aba34a6c5151bcee82090d2ad146`.

No numerical sample is used to infer a global inequality. The checker supports arithmetic reproducibility; the infinite-dimensional quantifiers in the profile statement are discharged by the source's exhaustive two-dimensional facet reduction plus the analytic optimization and limiting family in the proof.

The result does not verify the full post-activation profile, the companion plane \(Y\), or a general polygonal-space theorem.
