---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The deletion condition gives basis exchange: two distinct failed exchanges from the same basis would be adjacent deleted sets, and if there is just one choice the exchanged set is the surviving target. For iid continuous Gaussian coordinate scores the unconstrained top r-set is uniform; if it is deleted, the uniquely second-best r-set exchanges its smallest score for the largest outside score. No neighbor is deleted, and the two independent internal orderings make each replacement equally likely. Orthogonal projection onto the linear span of vertex differences is standard Gaussian there and does not change the optimizer, so the law is intrinsic. Each deletion has d surviving neighbors; an unordered deleted pair has four common neighbors at Johnson distance two and none at larger distances. Hence Σt=md and Σt²=md+8q, giving the claimed C₂. In the star, a common neighbor either contains 1 and needs three other elements, or omits 1 and needs all six other elements. In the triangle the common-neighbor list is exactly {124}: the four candidates for the first two deletions are 124, 125, 134, 135 and only 124 shares two with 246. Thus the histogram changes by (−1,3,−3,1), yielding the displayed third forward difference, strictly positive for real s>2 by integration of the positive third derivative on [d,d+3]. At n=7, 6/(35·12)³=1/12348000. Rank-three polytopes are full dimensional in the sum hyperplane (each e_i−e_j arises from two surviving bases with a common pair; at most three choices are obstructed), hence the matroids are connected for the cited face theorem. Their parameters n,r,λ=3,μ=3 match. Tutte equality follows because only the deleted r-sets have a different rank from the uniform rank, and Ehrhart equality follows from the equal number of symmetric, disjoint lattice caps. Independent bounded replay: enumerated all strict score permutations with integer scores 1,…,n and directly maximized over surviving bases at n=7,8; all exposure counts agree. Enumerating integer points with coordinate cap ℓ, total 3ℓ and the three deletion inequalities at ℓ=1,2,3 gave (32,318,1699) at n=7 and (53,736,5010) at n=8 for both families. These checks corroborate the general arguments of RESULT.md and do not establish the universal face equality by computation.

## originality

PASS

The supported distinct claim is the rank-three star/triangle witness of identical Tutte and Ehrhart polynomials, full face vector and C₂ but unequal full angular spectra and all real moments above two, including its sharp first separation. Do not claim the pointwise angle or C₂ formulas as uncatalogued in the overlapping domains: there are exact matches in rank two and in the interior range r,n−r≥3. The matched angle law is a tool to verify the witness, not itself a non-identifiability theorem: this witness requires a triple-neighborhood discrepancy under matched lower-order combinatorial invariants. No inspected statement supplies that separation or a general implication guaranteeing it under all the target constraints. Later or same-day dates do not establish priority.

## value

PASS

The canonical normal fan records optimizer frequencies that matter independently of lattice-point counts and the face vector. This witness prevents reconstruction even after the second collision moment is added. The star versus triangle construction isolates a third-order geometric statistic with a sharp exact, dimension-parametric gap; the moment order is forced by matching the lower-order data, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
