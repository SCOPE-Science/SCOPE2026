---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For n>=3 and the simple labeled prism P_n=C_n square K_2, reconstructed the 3-symbol column encoding: a selected column has exactly one A/B vertex; consecutive occupied columns must use opposite layers, every zero must have occupied neighbors in opposite layers, and zeros are isolated. Thus every occupied list has even length k>=n/2 and the minimum is k=2ceil(n/4), with h=n-k zeros. Root at a top occupied vertex and write a cyclic gap bit vector of length k, weight h; dividing by k/2 roots per configuration gives V=2n binom(k,h)/k. One-for-one independent-domination exchanges coincide with moves along original edges and swap adjacent unequal gap bits; cyclic run compositions count degree-2r vertices as 2n/r binom(h−1,r−1)binom(k−h−1,r−1), summing to E=2n binom(k−2,h−1). If h=k (n divisible by4), four configurations have no moves. Otherwise fixed-root adjacent gap swaps on a path connect all bit vectors, and a permitted boundary move shifts the marked top occupied token by one column, proving full connectivity. Gap index parity flips under each swap because k even, giving bipartiteness; when h=k−1 (n=3 mod4), connected 2-regular graph has 2n vertices and equals C_{2n}. Maximum degree <=6 as k−h<=3. Independently enumerated every vertex subset and full exchange graphs for n=3,...,9: counts/components/degrees exactly agree, including n=3 and n=4 boundaries; this is corroboration of the explicit uniform proof, not an extrapolation.

## originality

PASS

Brewster–Mynhardt–Teshima already define i-graphs and prove a general equivalence of token-jump and token-slide for independent dominating sets, credited here. Their inspected full primary text addresses structural realizability, not this prism reconfiguration classification. Allagan et al. (2026) give an exact census for minimum ordinary dominating sets of the same labeled prism. For n=0 mod4 its four rigid optimum sets coincide with independent optima, so that cardinality is already known. Other congruences need not coincide: e.g. n=3 has ordinary minimum-dominating count 9, while minimum independent-dominating count is 6, and n=9 current i-graph has 60 vertices. The new contribution is the i-graph edge/degree/connectivity/bipartite classification and its exact independent-domination counts outside prior overlap; no claim of novelty for the basic token-slide equivalence or overlapping old counts.

## value

PASS

Minimum independent dominating sets and their reconfiguration connectivity are natural graph invariants. This supplies a complete labeled infinite-prism-family classification: exact degree distribution, zero/exchange-edge counts, all connectivity exceptions, bipartiteness and sharp max degree. Especially informative is the four isolated configurations exactly for n divisible by4 and a cycle for n=3 mod4. The result is a meaningful classification, not an arbitrary small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
