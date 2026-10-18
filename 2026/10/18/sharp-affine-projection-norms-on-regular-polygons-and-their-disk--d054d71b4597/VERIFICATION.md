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
The proof derives the covariance, reproducing kernel, vertex extremality, cap formula and fourth-order angular cancellation analytically. The included standalone `verify.py` runs on Python 3 standard library only, without external data. It calculates cap moments with shoelace identities and independently calculates the same \(L^\infty\) integral in polar coordinates by composite Simpson quadrature. The script checks sixteen side counts, three low-side exact rational evaluations and seven large-side rescalings of the asymptotic coefficient. Numerical comparisons have finite precision; they do not prove uniform limits or uniqueness of prior results.

The historical-priority comparison is limited by inability to inspect the full 1987 hexagon paper. Scientific limitations and competing source scopes are described in `RESULT.md` and `REVIEW.md`. No independent audit or external validation has been performed.
