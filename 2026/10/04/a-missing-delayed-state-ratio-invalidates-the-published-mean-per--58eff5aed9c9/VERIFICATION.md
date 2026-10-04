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

The exact checker `verify.py` reconstructs the parameter choices used in the persistence proof and the counterexample using Python rational arithmetic only. It verifies:

- \(a=80/9\) and \(b=16/3\);
- \(\widetilde{\mathcal R}_0^S=80/21>1\);
- the AM–GM product ratio \(\rho=10^{-6}\);
- the exact displayed generator value \(2486393/90900\);
- the paper's state-independent post-AM–GM expression \(-8761/900\);
- strict violation of the claimed upper-bound ordering.

The check is algebraic, not a simulation. It proves only that the displayed drift inequality fails on one admissible positive current/delayed state. It does not establish or refute long-time persistence of the stochastic delay system.
