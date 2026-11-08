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

For B_q with words (a,b) and directed E((a,b),(c,d)) iff b=c, a single-variable atomic type recognizes q=1 versus q≥2; a two-variable formula separates q=2 from q≥3, and the full two-pebble local response table uses only three letters and proves permanent equivalence for any q,q′≥3. For k≥3, the three-variable formulas ∃z(E(z,x)∧E(z,y)) and ∃z(E(x,z)∧E(y,z)) encode equality of first/second coordinates. By locally shadowing a third variable only inside a conjunct, k word-variables can describe all equality patterns of up to 2k alphabet positions, including an odd t with a final diagonal word, yielding separating sentences for thresholds t≤2k. Duplicator maintains the complete equality pattern of all coordinates of ≤k pebbled words for q,q′≥2k since replacing one word needs ≤2 fresh letters. Thus cutoffs are 2,3,2k and the stated distinguishing-width law follows. These are unbounded-round strategies, not finite-depth experimental extrapolation.

## originality

PASS

Qualified PASS for the exact all-k logical equivalence and minimal alphabet representatives of length-two de Bruijn digraphs; neither classical line-digraph structure nor standard pebble equivalence characterization alone states this sharp exceptional k=2 and general 2k spectrum. A broader definable-incidence/finite model theory transfer may conceal a stronger prior implication.

## value

PASS

The pure adjacency length-two de Bruijn graph is a canonical automata/network structure with q² vertices. The exact classification of all finite-variable theories, the anomalous two-variable plateau and the constructive minimal separating width provide a complete natural model-theoretic invariant, illustrating sharp expressivity costs of definable coordinates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
