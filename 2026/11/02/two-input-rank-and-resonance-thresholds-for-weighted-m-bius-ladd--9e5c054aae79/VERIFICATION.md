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

# Verification record

The standalone `verify.py` uses both `numpy` and `sympy`. It constructs the weighted graph Laplacians edge-by-edge, checks the independently calculated matrix spectra, confirms the Fourier resonance multiplicities, and checks the rank of consecutive-control Fourier restrictions. It also computes direct eigenspace projections for the two adjacent controls at the first resonance and independent exact rational Kalman ranks for three small weighted graphs.

Command: `python verify.py`

Observed output: `PASS 24847 checks; 663 weighted graphs, direct eigenanalysis, Fourier PBH, direct Kalman ranks`

The finite numerical tests use explicit tolerances; they are not substitutes for the all-dimension, all-weight proof. Exact rational Kalman tests are limited to the stated small cases. The proof establishes the first-resonance classification analytically; no exhaustive machine verification for arbitrary \(n\) or arbitrary real \(g\) is asserted. The full text of one closely relevant historical source was unavailable. No independent mathematical audit has been performed.
