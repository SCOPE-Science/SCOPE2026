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

# Reproducible checks

Run `python verify.py` with NumPy/SciPy. It enumerates twelve cuboctahedron vertices directly as signed coordinate differences in four-space, computes its fourteen distinct facet planes and facet areas in the intrinsic three-space, and independently constructs each central polygon section and its Minkowski perimeter from half-space inequalities. It also checks the sixteen facets of the ambient regular four-cross-polytope and their orthogonal central sections. Numerical outputs agree with \(\mathcal W_3(C)=16/3\), \(\mathcal W_4(B)=128/15\), and the ordinary reference volumes \(5/6\), \(2/3\).

For the exact proof, check the facet-geometry table and substitute the values into the single recurrence stated in RESULT.md. This is not an exhaustive computational theorem about arbitrary convex bodies; independent mathematical verification has not been performed.
