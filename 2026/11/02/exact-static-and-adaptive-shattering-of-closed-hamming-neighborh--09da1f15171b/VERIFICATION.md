---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Geometry of two distinct closed radius-one balls gives overlap a whole coordinate line for centers at distance 1, two recombinations at distance 2, empty beyond. For four shattered queries the all-1 and each single-0 center would force every three-query subset into the same coordinate line, contradicting an exact 2+2 trace, so VC≤3. Positive branch of any first online query has Ldim≤2 because every subsequent positive center restriction is line / 2-point / empty, giving Ldim≤3. Copies of H(3,2) or H(2,4) shatter three fixed queries, and explicit complete ternary rook depth-three tree witnesses gap; d=1 and (2,2) direct. Independent brute force static+adaptive for nine representative pairs reproduced all claims and exceptional values. Induced-class restriction cannot increase either dimension.

## originality

PASS

Adler–Benediktsson–Macpherson prove open-neighborhood Hamming VC results and a general bound for closed, not these exact closed parameter-by-parameter VC/Ldim formulae. Bhaskar gives general thicket theory, not the exact q-ary geometry. Published semantic search yielded no covering identity.

## value

PASS

This is an exact two-parameter infinite classification of offline and online complexity for canonical metric balls; a unique strict gap at the ternary 3x3 rook graph is a meaningful structural boundary, with an inherited universal upper bound for all induced Hamming subgraphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
