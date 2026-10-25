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

## Verification scope

The formal statement uses complete deterministic binary automata, an explicitly supplied subset, and strong connectivity of the transition graph. Membership in PSPACE follows by reachability in the implicit subset graph with a polynomial-space counter. Hardness follows from the primary paper's polynomial reduction to strongly connected automata and its polynomial alphabet reduction to two letters.

The earliest verified public date is 2014-03-16 for arXiv:1403.3972v1. The published record classifies the work under MSC 68Q45. The later literature citation is used only as corroboration, not as evidence that the claim predates the primary source.

This verification does not constitute an independent audit or external validation. No computational certificate is needed for the proof-based claim; the base unrestricted PSPACE-completeness is cited through the primary paper's references.
