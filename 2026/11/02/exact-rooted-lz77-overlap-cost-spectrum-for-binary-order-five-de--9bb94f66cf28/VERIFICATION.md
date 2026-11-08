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

PASS: Every 32-state de Bruijn successor permutation is encoded by exactly 16 binary local switches t_x, since predecessor/successor balancing at each 4-bit suffix forces a bijection (0,x),(1,x) to (x,0),(x,1). The one-orbit condition enumerates all binary order-five cyclic words without rotation duplicates via their unique 00000 state. The greedy LPF matching definitions for overlapping and disjoint-source LZ77 are explicit and exhaustive over all earlier source positions, with end boundary truncation. A fresh independent implementation enumerated all 65,536 switch settings, selected exactly 2,048 cycles, all 32 roots, and recomputed both parsing counts directly; it reproduced all 24 nonzero joint cells, gap counts (8848,20732,20334,11878,3468,268,8) for gains 0..6, and eight per-cycle gain-range cells, total 65,536 roots. The supplied checker also provides independent Euler-tour and suffix-LCP checks, whose code was inspected. This is a complete finite census, not a sample; the theorem makes no claim for higher de Bruijn orders or other LZ conventions.

## originality

PASS

PASS (qualified): The exact rooted order-five two-parser joint table and per-necklace gain extrema are not given by the general LZ-versus-nonoverlap inequality, efficient parsing algorithms or de Bruijn concatenation compression results reviewed. Kosolobov–Shur's all-string z≤novLZ is expressly old. Small alphabet exact tables can exist unindexed, so absence in semantic Resultary and current primary sources is evidence of bounded comparison, not priority certification.

## value

PASS

PASS: Greedy LZ77 source-overlap behavior on the natural finite class of all binary order-five de Bruijn cycles is an exact, full, reproducible compression-invariant classification rather than an arbitrarily sampled word. Root selection changes both parsings substantially, and the sharp six-phrase benefit, all 24 joint cells and exact per-necklace root robust benefit are meaningful reusable benchmarks for cyclic parsing. Its finite scope is openly stated; no extrapolation to order six.

The dated certificate retains the supplied scientific assessment, sources and limitations.
