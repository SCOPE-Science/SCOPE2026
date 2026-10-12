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

# Verification record

Run `python3 verify.py` using standard Python 3, with `verify.py` in the working directory. The run enumerates every unoriented length-four hypercube geodesic in two independent combinatorial constructions, verifies that both give the same 192 vertex subsets, checks the compatibility degree and complete 31-list obstruction for a fixed geodesic, and independently excludes every possible disjoint triple. It also checks all explicit Q4, Q5, Q6 path witnesses, the uncovered vertices, and the ten-path dimension-six vertex covering.

The recorded output is in `verification_output.txt`; the final line is `VERIFY_OK`. This certificate supports a finite theorem, not an infinite search. The elementary size bounds are proven mathematically in `RESULT.md`. The code and documented source inspections have received self-review only, and no independent audit has been performed.
