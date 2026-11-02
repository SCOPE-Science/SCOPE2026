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

The complete proof derives a post-input derivative quadratic and establishes an exact necessary-and-sufficient positive-root criterion for every admissible parameter pair. Boundary cases, the stationary shoulder, and the reentrant parameter interval are proved analytically in `RESULT.md`.

`verify_hydrograph.py` passed 12,732 assertions when run with the standard Python 3 library. Its tests include exact rational polynomial identities and finite numerical examples. No finite test establishes the continuum theorem, and the script's decimal checks are not formal interval arithmetic.

Self-review was performed. Independent audit and empirical hydrological validation have not been performed. Historical priority remains provisional in view of general mixture-modality results and literature coverage limitations.
