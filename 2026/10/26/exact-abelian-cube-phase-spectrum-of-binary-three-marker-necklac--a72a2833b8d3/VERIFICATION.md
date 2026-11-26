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

Fix which marker enters the first block. The three allowable cut intervals have p integer positions each and left endpoints differing by the shifts 0,d₁−p,p−d₃. Their common size is max(0,p−maxᵢ|dᵢ−p|). The three choices of first marker are disjoint even if the necklace is periodic, since cuts are indexed. For K=R/3≥k≥1 put q=p−k and shift the three gaps by k. The resulting ordered triples sum to 3q and have upper bound 2q on each coordinate. Inclusion–exclusion excludes three single-coordinate sets of size binomial(q+1,2), with no double exclusions. Burnside accounts for the equal-gap triple and gives (p−k)(p−k+1)+1 directed necklaces at or above k. Differences and subtraction from the total give the full spectrum, including R=3 as the sole value when p=1. The atom, density and mean follow by the given Riemann sums. An independent direct block-index test of 7,875 labeled supports through p=9 and canonicalization under word rotations verified the gap rule and all histogram entries on 369 necklaces.

## originality

PASS

The closest inspected indexed Abelian-cube statement counts distinct strings among linear factors, expressly not cyclic factors. The closely related work on Abelian periods and powers does not give the indexed-cut census. The supported distinct claim is the gap-to-cut multiplicity theorem and its exact all-size distribution over directed weight-three necklaces, not the definition or detection of Abelian cubes or the classical total necklace count.

## value

PASS

The phase multiplicity answers more than existence: it measures how robust a full-circle Abelian cube is to a change of starting point. Three ones is the first positive feasible weight for three balanced blocks and makes this a natural exact test class. The min/max gap rule gives the multiplicity directly, while the finite law quantifies both failure and nonzero phase abundance and yields a mixed limit. The rotated-string distinction matters even at maximal symmetry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
