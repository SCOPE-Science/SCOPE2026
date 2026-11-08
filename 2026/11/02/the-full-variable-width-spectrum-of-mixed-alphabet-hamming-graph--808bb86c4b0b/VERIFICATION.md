---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For any factor product of K_{q_i}, every edge changing coordinate i sits in a unique maximal coordinate clique of size q_i. In counting-free FO^k (k≥3), an edge lies in an a-clique via x,y and a−2 witnesses, for 2≤a≤k. Thus E_j colors edges by min(q_i,k)=j with at most k names. Iterating finite E_j-path distance via three free-variable roles and locally reusable bound names defines, for each finite h, the existence of a distance-h pair with k variable symbols; maximum finite E_j distance in a component equals the number c_j of corresponding coordinate factors. Hence equality of all truncated counts is necessary. Sufficiency: a duplicator maintains coordinatewise equality patterns of k pebbles under a paired factor bijection for alphabets below k, or both≥k, because at most k−1 coordinate values remain on each move. Width-1/2 cases and fixed-d weak-composition count follow; the first differing exact factor multiplicity t gives minimum width t+1 except different factor counts (width3) and one-factor versus product (width2). Independent small mixed-product E_j-component distance checks at k=3,4,5 corroborate; the unbounded-quantifier-rank theorem rests on the pebble argument, not finite check.

## originality

PASS

The earlier same-family three-variable classification is fully credited; it does not yield the all-width spectrum or sharp width t+1 distinguishing any first unequal coordinate-size multiplicity. General pebble-game characterization by Grohe–Otto, Hamming embedding theorems by Klavžar–Peterin and VC-dimension results by Adler et al. do not explicitly imply the product-specific classification without additional colored edge and game arguments. This is qualified best-of-knowledge originality, with risk of a general finite-variable product decomposition theorem.

## value

PASS

Provides a natural exact invariant for a canonical product-graph class at every variable width: a complete classification, number of theories for fixed d, smallest representatives and sharp logical width hierarchy. Distinguishing what bounded-variable logic can and cannot count despite unlimited quantifier depth is a substantive finite-model-theory problem, not a parameter renaming or finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
