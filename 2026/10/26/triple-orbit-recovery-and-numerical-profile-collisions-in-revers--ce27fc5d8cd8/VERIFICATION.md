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

The accompanying standard-library Python checker enumerates the eight signed coordinate transformations, all ten subgroups, and their actions on ordered pairs of labelled linear orders for arities 2 through 5. The checker directly computes orbit partitions and compares them with the closed formulas; it also verifies a free triple orbit and that no pair type has trivial full-group stabilizer. The finite verification corroborates but does not prove the all-arity formula or the model-theoretic reduction, both addressed by explicit proofs in RESULT.md.

Execute with `python3 verify.py`; the expected final line is `ALL_CHECKS_PASS`. No independent audit has been performed.
