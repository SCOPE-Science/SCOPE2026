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

The central equality was checked from the definitions without numerical experiments. The unit sphere in a finite-dimensional Hilbert space is totally bounded. Given any \(r>0\), finitely many radius-\(r\) balls cover the sphere, so an infinite indexed family places two distinct indices in one ball. Their vectors \(u,v\) satisfy \(\|u-v\|<2r\), whence
\[
\operatorname{Re}\langle u,v\rangle=1-\frac12\|u-v\|^2>1-2r^2.
\]
Letting \(r\) decrease to \(0\) proves the lower bound \(1\); Cauchy--Schwarz proves the matching upper bound. In the real case the same estimate is signed, and in the complex case modulus dominates real part.

Boundary checks were explicit. A repeated vector attains \(1\) exactly. An injective infinite family need not attain \(1\), but its supremum is \(1\). Finite index sets are excluded because finite Grassmannian packings can have smaller correlation. Infinite-dimensional Hilbert spaces are excluded because an infinite orthonormal family has zero off-diagonal correlation.

For a finite positive nonatomic measure space, an equal-measure measurable \(d\)-partition gives a piecewise-constant normalized family. Direct integration gives the tight frame identity
\[
\int_\Omega |\langle h,\tau_\alpha\rangle|^2\,d\mu(\alpha)=\frac{\mu(\Omega)}d\|h\|^2.
\]
Thus the stated existence consequence is independent of the compactness step and then inherits the correlation equality.

The primary source was checked at the normalized continuous-frame definition, continuous correlation definition, continuous Grassmannian definition, the open classification question, and its sample calculation. The later continuous Rankin source was checked at its signed supremum statement. The literature comparison found no checked source asserting the universal infinite-index equality.
