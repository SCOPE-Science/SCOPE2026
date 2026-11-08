---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Full 3-deck compresses to four invariants (z,U,V,Q). Equal z,U,V implies zero-gap difference (-t,3t,-3t,t) and Q equality forces c-b=3t, giving unique involutive collision partner and no classes of size above two. Orienting b<c counts one pair for each t≥1,u,b,d≥0, z=4t+u+2b+d, proving generating function x^4/((1-x)^2(1-x^2)(1-x^4)). Independent literal subsequence counting for z=0..9 reproduced Pz=0,0,0,0,1,2,4,6,10,14. Infinite result follows algebraically.

## originality

PASS

Best-of-knowledge originality after primary-literature and published-record comparison; limited access and substantive priority risks explicitly recorded. 

## value

PASS

Exact all-length fiber classification and a rational collision enumerator for a canonical constant-weight slice of the reconstruction problem; known finite collisions and general compression do not mechanically give these fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
