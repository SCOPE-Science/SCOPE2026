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

Run `python3 check.py` in the same directory as this document. The program depends only on Python 3 standard-library `fractions` and `itertools`, uses a deterministic grid, and checks 156 admissible rational parameter triples, five evenly spaced cycle phases including the switching endpoints, eigenvector and trace identities, and selected exact transverse fourth iterates. During preparation it completed successfully with output `PASS: 156 admissible exact-rational parameter triples; five four-cycle phases per triple; multiplier, switching, and local transverse identities checked.`

The proof for all real parameters is the matrix-and-inequality argument in `RESULT.md`. The code checks only a finite grid; it cannot establish originality, generic nonlinear persistence, or global attractor statements. No independent audit was performed.
