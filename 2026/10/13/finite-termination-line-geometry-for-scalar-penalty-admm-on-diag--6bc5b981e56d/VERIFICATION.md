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
The proof was reconstructed from the exact scaled over-relaxed ADMM updates. For one coordinate, the \((z,u)\)-error matrix has determinant \(0\), trace
\[
1-\frac{\alpha\rho(a+b)}{(\rho+a)(\rho+b)},
\]
and therefore satisfies \(M^2=(\operatorname{tr}M)M\). This supplies the all-dimensional finite-termination proof after diagonal decoupling.

The embedded `verify.py` uses only the Python standard library and exact `Fraction` arithmetic. It checks the heterogeneous witness \(A=\operatorname{diag}(1,2)\), \(B=\operatorname{diag}(5,6)\), \(\rho=4\), \(\alpha=15/8\), verifies both modal matrices square to zero, verifies the line relation with \(\tau=7/2\), and replays the affine instance with solution \((1,1)^{\mathsf T}\).

The computation is a witness replay, not an exhaustive proof. Unproved limits include noncommuting or singular Hessians, matrix-valued penalties, iteration-varying parameters, and finite-precision robustness.
