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

The derivation was replayed from the exact spectral representation of the limiting laws.

For dimension three, the radial integral
\[
J(a)=\int_0^\infty r^2\left(\frac a{r^2}-\log\left(1+\frac a{r^2}\right)\right)dr
\]
was differentiated to obtain \(J'(a)=\pi\sqrt a/2\), hence \(J(1)=\pi/3\). This gives \(K_3(s)\sim s^{3/2}/(3\sqrt2\,\pi)\). Substitution into the Legendre transform gives
\[
\frac4{27(1/(3\sqrt2\,\pi))^2}=\frac{8\pi^2}{3}.
\]

For dimension two, differentiating the cumulant generating function reduces the asymptotic to the lattice sum
\[
\sum_{k\ne0}\frac{R^2}{|k|^2(|k|^2+R^2)}\sim2\pi\log R.
\]
Together with \(R^2=s/(2\pi^2)\) and the quotient by \(k\sim-k\), this yields \(K_2'(s)\sim(4\pi)^{-1}\log s\).

The variance under the tilted law is \(K_d''(s)\), which is \(O(s^{-1})\) in dimension two and \(O(s^{-1/2})\) in dimension three. These bounds are sufficient for the concentration step that matches the Chernoff upper bounds.

Limits: this verifies asymptotics for the limiting random variables only. It does not verify any uniform finite-sample tail approximation.
