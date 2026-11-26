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

The binary parallel firing rule translates the support, so the facets are exactly the translates D+t. An intersection of two facets is indexed by the unique ordered representation of their nonzero translation difference, hence positive-dimensional faces have just one facet owner. In each facet rooted at a+t, take the pairs (σ, σ∪{a+t}) for faces σ excluding the root of size at least two. Descending size removes every competing coface before σ, and pairs at each size do not interfere. These are equivariant stages of elementary orbit-family collapses: translation preserves the families and the free-face retractions can be chosen on one facet and translated, relative to shared vertices. The surviving step orbits are disjoint by unique ownership and the unit edges form the spanning cycle. Replacing each chord by its start loop followed by the forward unit arc, with inverse sending that loop to chord followed by reversed arc, gives equivariant inverse homotopies by path cancellation relative to the cycle. For the integral basis, a chord-minus-arc cycle has coefficient 1 on its own chord and 0 on all others; subtracting these terms from any integral cycle leaves constant coefficients on the oriented unit edges. Thus the norm cycle is a trivial summand and each nonunit step supplies one free regular summand, with no divisibility or extension assumption. Singer's theorem gives the stated parameter family and the rank simplifies to q³.

## originality

PASS

The underlying complex and nonequivariant collapse/rank are already covered by the Steiner-design point-side calculation, and the complexified character is a graph-cover consequence. Credit the narrow refinement: a specified unit-step Cayley target and translation-compatible elementary collapse, together with the integral decomposition in explicit rotated coordinates on that graph. Neither the previously identified incidence cycle lattice nor the complex character is an explicit integral permutation basis on this avatar of the avalanche complex.

## value

PASS

The ordinary wedge rank and complex trace would be insufficient as new findings. Here a natural cyclic symmetry from the firing dynamics is kept throughout an explicit collapse, and the output is a usable integral basis with translation acting by permutations of whole families of cycles. It distinguishes integral coordinates from a complex character and gives a uniform model for a natural family of cyclic supports; the utility is in that refinement, not in the known q³ count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
