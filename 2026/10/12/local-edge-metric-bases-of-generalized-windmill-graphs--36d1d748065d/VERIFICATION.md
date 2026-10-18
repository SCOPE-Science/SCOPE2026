---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Each spoke pair cu,cv sharing center can only be locally edge-resolved by u or v: every other vertex, including center, has the same distance to the two spokes. Therefore every generator contains at least rm-1 noncentral vertices. Conversely S equal to all noncentral vertices except w distinguishes adjacent e=pq,f=pr by a selected noncommon endpoint; the unique configuration with omitted w and center as noncommon endpoints is resolved by any selected vertex in another blade, giving edge-distances 2 and 1. Equality in lower bound rules out center and fixes all minimum sets. Independent all-subset BFS enumeration for W_(2,2), W_(2,3), W_(3,2) agrees; finite checks are supplementary.

## originality

PASS

Local edge metric dimension introduced in Adawiyah et al 2020, with paths/ladders/cycles/stars/wheels, not generalized clique-windmills. 2022 wheel-related paper lists fan and Jahangir graphs; 2024 same-parameter structural article addresses corona products. Fractional edge resolvers of friendship graphs in published Resultary use a distinct relaxation and edge metric criterion, do not determine local integral bases.

## value

PASS

Natural infinite family of clique-amalgamation graphs with friendship-graph subfamily; exact number and classification of all optimal bases is a useful structural benchmark not supplied by generic monotonicity under adding edges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
