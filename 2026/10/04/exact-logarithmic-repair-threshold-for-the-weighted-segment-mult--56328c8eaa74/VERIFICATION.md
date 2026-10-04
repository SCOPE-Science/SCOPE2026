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

For
\[
q=\frac{\gamma}{p-1},
\]
the reciprocal defect has the exact integral
\[
\int_0^1
x^{-1}\bigl(\log(e/x)\bigr)^{-q}\,dx
=
\int_1^\infty u^{-q}\,du.
\]
It is finite exactly when
\[
q>1,
\]
which gives the threshold
\[
\gamma>p-1.
\]

When that condition holds, both the weight and reciprocal have finite mass on the compact region where they differ from one. This uniformly bounds the Muckenhoupt product on all intervals of length at least one, so the primary source's characterization applies.

For the classical small-scale test,
\[
\int_0^r
x^{-1}\bigl(\log(e/x)\bigr)^{-q}\,dx
=
\frac{\bigl(\log(e/r)\bigr)^{1-q}}{q-1}
\]
is exact, while
\[
\int_0^r
x^{p-1}\bigl(\log(e/x)\bigr)^\gamma\,dx
\sim
\frac1p r^p
\bigl(\log(e/r)\bigr)^\gamma.
\]
Their normalized product yields the displayed
\[
\bigl(\log(e/r)\bigr)^{p-1}
\]
divergence and its exact leading coefficient.

As \(\gamma\downarrow p-1\), the total reciprocal defect mass equals
\[
\frac{2(p-1)}{\gamma-p+1},
\]
which gives the upper characteristic bound; a fixed unit interval through the origin gives the matching lower bound.

No finite computation, numerical approximation, or external certification is used.
