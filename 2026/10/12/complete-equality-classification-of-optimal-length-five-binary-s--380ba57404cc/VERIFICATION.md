---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

A one-error Z-channel downward ball of x consists of x and words obtained by erasing one 1-bit. Two balls are disjoint if and only if asymmetric distance max(#1->0,#0->1)>=2. Reconstructed both adjacency definitions for all 32 words; independently enumerated ALL maximal cliques with a separate graph implementation and obtained maximum size 6 and exactly 120 maximum six-word codes. The S5 coordinate group plus global bit-complement acts by graph automorphisms (even though complement exchanges up/down, the symmetric max distance is invariant); exhaustive orbit calculation yields precisely three orbits of sizes 30,30,60, stabilizers 8,8,4 by 240/orbit size. Thus no unenumerated larger or six-word codes; this is finite exact graph exhaustion, not a bound from sampled constructions.

## originality

PASS

The upper bound and maximum 6 at n=5 were already tabulated by Weber et al. and OEIS A010101. Primary Weber–de Vroedt–Boekee (1988) was read in complete 11-page text through authorized institutional access and contains bound/construction methods and optimum-size tables, not an equality census. Resultary publishes the structurally related LENGTH-SIX Z-channel optimum (size12, 30 maxima), fully inspected and distinguished by underlying length; neither its result nor classical known cardinality implies this length-five 120-code orbit classification. A 1989 Weber thesis was not available and remains a specific risk.

## value

PASS

Exact equality-case classification is mathematically distinct from the known optimum number and is meaningful for small-blocklength asymmetric-channel coding: 120 labeled optima fall into three genuine equivalence types rather than a unique design. The complete finite codebook census and stabilizer data can be used as reproducible classification/baseline for constructions and automorphisms; it is a natural complete object, not an arbitrary code slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
