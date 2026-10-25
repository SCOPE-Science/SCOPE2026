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
# Verification evidence and limits

The proof of the theorem is analytical and contained in `RESULT.md`. `verify.py` implements the independent matrix-exponential method rather than the paper formula's intermediate triangular eigenvalue decomposition.

Run `python verify.py` using Python 3, NumPy and SciPy. The program compares direct matrix exponential Perron eigenvalues with the derived closed formula for 128 parameter choices, checks finite strict ordering in each parameter, and corroborates the exact threshold for \(a=1\), \(b=3\), \(m=2\). Its expected output begins `CHECK_OK`.

The numerical comparisons are finite and subject to floating-point accuracy. Proof of uniqueness, monotonicity for all admissible rates, and two exact endpoint limits depends on the explicit algebra and inequalities in `RESULT.md`, not these tests. No external independent audit or formal proof-assistant certification has been performed.
