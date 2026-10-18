---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. The complete primary facet list in Behrend et al. Proposition 2.7 (Proposition 2.8 in a cited version) has coordinates x_i≥0, proper upper cardinalities 1≤k≤n−1 with support z_k=k(2n−k+1)/2, and full sum ≤T=n(n+1)/2 for m≥n+2. At c=r1, r=T/(m+√m), the m coordinate distances and full-sum distance exactly equal r. The proper upper facet distance (z_k−kr)/√k>r reduces to r<h_k=z_k/(k+√k). Treat h_k as φ(√k) with φ′ numerator 2n+1−3x²−2x³ decreasing, so minimum on 1≤x≤√(n−1) is an endpoint. Checked h1>r and h_{n−1}>r via a=√(n−1),b=√(n+2)>a, leaving a strict positive polynomial difference. For any contained radius ρ, coordinate inequalities imply q_i≥ρ and total cap Σq_i+ρ√m≤T, whence ρ≤r; equality forces every q_i=r, establishing uniqueness. Verified 28,560 independent facet inequalities n≤120 and selected m; symbolic proof covers all m,n in domain, not finite enumeration.

## originality

PASS

PASS. Behrend et al. and Heuer–Striker supply the exact facet system, face lattice and volume/Ehrhart results, but not Euclidean inball or contact classification. Separately published exact partial-permutohedron inradius formula assumes n≥m−1 and derives min{n/2,√m(2n−m+1)/(2(√m+1))}; it expressly leaves n<m−1 unresolved. Present m≥n+2 is disjoint and has a different facet deletion structure, so its formula does not formally specialize. Searched symmetric polymatroid Chebyshev-center aliases; no broader domination found.

## value

PASS

PASS. The Euclidean inball and complete tangency/facet separation in the entire complementary redundant-inequality region m≥n+2 are natural intrinsic metric invariants of a standard polytope family. Proving all proper subset-sum facets inactive gives a structural simplex-envelope phenomenon across an infinite disjoint parameter regime, beyond a mere arbitrary slice or recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
