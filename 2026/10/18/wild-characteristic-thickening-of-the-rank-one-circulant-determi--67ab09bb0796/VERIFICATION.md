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

# Verification of integral cyclic determinantal scheme

The algebraic certificate is the explicit degree-wise free normal-form basis of the cyclic quadratic quotient and the isomorphism of its entire projective scheme with Spec Z[z]/(z^n-1). The proof is characteristic-free.

To reproduce the finite checks, run `python3 verify.py` with Python 3 and no third-party packages. The checker enumerates all n×n circulant 2-minors and their cyclic-sum components for n=3,...,8; verifies the n independent positive-degree residue classes through degree six, the alternating Betti-polynomial coefficient formula, and Frobenius factorizations for eight characteristic-dividing pairs. The expected final line starts `VERIFY_OK:`.

Finite checks do not establish the theorem for untested n or characteristic. The proof supplies the general result. Independent audit has not been performed.
