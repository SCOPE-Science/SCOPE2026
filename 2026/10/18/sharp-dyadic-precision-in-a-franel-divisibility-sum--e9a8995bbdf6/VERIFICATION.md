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

Guo’s exact transformed quotient sum has terms T_(n,j) with v2(T_(n,j))=2j−3+v2(j)+s2(j)+3s2(n−j)−s2(3n−2j). At n=2^r binary complementation yields 2r+2j−2−s2(j−1) for j≤n/2, with the unique minimum 2r at j=1. For j>n/2 the factor 4^j and integral multinomial bound every term strictly above 2r, including explicit r=2 endpoints; no cancellation is possible. Since v2(n binom(2n,n))=r+1, v2(S)=3r+1. Independently computed direct Franel sums n=4,8,16,32,64,128,256 and checked both S and quotient valuations. S2=0 and r=1 are correctly excluded.

## originality

PASS

Best-of-knowledge originality passes for the precise contribution, with prior shared lemmas and coarser theorems expressly excluded and access limitations retained. The four independent statement-implication comparisons below were performed against Resultary and the specified primary sources.

## value

PASS

Exact 2-adic precision at n=2^r sharpens Guo’s uniform divisibility by 2r valuation units and locates the unique dominant transformed summand. The natural powers-of-two boundary in a named Franel congruence is motivated and mathematically informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
