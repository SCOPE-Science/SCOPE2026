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

The package includes `verify_octagon_angle.py`, a standard-library exact checker over \(\mathbb Q(\sqrt2)\). It enumerates all \(8^3=512\) choices of active facets for \(x\), \(y\), and \(x-y\), solves the three boundary equalities exactly, imposes every remaining support inequality, and minimizes the maximum of the eight affine support functions for \(x+y\) on every surviving interval.

The replayed certificate reports 32 inconsistent active triples, 48 feasible one-parameter branches, 32 equality branches, global minimum \(3-\sqrt2\), and final angle-modulus value \(3\sqrt2-9/2\). It also checks the explicit equality witness exactly.

This verifies the finite polyhedral reduction used in the proof. It does not verify any unstated value of \(\rho_{X_8}^a(\varepsilon)\) for \(\varepsilon\ne1\), does not establish literature completeness, and is not an independent audit.
