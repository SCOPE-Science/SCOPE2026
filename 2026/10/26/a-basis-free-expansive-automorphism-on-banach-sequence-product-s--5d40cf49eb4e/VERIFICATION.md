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

# Verification details

The proof reconstructs the one-coordinate isometry, its left inverse, both compositions of the automorphism and inverse, and the disjoint-support decomposition for every positive iterate. The two-sided obstruction is an explicit nonzero vector with globally bounded compatible seminorms.

Run `python CHECK.py` for deterministic, finite-support verification of these algebraic identities. In the review execution it reported 21,600 successful assertions over 1,200 complex input cases. These finite tests are checks, not infinite-dimensional proof or independent audit.

No numerical approximation, probabilistic inference, or external certificate is needed for the theorem. The public date refers to the initial motivating preprint, not a journal publication or subsequent revision.
