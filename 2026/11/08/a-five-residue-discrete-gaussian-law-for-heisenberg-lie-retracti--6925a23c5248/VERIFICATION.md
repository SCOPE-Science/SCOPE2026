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

# Finite computations and proof boundaries

Execute `python3 verify.py` with standard-library Python 3. It directly tests all linear maps on the three-dimensional Heisenberg Lie algebra over F2 and F3, enumerates induced 4-by-4 maps and central data for the five-dimensional Heisenberg Lie algebra over F2, checks matrix idempotence and all basic Lie brackets, and reports counts by linear-algebra rank. It compares complete predicted exact rank polynomials against the direct counts. An independent centered-weight calculation compares the finite q=2 rank distribution to the limiting discrete Gaussian at m=10, 20, and 40.

Observed output:
```
DIRECT_H3_OK 2 {0: 1, 1: 12, 3: 1}
DIRECT_H3_OK 3 {0: 1, 1: 36, 3: 1}
DIRECT_H5_BINARY_OK {0: 1, 1: 240, 2: 960, 5: 1}
DISCRETE_GAUSSIAN_OK 10 L1_error 0.0290225741
DISCRETE_GAUSSIAN_OK 20 L1_error 0.0018382579
DISCRETE_GAUSSIAN_OK 40 L1_error 7.1875e-06
VERIFY_OK
```

This verifies small finite cases and numerical convergence only. It does not prove any infinite limit, validate all prime-power extensions by brute force, or certify originality. The proof in RESULT.md supplies the classification, finite-field counting, and dominated-convergence argument for the infinite statements.
