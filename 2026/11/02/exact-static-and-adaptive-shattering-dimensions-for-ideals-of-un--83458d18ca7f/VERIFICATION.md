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

# Verification procedure
Run `python3 verify.py` using the Python standard library. The program contains two distinct computational routes: full ideal-bitmask enumeration with adaptive rank recursion for small uniform profiles, and a level-profile deletion recurrence for a larger range and endpoint-truncated cases.

The observed output is `UNIFORM_WEAK_ORDER_IDEAL_CHECKS_PASS 18 158 1183 186` and is supplied in `verification_output.txt`. The 18 direct cases each include full VC support enumeration. The 158 uniform-profile checks include 32 small-profile cases and 126 larger-profile cases; the endpoint-bound checks enumerate 1,183 profiles. The last output integer sums the numbers of distinct ideals across direct cases, not the number of searched adaptive game states.

These computations are finite sanity checks. Correctness for arbitrary positive widths and heights rests on the unrestricted inductive proof in `RESULT.md`; the verifier cannot establish novelty or all-parameter validity by enumeration alone. Independent scientific review has not been performed.
