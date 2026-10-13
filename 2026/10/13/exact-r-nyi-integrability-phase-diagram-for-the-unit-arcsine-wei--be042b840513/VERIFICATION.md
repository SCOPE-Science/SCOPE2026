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
The defining quantity is
\[
J_p=\int_0^1 g(y)^p\,dy.
\]
With \(t=((-\log y)/\lambda)^k\), direct substitution yields
\[
J_p=C_{p,k,\lambda}\int_0^\infty
t^{(p-1)(k-1)/k}
\exp\!\left((p-1)\lambda t^{1/k}-\frac p2t\right)
(1-e^{-t})^{-p/2}\,dt,
\]
where \(C_{p,k,\lambda}>0\).

At \(t=0\), the integrand has power exponent
\[
\frac{(p-1)(k-1)}{k}-\frac p2,
\]
so local integrability is equivalent to
\[
k>2-\frac2p.
\]

At \(t=\infty\), for \(p>1\) the positive term \((p-1)\lambda t^{1/k}\) is sublinear when \(k>1\), linear when \(k=1\), and superlinear when \(k<1\). Thus the tail is finite for \(k>1\), infinite for \(k<1\), and at \(k=1\) finite exactly when
\[
\lambda<\frac{p}{2(p-1)}.
\]
For \(0<p<1\), both exponential contributions are decaying and the zero-end condition is automatic.

Combining the independent endpoint tests gives the claimed three-branch finiteness classification. Equality in the zero-end threshold gives a \(t^{-1}\) singularity; equality in the \(k=1\) tail threshold leaves a non-decaying constant-order integrand. Both boundary cases diverge.

As a direct local check, when \(p=2\) and \(k=1\),
\[
g(y)^2\sim\frac{1}{\pi^2\lambda}(1-y)^{-1}
\qquad(y\uparrow1),
\]
so the Rényi integral diverges logarithmically.

The source's fitted maximum-likelihood value \(k=0.9952<1\) therefore lies in the divergent tail regime for every \(p>1\). No conclusion about \(p=1\) or about formal series interchanges inside the finite region is asserted.
