---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

An independent dominating set of central graph C(G) intersects original vertices in a clique I of G; triangle-free implies |I|≤2. Each subdivision vertex s_uv is forced in exactly when neither u nor v lies in I, giving the unique set S(I). For δ(G)≥2, all three clique types I=empty, singleton and edge dominate every original outside vertex: for singleton v, neighbors have another incident edge; for adjacent pair u,v, every outside w is not adjacent to at least one of u,v by triangle-freeness. Thus D_i(C(G),z)=z^m+sum_v z^(m−d(v)+1)+sum_uv z^(m−d(u)−d(v)+3). Min edge exponent m+3−max_uv(d(u)+d(v)) dominates singleton exponents; ties counted by edge maxima plus vertices of degree M−2. Independent direct central-graph brute-force computation confirmed both six-vertex same-degree-sequence examples, yielding z^7+6z^6+6z^5+z^4 and z^7+5z^6+8z^5; inspected provided exhaustive 560 labeled graphs n4..6. Formula covers disconnected triangle-free δ≥2 graphs, with labelled independent dominating sets counted as distinct.

## originality

PASS

Qualified best-of-knowledge PASS for the complete independent-domination polynomial and multiplicity formula, NOT for the minimum i(C(G)) which was already published exactly in Cabrera-Martínez et al. 2026 Theorem 2.2. Their Theorem 2.1 supplies a general clique-minimum framework but does not explicitly determine every enumerator coefficient or show unique maximal independent sets for the entire triangle-free δ≥2 class. The new enumerator is a relatively direct strengthening and modest in novelty, but a natural complete invariant. Accessible complete 13-page primary paper inspected.

## value

PASS

Computing the entire size distribution and minimum-set multiplicity for independent dominating sets of a natural graph operator is a complete closed polynomial invariant of a whole graph class, not just a minimum. Explicit same-degree-sequence graphs have different polynomials, showing the enumerator captures edge degree-assortativity that a degree list misses. Prior minimum-only formula is credited and not used to inflate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
