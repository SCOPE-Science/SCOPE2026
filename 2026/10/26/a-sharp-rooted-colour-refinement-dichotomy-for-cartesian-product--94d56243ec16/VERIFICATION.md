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
# Verification of the mathematical claim

The complete symbolic proof is in `RESULT.md`. Execute `python3 verify.py` using Python 3's standard library. Its code independently constructs the Petersen graph, triangular graph, Clebsch graph, Shrikhande graph, even cycle and rook graphs; it verifies their strongly regular parameters before constructing Cartesian products.

For each sample it computes all vertices and all adjacency lists, then iterates ordinary rooted colour refinement from a unique root colour. It verifies that the partition is unchanged from round \(2d-1\) to round \(2d\), that it is strictly coarser at round \(2d-2\), that the final partition is exactly the theoretically predicted distance-shell or coordinate-profile partition, and that every stable class has its exact predicted size. The mixed Shrikhande/rook tests include nonisomorphic factors sharing strongly regular parameters.

`verification_output.txt` contains the execution record: 20 tests, final line `CASES 20 ALL_TESTS_PASS`. The sample includes up to 1000 vertices in a Cartesian product. A separate profile-quotient exploration was used during mathematical derivation but is not required by this package; only the packaged standard-library program and symbolic proof support the verification claim. These finite checks do not establish the infinite family or originality.

This is not an independent mathematical audit or external proof certification.
