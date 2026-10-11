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
\phi(x)=S(u,e^x).
\]
The inspected primary source gives that \(\phi\) is increasing and convex and that
\[
\lim_{x\to-\infty}\frac{\phi(x)}x=\nu(u,0).
\]

For every fixed
\[
s\ge0,
\]
convexity and the asymptotic slope imply
\[
\phi(x)-\phi(x-s)\longrightarrow \nu(u,0)s.
\]

Choose a fixed
\[
x_0
\]
in the domain of \(\phi\). Convexity bounds all secant slopes to the left of \(x_0\) by a finite one-sided slope there. Hence
\[
0\le\phi(x)-\phi(x-s)\le Cs
\]
for all sufficiently negative \(x\) and every \(s\ge0\).

For a radial law \(\beta\), take
\[
s=-\log t.
\]
The majorant becomes
\[
C(-\log t),
\]
which is integrable exactly under the finite logarithmic-moment hypothesis. Dominated convergence yields
\[
\lim_{r\downarrow0}
\left(
S(u,r)-A_\beta(u,r)
\right)
=
\nu(u,0)
\int_{(0,1]}-\log t\,d\beta(t).
\]

Subtracting two such identities proves the pairwise formula.

For normalized volume measure on the unit ball, the radial density is
\[
2n\,t^{2n-1}\,dt
\]
and
\[
2n\int_0^1(-\log t)t^{2n-1}\,dt=\frac1{2n},
\]
recovering the source theorem exactly.

For a smooth radial mollifier, pushforward under
\[
w\mapsto|w|
\]
gives the stated kernel law and logarithmic moment. No numerical experiment or finite approximation is used.
