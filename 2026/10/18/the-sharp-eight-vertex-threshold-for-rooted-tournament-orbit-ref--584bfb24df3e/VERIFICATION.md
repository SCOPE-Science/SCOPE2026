---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The directed 1-WL signature retains old colour and outdegree counts per colour (indegrees determined in tournaments). Independently reconstructed canonical unrooted tournament augmentation by sorted-degree blocks produces 1,1,2,4,12,56,456 classes at orders 1..7, with all 2,4,16,64,384,3584,58368 root-incidence extensions through order 8. Every rooted extension was compared with automorphism orbits, yielding 0 failures through n=7 and exactly two at n=8, with all-outgoing or all-incoming unique root on the same non-vertex-transitive regular seven-tournament. Direct independent automorphism calculation obtains order 3 and orbits 1,3,3 in that tournament; stable colour classes root/others have sizes 1,7. Exhaustiveness is justified by delete-root extension and degree-preserving canonicalization, not by raw output alone.

## originality

PASS

The general Arvind–Köbler–Rattan–Verbitsky theory of refinability and Arvind–Fuhlbrück et al study of individualization supply definitions/general complexity, while McKay supplies 456 unrooted seven-tournaments. Neither reference gives the exact rooted tournament first failure or two pointed types. No Resultary hit implied the stated rooted isomorphism classification.

## value

PASS

Rooted colour refinement versus rooted automorphism orbit is a natural first-error threshold, and the exact two exceptional rooted tournaments plus explicit automorphism obstruction clarify the boundary of a standard graph-isomorphism heuristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
