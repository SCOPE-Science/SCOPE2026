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

# Mathematical verification and limits

The analytical argument has four independently reconstructible stages: signed-permutation averaging for all invertible Euclidean pullbacks; an exact rank-two eigenvalue for the sphere maximum; mass-transfer majorization and a one-turn derivative for the sphere minimum; and a two-sided \(n^{1/4}\)-scale bound valid uniformly for all positive mixing parameters. The witness for the upper extremum is a normalized one-spike vector, and the witness for the lower extremum is an equal-amplitude sparse vector.

Run `python3 artifacts/verify_quadratic.py` in the package root. A successful execution prints 72,000 passed deterministic finite random checks, 48 extremizer substitutions, and four finite-dimensional tuned distortion ratios. The code is self-contained and uses only the Python standard library. The outputs confirm low-dimensional arithmetic, not any universally quantified statement.

No proof assistant was used. The theorem does not assert complex-scalar validity, an explicit exact optimizing mixing parameter at finite dimension, or absence of all equivalents in unindexed literature. Independent external audit is not performed.
