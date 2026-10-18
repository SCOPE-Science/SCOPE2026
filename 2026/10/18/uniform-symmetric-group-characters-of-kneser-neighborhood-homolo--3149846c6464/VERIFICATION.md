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
# Reproducibility and proof boundary

Run `python3 verify.py` with Python 3 and its standard library. The script exhaustively enumerates every invariant edge-orbit selection for each of the 5, 7, 11 and 15 permutation cycle types in respective ground-set sizes 4, 5, 6 and 7. It independently checks the vertex-support condition, the signed augmented Euler trace, the all-size expression evaluated in those finite cases, and the two Specht character polynomials. The observed final line is `VERIFY_OK`. These are complete finite tests for the stated sizes but **not** an infinite proof.

The all-size proof is in RESULT.md: the count of fixed augmented faces is transformed by Möbius inversion on the cycles of an arbitrary permutation. The published nonequivariant homotopy theorem of Nilakantan and Singh is required to isolate degree \(n-4\). A character equality then establishes rational representation equivalence. No integral equivariant lattice, equivariant homotopy equivalence, or external independent audit was checked.
