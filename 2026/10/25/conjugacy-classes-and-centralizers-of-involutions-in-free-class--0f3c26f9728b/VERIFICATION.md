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

# Verification record

Run `python verify_involutions.py`. The standard-library program constructs the full linear involution equation from exterior-square minors for each enumerated matrix and computes its solution-space dimension by an independent finite-field rank algorithm. It also enumerates the linear \(+1\) eigenspace rank and checks orbit-stabilizer independently.

Complete comparisons performed:

- \((n,q)=(2,3)\): \((9,36,1)\) observed and predicted class sizes.
- \((n,q)=(2,5)\): \((25,150,1)\) observed and predicted.
- \((n,q)=(3,3)\): \((19683,9477,28431,1)\) observed and predicted; all centralizer orders verified.

The run finishes `ALL_INVOLUTION_CHECKS_OK`. Rank-two cases are boundary checks. The claimed theorem begins at rank three. Large ranks and nonprime fields are covered by the algebraic proof, not by exhaustive finite enumeration. The characteristic-two analogue is excluded. No independent validation is asserted.
