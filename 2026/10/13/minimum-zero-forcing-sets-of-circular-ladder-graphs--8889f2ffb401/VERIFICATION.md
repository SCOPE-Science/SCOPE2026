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

Each Y_n for n>=5 is cubic and triangle-free. With three initially blue vertices, any first force must center at a blue three-vertex path; the two possible rail-rail or rail-rung local shapes stall after the force, proving Z>=4. Two adjacent complete rungs force around both rails, so Z=4. For a size-four zero forcing set choose an actual first force. A fourth initially blue vertex permitting continuation must lie at one of four local neighboring positions for each of the two first-force shapes; these cases reduce to four disjoint families: adjacent full rungs (n); full rung plus two same-rail offsets (8n); full rung plus opposite-rail adjacent neighbors (2n); four consecutive same-rail vertices (2n). Constructive forcing sequences establish sufficiency and no wraparound identifications for n>=5; total exactly 13n. An entirely independent direct color-change enumerator compared all size <=4 subsets and families on n=5..11 (65,78,91,104,117,130,143), with no mismatches.

## originality

PASS

The same family may be called prism Y_n, circular ladder or generalized Petersen P(n,1); the scalar forcing number was already known. The result instead classifies every size-four basis and counts 13n, which is absent from inspected zero-forcing polynomial, graph-class min-set and generalized-Petersen sources. Best-of-knowledge novelty with residual notation/atlas risk.

## value

PASS

This is a natural full basis classification for the prism family, central in graph zero forcing and reconfiguration: the exact 13n coefficient counts all starting sets of minimum cardinality and explicitly separates four distinct local forcing mechanisms. It goes beyond the already known scalar Z=4 and supports future study of prism basis-reconfiguration adjacency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
