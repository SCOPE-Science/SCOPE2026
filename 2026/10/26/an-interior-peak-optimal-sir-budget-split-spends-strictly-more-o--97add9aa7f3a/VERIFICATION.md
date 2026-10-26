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

# Verification of the result

Run `python3 check.py` using Python 3, SciPy and mpmath in the directory containing this file and the checker. It returns `CERTIFICATE_OK 522 checks` for the exact rational bounds, two independent final-size calculations, numerical derivative consistency, and numerical SIR trajectories. The exact rational comparisons are valid for the entire explicit example. Numerical samples do not establish global uniqueness on \([0,1]\); that follows instead from the exact analytical expression for \(Q'/Q\) and \(0<\mathcal R s<1\) in `RESULT.md`.

For the general statement, check the final-size implicit derivative and the uniform exponential bound as written in the proof. Independent review has not occurred. No stochastic simulations or empirical validation are claimed.
