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

# Reproduction of algebraic and computational checks

The analytical proof is in `RESULT.md`. Execute `python3 verify.py` with NumPy available to inspect finite examples independently using numerical diagonalization and exact rational arithmetic.

A completed run reported:

`VERIFY_OK independent_matrix_cases=119 exact_projector_cases=86 distinct_eigenvalue_groups=526 diamond_rank=2/4 least_positive_eigenvalue_tested=0.25`

The checker constructs every nondecreasing list of \(2\) to \(5\) positive part sizes from \(1\) to \(4\), with total number of vertices at most \(18\), giving \(119\) cases. For all cases, it compares the nullity of the independent full average mixing matrix \(\sum_\lambda E_\lambda\circ E_\lambda\) with the claimed formula and checks predicted difference vectors, row sums and numerical positivity. For \(86\) cases of order at most \(12\), it independently constructs the claimed \(0\) and \((-1)\) projectors over exact rational numbers and verifies idempotence, orthogonality, eigenspace equations, and Schur-square block identities. The checker explicitly verifies the rank-two diamond graph case.

The exact infinite-family claim relies on the proof of the projector formulas, nonnegativity of Schur squares, and kernel dimension bounds. The finite examples neither establish unrestricted correctness nor exclude undiscovered equivalent literature. This package has not undergone independent audit.
