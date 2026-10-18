---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

H_n uses a involutive swap of 1,n and b with collision {2,n}. b is the sole rank-reducing letter. Every b omits n; to make a later b effective, a must restore n from state 1, forcing state 1 then absent and the previous b to leave both 2,n absent; another drop after the second requires b to restore 2, then a to restore n, then effective b. Thus initial b followed by the minimal ab and thereafter bab blocks gives length 3s−3 for s≥2, with rigid unique equality word (bab)^(s−1). Inducting the holes {n,2,4,...,2r}, including the even-n n↔1 transition, yields h=floor(n/2)+1 and saturation immediately after. Independent subset BFS n4..13 checked uniqueness and the next deficiency; packaged verifier BFS n4..14 and replay to 300 was source-read, not assumed sufficient for all n.

## originality

PASS

Best-of-knowledge PASS: AGV 2013 full Section 4.2 proves full reset length via a different reduction and names H_n, but not the unique shortest intermediate-rank words or first saturation. AGV 2010 only previews an unnamed related family. General synchronizing-length results do not entail this detailed profile. Residual risk of differently named rank profiles persists.

## value

PASS

Exact parameter-wide high-rank metric and uniquely forced words in a celebrated extremal automaton family, with a sharp n-parity hole-saturation transition. This structural bottleneck is not routine consequence of the known final reset length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
