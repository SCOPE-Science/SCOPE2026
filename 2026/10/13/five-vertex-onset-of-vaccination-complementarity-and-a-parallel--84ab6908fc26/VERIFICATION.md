---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Sample all open edges first and restrict the same graph after each deletion. The burden counts ordered connected pairs, including diagonals, divided by the fixed original order for the expected outbreak. Benefit submodularity is therefore the nonnegative mixed difference of the unnormalized burden. Sites in separate components give zero. In the common component, after both sites are removed, every residual component touches at least one site. Writing A and B for the sizes attached only to one site and c_i for sizes attached to both, squares for singly attached pieces cancel. Expanding the remaining squares gives 2[(A+1)(B+1)−Σ_{i<j}c_i c_j]. With at most four vertices the sum is at most 1. Both statements hold pointwise. On a forest an ordered pair contributes its path-open probability times the indicator of deleting no vertex of the path; each indicator has nonnegative mixed difference, including the length-zero path. On C5, any nonempty deletion set leaves a forest. For adjacent sites at most one residual component in the open graph can touch both, so only nonadjacent sites at the empty set can give a negative difference. The two complementary routes for a pair at distance d=1 or 2 give connection probability p^d+p^(5−d)−p^5. Subtracting the two four-vertex path burdens and adding back the 3+2p residual burden gives 2p²(1+3p+5p²−10p³). The derivative of the cubic has a single positive zero, a maximum, and the cubic changes from +1 to −1 across [0,1], proving the unique threshold. Independent Boolean reachability enumeration gave no negative deterministic differences for n≤4 (1,586 cases for n=2–4), the exact C5 coefficient vector, and the gap −61009/160000 at p=19/20, giving −61009/800000 after normalization. Independent bisection gave 0.935152824805653192… . These checks establish the sharp onset without transferring it to other seeding conventions.

## originality

PASS

The distinct contribution supported by the comparisons is the exact two-site identity for the uniform-original-source burden, the sharp universal four-vertex guarantee, and the complete five-cycle phase for that burden. Pairwise fragmentation, non-submodularity in related immunization models, and unique-path coverage are not credited as new in themselves.

## value

PASS

Expected pairwise connectivity is a standard measure of fragmentation, and diminishing returns is a meaningful structural property of the deletion benefit. The attachment formula identifies exactly what competes with fragmentation and explains why the first deterministic obstruction cannot arise below five vertices. The threshold gives both sides of the obstruction under iid edge thinning, rather than only an endpoint example at p=1. These are reusable mathematical facts even without an optimization theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
