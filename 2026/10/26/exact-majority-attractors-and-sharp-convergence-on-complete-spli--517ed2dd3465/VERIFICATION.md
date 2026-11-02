---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

At a state with c clique and l periphery ones, total s=c+l, clique updates all 0 or all 1 depending on 2s<N or >N, and complements precisely at 2s=N; periphery updates 0, unchanged or 1 according to 2c<a,=a,>a. For recurrent mixed clique, total balance forces complementary clique each step. Its independent part is fixed if a,b both even and c=a/2,l=b/2 (H) or switches all-zero/all-one for a>b matching parity (J). Monochromatic clique yields two consensus fixed and the anti-aligned 2-cycle iff b>=a. The balanced/unbalanced case split proves all states enter 2-cycles within 3 rounds, sharp iff an integer c lies strictly between (a-b)/2 and a/2. Direct graph-neighbor bit-level enumeration verified 71 eligible parameter pairs a+b<=14.

## originality

PASS

Goles--Olivos qualitative period <=2 applies to every symmetric threshold graph, so this aspect alone is prior. Benjamini et al explain general convergence, and Turau 2022 gives exact counts for trees. The complete split graph two-parameter binomial census plus F^5=F^3 sharpness is not provided by these general results or tree special cases; unindexed complete multipartite majority variants remain a risk.

## value

PASS

The dense core-periphery split family is natural for opinion dynamics. The exact recurrent-state counts separate balanced even sizes, with exponentially many oscillatory states, from balanced odd sizes with only four periodic states. The three-step sharp bound is much stronger than general eventual-period-two and identifies a precise parity/imbalance boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
