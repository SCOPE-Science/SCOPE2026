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

Exact verification: run `python3 check_witnesses.py` (Python standard library only). It independently counts representations by a modular-inverse sum over the third generator and by two floor-indexed branches. For 19 odd generators from 3 through 39, it checks four exact counts (two base and two shifted) plus six period shifts, for 190 assertions. Expected full stdout is `check_output.txt`. The argument for all odd generators is algebraic and is written in `RESULT.md`; the finite checks do not establish the infinite theorem. Scientific independent audit has not been performed.
