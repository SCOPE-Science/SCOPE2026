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

Run `python verify.py` with Python 3 and the `mpmath` package. The packaged program independently computes the actual \(2\times2\) matrix-exponential monodromy and compares its positive eigenvalue with the stated explicit Floquet formula in 24 cases. It also checks the compact-scale \(O(T^2)\) approximation on 10 points and numerically optimizes migration in four small-period instances. The checks ran successfully at 65-digit working precision.

# Analytical dependencies and limits

The mathematical theorem requires the exact matrix-square identity, the monotonicity of \(\sinh z/z\), the global \(1/(2z)\) tail, compact-interval Taylor expansion, unique maximizer of \(g\), and strict concavity near that maximizer. The executable cannot certify universal quantifiers or an asymptotic \(O(\cdot)\) statement; those follow from the written proof. The equality case for the leading mortality threshold is not determined, and the study is restricted to deterministic principal Floquet growth.
