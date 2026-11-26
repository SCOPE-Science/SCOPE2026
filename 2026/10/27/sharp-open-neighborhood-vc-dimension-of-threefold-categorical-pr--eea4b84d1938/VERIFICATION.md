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

For open neighborhoods in exactly three categorical clique factors, an all-included trace reserves an unused symbol in each coordinate. Complements of traces are exactly unions of at most one block per coordinate equality partition. Conversely, a full union family gives a sample with distinct tuples: duplicate tuples could never be separated. The three capped cases and the unrestricted six-point case suffice by heredity. Relabeling the first six-point partition by shape and interchanging the two unrestricted remaining partitions preserves coverage; both singleton support and the candidate-count product are necessary filters. A separate insertion-based partition enumeration reproduced the capped maxima 15, 28, and 30 on 960, 43264, and 68921 triples, and found a maximum of 61 on the 27375 six-point survivors (227766 prefilter choices). Direct original-graph evaluation gave 8, 16, and 32 traces for the stated witnesses. Embedding the alphabets and permuting factors preserves these witnesses. The finite checks certify the finite kernels, not originality. The bundled verifier uses int.bit_count (Python 3.10+), despite the 3.9 wording; this does not affect the checked certificate.

## originality

PASS

The inspected closest prior results compare different trace systems or different graph invariants; none establishes or implies the three thresholds. This is a bounded best-of-knowledge judgment, not proof of historical priority.

## value

PASS

The result resolves a natural shattering invariant of standard graph products for all three alphabet sizes, not a single small graph. The three distinct alphabet regimes, exact minimal witnesses and universal finite obstruction explain why Cartesian-product conclusions cannot simply be transferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
