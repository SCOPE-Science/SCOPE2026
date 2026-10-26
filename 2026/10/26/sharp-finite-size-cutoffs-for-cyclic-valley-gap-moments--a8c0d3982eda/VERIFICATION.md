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

# Verification and limits

The proof of the mean-boundary integral uses exact integration over a triangular subset of the unit square. The variance-boundary proof is an exact cyclic overlap classification and a trace identity for bounded symmetric integral kernels, followed by a strict operator positivity argument. The universal assertions rely on these analytic steps, not on numeric computations.

The `verify.py` program exhaustively enumerates \((K-1)!\) circular rankings after fixing the lowest-priority site at zero. It runs 16 independent exact-rational assertions: mean boundaries for \(i=1,\ldots,6\), plus mean/variance checks at the variance boundary for \(i=1,2\). The latter checks use the published coefficients \(b_1=1772/14175\), \(b_2=32/405\) and independently specified boundary traces \(\delta_1=29/28350\), \(\delta_2=1/2025\).

Run `python verify.py` using Python 3 without nonstandard dependencies. These finite tests neither establish results for all integer indices nor constitute independent external validation. The integral-kernel identity and positivity proof are the mathematical certificates of the infinite quantifiers.
