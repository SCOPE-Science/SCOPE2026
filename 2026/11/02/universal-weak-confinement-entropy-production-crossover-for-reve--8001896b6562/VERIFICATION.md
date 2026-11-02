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

# Reproduction and limits

Run `python3 verify.py` with a Python 3 standard-library interpreter. The script checks the two-state reversible propulsion spectrum and a three-state path-chain spectrum, evaluates the exact confinement flux, verifies the stated \(O(\kappa)\) flux error against four scaled times and three positive trap strengths, checks integrated flux profiles by quadrature, and simulates switching diffusion paths to check the one-time heat-flux normalization. Constant-velocity and zero-mean cases are also included.

The script does **not** compute the full entropy-production functional, nor does a finite sample prove the entropy-production window limit. The latter follows from the entropy-balance identity and the two Gaussian entropy bounds proved in `RESULT.md`. All checked numerical cases must be understood as finite diagnostics, and no external independent audit has been performed.
