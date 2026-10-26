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

The standalone `checker.py` uses only Python's standard library. Executed directly from the current package: `python3 checker.py`; result: `ALL_CHECKS_OK K=276 precomp_induced=96 genuinely_noninduced=180 MP=59 T=15 F=5`. The checker directly evaluates every P1–P5 instance for 5,250 reduced candidates, compares the normal form exactly, and independently enumerates all antitone precomplementations. The underlying finite domain is exhaustively checked; an independent audit was not performed. T and F counts are cross-checks only.
