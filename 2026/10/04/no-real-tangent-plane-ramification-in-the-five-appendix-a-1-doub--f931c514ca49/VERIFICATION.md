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

The exact verifier reconstructs the five Appendix A.1 symmetric pencils, expands each determinant over the rationals, extracts the degree-two part in two normal coordinates to the double line, and computes the binary discriminant \(B^2-4AC\). It checks the stated factorization for all five cases, tests each quadratic factor for positive definiteness using its exact binary discriminant, and checks coprimality of the two factors. These checks prove that no real point of the double line is a tangent-plane coalescence point and that the complex coalescence divisor has four distinct points.

Run `python verify.py`. A successful replay prints `VERIFY_OK`.

The verification does not test or claim a universal theorem for all double-line spectrahedral symmetroids, nor does it settle the missing \((0,0)\) node-count case.
