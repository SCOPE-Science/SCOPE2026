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

Writing n_i=1+y_i with sum y_i=r gives fixed-total Berger-Parker order by M=max y_i and Simpson order by Q=sum y_i^2. For fixed r and smaller maximum m, Q is at most floor(r/m)m^2+(r mod m)^2, while with larger maximum m′ it is at least m′^2+(r-m′); direct finite algebra check for every r<=7 and m<m′ ensures no opposite order. Independent partition generator (not package verifier) exhaustively found strict-reversal counts 0 through r=7 and four at r=8. Four explicitly listed partitions have maximum-coordinate versus sum-of-squares reversal. At k>=3 excess (1,2,5) vs (4,4) yields (2,3,6) vs (1,5,5), M=5>4 but Q=30<32; k-padding preserves both. Four types require 6,5,4,3 nonzero coordinates, giving 1,2,3,4 for increasing richness. Two shares p>=1/2 have p and p²+(1-p)² monotone, proving all N nonreversal at k=2. Finite-sample Simpson is fixed-total affine transform and retains ranking.

## originality

PASS

The measures and qualitative non-equivalence are classical; the fully quantified sharp positive-integer excess threshold and four-type first-layer census are not consequences of the examined ecological index definitions or qualitative ranking comparisons. Full relevant ecological source text was read; this is a best-of-knowledge assessment with the identified residual unindexed-example risk.

## value

PASS

Berger-Parker and Simpson are natural, widely used indices; exact minimal integer resolution at which they induce opposite strict comparisons under controlled richness and total is a meaningful sampling-design boundary. The all-k theorem and full first-layer classification are genuine finite extremal results, not merely a numerical sample: a researcher deciding when discordance is combinatorially possible can use the precise k+8 threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
