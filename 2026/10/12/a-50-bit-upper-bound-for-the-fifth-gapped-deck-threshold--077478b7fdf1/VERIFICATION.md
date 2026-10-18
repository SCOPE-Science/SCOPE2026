---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For the two displayed distinct length-50 binary words u=0xy1 and v=0yx1, independent exact prefix-DP and independently enumerated nonadjacent index-tuples give the same multiplicity for all 62 binary patterns of lengths 1..5, with zero mismatches; common totals are 50, 1176, 17296, 178365, 1370754 by length. The required convention is index gaps >=2. The words are different, so this is an explicit collision and proves the finite upper bound G(5)<=50 without claiming minimality.

## originality

PASS

Golm–Nahvi–Gabrys–Milenkovic gave G(2)=6, G(3)=13, G(4)=24 and their general bound gives G(5)<=122. Rigo–Stipulanti–Whiteland (2023) treat gapped-binomial equivalence/infinite-word complexities and do not supply this finite order-five witness in material inspected. A targeted published-findings semantic search for the same threshold did not find a covering result. Original 2022 full PDF unavailable on attempted arXiv download; originality is best-of-knowledge, not a claimed negative full-document inspection.

## value

PASS

G(5) is the first unresolved finite binary gapped-deck threshold after exact k<=4 values. An explicit order-five collision cuts a genuinely central finite upper bound from 122 to 50, with two exact independent finite verification procedures, without claiming an exact G(5).

The dated certificate retains the supplied scientific assessment, sources and limitations.
