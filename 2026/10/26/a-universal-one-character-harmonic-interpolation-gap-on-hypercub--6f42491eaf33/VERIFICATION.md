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

The proof is self-contained. Explicit solid harmonic factors have Laplacian zero and values \(-4,6,15u\) on unnormalized sign corners. Their disjoint-coordinate products construct every Walsh character asserted in the three exact degrees. The coordinate-sign projection proves the full-sign Walsh mode vanishes at degree \(d+2\).

A standalone SymPy checker (`checker.py`) verified the factor derivatives and values, and independently computed the exact rational character-eigenvalues of the spherical-harmonic Gram matrix in dimensions 3 through 10 at degrees \(d,d+2,d+4\). Its finite sweep does not certify infinitely many dimensions and is not used as the proof.

The rank statement makes no assertion about other degrees, nor about singular values or numerical conditioning. Independent audit and external validation have not been performed.
