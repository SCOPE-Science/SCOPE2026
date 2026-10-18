---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For each zero-sum 3-vertex molecule, three signed edge flows form a one-parameter affine line, and for 0<p<=1 their p-cost is concave between three breakpoints, attaining a global minimum at a breakpoint: an explicit spanning-tree reduction valid also for p=1. For a molecule with two like-signed terminals the direct source/sink star minimizes the ordinary 1-transport cost by strict Euclidean triangle inequalities; its two weighted costs A,B imply ||m||_p<= (A^p+B^p)^(1/p) <= 2^(1/p-1)||m||_1. In the p=1 dual Lipschitz potential hexagon, the six extreme points are +/- distance potentials. Their affine gradients at each vertex bisect the interior angle and have exact norm sec(theta_i/2), proving the upper bound. For any largest-angle vertex a the opposite side is longest; the normalized two-edge star has exact p-cost 2, while the other spanning trees have costs (1+b/c)^p+(a/c)^p>2 and (1+c/b)^p+(a/b)^p>2. A small displacement from a along the sum of two outgoing edge unit vectors has Euclidean length 2cos(theta_max/2), attaining the lower bound exactly. Handles all real 0<p<=1 and all nondegenerate triangle shapes; finite direction-grid verification is not a universal proof.

## originality

PASS

Statement-level comparisons against direct primary mathematical texts found no implication of this full exact claim in the inspected sources; separate specific comparisons below, with documented residual priority risks rather than a negative-search novelty proof.

## value

PASS

Computes the exact nonlinear-in-p quasi-Banach norm of a natural prescribed affine simplex interpolation on every Euclidean triangle, with sharp geometric dependence on maximum angle. Useful as a local cell constant for free p-space interpolation and shape-sensitive stability; distinct from merely providing a nonsharp extension bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
