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

The result is established by four finite-symbolic reasoning steps over arbitrary odd finite fields: splitting of the reciprocal quartic over the quadratic extension; a four-to-one root parameter map; fixed even subsets modulo complement; and fixed perfect matchings for each Frobenius cycle type. The bound on the splitting field is algebraic and does not rely on sample counts.

The standalone checker `verify_richelot.py` was run against every smooth parameter over prime fields of orders \(3,5,7,11,13,17,19,23,29,31\), totaling 138 parameter checks. It enumerates roots over quadratic extensions, all fifteen maximal isotropic matchings, rational two-torsion and the exact frequency distribution. It finished with `D4_RICHELOT_FROBENIUS_FREQUENCIES_PASS`.

This finite execution does not check the infinitely many nonprime prime powers, does not compute isomorphism classes of targets, and is not independent verification. Potential earlier equivalent formulas remain a scientific-priority risk.
