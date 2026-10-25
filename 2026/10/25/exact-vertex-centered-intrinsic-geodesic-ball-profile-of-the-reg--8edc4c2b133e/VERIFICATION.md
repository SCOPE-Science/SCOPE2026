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

# Reproducible verification

The analytic proof depends on (i) distance-minimization through a last entry into the opposite face, (ii) three congruent planar nearest-image triangles, and (iii) exact evaluation of the two one-dimensional area integrals with break angles. It does not rely on numerical finite checks. The included standalone `check_profile.py` computes the incident-face and opposite-face integrals separately, compares their sum against the piecewise closed formula at specified radii, and asserts correct limiting total area, monotonicity at sampled radii, and matching one-sided first derivatives. Run with `python check_profile.py` using a Python environment with SciPy installed. The program prints a success message or raises an assertion if a check fails. Neither these finite tests nor literature searches imply independent certification of the general statement.
