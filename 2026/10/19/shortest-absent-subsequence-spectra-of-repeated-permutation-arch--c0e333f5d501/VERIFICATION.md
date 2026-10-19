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

Run `python3 verify.py`. The exact finite enumeration must report the table's seven supports and finish with `ALL_SAS_ARCH_SPECTRUM_CHECKS_PASSED`. Exhaustion covers all permutations with q<=7, and direct subsequence enumeration independently checks the formula for q<=4 and t<=3. The general formula is established by a separate universal combinatorial argument; the code does not certify the unbounded domain or any q>=8 spectrum. An independent audit has not been performed.
