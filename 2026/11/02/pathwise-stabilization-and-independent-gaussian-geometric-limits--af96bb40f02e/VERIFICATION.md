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

# Verification scope

Reproduce with `python3 verify.py`. This file reports a completed test run of 26,859 exact finite checks. The verifier uses rational arithmetic for finite biased-cycle last-vertex distributions, exhaustive short-increment traces for the range/coverage equivalence, and seeded long-prefix examples for the strong pathwise identity. Those finite checks cannot establish almost-sure stabilization or limiting independence. The proof in `RESULT.md` supplies the required infinite argument using the strong law, gambler's ruin, first-passage renewal CLT, and finite-prefix conditioning.

No independent audit or validation was conducted. The search for historical equivalences is qualified by the accessible full-text material listed in `AUDIT.json`.
