---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The edge-distance graph is L(F_r): 2r spokes form a clique and rim z_i meets only its two spokes. Twin spokes force one spoke landmark per page, and two one-landmark pages leave unselected spokes metrically identical; hence metric dimension>=2r-1. Every page except one chosen with two edges and one exceptional spoke resolves all edge pairs, yielding 2r*3^(r-1) bases. For doubly resolving, a singly covered page makes its selected spoke and rim have constant distance difference against all landmarks; two per page are necessary and sufficient, yielding 2r and 3^r. Independently enumerated all landmark subsets in L(F_r) for r=2,3,4 confirming exact complete basis families. Symbolic page proof covers all r>=2.

## originality

PASS

The 2018 original edge-version doubly-resolving work and 2024 circulant continuation employ this same line-graph distance but treat other graph families. The 2019 friendship-graph edge-metric quantity uses vertices as landmarks, a genuinely different invariant. No known prior statement implies either complete basis-family characterization for L(F_r).

## value

PASS

The explicit minimum bases, their exact counts and sharp separation between ordinary and double resolving numbers classify a natural repeated-triangle line-graph family. The two notions genuinely differ by one even as size grows; this is more than a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
