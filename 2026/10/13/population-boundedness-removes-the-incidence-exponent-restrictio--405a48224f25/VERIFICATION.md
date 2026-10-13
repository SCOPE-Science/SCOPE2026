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
The verification is analytic.

Let
\[
N=\|n\|_\infty.
\]
The conserved nonnegative population identity gives
\[
0\le i\le N.
\]
For
\[
L=(I-\varepsilon\Delta_N)^{-1},
\]
positivity and
\[
L1=1
\]
give
\[
0\le b=Li\le N.
\]
For every reachable \(b\) and every \(p\ge1\),
\[
\frac{b^p}{1+\kappa b^q}
\le b^p
\le \max\{1,N^{p-1}\}b.
\]
This estimate is independent of \(q\).

Integrating the elliptic equation with homogeneous Neumann boundary condition yields
\[
\int_\Omega b=\int_\Omega i.
\]
The source independently proves
\[
\int_0^\infty\int_\Omega i<\infty.
\]
Therefore the total incidence is finite, and the exact susceptible formula gives a strictly positive limiting susceptible density almost everywhere wherever the initial susceptible density is positive.

No enumeration, simulation, numerical limit, or finite certificate is used to infer the infinite-time conclusion.
