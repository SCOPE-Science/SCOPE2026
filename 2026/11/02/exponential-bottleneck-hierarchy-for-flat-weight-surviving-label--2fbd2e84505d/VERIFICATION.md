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

# Verification

- `python checker.py` performed 625 exact rational assertions, including normalization of the finite occupancy transitions for \(3\le n\le17\), exact two- and three-state escape identities, and recursively computed finite absorption expectations and visitation bounds.
- The analytical proof derives the full \(n\to\infty\) claim from a fixed-level skip bound, geometric residence times and uniform remaining-level expectation bounds; finite assertions are not substituted for infinite proofs.
- No independent audit or independent expert verification has been performed. The boundary definition is outside the fixed-positive-power assumptions of the motivating preprint.
