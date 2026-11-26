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

Each block of q+1 positions supplies an equal pair; concatenation preserves the run condition, including when adjacent chosen runs merge. For the odd threshold, reserve a final 2q+1 positions to force a triple, and take pairs in the preceding r−1 blocks. Thus the universal lengths 2r and 2r+1 are guaranteed at (q+1)r and (q+1)r+q. In the cyclic source, greedy embeddings minimize each selected index. An LDS of length L with r maximal runs has first index of appearance 1+x₁+q(L−r)+Σδᵢ≥qL−(q−1)⌊L/2⌋. This bound is attained with initial letter 0, all jumps +1, and maximal r, including for q=2 after wraparound. The resulting thresholds invert to the stated minimum, also at n≤q. The unique run decomposition weights the first letter by Σz^j (1≤j≤q), each run by z^q y²/(1−z^q y), and each distinct-letter transition by Σz^j (1≤j<q); summing the geometric series counts words, not embeddings. Multiplication by 1/(1−z) gives cumulative counts. An independent distinct-subsequence enumeration agreed for q=2,3,4,5 over all words up to n=8,7,6,5 respectively, and checked every first-appearance length cell for these four cyclic sources through n=14.

## originality

PASS

The accessible primary LLDS papers use precisely the same admissibility definition but study optimization on a given input and related variants. The strongest indexed run and periodic deletion results concern different languages or different enumeration questions. No inspected result states or supplies the exact two claims by direct specialization.

## value

PASS

This is a natural exact worst-case benchmark for an established subsequence optimization problem. The formula resolves the parity/residue transition beyond the disjoint-pairs bound and identifies a single family of extremizers for all q and n. The rational bivariate series separately supplies the number and lengths of feasible outputs on that extremal family, rather than just the optimizer length. Both facts apply across alphabet sizes and prefix lengths, not to a sampled or arbitrary small slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
