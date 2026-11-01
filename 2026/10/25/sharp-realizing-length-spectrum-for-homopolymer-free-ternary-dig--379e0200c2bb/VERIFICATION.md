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

The circular word model has 6 positive pairwise distinct counts c_uv for u≠v and zero loop counts. Conservation of directed degree at each symbol forces c01−c10=c12−c21=c20−c02=δ≠0. Orient the three paired differences positively, write lower counts y=(a,a+p,a+p+q), upper counts y+d, with a,p,q,d positive integers and d not equal p,q,p+q. All 6-value increasing interleavings are the five Dyck words OCOCOC, OCOOCC, OOCCOC, OOCOCC, OOOCCC. Their strict inequality regimes yield minimal (a,p,q,d) respectively (1,2,2,1), (1,3,1,2), (1,1,3,2), (1,2,2,3), (1,1,1,3), under the exact length function 6a+4p+2q+3d, with minimal lengths 21,26,22,27,21. Each type gives 2 orientations×3! arc pair orders=12 distinct rank orders, so 60 total and min-length histogram {21:24,22:12,26:12,27:12}; worst shortest length 27. Each positive balanced multigraph is strongly connected/Eulerian and gives an actual circular homopolymer-free word. Independent six-integer count enumeration over all distinct positive vectors of sum ≤27 visited 21,600 vectors, 216 balanced, recovered 60 ranks and exact histogram; the parametric all-length proof independently excludes arbitrarily long unsearched witnesses. The coarse count 60 is prior-derived, not independently novel.

## originality

PASS

The final statement, not the title or isolated numbers, was compared against the actual prior implications and synonyms, with bounded source reading and explicit priority risks. The surviving precise assertion is not implied by the inspected sources. Best-of-knowledge PASS, not unconditional certification. Earlier rank-modulation work might contain an equivalent loop-free shortest-length table or other unstated constrained representative optimization. The inspected primary Raviv paper does not settle this per-six-ranking length spectrum; Beeri–Schwartz related material was only partially accessed, so it remains a residual priority risk.

## value

PASS

Frequency ranking of adjacent dinucleotides is a natural DNA storage model, while forbidding identical adjacent symbols is an important synthesis constraint. Beyond the already-known combinatorial feasibility count, the complete minimal loop-free realizing-length spectrum shows precisely how many cyclic positions each feasible message needs; it identifies the worst-case budget 27 and the 12 hardest rankings. A motivated exact constrained representation-cost invariant, distinct from full-nine length 86.

The dated certificate retains the supplied scientific assessment, sources and limitations.
