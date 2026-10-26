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

# Analytical and executable verification

The complete proof, normalization conventions, boundaries, exact cumulant integral, the four-variable recurrence, Gaussian control comparison, and cyclic reversal are given in `RESULT.md`.

The standalone `checker.py` uses Python 3, NumPy and SciPy. Execute `python checker.py`. It computes the optimal-protocol fourth cumulant twice using independent initial-moment techniques, evaluates the exact covariance, tests the large-duration kurtosis coefficient, and numerically compares the cyclic-reversal fourth cumulant with its sharp large-stiffness limit.

Observed result: `PASS 171 deterministic checks`. The finite-stiffness cyclic sample returned `1.027222619811016` for the normalized fourth cumulant at stiffness 20, decorrelation rate 1 and inter-jump delay 0.5, with unit amplitude.

The mathematical proof is independent of numerical sample counts. Numerical integrations do not certify all values of the continuous model parameters; the strict inequality for all monotone protocols and the large-stiffness existence claim follow from the connected four-time formula and an approximate-identity argument, respectively. Independent external verification has not been performed.
