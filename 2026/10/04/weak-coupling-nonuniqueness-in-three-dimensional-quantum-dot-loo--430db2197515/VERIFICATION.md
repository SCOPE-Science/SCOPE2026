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

The proof was checked symbolically from the stated hypotheses. Pairwise disjoint support gives the exact identity
\[
\|W_Y\|_{3/2}=N^{2/3}\|v\|_{3/2}.
\]
Hölder and Sobolev then imply
\[
\int W_Y|u|^2\le C_S N^{2/3}\|v\|_{3/2}\|\nabla u\|_2^2,
\]
so the stated coupling interval makes the quadratic form nonnegative for every admissible geometry. The compact support and regularity of the finite potential preserve essential spectrum \([0,\infty)\), hence the spectral bottom is exactly zero.

No finite numerical computation is used to establish the infinite-dimensional claim. The bound is sufficient, not claimed sharp. The endpoint permits the possibility of a zero-energy resonance, which does not alter the conclusion about the spectral bottom. The two-dimensional problem and the binding-regime optimizer are outside the claim.
