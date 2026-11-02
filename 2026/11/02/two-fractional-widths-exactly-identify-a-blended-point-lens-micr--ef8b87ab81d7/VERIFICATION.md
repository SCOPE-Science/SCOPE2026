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

The exact amplification inversion and strictly ordered width-ratio integrals in RESULT.md form the full proof. The derivative comparison is pointwise strict for every \(a\le s<b<t\le1\) and every \(y>0\), so it proves a global statement without enumeration. The explicit inverse and bounds were inspected for positivity and boundary attainability.

To repeat numerical corroboration, extract the accompanying `CHECK.py` and run `python3 CHECK.py` (Python 3 standard library only). It checks many finite parameter configurations using 75-digit decimal arithmetic, compares direct forward light-curve threshold crossings and inverse reconstructions, and displays one example. Its checks are finite, not a certified exhaustive search or proof of the universal theorem. No independent scientific audit has been performed. The cited primary literature and residual historical-priority uncertainties are described in REVIEW.md.
