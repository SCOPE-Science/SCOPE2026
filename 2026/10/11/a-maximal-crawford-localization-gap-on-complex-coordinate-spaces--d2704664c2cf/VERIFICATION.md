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

# Reproducibility and verification

The analytic proof in `RESULT.md` applies to all index sets with at least two members, including infinite and uncountable sets, and all \(0<r<1\). Its critical identity is \(f_jx_j\ge0\) with \(\sum_j f_jx_j=1\) for norming pairs; this follows by equality in two triangle inequalities. The prescribed multipliers lie in the closed half-plane with real part at least \(r\), and the special two-coordinate state attains the boundary.

Run `python verify.py` using the standard Python library. The checker tests exact rational Pythagorean phase parameters and finite barycentric meshes with `fractions.Fraction`, asserting that the squared modulus of every tested convex combination is at least the prescribed exact Crawford square, with equality at the explicitly constructed midpoint. It also checks the coordinate-restricted value and maximal-defect arithmetic. These tests do not enumerate arbitrary functionals on an infinite-dimensional space and are **not** a replacement for the proof.

For perturbations, both the full and restricted infima are one-Lipschitz in operator norm by the pointwise state evaluation inequality. The strict condition \(\|E\|<\min\{r,(1-r)/2\}\) is essential for simultaneously retaining positivity and a nonzero gap. Independent audit has not been performed.
