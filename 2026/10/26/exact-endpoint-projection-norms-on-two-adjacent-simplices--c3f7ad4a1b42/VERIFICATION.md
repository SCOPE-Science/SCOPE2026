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

## Reproduction
Run `python check_exact.py` with Python 3; no external packages or network access are needed. The script uses exact rational Gaussian elimination of assembled finite-element mass matrices and independent exact polynomial integration of absolute affine functions against the uniform-simplex barycentric marginal. It checks all nodal inverse coefficients and absolute row norms for nine dimensions and six positive rational area fractions, with 432 node comparisons and 54 complete-norm comparisons. Special planar equal-area and degenerating-limit constants are checked by exact arithmetic.

## Scope of evidence
The script is finite diagnostic evidence for formulas proved in RESULT.md. It does not certify the infinite-dimensional family by enumeration, the absence of prior equivalent publications, or an independent scientific audit. The proof uses explicit reproducing kernels, elementary beta integration, and strict differentiation to cover every integer dimension and every permitted positive area ratio.
