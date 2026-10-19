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

# Scientific verification

The finite-dimensional equations in RESULT.md can be reconstructed from the Erlang stage-chain generator and exact conditional Gamma moments. For each integer stage count the covariance is the sum of the phase-weighted centered-age moments. The four closed forms were also independently evaluated from the matrix exponential, and the all-shapes sign reversal follows analytically from nonzero spectral residues, not from simulation.

With NumPy and SciPy installed, execute `python verify.py` in a directory containing this document's accompanying script. The script uses the explicit ODE matrix to compare 124 values with the independently stated closed forms; it verifies negative finite-lag values at three stage counts, evaluates the dominant residue algebraically, and directly samples stationary renewal cycles to cross-check the covariance at representative lags. The direct-renewal sampling is stochastic and finite; it is supportive rather than an infinite-lag proof. A reader can repeat all analytic derivations without numerical code.

Limitations: finite tolerance tests are not theorem certificates; only integer Erlang shapes and independent Brownian noises under exact collective resets are covered. There has been no independent audit or external validation.
