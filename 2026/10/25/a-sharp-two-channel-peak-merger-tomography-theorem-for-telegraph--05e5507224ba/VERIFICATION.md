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

# Verification record

The self-contained `check.py` evaluates the exact rational susceptibility and separately solves the conditional two-state linear response system. It checks the two spectral derivative signs on both sides of each coalescence rate and numerically inverts both measured rates to the original positive parameters.

Running `python3 check.py` on the packaged source produces 500 successful full forward/inverse cases, 1,500 separate matrix-response comparisons, 1,500 peak-sign comparisons, and tests of the sharp universal ratio boundary. The code uses a fixed random seed and only the Python standard library.

These are finite numerical and algebraic consistency tests, not independently certified infinite proofs. The theorem's global assertions rely on the exact derivative signs and a strict logarithmic-monotonicity inequality provided in `RESULT.md`. The normalization uses the total correlation decay rate, twice the individual-state transition rate. Experimental identifiability in noise and independent audit are not assessed.
