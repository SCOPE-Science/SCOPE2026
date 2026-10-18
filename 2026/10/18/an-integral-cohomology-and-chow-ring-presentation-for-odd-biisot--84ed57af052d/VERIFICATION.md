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

# Verification

The accompanying CHECK.py is standalone and depends only on the Python standard library. Run `python3 CHECK.py`. It evaluates the complete middle Schubert intersection matrix for each integer n from 2 through 35, verifies unimodularity and the selected high-degree unit-triangular pairing minors, and cross-checks coefficients through n=12 using independent two-variable monomial extraction. The independent methods agree in these finite ranges. Its finite range is not an exhaustive proof for all integers.

The theorem for every n >= 2 is established by the all-n Schubert complement and Pieri argument, the determinant recurrence, integral weak Lefschetz, the available affine-paving ranks, and integral Poincare duality. No independent audit is represented.
