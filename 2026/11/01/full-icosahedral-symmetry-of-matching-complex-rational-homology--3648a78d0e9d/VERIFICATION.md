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

# Verification and limits
The standalone program `verify.py` uses only the Python 3 standard library and requires no input data. Run `python3 verify.py`; expect the final line `icosahedral_matching_symmetry_PASS`. It exhaustively constructs the thirty-edge icosahedron, its 5887 nonempty matching simplices, all 120 graph automorphisms, exact finite-field boundary ranks, signed oriented fixed-face Lefschetz traces and independent compatible-edge-orbit traces. It also checks the precise rational irreducible decomposition and quotient invariant dimensions. Recorded stdout is in `verification_output.txt`. The rational homology concentration uses both finite-field rank bounds and the exact Euler characteristic, not finite-field calculations alone. The old nonequivariant integral homotopy result is cited, not recalculated. No independent audit has been performed.
