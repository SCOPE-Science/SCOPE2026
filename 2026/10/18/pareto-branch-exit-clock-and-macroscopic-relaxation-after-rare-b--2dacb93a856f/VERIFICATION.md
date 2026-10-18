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

The included `verify.py` uses exact rational arithmetic and the exact floor-based BCZ map. It checks 120 cusp configurations, both corner reductions, the index-two arithmetic progression, the first non-two return and its ceiling formula, and an exact deterministic deviation bound against \(1/(2d)\). Executing it with Python 3 printed `VERIFY_OK 120 exact branch-and-exit cases`.

The analytical proof independently establishes the rare-event area limit and the limiting distribution of \(Rd\), followed by continuous mapping for the scaled exit clock and macroscopic path. Sample checks cannot establish those infinite-parameter limits, uniqueness in literature, or any external certification. Independent audit was not performed.
