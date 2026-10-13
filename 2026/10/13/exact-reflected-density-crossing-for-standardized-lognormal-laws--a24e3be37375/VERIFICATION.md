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

The proof uses only exact algebra, monotonicity, and elementary limits. For \(s=\sigma^2\), \(c=\sqrt{e^s-1}\), and \(u=cz\), direct substitution into the original lognormal density gives
\[
\log\frac{g_\sigma(z)}{g_\sigma(-z)}
=
\operatorname{artanh}(u)
\left(
-3-\frac{\log(1-u^2)}{s}
\right).
\]
The second factor is strictly increasing from \(-3\) to \(+\infty\), which proves existence and uniqueness of the reflected crossing. Solving its zero gives
\[
\kappa_\sigma^2=e^{-\sigma^2}+e^{-2\sigma^2}+e^{-3\sigma^2}.
\]

The standalone script `verify_lognormal_reflection.py` evaluates the standardized density from its original formula, compares its log ratio with the closed expression, checks signs on both sides of the crossing for representative shape parameters, verifies the numerical root of the one-standard-deviation equation, and checks monotonicity on a deterministic mesh. It prints:
`VERIFY_OK sigma_star=0.780626583864530 q=0.543689012692076`.

The numerical checks are not exhaustive and are not used to prove the theorem. The theorem is limited to ordinary one-dimensional lognormal laws and to the common support where both reflected density values exist.
