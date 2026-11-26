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

For distinct smooth complex conics with precisely the stated two-branch singularities, the local Tjurina contributions are 1 for A1 and 3 for A3. The baskets give total Tjurina numbers 5,17,35 and exactly saturate the pairwise Bezout multiplicity counts. The minimum local Arnold exponent is 3/4, giving minimal syzygy degree r at least 1,3,4 in degrees 4,6,8. A Koszul relation supplies r<=d-1. In degree 4 the du Plessis–Wall lower bound at r=1 is 6 and the sharpened upper bound at r=3 is 3, so only 2 is allowed. In degree 6 the sharpened upper bounds for r=4,5 are 15,10; in degree 8 the corresponding bounds for r=5,6,7 are 33,28,21. They lie strictly below the basket's Tjurina number in each degree. Thus r=k=d/2 without assuming plus-one generation or fixing a realization. Now (d-1)^2-r(d-r-1) is 7,19,37, exactly two above the respective Tjurina numbers; the minimal-plus-one criterion applies at r=d/2 and gives (k,k,k+1). The odd-degree four-syzygy exception in the defect-two characterization is irrelevant. For a three-syzygy curve the unique relation shift in the Milnor resolution is the sum of the three syzygy degrees (3k+1 here), with the three syzygy shifts d-1+d_i. Hence the graded Betti table is fixed. Identical resolutions here refers to graded free-module shifts and multiplicities, not equality of the differential matrices for different equations. The uploaded script was read, not run; all decisive finite substitutions are listed above.

## originality

PASS

The cited constructions and enumerative classification already give the same baskets and exponent triples for examples or for arrangements assumed plus-one generated. The supported distinct result is the converse on all realizations of the two-node baskets: the singularity data alone exclude every competing minimal degree and then force the full Betti table. This uses existing numerical theorems; none of the strongest inspected sources states the unconditional rigidity or supplies it by merely specializing an existing basket classification.

## value

PASS

This is a complete positive rigidity statement for all realizations in three natural near-maximal-tacnode strata already known to be nonempty. It resolves whether weak data suffice to determine the full syzygy profile in those strata, including excluding possible weak Ziegler pairs, rather than recalculating the exponents of a known example. Its short proof is a use of sharp numerical constraints at a boundary, not the substitution of a single chosen model into a resolution algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
