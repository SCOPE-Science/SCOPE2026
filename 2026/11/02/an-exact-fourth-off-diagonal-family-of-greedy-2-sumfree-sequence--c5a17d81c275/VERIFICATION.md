---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Candidate intervals are disjoint for f>=8; distinct-pair interval sumsets reduce greedy membership to exact cover/disjointness. The 57-component, 1640-sum affine interval verifier compares endpoint slopes and shifted intercepts: no crossings after f=14, and checks f=8..15; this is a legitimate all-f certificate, not finite extrapolation. Four repeated nonempty 3M-blocks from the certified prefix invoke van Berkel--Bosma Theorem 15 to extend indefinitely. A distinct-gap-size argument rules out a shorter tail period, and the last transient gap proves exact preperiod. Independently computed 250 greedy terms for each f=8..19. Reliance on the published four-block theorem was checked for stated hypotheses in RESULT.md, but the primary paper theorem proof was not available in full this run.

## originality

PASS

Theorem is an additional natural fourth off-diagonal g=2f+4, rather than a renaming of earlier g<=2f or first three off-diagonal identities. Best-of-knowledge originality is qualified because the 2026 primary theorem text could not be retrieved for full inspection; indexed primary abstract frames full periodicity as conjectural, and published Resultary findings cover earlier diagonals only.

## value

PASS

Exact infinite-parameter family advances a specifically conjectured periodicity program, giving full term membership and sharp period/preperiod rather than a bounded computation. A uniform affine-interval certificate is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
