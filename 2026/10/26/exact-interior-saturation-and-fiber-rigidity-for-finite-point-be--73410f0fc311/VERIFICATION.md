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

The analytic proof uses the area change of variables for finite Blaschke products, the resulting Bergman weighted-pullback isometry and its adjoint fiber trace, and meromorphic pole propagation across a rational covering. Its boundary cases are explicitly addressed: degree at least two, pairwise distinct sampling nodes, and regular image values for the converse. Numerical checks are not a proof of general degree or of converse rigidity.

Run the standalone checker with `python3 verify_fibers.py`. It uses only the Python standard library and checks nine degree-two complete inverse fibers and nine perturbed configurations. Expected output: `VERIFY_OK degree_two_full_fibers=9 degree_two_off_fibers=9`. No independent audit has been conducted.
