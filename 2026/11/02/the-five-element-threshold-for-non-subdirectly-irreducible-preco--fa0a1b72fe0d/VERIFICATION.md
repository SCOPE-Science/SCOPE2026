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

Run `python3 checker.py` (no third-party packages required). The checker enumerates row candidates on chain sizes 2 through 5, tests P1--P5 and the three additional defining equations for the stronger algebra, and checks each interval-partition congruence. The observed total/SI pairs are (1,1), (1,1), (2,2), and (6,4). It also tests the explicit all-size family up to size 12, including the two stipulated one-pair congruences. The universal claim is derived in RESULT.md and is not inferred from the bounded computation. Independent external audit has not been performed.
