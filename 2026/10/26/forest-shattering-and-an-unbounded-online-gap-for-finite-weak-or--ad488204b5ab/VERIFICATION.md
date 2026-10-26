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

# Verification evidence

Run `python verify_preorder.py adaptive_preorder_trees.json` from the directory containing these files. The program requires only Python 3 and produces the reference output in `verifier_output.txt`. The adaptive-tree JSON specifies a query at each internal node and a normalized tie-block rank vector at every leaf. The checker enumerates all ordered partitions by its own recursive block method, tests every answer path, confirms each leaf vector encodes a valid total preorder, and validates both small-case dimension profiles using exact finite recurrences. The depth-three certificate has eight leaves and seven internal queries; the depth-five certificate has 32 leaves and 31 internal queries. The enumeration has 13 and 75 hypotheses on three and four labels, respectively.

The all-order VC theorem, the strict-positive root upper bound, and the unrestricted block-concatenation theorem are proved separately in `RESULT.md`. The checker supports but does not replace those infinite mathematical arguments. Its output is finite, and no computation purports to determine larger-size online ranks. External audit and independent validation are not performed.
