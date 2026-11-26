---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction

Run `python3 verify.py` with standard-library Python 3. It enumerates all 16 two-column states and their four candidate successors, finds 10 allowed arcs, and checks for exactly two loops and one directed four-cycle in cyclic strongly connected components. Its direct neighbourhood check enumerates all vertex labellings on circular ladders with circumferences 3 through 8 and checks the complete solution sets. The all-circumference proof instead uses propagation from a crossing spoke and the period-four relation when no spoke crosses.

# Boundaries

The circumference is at least three, and the count distinguishes complementary vertex subsets. Only circular ladders are included.
