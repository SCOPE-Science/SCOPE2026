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

The local proof was replayed from the defining coordinates. For a positive-curvature point, the graph expansions are
\[
f(\pm t)=\frac{\kappa}{2}t^2+o(t^2),\qquad f'(\pm t)=\pm\kappa t+o(t).
\]
With \(X_t=(0,\kappa t^2)\), the two dent-edge slopes are \(\kappa t/2+o(t)\) and \(-\kappa t/2+o(t)\). Their turn at the dent vertex is therefore negative with magnitude \(\kappa t+o(t)\). The endpoint turns are positive for small \(t\), so this is the only negative turn. Since the signed turn of a simple closed curve is \(2\pi\), the absolute total curvature is \(2\pi+2\kappa t+o(t)\).

The removed arc length is \(2t+\kappa^2t^3/3+o(t^3)\), while the two replacement segments have total length \(2t+\kappa^2t^3/4+o(t^3)\). Thus the cell perimeter differs from the original perimeter only by \(O(t^3)\), giving
\[
\operatorname{ac}(\partial K_t)=\frac{2\pi}{p}+\frac{2\kappa}{p}t+o(t).
\]

For containment, the removed cap has uniform depth \(O(t^2)\). If \(B(o,r)\subset\operatorname{int}K\), then for \(K^\varepsilon=o+(1-\varepsilon)(K-o)\), convexity gives \(K^\varepsilon+\varepsilon rB(0,1)\subset K\). Therefore a fixed choice \(\varepsilon=Mt^2\) with \(M\) large enough places the whole homothetic copy inside the dented cell. Its average curvature is
\[
\frac{2\pi}{(1-Mt^2)p}=\frac{2\pi}{p}+O(t^2),
\]
which is smaller than the dented cell's value for all sufficiently small \(t\).

As a sanity check, the construction was evaluated on the unit circle, where \(\kappa=1\) and \(p=2\pi\). The computed quotient \((\operatorname{ac}(\partial K_t)-1)/t\) approaches \(1/\pi\), matching the proved coefficient \(2\kappa/p\). This finite numerical check is not used as proof.

Scientific limits: the undeformed cell is \(C^2\), the dented boundary is piecewise smooth, and only the explicit local V-dent family is classified. The theorem does not prove that every small dent fails and does not settle Larson's full piecewise-smooth dent criterion.
