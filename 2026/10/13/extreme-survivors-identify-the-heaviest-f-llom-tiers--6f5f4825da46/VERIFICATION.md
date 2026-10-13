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
For fixed finite covariates, each component has
\[
S_m(y\mid x)
=
\left(1+\frac{y}{\kappa_m(x)}\right)^{-\lambda_m}
\sim
\kappa_m(x)^{\lambda_m}y^{-\lambda_m}.
\]
A finite positive-weight sum therefore has leading exponent
\[
\lambda_*=\min_m\lambda_m
\]
and constant
\[
C_*(x)=\sum_{m:\lambda_m=\lambda_*}\pi_m(x)\kappa_m(x)^{\lambda_*}.
\]
The density has the matching leading constant multiplied by \(\lambda_*\), which proves
\[
h_Y(y\mid x)\sim\lambda_*/y.
\]

The survivor-tier posterior is exactly
\[
\frac{\pi_m(x)S_m(y\mid x)}{S_Y(y\mid x)}.
\]
Dividing numerator and denominator by \(y^{-\lambda_*}\) gives the stated tie weights and zero mass for every larger-shape tier. Under a unique minimum, the first Lomax correction is \(O(y^{-1})\) while a competing tier with gap \(\delta\) contributes \(O(y^{-\delta})\); hence the stated rate.

The included checker uses exact model formulas for representative unique-minimum and tied-minimum mixtures and verifies all normalized limits numerically. These computations are consistency checks only.
