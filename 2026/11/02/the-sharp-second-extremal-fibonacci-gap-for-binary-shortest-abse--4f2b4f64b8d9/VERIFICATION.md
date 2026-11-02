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

The theorem is proved by a recursive count of absent scattered subsequences, a strict local improvement argument, and an exact Fibonacci defect calculation. Run `python checker.py` using Python 3 standard library only. The checker must print `ALL_CHECKS_PASS`.

Direct subsequence enumeration is used only for small mixed-pair words. A separate earliest-occurrence subsequence automaton verifies all mixed-pair words with between two and eleven blocks and checks all binary words of lengths ten, twelve, fourteen, sixteen, and eighteen. Those finite checks do not certify all lengths. Independent mathematical verification has not been performed.
