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

# Reproducibility and scope of checks

The command `python3 artifacts/verify.py`, run in the directory containing `RESULT.md`, completes with `VERIFY_OK` using exact integer and binary-vector arithmetic and only the Python standard library. The verifier independently generates the sixty even permutations on five letters, the six Sylow \(5\)-subgroups, and their conjugation action on six points. It checks that two specified elements generate all sixty induced permutations, that this action is \(2\)-transitive, and that its binary permutation module has precisely the four invariant subspaces of dimensions \(0,1,5,6\), by enumerating all reduced-row-echelon subspaces in dimension six. It lists the five Sylow \(2\)-subgroup orbit matchings, verifies that they partition all fifteen two-element subsets, and checks that the intersection of the five corresponding commutator spaces is exactly the one-dimensional constant line.

The computation verifies the finite six-point input to the general proof. It does not enumerate all subgroups of the semidirect product or prove an infinite family by extrapolation. The formulas for arbitrary \(t\ge1\) use the maximal-subgroup argument for split elementary abelian extensions, the direct-sum behavior of module radicals, and the commutator-space direct sums, as written in `RESULT.md`. Historical priority is not computationally certifiable, and an earlier unindexed exact application of the same module remains possible. Independent audit has not been performed.
