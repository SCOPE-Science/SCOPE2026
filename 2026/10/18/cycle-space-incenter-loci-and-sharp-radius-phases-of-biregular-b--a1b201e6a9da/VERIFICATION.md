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

The analytical proof derives the exact intrinsic ball-containment inequalities from the finite halfspace presentation of the bipartite fixed-cardinality matching polytope. It separately computes affine-hull projections in the nonsaturated and saturated cases. Summing each symmetric family bounds the radius; the uniform center reaches the minimum. Tightness forces either a single center, free left-star contrasts, or a translated graph-supported transportation polytope. The rank of a connected graph's incidence matrix determines the last affine dimension exactly.

The standalone code `check_inballs.py` constructs the linear programs from the *edge lists*, with no use of the predicted radius to define the optimization objective or feasible halfspaces. It numerically compares optimal radii with closed forms; checks uniform-center containment; and verifies the number of active support planes and the rank/dimension of forced equality spaces. SciPy HiGHS solved 110 complete-bipartite and 22 connected sparse incidence-graph instances: **132 profiles passed**. It also confirms the distinct center phases for the incidence graphs of \(K_4\) and \(K_n\), \(n=5,6,7\). Run `python -m pip install -r requirements.txt` and then `python check_inballs.py`.

Finite optimization is corroboration, not an exhaustive proof of the infinite family. Exact symbolic identities and rank arguments in `RESULT.md` supply the universal proof. An independent mathematical audit has not been performed, and a sufficiently broad undocumented prior result could still cover the claim.
