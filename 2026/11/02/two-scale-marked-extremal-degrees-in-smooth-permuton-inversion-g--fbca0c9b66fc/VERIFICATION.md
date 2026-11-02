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

Run `python3 verify.py` with Python 3.10 or later; no external packages are needed. The retained `verify_output.txt` is the observed result of the included script. There were 362894 assertions: exact exhaustive inversion-degree identities on all permutations of orders 2 through 8, rational uniform-margin/boundary checks for a positive asymmetric density, and reproducible finite-sample diagnostics with 350 samples of size 1800. The first two scaled-degree empirical means were 0.878900 and 1.318990, compared with the Poisson limits 0.886227 and 1.329340.

The checker does not certify functional weak convergence or an infinite Poisson/Gaussian law; the proof in `RESULT.md` separately supplies the boundary-strip functional CLT, de-Poissonization, Poisson-mark independence, and Chernoff localization. No independent mathematical audit was performed. The result does not cover singular permutons, zero corner density, or growing rank.
