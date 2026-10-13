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
The explicit arithmetic was replayed from the bundled file `verify_counterexample.py`. The recorded output verifies that the dehomogenized collision cubic has no rational root, has discriminant \(-31\), and therefore is irreducible and separable; it also records the collision determinant and the Euler-characteristic calculation.

The checker does not prove the general theorem. The general necessity is deductive from base change and geometric collision counting. The sufficiency statement uses the ruled-surface and affine-bundle construction of arXiv:2608.27341v2 after strengthening the unique collision fibre to be \(k\)-rational.

Limits: the corrected equivalence is asserted only in characteristic zero. No independent audit has been performed.
