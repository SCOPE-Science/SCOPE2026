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

Run `python3 verify.py` with a standard Python 3 installation. Its deterministic exact-rational parameter grid checks polynomial coefficients, sign identities and the derived algebraic inequalities; separate eigenvalue computations corroborate the predicted stable/unstable transition. The observed run returned `VERIFY_OK 13860 exact-and-spectral checks`.

The proof in `RESULT.md` independently establishes the theorem for all continuously varying parameters in the stated domain. The finite checker cannot certify an infinite parameter domain, publication priority or an independent audit. The work does not cover negative disagreement modes or more than two agents.
