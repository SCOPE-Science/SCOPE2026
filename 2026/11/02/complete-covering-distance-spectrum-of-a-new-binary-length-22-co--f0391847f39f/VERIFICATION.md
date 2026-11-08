---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The actual complete codewords.txt list contains 84 distinct integers in [0,2^22), with minimum pairwise Hamming distance exactly 9. For each x in 0,...,2^22-1 the minimum of popcount(x xor c) over all 84 codewords determines exact distance; an independent full C++ enumeration over all 4,194,304 ambient words reproduced buckets N0..8=(84,1848,19404,129360,614460,1712308,1566756,149908,176), with all other buckets zero, integer distance moment 21899416, radius 8, first deep hole x=78501, and mean 2737427/524288. The source also provides a logically independent 22-cube BFS crosscheck; its code was inspected but not independently executed in this run. This is exhaustive finite proof for the specific supplied code, no extrapolation.

## originality

PASS

Ota–Osa–Harada arxiv:2610.11609v1 publish this exact (22,84,9) list for improved maximal-code-size bounds; their construction and min distance are prior. The open complete article and its embedded 84-word list were inspected; no all-ambient covering-distance distribution, radius-eight statement or number of 176 deepest holes appears. Minimum pairwise distance nine and 84 words do not determine the covering profile without examining spatial placement; independent full enumeration produces a distinct natural metric statistic. Exact Resultary queries found no duplicate, but historical unindexed computations remain possible.

## value

PASS

Covering radius and complete nearest-codeword-distance distribution are canonical decoding-geometric invariants of a named finite code, distinct from packing/minimum-distance parameters used to introduce the 84-word construction. The exact number of deepest holes and mean distance are mathematically useful for evaluating the construction even without new size optimality. A whole-cube exhaustive result is a meaningful motivated finite classification rather than arbitrary subsampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
