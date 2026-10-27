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

# Verification and scope

The accompanying `verify_regular_gauss.py` is a standalone exact-rational Python 3 program. It constructs seven finite regular graphs, computes their Laplacian pseudoinverses through an exact inverse of a rank-one shifted Laplacian, checks the projection identity, compares their edge pseudoinverse sums with spectral traces, and forms the completed Gauss matrix by exact rational inversion for five positive step sizes. It verifies the rational entry formulas for the nine-vertex Cartesian torus and checks selected late negative edge entries in the six-cycle and twelve-vertex torus.

Recorded observations: seven graphs; 35 exact step matrices; 270 row-sum tests; 405 nine-vertex entry-class tests; seven trace tests. Run `python verify_regular_gauss.py` and compare stdout to `verify_output.txt`. No third-party packages are required. The code's rational arithmetic guards against floating-point false-positive signs for those selected finite examples.

**Limits:** Seven graph cases and five steps do not establish the theorem for arbitrary graphs or arbitrarily large steps. Universal correctness follows from the proof's spectral trace inequality, the strict equality analysis, and the asymptotic matrix expansion. Source-coverage review is not a certification of novelty. No independent mathematical audit is asserted.
