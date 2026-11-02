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

Run `python verify_switching.py` in a Python 3 environment with NumPy and SymPy. The run on the included file yielded `PASS 711 finite/symbolic checks`.

The script checks the squared singular factors of both discrete update matrices, symbolic product and stability identities, a symbolic equality for the mean-square critical probability, one hundred random two-dimensional matrix cases, finite-time expected moments against a direct enumeration of every Markov path for horizons through eight, and critical-probability ordering for multiple real moment orders. It also checks the exact rational witness and the second/fourth moment phase separation.

The main theorem is analytical. Finite path checks do not establish the almost-sure limiting exponent, the infinite-time Perron asymptotics or the claimed monotonicity for all positive real moment orders. Those statements are proved in the accompanying `RESULT.md` by Markov occupation frequencies, the positive transfer operator, eigenvalue monotonicity and the hyperbolic-sine identity. No independent audit or external formal certification has been performed.
