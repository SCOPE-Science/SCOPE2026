---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For N=2p^alpha even and x=p/a of valuation one, differentiating sum_{k<=N}(X^k+(-X/(1-X))^k)/k gives X^N((1-X)^(-N-1)-(1-X)^(-1)). Coefficient integration yields [(binom(N+j,j)-1)/(N+j+1)]X^(N+j+1), j>=1. j=1 has valuation N+alpha+2 for odd p. The telescoping identity binom(N+j,j)-1=N sum_{h=1}^j binom(N+h-1,h-1)/h bounds each remaining term at N+alpha+3 or higher, including the p=3 and p=5 boundary j=3,4. A single strictly lowest p-adic term cannot cancel. Independent direct exact rational evaluation in 30 cases (p=3,5,7, alpha=1,2, signed p-units) matched. No claim for p=2 or unrestricted indices.

## originality

PASS

Best-of-knowledge new exact post-extremal valuation for Farhi complementary truncated logarithms; the full original gives a sharp lower bound and equality characterization one index earlier, not the exact value at the next index. Residual unindexed evaluation risk.

## value

PASS

The first index immediately after the sharpness indices presents a genuine cancellation spike of size 2alpha+2 relative to the preceding valuation. The exact prime-uniform evaluation is a motivated sharp boundary refinement, not a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
