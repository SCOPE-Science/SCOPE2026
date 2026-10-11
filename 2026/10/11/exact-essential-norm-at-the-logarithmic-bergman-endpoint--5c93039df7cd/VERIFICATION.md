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

The mathematical evidence is the infinite-dimensional argument in `RESULT.md`; the supplemental script `artifacts/verify.py` checks exact small-index beta-product arithmetic, the exact factorization of the matrix entries in sample blocks, and the closed-form analytic lower-bound integral. It does **not** certify an infinite sum, compactness, or a Hilbert-space operator norm on its own.

Execute `python3 artifacts/verify.py` from the package root. A completed check prints `VERIFY_OK: exact beta coefficients and finite comparison checks; infinite proof is analytic`. The proof requires four noncomputational checks: coefficient isometries; summability of all regions of the Hilbert--Schmidt difference; the two row/column Schur inequalities uniformly beyond the cutoff; and weak convergence of logarithmic-block vectors as their support escapes to infinity, yielding the sharp lower bound. All these steps are written explicitly in `RESULT.md`.

The exact input normalization is \(dA=dx\,dy/\pi\) and source weight \((\log(e/(1-|z|^2)))^2\). The result is limited to distance from compact operators; the full operator norm is uncomputed, and two named comparison manuscripts had incomplete access. No external independent review has been performed.
