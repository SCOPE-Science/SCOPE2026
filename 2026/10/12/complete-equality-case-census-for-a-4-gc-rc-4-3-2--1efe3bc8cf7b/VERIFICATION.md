---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Single-codeword self reverse-complement feasibility leaves 72 of the C(4,2)*2^4=96 GC2 words. Independent direct distance construction gave 1168 compatibility edges, and a complete pivoted Bron-Kerbosch maximal-clique enumeration yielded size histogram 2:64,4:640,5:1024,6:512. A second direct check of every six-clique independently confirmed self RC distance 4, three disjoint pairwise distance-(4,4) edges forming a perfect matching, and other 12 pairs distance-(3,3). Explicitly generated the coordinate reversal centralizer of order 8 and alphabet Watson-Crick centralizer of order 8 and checked their 64 transformations on every maximum, giving orbit sizes 32x12 and 64x2. This finite graph enumerates all admissible codewords and all feasible codebooks; King provides prior optimum 6.

## originality

PASS

Compared the same objects and implications with primary prior literature and published research search. Prior optimal values or constructions are fully credited; no inspected stronger theorem implies the final complete classification. This is a best-of-knowledge determination, with the explicitly recorded unread-source risks.

## value

PASS

The exact equality layer of a standard DNA-code packing optimum is a natural complete classification: 512 optimal books, a rigid universal three-pair matching distance structure, and a specific symmetry orbit decomposition. Those structural restrictions matter when choosing inequivalent constant-GC code designs and do not follow mechanically from upper-bound value 6.

The dated certificate retains the supplied scientific assessment, sources and limitations.
