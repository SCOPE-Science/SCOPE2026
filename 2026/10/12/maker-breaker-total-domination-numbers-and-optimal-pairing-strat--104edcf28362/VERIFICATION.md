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

Any total-dominating set needs at least 2 vertices on each shore; any 2+2 works. On 6 vertices Dominator can obtain <=3 vertices and cannot win. For n>=4 four disjoint within-shore pairs, two per side, supply a force-one-from-each pairing strategy in either start convention and the gamma_t lower bound forces 4 moves. Every transversal of a four-pair certificate is a 2+2 selection, so a cross-pair would change the shore count under flipping its choice; thus precisely two within-shore pairs per part. Matching count is 3*C(n,4) independently per shore.

## originality

PASS

No prior mathematical result located implying the all-parameter family-specific theorem; best-of-knowledge, with residual indexed/access limitations.

## value

PASS

Optimal pairing certificates directly encode first- and second-player strategies. The sharp small-order threshold and complete classification/count of all minimum certificates are natural exact game invariants beyond evaluating gamma_t, suitable for comparison with other matching-deleted bipartite families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
