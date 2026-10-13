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

# Independent reproducibility of finite calculations

Execute `python3 verify.py` from the directory containing this file. Python 3 standard-library exact rational checks run without optional dependencies; NumPy adds numerical spectral and fidelity tests. The expected successful output starts with `VERIFY_OK`.

The certificate program constructs the exact degree-normalized four-cell Jacobi recurrence, verifies the factorization \((x^2-1)(x^2-pq/((p+1)(q+1)))\) for every \(1\le p,q\le20\), and scans the Pell rationality condition for \(1\le q\le100000\). Its optional numerical stage independently diagonalizes every double-star normalized-Laplacian matrix with \(1\le p,q\le10\), checks the complete spectrum including eigenvalue multiplicities, and gives high-fidelity odd-time witnesses for five irrational parameters. For rational exceptional parameters it checks the exact numerator/denominator parity exclusion.

These finite computations verify algebra and examples only. The unbounded parameter quantifiers, exhaustive pair exclusion, irrational-rotation density and complete Pell sequence are proved in RESULT.md, not by computation. There has been no independent external audit.
