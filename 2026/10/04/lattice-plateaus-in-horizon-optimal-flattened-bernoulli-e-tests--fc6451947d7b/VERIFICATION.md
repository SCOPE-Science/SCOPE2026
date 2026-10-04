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
# Verification

The proof in `RESULT.md` establishes analytically that the first-passage event depends only on a finite vector of integer count boundaries and that each relevant scalar level equation has at most two roots.

`verify_plateau.py` performs the finite check for \((p_0,p_1,\alpha,t)=(2/5,3/5,1/20,30)\). It reconstructs all effective root locations from the monotonicity structure, checks the isolated root residuals and separation, enumerates every induced boundary cell, and evaluates each survival probability by exact rational dynamic programming. It also recomputes the smooth stationary point and its exact first-passage probability.

Expected terminal line:

`VERIFY_OK`

The numerical bisection is not used as evidence for an infinite statement. Its role is only to locate finitely many analytically isolated roots in the displayed finite example. Exact probability comparisons use rational arithmetic.
