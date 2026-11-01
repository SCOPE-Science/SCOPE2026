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
# Verification and proof limits

Command: `python3 verify_square_cycle.py`. The included `verification_output.txt` records the exact completed run for all integers from 9 to 64 inclusive and ends in `CYCLE_SQUARE_DIHEDRAL_VERIFY_OK`. The verifier reconstructs every maximal open neighborhood, checks all simplex counts, proves locally that any shared tetrahedral face is already in the retained surface, checks the unique deleted outer edge, computes every edge-incidence and vertex-link profile, verifies the integral orienting cycle, checks invariance under every dihedral symmetry, and computes all signed cellular Lefschetz traces on the retained complex.

The universal quantifier is discharged in the accompanying proof, not by this finite verification. In particular, the separation of cyclic offsets for all integers at least nine, the gluing of the minimum-coordinate retraction, the two-triangle torus quotient and the four fixed points of the residual reflection are mathematical arguments independent of finite sample size. This verification does not constitute independent mathematical audit, prove a literature search exhaustive, or claim an original graph's quotient is homeomorphic to a sphere.
