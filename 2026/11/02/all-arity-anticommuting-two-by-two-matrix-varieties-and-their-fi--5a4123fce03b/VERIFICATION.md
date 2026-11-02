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

# Reproducible finite-field checks

Run `python3 check.py` and compare standard output byte-for-byte to `check.out`. The code constructs field arithmetic directly, including the extension-field multiplication in \(\mathbb F_9\), and calculates the original anticommutation matrix products, not just the theorem's formulas. It separately counts the orthogonality problem in \(\mathfrak{sl}_2\) using the bilinear form, and computes linear anticommutator-kernel ranks over \(\mathbb F_9\).

Observed checks: 16 exhaustive tracefree configurations over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9\); seven exhaustive full matrix tuple configurations over \(\mathbb F_3,\mathbb F_5\); one full-matrix pair check over \(\mathbb F_9\) using all first matrices and linear row reduction. All match the declared formula. Completion marker: `ANTICOMMUTING_M2_ALL_ARITIES_ODD_OK`.

Finite tests do not prove arbitrary-field irreducibility, incidence-image closure, higher-arity claims in all fields or historical originality. The proof handles those mathematically in `RESULT.md`. No independent audit has been performed.
