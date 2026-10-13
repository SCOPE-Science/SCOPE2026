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

# Reproduction and limits

Run `python verify.py` with Python 3 and installed NumPy and SymPy, from the directory containing that file. Symbolic rational and radical simplifications independently check five stated mixing distance coefficients, all five stated eigenvalues, the stochastic row-sum identity, multiplicity totals and the strict-positivity algebraic identity. The executable constructs the points and totally isotropic lines in four-dimensional symplectic geometry over the fields of orders two and three, forms each actual point-line incidence adjacency matrix, diagonalizes it independently of the theoretical distance algebra, and compares the resulting projector-Schur-square matrix with the claimed distance formulas.

Expected replay output:

```text
VERIFY_OK symbolic_distance_coefficients=5 symbolic_eigenvalues=5 finite_graphs=2 matrix_entries=7300 max_entry_error=6.66e-16 max_eigen_error=9.44e-16
```

The graph checks are floating-point with stated max errors and only cover orders two and three. Symbolic coefficient identities apply to a free parameter, but mathematical applicability to all generalized quadrangles rests on the geometric and projector argument in RESULT.md. No independent human or external certification has been performed.
