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

# Verification procedure and scope

Use Python 3 standard library and run `python3 verify.py` beside this document. The checker reconstructs the two projective flow matrices from the stated positive physical parameters and logarithmic durations; uses exact integer arithmetic for both composition products and the quadratic numerator; verifies positive/negative/positive numerator signs at adopters \(0,1/2,1\); confirms the two simple interior roots and individual positive equilibria; and independently integrates each continuous stage using fixed-step fourth-order Runge–Kutta at 200 reproducible initial conditions to compare against the exact flow formula. All checks in the supplied run succeeded. No nonstandard package, external data, randomness without a fixed seed, or remote service is required.

The universally quantified upper bound is supported by the elementary degree-two proof, not by numerical sampling. The common-equilibrium obstruction follows from two equal first derivatives and a double polynomial root, not from tests. Numerical integration is an additional consistency check and supplies no separate global proof or independently performed audit. Historical priority is not established by the program.
