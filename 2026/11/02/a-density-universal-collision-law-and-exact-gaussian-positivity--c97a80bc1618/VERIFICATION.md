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

# Reproducible checks and limits

Run `python verify.py` with Python 3. It recomputes the Gaussian two- and three-node tail constants, numerical elliptic integral, angular identity, and performs seeded sample checks on exact affine constraints, orthogonality/minimal-norm geometry, and probability estimation. The test script is supplementary; it does not certify the continuum dominated-convergence argument or exhaustive originality. The theorem remains restricted to bounded compact almost-everywhere continuous centered densities and Gaussian densities.
