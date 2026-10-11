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

The verified claim is the all-positive-\(\tau\) extension and monotonicity statement in `RESULT.md`.

For \(R(x)=(x_{d-1}^2+x_d^2)^{1/2}\), the exact source weight satisfies
\[
\frac{1}{x_d^{\beta-\tau}R(x)^\tau}
=x_d^{-\beta}\left(\frac{x_d}{R(x)}\right)^\tau.
\]
Because \(0<x_d/R(x)\le1\), increasing \(\tau\) can only decrease the weight. Equivalently, for \(\tau_2\ge\tau_1>0\),
\[
\frac{w_{\beta,\tau_2}(x)}{w_{\beta,\tau_1}(x)}
=\left(\frac{x_d}{R(x)}\right)^{\tau_2-\tau_1}\le1.
\]
Thus a remainder inequality with positive constant \(C\) at \(\tau_1\) automatically gives the same inequality with the same \(C\) at every \(\tau_2\ge\tau_1\).

The focal full text was checked at Theorem 1, where a positive Gagliardo remainder is proved on a nonempty interval beginning at zero, and at Theorem 2, where the analogous Sobolev--Bregman remainder is proved for \(0<\tau<1+\alpha\). For an arbitrary requested \(\tau>0\), choosing a strictly smaller exponent inside the appropriate source interval therefore proves the result. The test-function classes and sharp Hardy terms in the source do not depend on \(\tau\), so no domain change occurs in the transfer.

Taking the supremum of all admissible constants at each exponent gives the monotonicity of the best constants. The argument does not calculate those best constants and makes no uniform-in-\(\tau\) claim. No numerical experiment is used as proof. No independent audit has been performed.
