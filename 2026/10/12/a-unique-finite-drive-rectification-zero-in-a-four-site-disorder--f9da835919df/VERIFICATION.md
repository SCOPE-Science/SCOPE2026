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

The exact-arithmetic `verify.py` constructs the sixteen-state Markov generator directly from the specified physical transitions, with one common time rescaling of two, solves the normalized stationary equations symbolically, and checks the explicit rational current formula, the even-current polynomial identity, the two exact sign witnesses, and the zero-bias equilibrium law. The packaged verifier ran successfully and printed `VERIFY_OK`.

The proof uses strict polynomial inequalities on the entire domain, not interpolation or finite sampling. Numerical approximations identify the root but do not certify it; exact uniqueness follows from the analytic derivative bound. All calculations concern a four-site chain and its specified rates. A separate independent audit has not been performed.
