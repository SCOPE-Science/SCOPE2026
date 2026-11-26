---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A proper nonempty cycle subset is a path forest; marking a one-run start gives n choices of position and exactly r marks per labelled subset, including symmetric run configurations. For deficiency d the number r of components is at most d. For fixed shape there are O_d(n) labelled subsets and at most 2^d d! isomorphisms between any two. Thus the O_d(n^(r−1)) shapes with r<d give O_d(n^d) total. When r=d all d gaps are unit; imposing a unit part or equality of two parts in a d-part composition costs one degree of freedom, so all such exceptions cost O_d(n^d) maps as well. The good shapes number n^(d−1)/(d!(d−1)!)+O_d(n^(d−2)); for each there are n(d−1)! choices for each of domain and image and 2^d orientation choices. This proves the leading coefficient 2^d/d; d=1 separately gives exactly 2n² even at n=3. The original context checks also hold: empty and full contributions are 1 and 2n, the component bound and independent-set factorial sandwich give the claimed growth and rank deviation exponent, and the two-point distance witness works precisely for n≥6. For the path comparison, each rank-k map with k<n admits at least one pair of omitted vertices and each of the n² possible pairs is isomorphic to the reference P_(n−1) problem. Neither counting convention quotients labelled domains or maps.

## originality

PASS

Limited to the repaired asymptotic at moving rank n−d and the description of its leading class. The exact cycle rank polynomial overlaps a distinct record directly and no claim to it remains. The factorial growth and macroscopic concentration have near-equivalent path counterparts and are not the repaired finding. No compared statement supplies the leading fixed-d coefficient or the dominant-type assertion; obtaining it from the exact wheel formula requires identifying which shapes supply the leading order despite their varying symmetry factors.

## value

PASS

The natural fixed-deficiency stratum detects near-complete partial symmetries, a regime not characterized by typical-rank behavior. The uniform formula in each fixed positive deficiency gives both the growth power and a nontrivial leading coefficient, and identifies which domain/image structures account for that order and which are lower by a full power of n. This is reusable quantitative information rather than the evaluation of an arbitrary small case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
