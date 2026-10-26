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
# Verification evidence

Run `python3 verify.py` using Python 3 from this directory. The program uses no third-party dependencies. It enumerates all colorings and all candidate pairwise swaps, recomputes strict utility comparisons at swapped destinations, compares predicted stable states and exact coefficients, and verifies one-step convergence from unstable colorings. The exhaustive run covers \(n=2,3,\ldots,10\), and the numerical-rational identity loop separately covers even \(n\) up to \(98\). The reported final string is `VERIFICATION_OK`.

The analytical proof covers all integers \(n\ge3\). Computations do not establish originality or replace that proof. Independent audit and validation have not been performed.
