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

For \(X_{\mu,\lambda}\sim\operatorname{IG}(\mu,\lambda)\), scaling by \(\mu\) shows that the standardized law depends only on \(\kappa=\lambda/\mu\). With \(\varepsilon=\kappa^{-1/2}\), its exact density relative to the standard Gaussian density is
\[
R_\varepsilon(z)=(1+\varepsilon z)^{-3/2}
\exp\!\left(\frac{z^2}{2}-\frac{z^2}{2(1+\varepsilon z)}\right).
\]
For any fixed \(c>0\), this is analytic uniformly on \([-c,c]\) once \(|\varepsilon|c<1\). Also \(R_\varepsilon(-z)=R_{-\varepsilon}(z)\), so the symmetric integral contains only even powers of \(\varepsilon\).

The bundled checker reconstructs the formal series from \(\log R_\varepsilon\) using rational polynomial arithmetic. It verifies
\[
A_2(z)=\frac{z^6-10z^4+15z^2}{8}
\]
and
\[
A_4(z)=\frac{z^{12}}{384}-\frac{3z^{10}}{32}+\frac{63z^8}{64}-\frac{105z^6}{32}+\frac{315z^4}{128}.
\]
It then checks exact polynomial primitives under the Gaussian weight, which yield
\[
\int_{-c}^c A_2(z)\varphi(z)\,dz
=\frac{c^3(5-c^2)\varphi(c)}{4}
\]
and
\[
\int_{-c}^c A_4(z)\varphi(z)\,dz
=-\frac{c^5(c^2-7)(c^4-18c^2+27)\varphi(c)}{192}.
\]
Analytic evenness makes the next integrated term order \(\varepsilon^6=\kappa^{-3}\).

The numerical portion of the checker compares direct quadrature with the two-term asymptotic at several radii, including both sides of \(\sqrt5\). These are regression checks only and are not used to infer the infinite-parameter statement.
