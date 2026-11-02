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

# Verification and reproducibility

Run the enclosed `verify.py` with Python 3 from the same directory using `python verify.py`. It uses only the Python standard library and prints a summary on success.

The program carries out exact rational state-distribution sums for \(d=2,3,4\), positive quota vectors, integer and fractional positive initial masses, and a range of finite observation times. It compares these with the closed completion CDF and the quota-proportional terminal-colour formula in the unit-mass case. A separate direct time-step path propagation reconstructs these probabilities without calling the Dirichlet–multinomial formula. The minimal completion-time comparison for contrasting quota allocations is checked algebraically at several masses. Finally, numerical spot checks compare beta–binomial low-count probabilities with their theoretical Gamma-ratio asymptotic constants.

The checked program printed `PASS 6214 exact rational comparisons and asymptotic-constant spot checks`. The integers in this total include both strict-exact rational comparisons and explicitly approximate large-time constant checks; they must not be confused with a formal proof of an asymptotic statement. The proof's all-parameter conclusions require, and are supported by, the displayed Dirichlet–multinomial formula, Gamma-ratio asymptotics, low-count pair bounds, and finite quota-pattern comparison.

This verification is a reproducibility aid and does not constitute independent validation. Historical-priority assessment also remains non-exhaustive.
