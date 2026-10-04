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

The proof is exact. For a strictly positive periodic orbit, period integration of \(d(\log S)/dt\) and \(d(\log I)/dt\) gives the two nonlinear balance equations used in the derivation. Subtracting the corresponding positive averaged-equilibrium balances yields the stated identities.

`verify.py` uses exact rational arithmetic to replay the algebraic subtraction on a nonzero-covariance witness and checks the equivalent equality/sign forms. This computation is a consistency check only; it is not used to infer existence, uniqueness, stability, or a universal sign for any periodic solution.
