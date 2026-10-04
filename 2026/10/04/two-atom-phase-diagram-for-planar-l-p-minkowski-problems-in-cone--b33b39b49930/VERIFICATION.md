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

The proof was checked from the defining halfspaces rather than inferred from numerical output. For \(u_i=-n_i\), the support value is exactly \(-a_i\). The two interior facet lengths are obtained by measuring the change of the opposite normal along a supporting line, whose derivative has magnitude \(\sin\Delta\). This yields the two mass equations and the scalar map \(\Phi_p\).

The critical-point calculation was recomputed independently: for \(p>1\), critical points satisfy \(p-1=H(r)\) with \(H(r)=r(b-c)/((r-c)(b-r))\). Differentiating \(\log H\) gives the unique minimizer \(r=\sqrt{bc}\), hence the stated \(p_*\). The quadratic for \(r_-\) and \(r_+\) follows by clearing denominators.

`verify.py` checks representative geometries and parameters, reconstructs the same facet lengths from Cartesian line intersections, verifies recovered masses, and checks the predicted three-root regime. These finite checks do not prove the all-parameter theorem; they only guard the algebra and implementation of the displayed formulas.

No claim is made for three or more atom directions, higher-dimensional cones, or general uniqueness beyond this planar two-atom model.
