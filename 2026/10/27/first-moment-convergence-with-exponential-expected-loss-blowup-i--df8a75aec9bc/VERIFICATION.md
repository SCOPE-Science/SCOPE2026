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

The local verifier uses exact integer/rational arithmetic to reconstruct both client matrices, multiply them in the alternating order, verify characteristic polynomials by direct determinant evaluation at enough rational points, and check the closed-form alternating event iterate against explicit recursion for multiple parameters and horizons. The unbounded-moment conclusion is a proof by a positive-probability event and does not follow from numerical tests. The strict first-moment Schur test is analytic.

Execute `python3 verify.py`. No external software or data files are required. The verifier is a finite algebraic consistency check, not an independent audit or a general-purpose theorem prover. The claim is restricted to the two-client exact-proximal model and its specified open parameter interval.
