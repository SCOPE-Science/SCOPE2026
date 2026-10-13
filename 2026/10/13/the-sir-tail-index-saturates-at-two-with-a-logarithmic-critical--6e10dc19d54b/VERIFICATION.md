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
The exact survival follows from the stochastic representation:
\[
\overline F_Z(z)
=
q\int_0^1 y^{q-1}
\left[
1-e^{-\theta/(z^2y^2)}
\right]dy.
\]
With
\[
a=\theta/z^2,
\qquad
s=q/2,
\]
it becomes
\[
s a^s
\int_a^\infty(1-e^{-t})t^{-s-1}\,dt.
\]

For \(s<1\), the integral converges to \(\Gamma(1-s)/s\). At \(s=1\), it is \(\log(1/a)+O(1)\). For \(s>1\), it is asymptotic to \(a^{1-s}/(s-1)\). These are the three stated survival regimes.

Independence also gives
\[
\mathbb E[Z^r]
=
\mathbb E[X^r]\mathbb E[Y^{-r}],
\]
with
\[
\mathbb E[X^r]
=
\theta^{r/2}\Gamma(1-r/2)
\]
for \(r<2\), and
\[
\mathbb E[Y^{-r}]
=
q/(q-r)
\]
for \(r<q\). Hence the moment exists exactly when \(r<\min(q,2)\).

The bundled checker evaluates the exact survival integral, the source density formula, the hazard ratio, and selected finite fractional moments. Finite calculation is not used as proof.
