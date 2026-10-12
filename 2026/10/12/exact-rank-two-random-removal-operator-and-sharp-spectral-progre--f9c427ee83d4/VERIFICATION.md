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

Run `python verify_rank_two.py` with Python 3 standard library from the directory containing this document. Observed output:

`VERIFY_OK: 990 exact spectral-rational cases, six quadrature checks`

The script exactly checks 990 integer-parameter spectral families using `fractions.Fraction`, verifies the extremal generalized-eigenvalue certificate, and uses periodic trapezoid integration on six representative rank-two states. It additionally checks that maximal rank-one subtraction leaves a positive-semidefinite singular matrix at sampled angles. Those tests are finite, not a proof of universally quantified claims; the proof for all spectra and PSD test matrices is in `RESULT.md`.

External independent audit is not performed. Residual novelty risk arises from equivalently formulated general spherical-ratio integrals outside the reviewed corpus. Neither convergence rates nor higher-rank formulas are certified.
