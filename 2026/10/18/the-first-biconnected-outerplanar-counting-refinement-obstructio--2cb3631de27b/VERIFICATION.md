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
# Verification record

The complete universe consists of connected outerplanar simple graphs of orders one through eight. The first source program enumerates all seven-vertex nonisomorphic connected outerplanar graphs from the complete graph atlas, applies all degree-one and degree-two attachments, filters by the apex-planarity condition, and verifies all automorphism orbits by exact isomorphism enumeration. The second begins with every 7-vertex connected atlas graph (853), augments by every nonempty neighbour set (108331 possible labeled inputs), deduplicates the 5841 planar-positive inputs into 777 isomorphism classes, and tests orbit membership by uniquely marking two candidate vertices and asking whether the marked graphs are isomorphic.

The outputs `ear_output.json` and `all_attach_output.json` were produced by executing their accompanying scripts under NetworkX 3.6.1. They record the accepted graph counts, exception counts and structural signatures. `witness_catalog.json` gives the exact edge sets and the stable and orbit partitions of each exception. They establish a finite, exhaustive census only because the graph-generation completeness arguments hold. NetworkX's atlas and planarity functionality are shared dependencies, not independent mathematical certificates. The proof of the universal finite cutoff is conditional on the correctness of the executable enumeration and the stated standard graph-theoretic reductions. No extrapolation to orders exceeding eight or independent scientific audit is claimed.
