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

# Reproducibility

Run `python3 CHECK_HOLLOW.py` with Python 3.8 or later; no third-party modules are required. It returns `VERIFY_OK` after exhaustively checking all \(3^{10}=59049\) off-diagonal symmetric matrices of size \(5\) over \(\mathbb F_3\), using determinant and gradient polynomials expanded by signed permutations and modular Gaussian elimination. It also verifies integral witness ranks and three independent kernel-restricted perturbation directions for sizes \(5\) through \(12\). The observed exhaustive counts are: 30816 nonzero determinants, 4761 singular determinant-zero matrices, 23472 smooth determinant-zero matrices, and 2340 rank-four zero-star singular matrices. Characteristic-three tests check combinatorial identities only. The all-parameter characteristic-zero theorem follows from the independent symbolic Jacobian, Gram-irreducibility, Schur-complement, and dimension arguments in `RESULT.md`; this script is not an infinite certificate.

Only the named reduced singular support and generic transverse types are established. In particular, the scheme-theoretic Jacobian ideal is not asserted to be radical.
