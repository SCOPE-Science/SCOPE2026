---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Direct neighbor count on one clique is a−x+y and degree n. For even n=2m this gives shore update ∅ if a<m, B if a=m, U if a>m. For odd n=2m+1 it gives ∅ if a<m, B\A if a=m, (U\A)∪B if a=m+1, U if a>m+1; the other shore follows symmetrically. The all-n partition by (a,b,c=|A∩B|) isolates all primitive 2-cycles and odd one-step preperiod states; extremal shores reach fixed configurations. Combinatorics yield even C=binom(2m,m): fixed 4+C, primitive period-2 orbits (C²−C)/2, basin C²−C; odd D=binom(2m+1,m): fixed 4, primitive orbits (m+2)D, basin 2(m²+2m+2)D, preperiodic period-two states 2m(m+1)D. Explicit boundary witnesses give max transients 1 (n=2), 2 (n=3 and even n≥4), 3 (odd n≥5). Independent all-labelled-state simulation for n=2,…,8 confirms update, periods, basins and max transients; the uniform case division—not finite extrapolation—proves all n. Stirling yields the claimed exact leading parity scales.

## originality

PASS

The universal Goles–Olivos period-at-most-two theorem supplies only qualitative eventual period. It does not determine precise first-entry times or counts on K_n □ K₂. Primary papers on random/unimodular majority, information retention and static majority graph problems have different quantitative statements. No covering formula found for the graph’s two-clique, prism, crown-complement aliases; this is qualified best-of-knowledge novelty.

## value

PASS

Two highly cohesive communities coupled only by a perfect matching form a canonical regular graph family. The complete period-two orbit and attraction-basin census plus an exponential-versus-polynomial parity separation in oscillation probability is a significant dynamical distinction not predicted by eventual-period theorem alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
