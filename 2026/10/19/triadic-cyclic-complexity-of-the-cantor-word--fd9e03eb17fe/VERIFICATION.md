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

For N=3^k, write W=μ^k(1). It is palindromic with endpoint ones, and distinct W blocks in C=μ^k(C) have at least one whole zero block between them because C has no consecutive ones. A length-N window therefore has ones from at most one W and is either all zero or a zero-padded prefix or suffix of W (including the whole W). Every needed representative is realized inside μ^k(010)=0^N W 0^N, since 010 occurs. At positive weight j the zero-padded prefixes all yield the same necklace and the suffixes give its reversal. With zero-based positions p_i of the ones, the internal gap p_(i+1)−p_i is 2·3^r−2(1+3+⋯+3^(r−1))=3^r+1 with r=v_2(i), by the binary-to-ternary digit carry. Every internal gap is even, while the circular closing gap N−p_j is positive and odd. Thus a rotation identifying a necklace with its reversal must align that unique closing gap, equivalently reverse the internal gap list onto itself. For j=2^a the valuation list is symmetric under i↦j−i. Otherwise, for j>1, the unique largest internal gap occurs at i equal to the largest power of two at most j−1. A palindrome would put that gap at i=j/2, forcing j to be a power of two. The empty internal list at j=1 is symmetric, including k=0. This gives one all-zero class, two candidates at each positive weight and exactly k+1 identifications, for 2^(k+1)−k.

## originality

PASS

The supported distinct claim is the triadic cyclic class count refined by weight and the exact palindrome criterion on the gap lists. The closest same-word results cover other equivalence relations or require a whole cyclic class rather than an occurring representative. The judgment concerns the inspected evidence, not exhaustive publication priority.

## value

PASS

The scale 3^k is intrinsic to the substitution, not an arbitrary slice. The result settles a natural cyclic invariant at every such scale, quantifies how far it is from the abelian count, and gives a structural criterion identifying exactly the weights with one rather than two necklaces. The marked-gap technique explains the counting law rather than just listing computed values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
