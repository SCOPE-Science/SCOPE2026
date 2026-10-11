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

The mathematical proof is entirely symbolic. With the unnormalized Gaussian
\[
g(t)=e^{-\pi t^2},
\]
the Zak transform is unitary, and the biorthogonal Zak quotient is the Fourier character minus its value at the unique Zak zero, divided by \(\overline{Zg}\). The quotient is square-integrable because numerator and denominator vanish linearly at the same point.

The inspected 2025 reference uses \(2^{1/4}g\), so the local derivative is rescaled back by the factor \(2^{-1/4}\). For the present window,
\[
Zg(p+(u,v))=-\kappa(u+iv)+O(u^2+v^2),
\qquad
\kappa=\pi\theta_1'(0,e^{-\pi})>0.
\]
Consequently, \(|Zg|^{-2}=(\kappa^2 r^2)^{-1}+O(1/r)\) near \(r=0\). The error is integrable in two dimensions, uniformly over indices, because the numerator is at most four.

After rotation and angular averaging, the singular integral equals
\[
\frac{4\pi}{\kappa^2}\int_0^{2\pi\rho R}\frac{1-J_0(t)}t\,dt.
\]
For small arguments \(1-J_0(t)=O(t^2)\), and for large arguments the oscillatory angular representation gives \(|J_0(t)|=O(t^{-1/2})\). Therefore the last integral is \(\log R+O(1)\). The remaining square contributes a bounded term, and integer time-frequency shifts preserve the norms across all deleted lattice atoms. This establishes the universal quantitative statement for an infinite index set without exhaustive computation.

The theta derivative series was independently evaluated as
\[
\theta_1'(0,e^{-\pi})\approx0.9067676551677313,
\qquad
C_{\mathrm G}\approx1.5485244900509678.
\]
A separately executed \(1100\)-point-per-side midpoint quadrature, using a directly evaluated nine-term Gaussian Zak sum, gave squared norms approximately \(7.394044\), \(8.467403\) and \(9.540806\) at indices \((20,0)\), \((40,0)\) and \((80,0)\). These were used as consistency checks only. The included script reproduces the numerical check if NumPy is available; the theorem does not rely on any numerical sample.

The theorem does **not** assert an additive limiting constant or necessity of the explicit sufficient weight-summability condition for all possible weighted lower semi-frames. Independent audit is not performed.
