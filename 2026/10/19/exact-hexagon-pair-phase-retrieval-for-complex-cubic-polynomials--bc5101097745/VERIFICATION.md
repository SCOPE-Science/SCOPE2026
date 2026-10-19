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

The complete proof is in RESULT.md. Direct reproducibility: install NumPy and run `python VERIFY.py` from the extracted package directory. At the research evaluation, the script returned `VERIFY_OK 1430 comparisons` (four nondegenerate parameter configurations, five degeneracies, explicit kernel basis evaluations, seeded checks of kernel rank, and randomized coefficient comparisons).

The tests calculate the Hermitian real-linear measurement rank and evaluate all proposed nullspace generators. Exact algebraic inference for arbitrary positive radii and angular offsets uses six-point discrete Fourier orthogonality, the two-root polynomial factorization, the one-dimensional eigenspace property of irreducible Hermitian tridiagonal matrices, and the fact that a real binomial cannot have two distinct positive roots. Finite floating-point comparisons alone do not prove any universal statement. Independent audit has not been performed.
