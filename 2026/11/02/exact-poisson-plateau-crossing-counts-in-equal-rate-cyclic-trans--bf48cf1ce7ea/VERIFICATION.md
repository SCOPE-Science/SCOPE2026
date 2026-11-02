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

Install Python 3 with `numpy`, `scipy`, and `sympy`, then execute `python verify_stage_noise.py` in the same folder as this document. The checker constructs the continuous-time Markov generator independently of the Erlang spectral expression and compares the two expressions at nonzero frequencies, uses exact polynomial root-counting over a finite range of stage numbers, and checks nontrivial sign-change localization windows numerically.

The completed local verification returned `PASS 4464 assertions; maximal independent generator discrepancy 7.88e-15`. All claims about arbitrary integers and all real frequencies rely on the analytical monotonicity argument in `RESULT.md`; the numerical range is only a reproducibility sanity check. The Poisson plateau is normalized for a two-sided covariance Fourier transform and does not include the uncentered mean-intensity atom at zero frequency. The scope is stationary, strictly one-way, finite, equal-rate cyclic chains, with only return jumps counted.

No independent scientific audit or historical-priority certification is asserted.
