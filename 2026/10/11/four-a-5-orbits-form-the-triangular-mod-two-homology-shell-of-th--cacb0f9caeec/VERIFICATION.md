---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For the 30 explicit faces, the one-skeleton has all 45 edges, so the connected graph-cycle space has dimension 45-10+1=36. Independently reduced all 30 face boundaries over F2 to rank 29, giving H1 dimension 7. All 120 graph triangles were tested; 30 are faces, the other 90 reduce to 41 distinct nonzero classes with multiplicities 10x1,25x2,6x5. Independently generated the displayed A5 permutations, checked all 60 preserve faces and calculated carrier orbit sizes 20,30,30,10, image class orbit sizes 10,6,15,10 and fibers 2,5,2,1. The standalone source additionally recursively checks the FULL automorphism group, not just the supplied generators. These exhaust the relevant finite configuration, not samples.

## originality

PASS

Exact-object census and neighborly map classification give the surface/faces/group but not all ninety minimal nonfacial cycle classes, their multiplicities, nor the four carrier-to-class orbit fibers. Those derived homology data require an exhaustive quotient calculation. Old map-design sources are an explicit originality risk.

## value

PASS

For the canonical smallest A5-symmetric neighborly N7 surface, completely computes the first nontrivial mod-two length layer, its nonzero homology images and orbit-to-class fibers. This natural finite classification is a meaningful exact invariant of the named complex, not merely repeating f-vector or group census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
