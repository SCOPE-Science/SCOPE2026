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

The analytic proof establishes the covariance by a single reused-noise geometric series, the strict pairwise one-crossing inequality by monotonicity of \(s/(e^{st}-1)\), and the unique spectral maximum through a strictly monotone elementary geometric sum. It then proves the optimal consecutive rank-block rule and its one-way migration by exchange, with an exact two-level asymptotic sharpness witness.

Running `python3 check.py` gives 6,254 passed finite comparisons. The checker tests randomized spectra, mode-crossing orientation, integer-time rank-block motion, unique scalar spectral-filter peaks, and the two-block trace-loss limit. It uses only Python standard-library facilities and a fixed pseudorandom seed.

Finite checks are numerical corroboration, not proof of universal statements, historical originality, or independent validation. The theorem assumes real full-column-rank data, isotropic covariance, one fixed noisy observation and nonoscillatory relaxation. Independent audit and validation have not been performed.
