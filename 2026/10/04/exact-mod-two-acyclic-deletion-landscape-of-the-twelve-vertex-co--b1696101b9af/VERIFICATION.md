---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

An independent exact replay reconstructed all faces from the frozen 38-tetrahedron facet list, enumerated all 4095 nonempty induced vertex sets, computed F2 Betti numbers by binary boundary-rank elimination, and then built the reachable acyclicity-preserving deletion DAG. It independently reproduced 585 acyclic induced subcomplexes, 134 reachable states with layers 1,11,36,52,31,3 on 12 through 7 vertices, 17 size-8 plus 3 size-7 terminals, and 532 maximal deletion paths split 292/240. The three size-7 terminals exactly match complements of Benedetti--Lutz Proposition 3.3 exceptional five-deletion sets.

## originality

PASS

Benedetti--Lutz Proposition 3.3 exhausts only the five-deletion layer needed for evasiveness and records exactly three acyclic seven-vertex exceptions plus their one-step obstruction. It does not give the full reachable DAG, the 17 earlier size-8 traps, the 134-state layer profile, or 532 maximal-chain census. The later collapsibility/discrete-Morse paper does not state this object-specific deletion landscape. Resultary exact-number and alias searches found only the candidate itself as a matching record.

## value

PASS

B12,38 is a canonical explicit collapsible-but-evasive 3-ball whose evasiveness proof is driven by homology under vertex deletion. The complete reachable acyclic-deletion landscape is therefore a motivated structural benchmark: it exposes 17 earlier terminal traps invisible in the original one-layer proof and gives exact branch/path counts useful for non-evasiveness search algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
