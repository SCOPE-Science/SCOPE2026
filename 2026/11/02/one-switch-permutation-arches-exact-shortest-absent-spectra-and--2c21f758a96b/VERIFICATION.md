---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Each of k=a+b complete permutation blocks contains all q symbols, so every target length k embeds (one per block), whereas c^(k+1) is absent. In an infinite repeated permutation, leftmost greedy matching advances blocks at each weak rank descent. The two overlapping length-a+1 and length-b+1 rank-monotone conditions are necessary/sufficient for no embedding across the P^a|Q^b switch. Counting weakly decreasing choices before/after pivot c gives Σ_c binom(a+q-p(c),a)binom(b+s(c)-1,b). Strict rearrangement for decreasing A_j and increasing B_j uniquely minimizes at Q=P and maximizes at reversed order. Vandermonde gives minimum binom(a+b+q,q-1). The H_t ratio (a+t)b/((a+1)(b+t-1))>1 for b>=a+2,t>=2 proves balancing, and leading t=q summand gives k^(2q-2)/(4^(q-1)((q-1)!)²). Independent exhaustive leftmost-subsequence matching vs pivot formula for all 36 P,Q pairs with q=3,a=2,b=1 passed; these finite tests corroborate only checked parameters.

## originality

PASS

The Kosche–Koß–Manea–Siemer full primary paper already proves general arch and concatenation characterizations for SAS, including a pivot glueing Lemma 3.17 and global alternation-based extremality. The assessed contribution is an explicitly evaluated all-parameter P^aQ^b count, strict unique conditional Q extrema and balanced fixed-total phases; those precise identities do not occur in inspected §§3–4, although several proof ingredients specialize their general lemma.

## value

PASS

The exact spectrum and optimizer among a natural low-complexity word family quantify how one order switch changes absent-sequence complexity. The sharp conditional-order and balanced-phase extrema are potentially reusable benchmarks for universality/string indexing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
