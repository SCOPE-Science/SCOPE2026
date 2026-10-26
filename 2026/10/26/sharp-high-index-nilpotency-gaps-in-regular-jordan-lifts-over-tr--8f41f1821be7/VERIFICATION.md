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
Execute `python3 verify.py` using Python 3 and its standard library only. The terminating line is `HIGH_TAIL_OK`.

The executable enumerates all polynomials for the companion representation over seven small prime-field truncated rings of lengths three through five; it checks predicted upper-tail ranks and the total low-tail complement by direct powers. It separately checks 750 full random matrix lifts in five parameter configurations, computing coefficients and nilpotency orders by exact arithmetic in truncated polynomial rings.

The infinity-parameter proof relies on cyclicity over the local ring, the companion polynomial identity, and a uniform orbit count, as shown in RESULT.md. The finite experiments do not establish the all-parameter theorem or publication priority. Independent assessment is not performed.
