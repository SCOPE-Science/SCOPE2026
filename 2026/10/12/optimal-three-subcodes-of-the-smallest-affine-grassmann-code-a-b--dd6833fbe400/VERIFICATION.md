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

# Reproducibility and limitations

Run `python3 verify.py` with Python 3 and no third-party packages. The verifier enumerates all reduced-row-echelon rank-three subspaces of the six-dimensional coefficient space, computes each common-zero set from direct evaluation of the six generators on every \(2\times2\) matrix, and separately enumerates the rank-two matrix-space directions for which the determinant function is affine-linear. It repeats the procedure for \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); the latter uses the polynomial modulus \(T^2+T+1\). The exact expected results are:

| Field size | Three-subspaces tested | Largest zero set | Optimal three-subcodes | Eligible directions |
| --- | ---: | ---: | ---: | ---: |
| 2 | 1,395 | 4 | 60 | 15 |
| 3 | 33,880 | 9 | 72 | 8 |
| 4 | 376,805 | 16 | 160 | 10 |

The program asserts these values, including the equality between optimal-subcode count and number of eligible plane directions times the number of translates, and prints `VERIFY_OK`. It does not assert any result for fields larger than four. The all-finite-fields theorem follows separately from the linear-subspace and determinant-polarization proof in `RESULT.md`; this is an exact finite cross-check, not an infinite certificate.

No external validation or independent audit has been performed.
