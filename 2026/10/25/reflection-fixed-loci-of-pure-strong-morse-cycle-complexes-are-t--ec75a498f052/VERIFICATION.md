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

# Reproducibility

Run `python3 verify.py` (Python 3 standard library only). It enumerates every rooted-path facet for each size from 6 through 40, computes the full incidence-orbit partition of a representative of every reflection-axis conjugacy class, and checks that every maximal admissible incidence-orbit face is exactly one of the two specified sets. It also checks that the two faces are disjoint and have the predicted cardinalities. The expected terminal output is in `verify_output.txt`.

The finitely many checks confirm the combinatorial formula within the stated range; the unbounded theorem uses the rooted-path description and boundary/alternation arguments in `RESULT.md`. No independent scientific audit has been performed.
