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

Run `python checker.py` with Python 3.10 or later. No optional modules, data downloads or network access are required. The script constructs finite exchange kernels with exact rational hypergeometric probabilities and verifies row normalization, detailed balance, stationarity, conditional mean and conditional variance for all starts in all specified small finite models. It additionally computes selected two-step numerical total-variation distances for larger urns and checks elementary bounds.

In the executed package the script reported `PASS: exact finite assertions and numeric diagnostics: 5325` and, for \(n=80\) at exactly half exchange, two-step total variation `0.0015218949731202146` from the all-one-colour initial state. The numerical diagnostics do not prove convergence or originality. The infinite-order argument is in the `RESULT.md` Stirling local-limit lemma and total-variation mixture proof. The independent-audit status is not performed.
