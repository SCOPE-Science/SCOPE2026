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

The standalone verifier `verify_tournament_neighborhoods.py` uses only the Python standard library. It reconstructs all \(32768\) labeled six-vertex tournaments, partitions them into exactly 56 isomorphism classes under all \(720\) vertex permutations, rebuilds every directed out-neighborhood complex, and verifies the archived census row by row.

For every representative it constructs a stagewise discrete-Morse face matching and explicitly checks acyclicity on the complete oriented Hasse diagram. It verifies that no critical cells occur above dimension \(1\), that the critical-vertex count equals the component count, and that the resulting homotopy-type distribution is exactly the one claimed. It also checks the unique \(\beta_1=4\) representative, its orbit size and automorphism-group order, and its stated out-neighborhoods.

As a separate regression, the same code enumerates all 12 five-vertex tournament types and reproduces the reduced-homology-rank distribution in Dochtermann–Singh Table 1. A successful replay ends with `VERIFY_OK`.

The verification is exhaustive for six vertices but does not address larger tournaments. No independent audit has been performed.
