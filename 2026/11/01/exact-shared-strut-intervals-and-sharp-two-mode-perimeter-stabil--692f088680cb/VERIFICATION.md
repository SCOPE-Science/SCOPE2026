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

# Reproducibility

The theorem is proved analytically in `RESULT.md`. Run `python3 CHECK.py` with Python 3 standard library; its exact rational perpendicular-bisector intersection tests independently reconstruct the maximal radii and shear-feasibility condition on 1,530 configurations. Further checks exercise two vertex-only endpoint exclusions, the two independent saturating families, and the asymptotic rates near a square. All checks were executed successfully from the embedded checker source, with the final line `ALL_CHECKS_PASSED`.

Computations cover finite rational instances; they do not replace the theorem's proof and do not establish historical novelty. No independent mathematical audit has been performed.
