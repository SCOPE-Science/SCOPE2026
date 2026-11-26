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

With gap c between c−1 and c, an even gap 2h expands each parent mirror pair into two pairs with the opposite equality status. Thus P(2h)=2A(h) and A(2h)=2P(h) at successive depths, with the factor-of-two caps consistent. At odd gaps P=0; for A the initial pair always passes, pairs two and three pass together exactly when the two parent neighbors agree, and a fourth would then force a length-five palindrome centered on the parent letter. Checking the four offsets in the periodic concatenation of 0110/1001 blocks excludes such odd palindromes, also across seams. Repeated division by two proves the valuation formula; the length-two circular word and the odd gaps of 0110 settle the capped full-axis cases. At the largest permitted odd valuation the parent tests use 0110 for even k (all four neighbor tests unequal) and 01101001 for odd k (four equal out of eight). Lower valuations cannot reach the resulting bounds. Half-circle shift complements every letter, so above twice the off-axis radius the two full gaps yield distinct complementary factors, including length N. Independent even-radius Manacher computation on the trebled word, retaining the central copy with one-circuit caps (python3 /workspace/reproduce_reviews.py 5), matched all 131056 gaps at k=4..16 and checked the seam restriction and complementary factors at both ends of the long range. The proof, not that range, covers all k≥4.

## originality

PASS

Credit prior infinite-word odd-palindrome exclusion, centered desubstitution and aggregate palindromic complexity. The supported distinct result is the complete indexed finite circular radius law with parity-dependent sharp off-axis maxima and its long-factor consequence. The checked sources do not give this position-specific finite classification; the strongest desubstitution result provides ingredients, not the evaluated capped radii and their maxima.

## value

PASS

This gives the complete reflection-radius profile of a canonical finite cyclic substitution word, not a test for one block size or an ordinary aggregate count. It separates exact full reflection, the strongest off-axis reflection, and the entire intermediate scale with simple position rules. In particular the parity-dependent extremizers and long-factor cutoff are useful exact information for comparisons of circular palindrome statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
