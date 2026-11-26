---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A covering walk cannot revisit a strong component, so all intercomponent arcs must form a single directed path of components with exactly one actual arc per step. Conversely one can cover the edges within each strong component between its entry and exit. On at most three vertices a single strong component has imbalances of magnitude at most one; if there are multiple components, each is internally balanced and only the end components contribute uncancelled transition imbalances. In particular any intermediate component must be a singleton. The resulting Euler trail attains |E|+1. The independent weak-connectivity/imbalance census over all 512 masks and exact-length walk-state calculation agree with the polynomial and the 13 acyclic supports. The all-length result follows symbolically: repeat an available loop, extend the trail arbitrarily at a strongly connected terminal vertex, or pad at the cyclic end of the only remaining case, a reciprocal pair attached to a singleton by a single arc. Complete support forces the sharp threshold of ten. In the four-letter example imbalance (+2,-2,0,0) rules out length seven and the displayed eight-letter word realizes exactly the six arcs.

## originality

PASS

The distinct contribution is the exact presence-only ternary classification, sharp lossless alphabet boundary and length stabilization. Edge-cover walks in de Bruijn graphs and the general shortest-string optimization problem are already known. The closest records have different observations: cyclic or linear multiplicity matrices, sometimes with endpoints forgotten or a run restriction.

## value

PASS

Presence-only adjacent factors are a natural information loss relative to multiplicity profiles and define an exact shortest-representative problem. The result identifies where repetitions can first be forced, classifies all ternary observations and all attainable lengths, and provides a sharp finite threshold. The structural boundary and complete attainable-length invariant make the small-alphabet census useful beyond a standalone count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
