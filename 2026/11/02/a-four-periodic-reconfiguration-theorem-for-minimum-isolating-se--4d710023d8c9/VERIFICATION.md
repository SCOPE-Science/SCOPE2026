---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

An edge survives N[S] precisely for four consecutive unselected cycle vertices, so cyclic selected gaps are <=4. Minimum k=ceil(n/4), deficits ai=4-di sum r in {0,1,2,3}; count distinguished minima by weak compositions. Deleting x merges adjacent gaps to L=8-a_minus-a_plus>=5, valid insertions at 9-L positions including x; degree=2r. Deficit-unit exchanges connect all weak compositions and wind a unit around all gaps to translate every selected vertex by one, establishing global labelled connectedness. r=0 and n=4 boundaries separated. Independent direct-definition enumeration and BFS checked n=4..15.

## originality

PASS

Best-of-knowledge comparison of exact mathematical implications, including stronger prior results and aliases. The reviewed additional conclusion is not established by the primary/public mathematical results actually inspected; stated access and historical risks are retained.

## value

PASS

The exact number, all-exchange regularity and four-periodic connectedness of globally minimum isolating configurations is a natural complete reconfiguration classification, not implied by the known isolation number; explicit solution graphs permit further mixing and mobility investigations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
