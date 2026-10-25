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

For cubic M_n on 2n vertices n>=3, the complement bits in a twisted two-row ladder satisfy two exact local inequalities a_r+c_r+b_{1−r}<=1+b_r, encoding both 1-limited and domination conditions. The 16-state weighted transfer T(u) with row-swap S counts labelled allowed complements as tr(T(u)^nS). Its 10- and 6-dimensional ± blocks have the displayed exact integer polynomial determinant identities, with trace–log giving every coefficient of the closed generating function. Counting edges in the cut gives |D|>=n. Extracting constant and linear terms in z gives min n if 4|n else n+1, with multiplicities 4,2n (n≡2 mod4),3n (n odd). Independently brute-enumerated all labelled subsets for n=3,...,8: predicted minima/multiplicities (4,9),(4,4),(6,15),(7,12),(8,21),(8,4); the unbounded result depends on the symbolic transfer argument, not finite sampling.

## originality

PASS

Radić–Tepeh's exact Goldberg-snark work and general cubic complexity results do not subsume Möbius ladder all-cardinality polynomial; Tepeh's Cartesian-product results apply to untwisted products rather than antipodal cycle twists. Published (1,2)-domination bounds establish at most coarse minimum constraints, not the twisted 16-state characteristic determinants or all coefficients; known results on other cubic graph families give no implication of this recurrence. Priority is best-of-knowledge; accessible primary material and finite indexed Resultary results cannot establish exhaustive noncoverage.

## value

PASS

A complete cardinality polynomial and sharp mod-four minimum-multiplicity classification for the natural twisted cubic Möbius ladder family answer a graph-domination structural question beyond the existing half-order bound; the twist changes the transfer boundary and is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
