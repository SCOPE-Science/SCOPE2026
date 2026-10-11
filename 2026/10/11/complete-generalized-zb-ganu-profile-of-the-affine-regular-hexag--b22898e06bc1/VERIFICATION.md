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
The analytic verification has three layers.

First, for
\[
N(s,t)=\max\{|s|,|t|,|s-t|\},
\]
the map
\[
T(s,t)=(s,t,s-t)
\]
is an isometry into a two-dimensional subspace of \(\ell_\infty^3\). `verify.py` checks on all six unit-ball vertices that for any two distinct coordinate functionals, the dual norms of the same-sign and opposite-sign combinations are exactly
\[
a+b
\quad\text{and}\quad
\max\{a,b\}
\]
in some order.

Second, the checker symbolically verifies the two optimized upper envelopes. In the region
\[
z\le\frac1r,
\]
the certificate is
\[
\frac{z+2r+(1+r^2)/z}{2(1+r^2)},
\]
with stationary point \(z=\sqrt{1+r^2}\). Feasibility is equivalent to
\[
r^4+r^2\le1.
\]
Beyond that threshold the optimum lies at the boundary \(z=1/r\), producing the second branch.

Third, both explicit extremizer families are substituted symbolically into the defining quotient. Their values simplify exactly to the claimed branch formulas, and the two formulas agree at
\[
r_*=\sqrt{\frac{\sqrt5-1}{2}}.
\]

A deterministic numerical search over directions, relative magnitudes and several parameter values is included only as a reproducibility check. It is not used as proof of the continuum supremum.

No independent audit or independent validation has been performed.
