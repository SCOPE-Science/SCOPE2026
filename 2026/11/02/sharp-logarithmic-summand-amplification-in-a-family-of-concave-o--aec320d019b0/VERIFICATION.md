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

# Reproducibility and limits

The argument in `RESULT.md` supplies the infinite-dimensional proof. The finite script `verify.py` uses only Python 3 standard-library functions and independently evaluates strict negative curvature, monotone/subadditive test inequalities, the disjoint-vector modular identity, and the exact entropy-tail inequality for finite weight arrays. Run from this directory with `python verify.py`; the observed result was `PASS: 1686 finite checks`.

The checker does not certify global concavity for every real input, the uniform all-weight entropy bound, completeness, or any limit. Those statements are supported by explicit analytic steps in the proof and require mathematical review. Only the displayed fixed-parameter asymptotic is established; no finite-\(n\) exact optimizer classification or joint parameter limit is claimed.

Self-review: passed. Independent audit: not yet performed.
