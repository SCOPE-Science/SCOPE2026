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

# Verification and scope

The proof is symbolic and applies to every Steiner \(2\)-design satisfying the stated hypotheses. It rests on the explicit downset/furtherness weights, uniqueness of the line through two points, connectivity and graph cycle ranks, and Stong core uniqueness. All persistent positive-dimensional classes are represented by cycles in graphs, making inclusion injective on integral first homology.

`verify.py` is standalone Python 3 code with no external packages or data dependencies. Execute `python3 verify.py` and require `VERIFY_OK`. It constructs the all-pairs design on five points, the Fano plane, the affine plane over three elements, and the 15-point binary projective-space triple system. It verifies every pair lies in exactly one block and independently computes graph persistence at every root from principal downsets, comparing the complete degree-zero and degree-one interval multiplicities with the formulas. There are 100 roots across the four cases.

This finite exhaustive verification does not establish the universal theorem by itself, nor does it enumerate all 80 Steiner triple systems or independently verify their published enumeration. The cited classification and Stong theorem are used as established external results. Independent scientific audit remains unperformed.
