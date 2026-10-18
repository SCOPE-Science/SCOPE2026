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

# Reproduction

Execute `python verify.py` (Python 3, SymPy). The script builds the original six-vertex, twelve-edge, three-square integer cubical model and checks the two boundary maps. It computes a rank-five vertex boundary, a rank-three square boundary, determinant two for the face sublattice, and determinant negative one for a primitive basis containing the exchange. It checks the exact face/exchange relation and all twenty-four permutations. It proves statements about this finite chain model only; the deformation-retraction hypothesis and integral-equivariant consequence are reasoned in RESULT.md. No independent audit has been performed.
