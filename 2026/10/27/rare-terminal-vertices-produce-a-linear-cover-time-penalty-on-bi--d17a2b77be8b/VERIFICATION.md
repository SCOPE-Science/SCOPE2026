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

`verify.py` reproduces the full-state exact-rational backward first-step computation for every possible last vertex for cycle sizes 3 through 8 and three fixed biased probabilities. Its outputs match independently derived formulas for both last-site probabilities and conditional means. The program also checks numerical finite-size remainder ratios at n=10,20,30,40. Run `python verify.py`. The infinite uniform estimate is proved by the analytic gambler's-ruin identities, not by any finite checks. The full motivating preprint could not be read; no independent audit was performed.
