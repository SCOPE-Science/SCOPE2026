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

# Mathematical verification

`checker.py` was executed with Python standard-library exact `fractions.Fraction` arithmetic. It verified 216 branch-preimage identities on reference polynomial densities and 24 finite-tail telescope identities. These tests check the separate inverse branches, including the common right branch, at admissible parameters.

The infinite convergence, local positive periodic coefficients, scale relation and pointwise asymptotics follow from the proof in `RESULT.md`. The checker does not prove the published measure-existence and Lipschitz input; those are invoked from Kalle--Zeegers, arXiv:2206.07601. Finite tests are not a substitute for the general proof.

The scope excludes nonconstant periodicity, infinite stationary measures, and nonrandom switching. Independent scientific audit has not been performed.
