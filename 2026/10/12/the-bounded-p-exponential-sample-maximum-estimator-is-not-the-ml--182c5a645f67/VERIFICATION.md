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
For the published likelihood
\[
L(p)
=
\left(\frac{p}{p+1}\right)^n
\prod_i
\left(1-\frac{x_i}{p+1}\right)^{p-1},
\]
let \(m=\max_i x_i\).

If \(m>1\), set
\[
p=m-1+\varepsilon.
\]
Each maximum observation contributes
\[
\left(\frac{\varepsilon}{m+\varepsilon}\right)^{m-2+\varepsilon}.
\]
Thus the lower-boundary likelihood diverges for \(1<m<2\) and vanishes for \(m>2\). If \(m<1\), the likelihood is \(O(p^n)\) and vanishes as \(p\downarrow0\).

For every fixed sample,
\[
L(p)\to\exp\!\left(-\sum_i x_i\right)
\]
as \(p\to\infty\).

The bundled checker evaluates these regimes directly, verifies the simulation probability
\[
\Pr(M_{20}>2)=0.9412282299\ldots
\]
at \(p=5.3245\), and replays the two real-data likelihood comparisons from the observation lists printed in the source.
