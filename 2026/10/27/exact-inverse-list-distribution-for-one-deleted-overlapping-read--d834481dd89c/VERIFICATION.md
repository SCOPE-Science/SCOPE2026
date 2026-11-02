---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For q>=2, ell>=2, n>=ell+1, deletion removes one ordered overlapping whole ell-mer, not a source symbol. A consistent received vector determines a unique length-n−1 z. Boundary reinsertion yields q left and q right parent words, with a single overlap iff z is constant. Inserting an interior ell-mer into consistent adjacency forces its length ell−1 prefix and suffix to coincide, hence it is a constant word; each strictly interior maximal constant run of length>=ell−1 contributes exactly one additional distinct parent and boundary-touching runs contribute none beyond the 2q boundary words. Therefore the consistent lists have sizes 2q−1 (constant) or 2q+J_{ell−1}(z). A single deleted read can produce inconsistency at only one adjacency, forcing the inserted read uniquely; attainable inconsistent y have one parent. Packing disjoint interior runs gives sharp max 2q+floor((n−3)/(ell−1)). Decomposing z into two boundary runs and a marked sequence of interior runs yields the stated rational F(t); counting distinct read-deletion outputs by maximal runs of identical original reads, and subtracting consistent parent incidences, proves the exact H formula for inconsistent receivers. Independent enumerations of source words/receivers for five parameter triples verified each positive parent-list size and all sample maxima. The argument specifies empty sums and n=ell+1 boundary.

## originality

PASS

Best-of-knowledge statement-level primary-literature comparison: the identified antecedents cover qualitative mechanisms, methods or partial counts but no inspected theorem implies the precise assessed evaluated claim; limitations and possible older equivalents remain explicit. Whole-read deletion of the ordered unpadded ell-mer vector differs from deleting one source symbol, adapter-protected endpoints, composition-valued nanopore data, or transposition/duplication. The local periodicity mechanism is shared, but boundary multiplicities change with adapters.

## value

PASS

This is a complete exact inverse-list size distribution for a natural unpadded sliding-window deletion channel, including unique-decoding receivers and maximum ambiguity, not just a small experiment. The run formulation and rational generating function give directly reusable combinatorial data for channel decoding/list-size bounds. Difference from adapter-protected reads is mathematically consequential at boundary insertions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
