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

For independent fixed positive Poisson rates and n≥2, the homogeneous maximum mass factors f_k=p_b(k)H_k. Monotone log increments of the Poisson cumulative masses imply synchronized H_k log concavity; the Poisson factorial ratio converts it to all k≥1 ULC. For unequal rates, exact product-CDF telescoping yields h_k=f_k/p_b(k)=m+s·exp(b−a)(a/b)^k+o((a/b)^k) where a<b are top distinct rates. Consequently (h_k²−h_{k−1}h_{k+1})/(a/b)^k→−m s exp(b−a)(b−a)²/(ab)<0 and all sufficiently large k violate ULC. Independently recomputed exact rational Poisson CDF masses show first (1,2) violation at k=4 with scaled defect −17/360 and confirm finite homogeneous/heterogeneous samples, not substituted for proof.

## originality

PASS

Badiella–del Castillo–Puig (2023) prove preservation of ULC for independent identically distributed discrete order statistics: homogeneous sufficiency is known. Chowdhury–Kundu–Mishra (2021) compare heterogeneous Poisson order statistics by stochastic majorization, not this discrete curvature, and Yu treats distributional relative log-concavity. The novel asserted part is exact necessity for any heterogeneity plus its second-highest-rate tail constant; no covering result found in actual comparisons. Badiella full primary PDF was access-blocked, documented as residual risk, not automatically a failure.

## value

PASS

A sharp classification for arbitrary finite n of when a natural maximum retains a strong shape constraint; it identifies all heterogeneous failures and measures their eventual strict negative curvature scale. This is structurally informative beyond existing iid preservation and finite examples, with explicit limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
