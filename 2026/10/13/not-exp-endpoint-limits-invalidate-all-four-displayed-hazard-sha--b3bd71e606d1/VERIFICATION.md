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
For
\[
G(y)
=
\left[
\frac{(1+\alpha)(1-e^{-\theta y})}
{\alpha+1-e^{-\theta y}}
\right]^\gamma,
\]
the small-time hazard satisfies
\[
h(y)
\sim
\gamma
\left(
\frac{(1+\alpha)\theta}{\alpha}
\right)^\gamma
y^{\gamma-1}.
\]
Hence
\[
h(0+)
=
\begin{cases}
+\infty,&0<\gamma<1,\\
(1+\alpha)\theta/\alpha,&\gamma=1,\\
0,&\gamma>1.
\end{cases}
\]

At large \(y\),
\[
1-G(y)
\sim
\frac{\gamma\alpha}{1+\alpha}e^{-\theta y},
\]
and
\[
g(y)
\sim
\frac{\gamma\alpha\theta}{1+\alpha}e^{-\theta y},
\]
so
\[
h(y)\to\theta.
\]

The bundled checker differentiates the exact CDF numerically to confirm the PDF, checks the small-time asymptotic ratio for multiple parameter values, and verifies the large-time hazard limit for the four parameter triples used in Figure 1.
