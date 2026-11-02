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

The analytic proof derives finite-size centered second and third moments, a high-order lattice Edgeworth expansion for a strictly positive two-state Markov additive chain, and the exact monotone quadratic transport cost. The spectral gap and stationary prefactor justify the leading Edgeworth term; the Gaussian tail estimate justifies discarding noncentral quantile cells.

`check_two_state_markov_w2.py` independently calculates occupation-count laws by finite-state dynamic programming, checks low-length moments with exact `fractions.Fraction` arithmetic, and evaluates the monotone Gaussian quantile transport integral using SciPy. It produced the accompanying `verification_output.txt`, with 97 deterministic checks passed. These calculations verify finite instances and numerical asymptotic behavior only; they are not substitutes for the proof of the limiting identity.

Requirements: Python 3.10+, NumPy and SciPy. Execute `python check_two_state_markov_w2.py` from the directory containing this file. Scientific limitations include fixed interior parameters, a one-dimensional count statistic, and no independent audit.
