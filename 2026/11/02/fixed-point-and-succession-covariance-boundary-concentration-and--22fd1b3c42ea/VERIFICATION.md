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

# Verification of the covariance operator

Run `python3 verify.py` using Python's standard library. The program independently enumerates every permutation of orders three through eight and computes, in rational arithmetic, all products of fixed-point and succession indicators. It verifies all predicted matrix entries, aggregate covariance and component variances, and computes exact matrix rank for every order from three through thirty. It also confirms the alternating null mode in odd orders.

Observed output: `PASS 266 assertion groups; exhaustive permutations through n=8; exact matrix rank n=3..30`.

The infinite-size result is established by the conditional counting proof and the explicit kernel calculation in `RESULT.md`, not by the finite test. This verification does not evaluate absolute originality or constitute independent validation.
