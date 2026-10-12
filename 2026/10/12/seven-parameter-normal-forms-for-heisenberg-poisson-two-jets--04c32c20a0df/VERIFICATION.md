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

# Verification and scope

The supplied `verify.py` implements the quotient \(K[x,y,z]/(x,y,z)^3\) directly as monomial dictionaries. For each characteristic \(2,3,5,7,11\), it constructs the \(6\)-by-\(18\) Jacobi matrix and the \(18\)-by-\(18\) gauge matrix by evaluating their action on basis vectors. Their ranks are respectively \(3\) and \(8\); the gauge image is in the Jacobi kernel and the seven normal-form directions extend the image to dimension \(15\). It also tests randomly sampled brackets and gauge translations, and checks all \(2^{18}\) possible coefficient assignments in characteristic \(2\), obtaining exactly \(2^{15}\) Jacobi solutions.

These computations verify finite instances and linear identities, but they do not prove the arbitrary-field theorem. The full proof in `RESULT.md` gives the characteristic-independent rank arguments and handles all quantifiers. Only coordinate changes acting trivially on the first-order space are considered. No claim of independent audit or of higher-jet extendibility is made.
