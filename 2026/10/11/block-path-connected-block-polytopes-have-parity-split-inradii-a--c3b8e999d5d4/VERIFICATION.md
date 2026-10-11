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

The arbitrary-dimensional mathematical proof is in `RESULT.md`. This verification record reports reproducible, supporting calculations; it does not substitute for that proof.

Critical symbolic premises: the zero-inclusive interval-incidence polytope has nonnegative coordinate facets and all odd-length alternating-sign facets \(\langle\alpha,x\rangle\le1\). The two distinguished facet normals satisfy \(a+b=e_1+e_n\). Their combined clearances prove the global bound \(\rho(2+\|a\|+\|b\|)\le2\). The even uniform center and odd two-level center attain that bound. The full center locus is the feasible solution set of the radius-fixed clearance inequalities, and three forced independent equalities leave affine dimension at most \(n-3\). Explicit small perturbations give relative interior witnesses for every dimension \(n\ge4\), proving equality; \(n=3\) has a unique center.

Run the standalone file using `python verify.py` in an environment with `numpy` and `scipy`. It generates all predicted facets through dimension \(14\), reconstructs their normal lengths, independently solves the full Euclidean inball linear program, verifies the symbolic center witnesses and the rank of the three active equations, and compares the predicted facet set with a convex hull independently constructed from all interval vertices through dimension \(6\). Its successful output is:

`VERIFY_OK block-path-insphere n=2..14 full_facet_lp=yes center_witnesses=yes incenter_dim=n-3 convex_hull_facets=n2..6`

The finite computations are not an infinite proof and do not independently validate novelty or the scientific value assessment.
