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

The deterministic exact verifier `verification/verify.py` reconstructs the coordinate graph, compares it with the adjacent-transposition permutahedron graph, and enumerates all independent faces, matchings, and graph automorphisms. It checks the full directed Hasse acyclicity, exact integer Morse-chain reduction, all 56 primitive shortest-support cycles, orbit Smith diagonals, a unit integral basis minor, signed Lefschetz characters, and direct integral action matrices. Execute `python verification/verify.py` after installing `verification/requirements.txt`.

Limits: the calculation is exhaustive for the specified finite graph, not for higher-dimensional permutahedra. Smith computations use exact integers. The homotopy conclusion invokes the standard discrete-Morse theorem and the support cutoff invokes the stated flag-complex lemma. No independent external scientific audit has been performed.
