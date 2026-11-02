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
Run `python3 check.py` in the directory containing this file. The code uses standard Python libraries only and returns `PASS 158 exact and numerical assertions` under the tested runtime.

## Checks performed
The independent finite Markov recursion across the two visited part sizes was matched exactly, using rational arithmetic, against the coupon generating function for all ordered part pairs with sizes from 1 through 8. Singleton endpoint cases were checked. Additional occupancy-recursion comparisons evaluated the balanced tie law at small sizes, while numerical dynamic programming tested finite-size approach to the sharp 1/8 constant and the logistic imbalance window.

## Proof-dependent conclusions
The exact all-size identity follows from independent alternating uniform streams. The asymptotic coefficient uses Poisson convergence of missing coupon counts and an associated compact local limit; the logistic window uses independent Gumbel convergence. Finite checks cannot establish either all-size statement. The current review is not an independent audit, and no external certification is claimed.
