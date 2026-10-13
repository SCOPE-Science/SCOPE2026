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

# Verification scope
Run `python3 verify.py` in the directory containing this file. The script requires SymPy; its other modules are in the Python standard library. It is a standalone recomputation from the unweighted path adjacency matrix, not a replay of an unseen log.

The program verifies five exact spectral projectors, five eigenrelations, bipartite symmetry, a six-dimensional mixing moment system for all 15 independent entries, nonzero determinant \(\sqrt3/972\), the unique moment solution, and the target uniform matrix. A separate 64-node periodic phase-grid check confirms the positive product-density average numerically within \(10^{-12}\); the integrands are trigonometric polynomials whose frequencies lie below the eight-point quadrature aliasing threshold.

Proof obligations outside finite computation are the positivity and normalization of two explicit trigonometric densities, irrationality of \(\sqrt3\), relative-interior characterization via supporting hyperplanes, density of the phase orbit, and finite-dimensional Carathéodory reduction. They are argued in `RESULT.md`; finite checks cannot certify these infinite assertions by enumeration. The proof does not generate numerical exact weights and times and does not establish minimal support size.
