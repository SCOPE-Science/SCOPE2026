---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For k>=2, h=2^k-1, a binary [h,h-k,3] Hamming perfect code has a weight-three word, so its two parity classes have equal size 2^(h-k-1). Same-parity distinct codewords have distance >=4, hence their closed radius-one balls form induced h-stars. Alternating parity with the passive-fiber parity prevents cross-fiber endpoint adjacencies; the selected edge count is h*2^(d-k-1) for all d>=h, giving Q9>=224. For Q5 an independent exact maximum-clique search in the 80-edge compatibility graph, anchored at one edge by edge-transitivity, found maximum 12 and 12 anchored maximizers, hence 80 total; every optimizer is one of the 80 separately constructed 4x3-edge-star packings. Correctness does not assert Q9 optimality.

## originality

PASS

The lower bound and exact Q5 optimizer census go beyond cited hypercube data; an improved lower bound alone is not an equality formula for general dimensions. Literature and published-result searches did not reveal a prior theorem implying the complete Q5 count or this parity-lift construction. Originality is best-of-knowledge, not certified priority.

## value

PASS

Edge-open-packing number is a standard graph invariant; improving the published Q5 and Q9 bounds and completely classifying an odd-dimensional cube extremal family is an independently useful exact combinatorial fact. The induced-star parity mechanism is a nontrivial structural construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
