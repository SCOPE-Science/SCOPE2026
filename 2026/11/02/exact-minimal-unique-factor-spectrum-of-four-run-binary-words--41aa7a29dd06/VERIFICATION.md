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

For W=0^a1^b0^c1^d with all four runs positive, the descending digram 10 appears once, and any longer factor containing 10 cannot be minimally unique. Every remaining factor is either unary or 0^i1^j. Unary occurrence formulas yield precisely the unequal longest 0/1 runs; two 01 transition boundaries yield candidate extensions exactly when |a-c|>=2 or |b-d|>=2, with no mixed i,j>=2 candidate. This exhaustively proves five possible MUFs and count 1+1_{a!=c}+1_{b!=d}+1_{|a-c|>=2}+1_{|b-d|>=2}. Independent literal overlapping factor enumeration verified full predicted factor set for all 4^4=256 run-length quadruples a,b,c,d<=4. The independent-pair enumerator P(z,t) yields bivariate F=2tP², sharp max min(5,n-3) and first five at n=8; finite tests are corroboration only.

## originality

PASS

MFCS 2016 Mieno–Inenaga–Bannai–Takeda establish generic upper 2r-1 for r-run strings (7 when r=4) plus pure long-run MUS lemma and algorithms. Their general bound and algorithm do not imply as an explicit theorem the specialized complete binary alternating-four-run five-factor classification, length/count generating function or extremizer distribution. Sliding-window and BWT enumeration papers give algorithmic access to instances but not the displayed rational infinite-family enumerator, in inspected material.

## value

PASS

Four alternating binary runs form the first case with repeated increasing boundary 01 and unique decreasing boundary 10. Exact structural spectrum and joint length/count enumeration sharpen the generic 7 factor bound to 5 and supply a motivated test family for unique-substring behavior; a natural complete classification rather than a random finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
