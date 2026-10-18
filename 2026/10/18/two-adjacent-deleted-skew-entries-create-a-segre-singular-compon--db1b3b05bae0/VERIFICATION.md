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

The standalone `verify.py` enumerates every nonzero point of the 13-coordinate binary affine space for the six-vertex model (8191 projective points over the two-element field). It compares the gradient of the restricted Pfaffian to the stated reduced component union independently of matrix rank, and returns `VERIFY_OK` only if all points match. The comparison found 351 singular points, all accounted for by the union.

The same script checks Hessian rank six at rational witnesses on each of the three six-vertex components, rank six at an explicit generic-type rank-four witness for the eight-vertex corank component, and ranks 6, 10, and 14 at exceptional rank-two-corkernel witnesses for matrix sizes 6, 8, and 10. These integral calculations corroborate exact generic Hessian computations but do not certify all sizes; the mathematical proof uses the Pfaffian Schur complement and Grassmann incidence dimension arguments.

Run: `python3 verify.py`. No third-party packages or remote services are required. The self-contained proof is in `RESULT.md`. Independent audit is not performed.
