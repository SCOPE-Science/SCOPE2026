---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Graph definitions and all trace masks are deterministic and finite. Independently enumerated every size-1..4 support for each 16-vertex graph using separate adjacency/bit trace construction; got 16,120,288,0 for rook; 16,120,224,0 for Shrikhande; open 16,120,320,0 each. A shattered 4-set would require 16 distinct centers with 8 incidences per vertex, impossible because closed degree=7; exhaustive enumeration adds exact confirmation.

## originality

PASS

Neither general algorithm nor scalar VCdim=3 implies the differing highest coefficient; published rook result is strictly partial coverage.

## value

PASS

Complete face-count distinction for the canonical pair of nonisomorphic strongly regular (16,6,2,2) graphs is a natural exact invariant, not supplied by their shared parameters or scalar VCdimension, and can be used to compare their neighborhood range spaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
