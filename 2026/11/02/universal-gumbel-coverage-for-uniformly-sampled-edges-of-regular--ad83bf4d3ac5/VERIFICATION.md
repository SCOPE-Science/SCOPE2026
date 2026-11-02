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

# Reproducibility and verification

Run `python3 verify.py` using only Python 3 standard-library modules. The program reports `PASS 593 independent exact-rational assertions and checks`, then confirms that two nonisomorphic six-vertex regular graphs have distinct finite-volume distributions even though their first two moments agree. It tests 14 regular graph examples with exact-rational independent edge-status enumeration, checks moments at multiple rational untouched-edge probabilities, and computes finite-round coverage probabilities independently by a state-space recurrence and inclusion–exclusion. It separately tests the Poisson Stein error estimate and the essential degree monotonicity for fixed positive parameters.

The analytic proof of the Gumbel limit, the uniform error bound, the expectation and the one-regular boundary is in RESULT.md. Finite exact enumeration corroborates finite identities, not convergence for all graph sequences. A mathematical proof of the asymptotic claims does not follow from test success alone. No independent audit, external certification, or peer validation is represented by this report.
