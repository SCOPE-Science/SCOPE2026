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

## Mathematical verification

The proof uses conditional holding-time independence, the law of total variance, a bounded finite-state Poisson-equation martingale, Azuma tail bounds for every positive-drift signed edge weighting, and optional stopping at an integrable first-crossing index. The exact identity and the bounded overshoot for mean-holding-time weights control all thresholds analytically.

The separate reproducibility script `checker.py` uses Python 3 and SymPy. It verified 24 exact rational stopped-path cases across three edge-mark families and eight first-passage thresholds. It checks the Poisson corrector and the exact finite-threshold decomposition, plus optimal-weight overshoot statements. It is **not** an exhaustive verification of infinitely many thresholds, states, weightings, or waiting-time distributions.

Known limits: no general zero-drift statement; no finite-mean-only or infinite-variance cases; no stationary random-age initialization; no interacting holding times. The source gives only a fixed-time semi-Markov flux theorem and explicitly leaves the first-passage counterpart as a hypothesis.
