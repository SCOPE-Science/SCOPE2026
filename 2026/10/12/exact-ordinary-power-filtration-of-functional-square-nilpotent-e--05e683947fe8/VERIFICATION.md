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
# Verification

The proof was reconstructed from the definitions of ordinary powers and evolution-algebra multiplication. The critical support identity is that the product of two coordinate subspaces is spanned by squares of basis vectors in their support intersection. Under the functional-square assumption those squares each have one target, so ordinary powers remain coordinate subspaces and the induction is exact.

`verify.py` independently enumerates all acyclic partial functions on labeled vertex sets of sizes one through six, interprets them as functional-square support digraphs, builds ordinary-power supports directly from the defining recurrence, and compares them with the path-depth prediction. The completed run reports `VERIFY_OK cases=18248`.

The finite enumeration does not establish the theorem in arbitrary dimension; it stress-tests the support recurrence, boundary powers, branching, merging, disconnected components, and isolated vertices. The arbitrary-dimensional proof in `RESULT.md` is the actual proof.

Literature checks used full primary texts where the comparison was decisive. The 2012 exact-index paper and the 2013 graph paper are the closest predecessors; the 2015 annihilator-extension paper and the 2016 nilpotent-classification paper were inspected as plausible broader sources. No independent audit has been performed.
