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

Apply Definition 2.1 of Fallat et al. with spread before ignition and majority influence at each unburned vertex. If the centre ignites first, the next spread burns all leaves, with colour populations p+1 and q. If a leaf ignites first, the centre necessarily burns in the next spread, and for m>=3 exactly one additional leaf can be ignited before propagation of all remaining leaves. That ignition flips at most one natural leaf colour: for 1<=p<=m-1 optimal class size max(p+2,q+1); the endpoints p=0 and p=m separately give m and m+1. Every signing of the star is switching equivalent, so minimizing gives ceil((m+3)/2); the published coding identity gives covering radius floor((m-1)/2). Independently implemented spread/ignite recursion and exhaustively checked all 504 signings over m=3..8, without using the author verifier, confirming boundary cases. The two-leaf path is excluded explicitly.

## originality

PASS

Best-of-knowledge originality comparison by actual statement and implication, with historical and unavailable-material risks recorded; no priority certification. Inspected closest prior statements use different scopes/estimands or do not directly entail this final exact claim.

## value

PASS

The signed-graph burning plurality number is recently defined and the initiating paper computes signed paths but poses tree classes as open. A complete first non-path branching family, including all sign patterns and an exact reachable-colouring-code covering radius, fills a motivated extremal/classification gap. The simple two-ignition structure is an explanation of the exact result, not a basis to dismiss a new natural graph-family formula as valueless.

The dated certificate retains the supplied scientific assessment, sources and limitations.
