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

# Verification and reproducibility

The analytical argument in `RESULT.md` proves the all-circumference almost-sure finiteness and mean threshold from finite accepted capacity, Poisson thinning, a uniform two-gap law, and a positive-volume family of near-pinched later configurations.

Running `python checks.py` with Python 3's standard library independently verifies the two-gap admissible-length formula, the exact integral survival expression for the third deposition stage on representative circumferences, finite-sample estimates of that survival law, its leading asymptotic constant, and explicit geometric witnesses for larger circles. The script uses a fixed random seed for reproducibility and exits with an assertion error on check failure.

The numerical checks do not certify the continuum or all-size theorem. The exact integral and the open-set lower bound in `RESULT.md`, rather than numerical sampling, support those conclusions. The bibliographic comparison identifies relevant earlier large-time jamming analyses and circle-deposition models but cannot exclude every unpublished or inaccessible formulation.
