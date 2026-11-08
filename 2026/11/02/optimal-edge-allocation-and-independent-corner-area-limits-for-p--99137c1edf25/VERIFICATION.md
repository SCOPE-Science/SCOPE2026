---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each fixed strictly convex m-gon m>=3 and fixed w_i>0, on the event every edge is hit, the exact hull deficit is the sum of corner wedge areas d_i R_{i-1} L_i. Disjoint adjacent boundary subintervals give joint tail (1-w_{i-1}s-w_i t)^n, whose integral yields F_n; the missing-edge event is bounded by sum(1-w_j)^n. All 2m rescaled edge endpoint gaps tend jointly to independent exponentials and have uniform all-order moments, establishing n^2 deficit convergence, mean C=sum_i d_i/(w_{i-1}w_i), and variance 3 sum_i [d_i/(w_{i-1}w_i)]^2. Positive Hessian of 1/(xy) gives strict convexity of C on positive simplex and unique optimum; KKT says equal weights iff adjacent d sums constant, with parity and parallelogram consequences. Independent rational integration and convex-hull/rectangle checks corroborated the normalization, including 357/800 for n=3 and neighboring interval probabilities 1/5,3/10.

## originality

PASS

Reitzner–Schütt–Werner (2019 preprint/2023 paper) studies uniformly distributed polytope-boundary points and volume-deficit rates; its inspected main theorems do not give the arbitrary per-edge weighted joint exponential-product corner limit and strict optimizer. Smooth-curve Hausdorff/area density problems concern different sampling or loss. An old weighted planar polygon theorem could still dominate.

## value

PASS

Optimal allocation of sampling effort among edges is a natural geometric design problem; the joint law and full moment limits give quantifiable corner variability, and the iff parity/quadrilateral criterion separates geometry from mere area-perimeter scaling. It includes a genuinely nontrivial optimum even though corner order statistics themselves are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
