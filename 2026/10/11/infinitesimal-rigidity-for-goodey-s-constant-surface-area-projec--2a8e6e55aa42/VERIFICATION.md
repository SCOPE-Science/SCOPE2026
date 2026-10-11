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

The analytic proof has three independent components.

For planar projections, substituting
\[
h=1+\varepsilon f
\]
into
\[
\operatorname{Area}_2
=
\frac12\int(h^2-(h')^2)
\]
gives
\[
\left.\frac{d}{d\varepsilon}\operatorname{Area}_2\right|_{\varepsilon=0}
=
\int f.
\]

For three-dimensional projection surface area,
\[
\det(I+\varepsilon M)
=
1+\varepsilon\operatorname{tr}M+O(\varepsilon^2).
\]
With
\[
M=\nabla_{S^2}^2f+fI,
\]
the trace is
\[
\Delta_{S^2}f+2f.
\]
The integral of the spherical Laplacian is zero, leaving twice the equatorial integral of \(f\).

For the equatorial Funk transform on \(S^3\), the degree-\(\ell\) multiplier is proportional to
\[
C_\ell^1(0).
\]
The identity
\[
C_\ell^1(\cos t)
=
\frac{\sin((\ell+1)t)}{\sin t}
\]
shows exactly that the multiplier vanishes for odd \(\ell\) and for no even \(\ell\). Thus the kernel is precisely the odd functions.

The packaged checker independently replays the determinant linearization and exact Gegenbauer recurrence and performs symbolic regression checks for the planar area variation. Those finite checks support the algebra; the universal kernel statement is proved by the displayed closed identity, not inferred from enumeration.

Limits: no nonlinear local uniqueness theorem and no second-order classification are claimed.
