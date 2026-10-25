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

# Reproducibility and verification

The companion `triple_checker.py` uses only Python standard-library routines and exhaustively builds the cubical chain complex for three indistinguishable points on the four-path theta graph. Run `python3 triple_checker.py`; the program raises assertions on failure and prints the five cycle-type traces for both hub-exchange states on success. It verifies all 20 vertices, 48 edges, and 24 squares; each vertex-link cycle; two incident squares per one-cell; a primitive coherent orientation cycle; the zero boundary product; modular ranks 19 and 23; and all 48 signed group actions.

The proof additionally uses standard mathematical theorems: adequacy of the given subdivision for the Abrams graph-configuration deformation retract; integral surface homology; rational character theory of the symmetric group; Lefschetz fixed-point indices of finite-order orientation-preserving surface maps; cyclicity of finite oriented surface stabilizers; and Riemann–Hurwitz. These theorems are not replaced by finite experiments. The genus-three type and ordinary homology were known, and the correctness of those earlier publications is not recertified here. No independent validation has been performed.
