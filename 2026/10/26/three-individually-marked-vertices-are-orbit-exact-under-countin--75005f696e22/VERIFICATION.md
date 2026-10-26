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

The all-dimensional theorem follows from the structural proof in RESULT.md. The proof uses the intrinsic coordinate-edge decomposition of Hamming graphs, the relation between counting refinement and truncated distances to uniquely colored markers, and inversion of distinct neighbor distance-displacements for each marker equality partition.

Executed `python3 check_three_anchor.py` from the package on Python 3 with only standard-library dependencies. The attached `check_log.txt` records all 3,240 completed deterministic cases and the terminal `ALL_TESTS_PASS`. Exhaustive triples were checked for dimension 2 and alphabet sizes 4 and 5; dimensions 3–5 were checked by seeded sampling. For every tested triple the program directly constructed graph adjacency and iterated vertex recoloring, compared the final classes with a separately constructed coordinate-profile orbit partition, tested both the exact orbit-count formula and every individual multinomial orbit-size formula, and checked the uniform round bound. For the sampled configurations at selected dimensions it also reconstructed orbit profiles from one-neighbor distance-displacement counts, independently of refinement.

The random samples are finite checks, not an exhaustive test for larger dimensions or an infinite proof. No external formal prover or independent mathematical review was used. The dimension-two tests are boundary checks outside the claimed dimension restriction.
