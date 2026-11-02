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

Run `python3 verify.py` in a Python 3.9+ environment with no third-party dependencies. It independently enumerates induced-subgraph types and their automorphism groups, with the expected final marker `VERIFY_OK`. The script checks the exceptional cycle and rook graphs and 18 equal-clique/complement cases. The symbolic polynomial and the asymptotic transfer are proved in `RESULT.md`; no finite test is used as an infinite certificate. No external independent mathematical audit has been performed.
