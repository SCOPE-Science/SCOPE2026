---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The graph predicate on all 2^21 labeled seven-vertex graphs is tested by all domination sets of sizes 1,2,3. Re-execution of the inspected artifacts/verify.py returned VERIFY_OK: face-size histogram (1,21,210,1330,4515,7077,3605,630), 17388 nonempty faces, 83895 full Hasse covers; sequential toggle 8210 disjoint pairs and a full topological sort give acyclic critical cells (1 in dim0,847 dim4,120 dim5). Integer Morse boundary has exact rank 36 and a displayed 36x36 determinant -1. Therefore all 36 nonzero Smith invariants are units; the 4-skeleton is simply-connected wedge S4 and Hurewicz/elementary CW cancellations give 811 S4 and84 S5. F2 chain ranks independently in verifier are consistent, not standalone wedge proof.

## originality

PASS

Published all-n theorem applies to D_{n,n-2}; this instance D_{7,4} has k=n-3. Published exact D_{6,3} is a different labelled complex and does not determine seven-vertex Morse boundary or homotopy; an independent complete finite certificate addresses a natural next member of the filtration.

## value

PASS

D7,4 is the next natural seven-vertex n−3 bounded-domination complex beyond the published D6,3 mixed wedge, directly within the authors’ open all-Dn,k wedge problem. Its exact finite homotopy is a motivated nontrivial case and determines integral attaching information a dimension/census cannot supply; finite does not reduce its value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
