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

# Reproducibility and scope

Run `python3 verify.py` with Python 3; only the standard library is required. The expected first output line is `VERIFY_OK rational_state_transitions 1040 spectral_brackets 8`. The tests independently implement the original repulsive update with exact rational arithmetic, verify the deficit recurrence and invariant confidence-path pattern across 960 exact transitions, and verify 80 full-confidence three- and four-agent examples. Numerical tridiagonal eigenvalue calculations test the Rayleigh bounds for eight population sizes.

# Limits of computational evidence

The checker examines finitely many parameter choices, population sizes, and times, so it cannot establish the theorem for all real initial conditions, arbitrarily large populations, or infinitely many steps. Those assertions rely on the displayed invariant chamber induction, Perron–Frobenius spectral decomposition, and the reversible Markov-chain argument. The large-population asymptotic follows from the explicit analytic Rayleigh bounds, not numerical extrapolation. Independent external audit has not been performed.
