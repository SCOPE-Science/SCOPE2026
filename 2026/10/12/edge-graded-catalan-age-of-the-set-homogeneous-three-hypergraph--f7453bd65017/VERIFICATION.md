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

Replay: `python3 artifacts/verify.py` (Python 3, standard library only). The code is self-contained and has no external data dependencies. The output observed in the run was:

`VERIFY_OK 73 exact assertions; exhaustive plane-tree shapes through n=9; permutation-isomorphism classification through n=6`

It checks the independent tree-based and recursion-based edge-count distributions through nine leaves and uses exhaustive vertex permutations to verify pairwise nonisomorphism of the hypergraphs from every plane shape through six leaves. It also verifies the Catalan, palindromicity, 5-vertex gap, six-vertex full-support base, and ordered-tuple formulas at the documented finite sizes. The analytic all-arity claim follows from the proof, not from bounded computation. The structural identification and homogeneity are cited theorems, not a new computational assertion.
