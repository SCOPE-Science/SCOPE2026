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

For a dual quaternionic polynomial written as
\[
P=g+\epsilon h,
\]
the fresh source proves
\[
P(x_1+\epsilon x_2)
=
g(x_1)
+
\epsilon\left(
h(x_1)+dg_{x_1}(x_2)
\right).
\]
Therefore
\[
P(x_1+\epsilon x_2)=0
\]
if and only if
\[
g(x_1)=0
\]
and
\[
dg_{x_1}(x_2)=-h(x_1).
\]
This proves the affine-fiber description without approximation.

The source differential theorem gives
\[
\operatorname{rank}_{\mathbb R}dg_{x_1}\in\{0,2,4\}
\]
at nonreal points and
\[
\operatorname{rank}_{\mathbb R}dg_{x_1}\in\{0,4\}
\]
at real points. Hence nonempty fibers have real dimension
\[
4-\operatorname{rank}_{\mathbb R}dg_{x_1}.
\]

For
\[
P_*(x)=x^2+1+\epsilon i,
\]
a primal zero has the form
\[
J^2=-1.
\]
Direct expansion gives
\[
P_*(J+\epsilon v)
=
\epsilon(Jv+vJ+i).
\]
Writing
\[
v=a+bJ+w,
\qquad
w\in\mathbb C_J^\perp,
\]
yields
\[
Jv+vJ=2aJ-2b.
\]
Thus the lift equation is solvable only for
\[
J=\pm i.
\]
The solution sets are
\[
-\frac12+\operatorname{span}_{\mathbb R}\{j,k\}
\]
over \(i\), and
\[
\frac12+\operatorname{span}_{\mathbb R}\{j,k\}
\]
over \(-i\).

Every such dual part has nonzero real component, while the quadratic cone over a nonreal primal point requires a purely imaginary dual part orthogonal to the primal imaginary direction. Hence the two zero planes are disjoint from
\[
Q_{\mathbb{DH}}.
\]

The proof is exact real-linear algebra. No numerical experiment, finite enumeration, or unverified certificate supports the infinite statements.
