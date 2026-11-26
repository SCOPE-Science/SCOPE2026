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

The original domain calculation is valid for arbitrary group and sandwich support: nonzero a satisfying both domain equalities must have the two indices of gh, and its group coordinate cancels to force gh to be the local idempotent. With p=p_{λi}, q=p_{μj}, the normalized move is conjugation by tp when h=(j,t,λ), because sqtp=1. Choosing s=uq⁻¹ and t=u⁻¹p⁻¹ realizes every coset label, and different local domains meet only at zero. This gives the original Brandt rule with the all-zero and global-identity exceptions. The repaired example checks directly: both patterns have four idempotents, the same 16 local arrows plus identity and absorbing map, but different multisets of idempotent counts in the two fixed-last-index classes. In A, to keep all products except the zero input nonzero, three distinct images must be chosen among two elements; in B the displayed input-to-image and product lists are actual permutations. The use of α(0)=0 follows because any other preimage of 0 gives a second zero product. The finite checker was read but not run; the repaired proof decides both cases without enumeration.

## originality

PASS

The repaired finding is the explicit collision of partial inner monoids across opposite complete-mapping outcomes within the regular combinatorial class. The same Brandt classification on the regular class already appears in a distinct indexed record. The arbitrary-pattern extension is a short reduction to that core followed by a global-identity check, not needed in the repair. The general complete-mapping criterion decides either input separately; the cross-invariant separation requires a pair with equal support cardinality but opposite outcomes. No matching separation was established in the inspected sources; this does not assert first priority for the classification or the individual complete-mapping decisions.

## value

PASS

The sample is motivated by a structural question: how informative is the partial inner monoid for a naturally defined complete-mapping property of the original semigroup? The equal invariant, same support count and shape, and opposite answers in two regular combinatorial examples demonstrate precisely the information loss, without relying on degenerate zero rows, groups or the all-zero case. A concrete positive mapping and a clean obstruction provide a usable witness beyond classifying either pattern in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
