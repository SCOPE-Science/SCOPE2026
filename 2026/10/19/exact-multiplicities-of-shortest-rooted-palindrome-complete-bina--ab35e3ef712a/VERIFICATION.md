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

The cyclic factor sequence is a closed walk on (k−1)-bit de Bruijn vertices; placing its 0^k edge first fixes the required prefix. In the frozen BFS each continuation has one edge word and unique state path of suffix and seen-palindrome mask. The shortest-distance layer recurrence adds all arrivals at the same minimum length and cannot double-count a rooted string. For an independent exact check, choose one occurrence of each compulsory edge in any covering walk. Their cyclic order gives a tour whose costs, one compulsory edge plus the shortest de Bruijn connector, total at most the walk's length; conversely any such tour realizes a covering walk. Connector length is k−1 minus the maximal suffix-prefix overlap of the adjacent vertices. Held–Karp therefore certifies the minimum length. The independent counter does not use optimal-tour multiplicities: it fixes the first k zeros, counts all free suffixes of that minimum length by a layered suffix/mask DP, then appends the k−1 fixed leading zeros to account for precisely the windows across the join. A fixed state after t free bits has at most 2^max(0,t−(k−1)) contributing prefixes, at most 2^59 here, so the nonnegative uint64 state additions are exact; the final sum uses unbounded integers. The independent run returned CHECK_OK and (L_k,R_k)=(4,1),(8,2),(12,2),(22,8),(32,40),(60,6272),(74,768). The equality of the two frozen algorithms' output counts is not assumed to make every optimal tour a unique word.

## originality

PASS

The supported distinct claim is the census of shortest cyclic words with an all-zero window fixed at the first position, especially R_7=6272 and R_8=768. This is not a claim to have first tabulated the matching linear lengths or to introduce de Bruijn or overlap methods. The closest exact ordinary cyclic overlap is order three and is documented with its normalization; it does not cover the larger counts.

## value

PASS

Fixed-length palindrome coverage is a natural constrained de Bruijn problem and the minimum length alone cannot distinguish a rigid optimum from a family with many optimal covers. Counting those covers under a uniform rooting convention captures that distinction. Orders 7 and 8 have the same number of required patterns yet the number of optimal rooted covers drops by more than a factor of eight, a concrete comparison unavailable from the linear tables or the length optimum. The exact finite sweep goes through both sixteen-pattern orders and is useful on its own as an enumeration benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
