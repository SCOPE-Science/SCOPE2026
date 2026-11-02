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

The supplied `verify.py` uses exact symbolic matrix algebra, 3,510 rational branch/moment comparisons, and a fixed numerical example. Reproduced identities are the quadratic Lyapunov drift, its positive principal minors, the second-moment transfer determinant, and the stationary variance expression. Run the verifier with `python verify.py` after installing `requirements.txt`.

The proof of the all-parameter stability classification relies on the two-step positive-definite observability form and not on enumeration. The verifier does not certify publication priority, assumptions outside independent Bernoulli zero/one-step lags, or independent scientific review.
