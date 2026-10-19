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

# Reproduction

Run `python3 verify_chord.py` with Python 3.9+ and no nonstandard packages. The test exactly computes the 28-site gadget gain using rational first-arrival recursion and bounds the analytic factorial series by an explicit rational tail. It then checks every cycle length from five through twenty-eight, and independently enumerates all vertex permutations at sizes five, six and seven. The proof of all larger cycle sizes requires the priority-path influence bound in `RESULT.md`; a finite table alone does not establish the infinite theorem. The script prints the exact gadget fraction and strict positive universal lower bound.
