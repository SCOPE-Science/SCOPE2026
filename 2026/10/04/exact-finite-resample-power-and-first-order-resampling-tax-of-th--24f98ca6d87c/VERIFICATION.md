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
# Verification

The standalone `verify.py` uses only the Python standard library and independently evaluates the displayed power expressions by deterministic Gauss-Legendre quadrature.

It checks four items:

1. At \(\delta=0\), exact beta-integral arithmetic applied to the finite-\(B\) formula agrees with the uniform-rank size \(\lfloor\alpha(B+1)\rfloor/(B+1)\) for several budgets.
2. For \(n=20\), \(\delta=0.5\), and \(\alpha=0.05\), it reproduces the finite-\(B\) powers for \(B=19,39,99\) and the exact-quantile power stated in `RESULT.md`.
3. In the local limit with \(h=2\) and \(\alpha=0.05\), it reproduces \(\Pi_B\) for \(B=19,39,99,199\) and the infinite-resample value \(\Phi(h-z_{0.95})\).
4. It computes the analytic first-order coefficient and verifies that \((\Pi_B-\Pi_\infty)(B+2)\) moves toward that coefficient between \(B=99\) and \(B=199\), within a conservative numerical tolerance.

A clean replay from the embedded file prints `VERIFY_OK`. This verifies the algebraic/numerical content of the specified Gaussian CRT claim, not its literature originality or any non-Gaussian extension.
