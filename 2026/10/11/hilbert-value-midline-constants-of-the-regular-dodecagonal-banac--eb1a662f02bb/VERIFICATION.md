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
The verification target is the exact pair of endpoint inequalities
\[
\frac{N_{12}(x+y)+N_{12}(2x-y)}{2}\le\sqrt3
\]
and
\[
\frac{N_{12}(x+y)^2+N_{12}(2x-y)^2}{2}\le3
\]
under
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1.
\]

`verify.py` uses exact rational-pair arithmetic for \(\mathbb Q(\sqrt3)\). It constructs all twelve signed supporting facets and all thirty-six half-space constraints on \(x\), \(y\), and \(x-y\). It examines every one of the \(12^3=1728\) choices of one tight facet from each block.

Each consistent rank-three system is an affine line. Intersecting that line with all thirty-six half-spaces gives its exact feasible interval. The checker confirms \(168\) nonempty faces, including \(24\) nondegenerate segments. Because both objectives are convex on each such segment, endpoint evaluation is exhaustive.

The exact endpoint maxima are
\[
\sqrt3
\quad\text{and}\quad
3.
\]
The explicit pair
\[
x=(1,\sqrt3-2),
\qquad
y=(\sqrt3-1,\sqrt3-1)
\]
is checked independently and satisfies
\[
N_{12}(x+y)=N_{12}(2x-y)=\sqrt3.
\]

The third constant is then verified analytically:
\[
\frac{\sqrt A+\sqrt B}{2}
\le
\sqrt{\frac{A+B}{2}}
\le
\sqrt[4]{3}.
\]
No finite experiment is used as proof of this nonlinear supremum.

No independent audit or independent validation has been performed.
