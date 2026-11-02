---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For all n>=1, d>=1, 0<=k<d over C, the archival parameterization identifies O_{k,n,d} as projective image of pairs ([L],[F]) under [L^(d-k)F]. The 1-parameter diagonal subgroup with weights B^i (integer B>d) has distinct degree-d monomial weights; hence its fixed points in ambient projective space are precisely monomial points. The osculating variety is invariant, and a fixed monomial M=L^(d-k)F forces L to divide M. Unique factorization makes L a coordinate variable, so exactly monomials with some exponent >=d-k survive. Choosing j constrained variables leaves d-j(d-k) stars-and-bars units, giving the stated inclusion-exclusion formula up to min(n+1,floor(d/(d-k))). Compactly supported Euler localization chi_c(Y)=chi_c(Y^{C*}) applies also to singular projective varieties, and projectivity gives ordinary chi. When d>2k no double intersections exist, giving (n+1)binom(n+k,n). At k=0 count n+1; at k=d-1 the variety is the full ambient projective space; k=d is separately ambient and not substituted into a zero divisor. Independently implemented exact enumeration checked 396 triples with 478,621 monomial test instances (n=1..6,d=1..11,k<d) including base-B weight injectivity, formula, stable and endpoint cases; finite checks corroborate but do not prove universal quantifiers.

## originality

PASS

Best-of-knowledge originality for the UNIFORM Euler characteristic formula in dimensions n>=2 and all osculating orders: prior BCGI identifies exact factorization models but not the target-specific global Euler formula; generic C* Euler localization requires classification of the target fixed monomials and overlap inclusion-exclusion. Kőműves gives stronger binary-form coincident-root-locus machinery that covers n=1 as a subfamily, which is NOT claimed independently new. Resultary and targeted literature searches located no stronger result encompassing the n>=2 formula. This is not a priority guarantee; the short localization argument could exist as folklore or unindexed equivariant topology.

## value

PASS

The family of osculating Veronese varieties is a classical natural object in algebraic projective geometry. The topological Euler characteristic is an independently meaningful global invariant, not determined by dimension or secant defectivity. The formula supplies a uniform three-parameter exact answer, the sharp no-overlap threshold d>2k, and fully evaluated inclusion-exclusion corrections in the overlap range d<=2k. It can serve as a baseline for more refined topological or characteristic-class computations. The contribution is narrow/elementary and does not compute Betti groups, Hodge data or general secant invariants; n=1 and tangential subfamilies have relevant earlier coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
