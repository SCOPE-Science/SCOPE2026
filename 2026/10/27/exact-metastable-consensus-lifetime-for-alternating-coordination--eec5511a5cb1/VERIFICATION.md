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

The standalone `verify.py` uses Python standard-library rational arithmetic. Executing it from its containing directory reports `CERTIFICATE_OK 13814 exact rational assertions`; for the case of population 20 and threshold \(\eta=1/5\), it checks the closed expectation \(20759/21\). The program independently enumerates both game choices and individual action profiles for small population sizes and compares the resulting transitions against the birth–death rates in the proof. It verifies first-step equations, reflection symmetry, one-way consensus regions, and exact finite-time identities.

The limit \(\lim N^{-1}\log\mathbb E\tau_N=\log 2-H(\eta)\) is established by the written binomial-entropy proof, not by tests, numerical convergence or a finite range of populations. No independent scientific audit or externally certified verification has been performed. The stated assumptions exclude tie cases and general sparse-layer games.
