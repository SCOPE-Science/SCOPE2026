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

# Reproducibility
The file `CHECK.py` is standalone and uses Python's standard library, with exact integer arithmetic. Run `python CHECK.py` to obtain `EXACT_FOLDED_CUBE_SPECTRA_OK 1596`. This checks the closed eigenvalue formula against independent binomial Krawtchouk convolution for all even harmonic weights \(3\le n\le70\), and against a direct graph-distance Walsh sum on \(2^{n-1}\) quotient representatives for \(3\le n\le10\). It also checks zero trace, inertia, total multiplicity, and the sharp quadratic embedding constant.

# Verification limits
No finite test certifies the formulas for every \(n\). The infinite scope rests on the coefficient and monotonicity derivations in RESULT.md. Previous Laplacian and related folded-cube harmonic calculations are not independently re-certified. Historical uniqueness and external validation are not claimed.
