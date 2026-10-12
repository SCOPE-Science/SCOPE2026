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

# Exact verification and limits

Run `python verify.py` using `requirements.txt`. The checker is self-contained except for its declared SymPy dependency; there are no external data files. It reconstructs all four Johnson adjacency eigenvalues symbolically, verifies every distance recurrence for the lowest spectral projector and every eigenvalue identity for its Hadamard square, and establishes the relevant rational inequalities from exact polynomial identities.

For \(n=6,7,8\), it independently builds the unweighted adjacency matrix from three-subsets and the lowest eigenspace projector as a Lagrange polynomial in this adjacency matrix, verifying its idempotence, trace, eigenvalue equation and all \(4,761\) rational matrix entries. For the boundary \(n=6\), it builds all four projectors and checks the rank \(10\) of the complete average-mixing matrix. This is genuinely exact rational arithmetic, not floating-point sampling.

Expected exact terminal line:

`VERIFY_OK symbolic_projector_recurrence=4 symbolic_mode_eigenvalues=4 positivity_polynomials=3 exact_matrix_sizes=20,35,56 exact_projector_entries=4761 boundary_rank=10/20`

The computation is finite; validity for every \(n\ge6\) comes from the explicit polynomial identities and the analytic proof in `RESULT.md`. It does not certify journal priority or provide independent mathematical review.
