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

# Reproducibility and verification

Execute the companion `verify.py` using Python 3 with no third-party packages. The verifier performs exact polynomial arithmetic over \(\mathbb Q\) and finite prime fields, then checks the three proposed derivations are logarithmic, verifies the determinant equals \(F\) exactly, and checks the characteristic-dependent vanishing of the \(z\)-derivative. It covers thirteen admissible specializations, including positive characteristics dividing and not dividing the total weight.

The expected concluding line is:

`VERIFY_OK: exact coefficient-ring logarithmic identities and unit determinants in 13 cases`

The parameter-uniform proof is supplied in `RESULT.md`, Steps 1–6. Finite checks cannot certify an infinite parameter range; the universal polynomial identities, exact reducedness test and determinant-based spanning argument establish it. The existence of unpublished or unindexed equivalent prior results cannot be excluded through database searches, and independent validation has not been performed.
