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

## Checks performed
A standalone standard-library checker `verify.py` independently enumerates all labelled one-point extensions via transitive closure rather than relying on the ideal/filter formula. It compares this direct count to independent-set enumerations for every fixed-partition bipartite graph of total size two through six. For every missing cross-edge it checks the exact type-count change, both sharp bounds, and both necessary-and-sufficient equality characterizations. It also constructs the near-universal-pair reduction gadget for each bipartite graph with part sizes at most two, and for reproducible additional samples with larger sides.

The package records 1,290 full graph instances, 5,025 missing-edge perturbations, and 35 reduction gadgets. All tests passed, yielding `ALL_TESTS_PASS`. Byte-for-byte reproducibility is achieved by running `python verify.py` and comparing stdout to `verification_output.txt`.

## Proof limits
Exhaustive verification stops at six vertices for the extremal theorem and uses only small exhaustive/sampled inputs for the complexity gadget. The all-size statements follow from the displayed identities and induction-free extremal argument in RESULT.md, not from finite enumeration. The external published #BIS completeness theorem supplies the hardness premise. The independent scientific audit channel remains unperformed.
