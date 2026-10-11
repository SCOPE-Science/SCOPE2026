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

# Verification of the periodic square-root weighted-shift theorem

The defining weights are positive and bounded for all allowed parameters. The analytic argument is split into independent checkpoints: logarithmic expansion with remainder of order \(j^{-3/2}\); two periodic zero-mean Abel estimates; all-start/all-horizon normalized product bounds and finite nonzero product limits; the orthogonal orbit formula and the three exclusive sign regimes; and compact perturbation plus Fredholm/approximate-eigenvector reasoning for the unchanged spectral triple. At the critical boundary the nonzero orbit limit is explicitly \((\sum_{k\ge1}|x_k|^2L_k^2)^{1/2}\), not merely a boundedness assertion.

Run `python3 check_weight_phase.py` with Python 3 and no external dependencies. The included script checks 28 period/parameter/start-index combinations, compares finite logarithmic products against the derived exponent at lengths 100, 1,000 and 5,000, and prints converging residuals. It passed in the packaged environment. These are finite normalization diagnostics, not a computer-assisted proof of the infinite theorem or a spectral certification.

Limits: the proof assumes a real finite-period zero-mean modulation with amplitude at most one-half and drift in the displayed range. It does not claim stability under arbitrary nonperiodic errors or characterize arbitrary weighted shifts. No external independent audit has been performed.
