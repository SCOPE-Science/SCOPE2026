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

Run `python size_profile_checker.py` using Python 3. The checker exhausts all n-to-n maps and their candidate stable subsets for domain sizes one through six. It compares the resulting exact size histogram with the finite formula and tests strict log-concavity where the latter has two neighbors. The same code checks central-coefficient normalization numerically for three larger even domain sizes. No probabilistic simulation is treated as a theorem; the local limit and asymptotic variance follow by the analytic estimates in RESULT.md. The first-public date of the motivating 2026 source is 2026-05-13; source metadata and all evidence refer to original public sources. Independent validation has not been performed.
