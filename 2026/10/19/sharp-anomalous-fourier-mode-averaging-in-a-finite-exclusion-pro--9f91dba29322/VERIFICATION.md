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

# Reproducibility and verification

Run `python check.py` in an environment with Python 3.10 or newer and `mpmath>=1.2` as specified in `requirements.txt`.

The executable performs **1329 assertions** and prints `PASS 1329 independent assertions` if successful. It verifies the discrete SEP generator's sine eigenmode over every half-filled configuration on rings of sizes 4, 6, 8, 10, 12; checks that the step's initial mode amplitude equals the exact cosecant; evaluates two independent algebraic forms of the renewal-age two-time Laplace transform; compares stationary means against numerical quadrature; and checks the predicted nonanalytic transform amplitudes for Pareto exponents below, at, and above the finite-variance boundary.

The checks use high precision and are finite numerical corroboration. They do not prove the renewal asymptotic or certify uniformity of any limiting formula. The mathematical proof relies on the exact eigenfunction, renewal equations, the cited second-order renewal theorem, and the regenerative-reward variance theorem. All limits keep ring size fixed.
