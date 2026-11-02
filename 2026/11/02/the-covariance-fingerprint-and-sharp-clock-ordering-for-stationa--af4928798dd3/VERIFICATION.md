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

Execute `python verify_covariance.py` with Python 3, NumPy and SciPy installed. The packaged checker runs independent covariance-integral, length-mixture, stationary size-biased-age, inversion, two spectral-integral, deterministic-clock convexity, and regularly varying Lomax-tail comparisons. Expected completed output ends in `PASS 143 checks including independent spectral transforms`. The checker uses independent finite-dimensional tests; the full distribution-free identities, global strict optimum, and asymptotics are established analytically in RESULT.md. The software does not certify novelty, numerical inverse stability, or independent scientific validation.
