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

# Reproducible verification

Run `python3 checker.py` with Python 3 and the standard library. This checks all four-valued leaf-label assignments for \(n=1,\ldots,7\) in the \(p=1/4\), \(h=3\) case, exact rational binomial sums against stable ratio recurrences for four rational parameters through \(n=27\), and the predicted parity limits numerically for larger \(n\). Expected terminal marker: `ALL_CHECKS_OK`.

The general infinite statement is proved by pointwise convergence of exact binomial likelihood ratios under a summable bound. Numerical output only tests finite cases; it does not independently certify the proof or the historical novelty assessment.
