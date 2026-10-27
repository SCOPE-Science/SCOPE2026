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

# Verification notes

The submitted proof is finite but mathematically universal across all data functions on the two specified vertex sets. It uses all signed linear extension operators for the lower bound, not just positive extensions. The dual certificates are explicit 1-Lipschitz functions, and the upper bounds use probability couplings of prescribed marginals; the orbit enumeration is exact by the signed-permutation symmetry of the cube.

`verify_cube_midpoints.py` is standalone and uses only the Python standard library. Running `python3 verify_cube_midpoints.py` gave:

- Square: 4 vertices, 4 edge midpoints, 28 unordered output pairs; computed optimum 1.055050013198716 and arithmetic-midpoint norm 1.079669127533634.
- Three-cube: 8 vertices, 12 edge midpoints, 190 unordered output pairs; computed optimum 1.071912669955583 and arithmetic-midpoint norm 1.115355071650411.
- Every computed pair ratio was within 1e-9 of the analytical norm ceiling; the second cube near-midpoint potential passed all 28 input-vertex pair Lipschitz tests and reached equality in the claimed lower bound.

The numerical transport routine is a successive shortest augmenting-path solver with real floating-point edge costs. It checks the finished kernel but does not prove the symbolic inequalities or certify global optimality on its own. Global optimality is established by the analytical symmetry and dual-potential argument in `RESULT.md`. The proof's square-root bounds are elementary exact inequalities, rather than extrapolations from numerical data. No independent mathematical audit has been performed.
