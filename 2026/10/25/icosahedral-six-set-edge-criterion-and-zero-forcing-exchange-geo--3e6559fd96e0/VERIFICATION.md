---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For the explicitly labeled 12-vertex 5-regular icosahedron, a <=5 initial set cannot force: any possible first force from a five-set makes a six-vertex closed neighbourhood with no further force. Independently enumerated all 4096 masks with a separate synchronous forcing implementation, obtaining 200 minimal six-sets, exactly those with 8 or 9 induced edges; polynomial (200,480,450,220,66,12,1) in degrees 6..12. Constructed the 200-vertex token-exchange graph by one-out/one-in operations, verified 1320 edges and all 200 BFS eccentricities 6 with exact pair distances (1320,5160,6300,5010,2010,100). Finite exhaustive proof applies to this graph alone. Source verify.py also gives 18 complete orbits under 120 automorphisms.

## originality

PASS

The exact six-set edge condition, full polynomial and exact exchange-graph metric are not implied by the general zero-forcing polynomial or reconfiguration definitions in the inspected antecedents. No matching published record was found; an unindexed graph table remains possible.

## value

PASS

The icosahedron is a canonical vertex-transitive 5-regular graph. The complete minimum-set classification and exchange distance distribution give a naturally reusable precise reconfiguration benchmark, more than an arbitrary small-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
