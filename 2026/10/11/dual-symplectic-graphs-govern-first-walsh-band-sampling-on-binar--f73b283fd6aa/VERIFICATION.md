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

# Verification of the quadratic first-Walsh-band sampling theorem

The proof reconstructs the Walsh transform of a nonsingular quadratic, the exact dual-polar signed Gram matrix, the Pfaffian parity realization criterion, and a positive two-point intersection count that forces sampling injectivity. The four-coordinate spectral census is also exhaustively derived by perfect-matching classification and checked by exact characteristic polynomials.

`artifacts/verify.py` is a standalone Python 3 program using only the standard library. Run it with `python3 artifacts/verify.py` from the package directory. A successful check reports:

`VERIFY_OK exact_quadrics=476 four_vertex_graphs=28 three_Seidel_polynomials=15,12,1 difference_set_and_rank=PASS signed_Gram_identity=PASS`

The checker constructs every four-vertex graph, tests adjacency invertibility over the binary field, enumerates all its quadratic linear refinements, and evaluates restriction Gram entries by direct integer summation over the quadratic zero set. It compares the complete matrix with the dual-polar formula, recomputes the two-point intersection cardinality and exact rational rank, and checks the full characteristic-polynomial multiset by integral Newton identities. Two-variable boundary cases and a selection of six-variable examples are independently checked. These computations completely certify the finite four-vertex census but **do not** constitute exhaustive evidence in unbounded dimension; the stated general theorem relies on the algebraic proof.

The diagonal similarity and Fourier normalization should not be suppressed when applying the eigenvalue formula: unrenormalized ambient probability measure is used on the quadratic set. A normalized conditional measure rescales every sampling eigenvalue. Possible earlier equivalent representations in coding theory or finite-Hadamard frame theory have not been ruled out by a formal bibliographic priority certificate.
