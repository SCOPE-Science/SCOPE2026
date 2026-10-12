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
Let
\[
G(x)=e^{-\alpha(-\log x)^\beta},
\qquad
g(x)=\frac{\alpha\beta}{x}(-\log x)^{\beta-1}G(x).
\]
For the positive-geometric minimum transform,
\[
h_Y(x)=\frac{g(x)}{[1-G(x)][1-\rho+\rho G(x)]}.
\]

With \(t=-\log x\downarrow0\),
\[
1-G(x)=\alpha t^\beta(1+o(1)),
\qquad
g(x)=\frac{\alpha\beta}{x}t^{\beta-1}(1+o(1)),
\]
and the geometric factor tends to one. Thus
\[
h_Y(x)=\frac{\beta}{x t}(1+o(1)),
\]
while \((1-x)/(x t)\to1\). Hence
\[
(1-x)h_Y(x)\to\beta.
\]

At the left endpoint \(t\to\infty\),
\[
h_Y(x)\sim
\frac{\alpha\beta}{1-\rho}t^{\beta-1}e^{t-\alpha t^\beta},
\]
which gives the five stated cases.

The bundled checker evaluates the exact formula only as a numerical consistency test. The infinite-domain conclusions are the analytic consequences above. No exhaustive classification of interior critical points is claimed.
