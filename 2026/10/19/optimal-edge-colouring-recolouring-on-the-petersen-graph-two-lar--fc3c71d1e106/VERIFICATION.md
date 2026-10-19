---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite verification

Use Python 3 and only its standard library, starting in the directory containing this file:

```sh
python3 repro/verify_gp.py
python3 repro/verify_kneser.py
```

The first construction uses fifteen prescribed edges in GP(5,2); the second builds KG(5,2) as the disjointness graph of two-subsets of a five-set. A direct isomorphism between these presentations is given in RESULT.md.

The first program recursively enumerates all legal assignments and constructs all single-edge legal transitions from the four conflicts of each edge. It verifies 49,920 states, 109,440 undirected transitions, 962 components, component-size histogram [(1,960),(24480,2)], and the full state-degree histogram. The second program uses independently written bitmask assignment and recolouring algorithms, obtains the same counts, computes missing-colour degree statistics, enumerates the 120 natural graph symmetries and 24 palette symmetries, verifies one 960-state orbit of frozen colourings and checks that even/odd natural graph symmetries act respectively within/across the two large components.

The checked terminal token of each run is `VERIFY_OK`; captured outputs are stored alongside the scripts. The transition graph is finite and every assignment is generated without heuristic omissions. Neither program proves anything about larger graphs or recolouring with five or more colours. The already known count of proper four-edge-colourings is corroborated by OEIS A159233. Independent external audit remains unperformed.
