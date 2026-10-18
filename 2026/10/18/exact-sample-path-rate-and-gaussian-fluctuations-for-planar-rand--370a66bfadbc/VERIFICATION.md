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

To reproduce, install the Python dependencies listed in `requirements.txt` and run `python verify.py` in the same directory. This tests the exact fourth-moment characteristic polynomial, checks three independent angular integrals for each of seven anisotropy parameters, and samples four Gaussian direction processes; all checks passed at preparation. The checker uses numerical quadrature near a logarithmic singularity and emits a SciPy integration roundoff warning without failing the stated tolerances. The infinite-horizon results follow from the proof, not from finite numerical tests.
