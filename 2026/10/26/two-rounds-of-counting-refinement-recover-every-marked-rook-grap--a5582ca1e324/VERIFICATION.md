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

Reproduce the finite checks by executing `python3 rook_verify.py`; the exact recorded standard output is in `rook_verify_output.txt`. The program checks six complete subset censuses (70,480 configurations), 2,500 reproducibly randomized larger-board configurations, the closed orbit-class formula in each instance, and explicit automorphism-generated orbit partitions for the boards with at most nine vertices. Its verification asserts refinement-orbit equivalence, at most two strict splits, and the sharp witness with three markers on the four-by-four board.

The mathematical proof covers all \(m,n\ge2\) and all marking sets. Finite testing alone does not establish the infinitely quantified theorem. No theorem prover, independent human review, or external certification has been used. Independent audit has not been performed.
