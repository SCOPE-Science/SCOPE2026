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

Run `python3 verify.py` from this directory using the Python standard library only. The executable directly reconstructs Petersen vertices and edges as disjoint two-element subsets of a five-point set and constructs the line graph. It checks 105 pairwise graph distances and verifies the five antipodal fibers; enumerates 56 radius-one faces and 1024 radius-two faces including the empty face; and calculates exact mod-two boundary ranks for both complexes. It constructs the 120 permutations of the underlying five symbols and checks the proposed degree-one and degree-four traces by *separate* signed simplicial Lefschetz calculations; it also checks the group irreducible character table and multiplicities via exact integer inner products.

An actual invocation completed successfully with the output:

`PETERSEN_LINE_RIPS_EQUIVARIANT_CHECKS_OK r1_faces 56 r2_faces 1024 permutations 120`

The mod-two ranks verify finite field homology and cannot alone exclude integral torsion or prove an infinite-family statement. Integral torsion-freeness and homotopy follow instead from the explicit simplicial nerve and fivefold-join description; the character formulas follow from cellular and reduced-join trace identities. Only the stated graph and natural \(S_5\) action are treated. The rational character decomposition is not a claim of integral direct-sum splitting. No external validation has been performed.
