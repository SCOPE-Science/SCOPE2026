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
Run `python3 hamming_power_verify.py` from the extracted package, with Python 3 and no third-party packages. Expected last line: `HAMMING_POWER_EXACT_CHECK_OK 5278`.

The script independently computes finite character coefficients, checks all admissible and forbidden signs in a finite parameter rectangle, verifies rational endpoint spectra and their exact zero levels, and reconstructs small Hamming graph powers by breadth-first search. A finite test cannot establish all-dimension claims; the analytic proof uses isometric subcubes and explicit character maxima to cover the complete infinite parameter space.

Independent mathematical audit and validation have not been performed.
