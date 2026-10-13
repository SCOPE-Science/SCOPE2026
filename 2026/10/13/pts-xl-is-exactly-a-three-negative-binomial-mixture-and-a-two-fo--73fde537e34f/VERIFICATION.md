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
Set
\[
a=\frac{\theta(\theta+2)}{(1+\theta)^2},
\qquad
b=\frac{1}{(1+\theta)^2}.
\]
Then
\[
a+b=1
\]
and
\[
a\theta e^{-\theta t}
+
b\theta^2t e^{-\theta t}
=
\frac{\theta^2}{(1+\theta)^2}
(\theta+2+t)e^{-\theta t}.
\]

The sum of two independent latent gamma variables therefore has shapes \(2,3,4\) with probabilities \(a^2,2ab,b^2\). Poisson mixing of \(\Gamma(k,\theta)\) gives
\[
\binom{x+k-1}{x}
\left(\frac{\theta}{1+\theta}\right)^k
\left(\frac{1}{1+\theta}\right)^x.
\]

The single-PXL PGF derived from the same latent mixture is
\[
G_{\mathrm{PXL}}(z)
=
\frac{
\theta^2[\theta^2+3\theta+3-(\theta+2)z]
}{
(1+\theta)^2(1+\theta-z)^2
},
\]
so its square is exactly the PTS-XL PGF printed in the 2026 source.

The bundled checker symbolically verifies the density, PMF, and PGF identities and numerically compares representative PMF values. The finite numerical checks are not used to prove the identities.
