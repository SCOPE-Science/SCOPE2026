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

## Analytic checks

The proof independently reconstructs the four necessary implications: substitutability makes the globally individually rational family hereditary; substitutability reduces all nonempty blocks to singleton blocks; persistence turns each singleton block into an individually rational augmentation; and the algorithm's acceptance test coincides with hereditary augmentation. The universal construction is then checked against the exact subset and persistence axioms. The empty-contract case is included.

## Finite experiments

The accompanying `verify.py` enumerates all nonempty downward-closed families on zero through four labels, tests each associated star-market choice function for substitutability and persistence, checks stability against all nonempty blocking contract subsets, and runs every possible arrival order. The script additionally enumerates all 4096 unrestricted three-contract firm-choice tables, filters for both axioms (67 survive), and checks the stable-facet equation and all SMA order ranges for each surviving choice. The run of `python3 verify.py` completed successfully; `verification_output.txt` contains the captured output. The resulting counts are 194 hereditary families, 14092 SUB comparisons, 3709 IRP pairs, 1440 CY candidate checks and 4135 SMA permutations.

## Evidence boundary

Finite enumeration is not a proof of the arbitrary-finite theorem. The exhaustive calculation covers only universality examples on at most four labels; it does not enumerate arbitrary networks or all SUB–IRP functions. No independent external verification has been performed.
