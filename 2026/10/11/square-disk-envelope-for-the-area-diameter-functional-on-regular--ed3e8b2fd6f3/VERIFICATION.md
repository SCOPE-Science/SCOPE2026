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

The proof was checked symbolically from the displayed regular-polygon formulas.

For even polygons, with \(\theta=\pi/n\), the checker derives
\[
x(\theta)=\frac{\theta}{\pi\sin\theta},
\qquad
y(\theta)=\frac{\cos\theta}{4},
\]
and verifies
\[
\frac{d}{d\theta}\left(\frac{dy}{dx}\right)
=
\frac{\pi\sin^2\theta}
{8(\theta\cos\theta-\sin\theta)^2}
\left(2\theta\cos2\theta+4\theta-3\sin2\theta\right).
\]
The sign chain
\[
h''(\theta)=4\theta\sin2\theta\ge0,\quad
h'(0)=h(0)=g(0)=0
\]
proves strict convexity of the graph on the relevant interval.

For odd \(n\), with \(u=\pi/(2n)\), the checker verifies
\[
x(P_n)=x(P_{2n})
\]
and
\[
y(P_{2n})-y(P_n)
=
\frac{\sin^2u}{4\cos u}>0.
\]
This establishes the required domination without finite enumeration.

The crossover equation between the square and disk branches is solved exactly and checked as
\[
\alpha_*=
\frac{2(\sqrt2\pi-4)}
{\pi(\sqrt2+2)-8}.
\]

A finite regression scan through \(n=10000\) is included only to catch implementation or indexing mistakes. It is not evidence for the universal theorem.
