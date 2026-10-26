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

The analytic identity for the BDF2 generating polynomial is \(\delta(\zeta)+s=(3/2+s)(1-\lambda_+\zeta)(1-\lambda_-\zeta)\). This leads exactly to \(w_n=(p_n(ha)-p_n(hb))/n\) for \(n\ge1\) and the positive zeroth logarithmic coefficient.

Run `python3 checks/verify.py` using a standard Python 3 interpreter. Its exact-rational tests compare two independent coefficient generators: the two-root power recurrence and division of the derivative of the original logarithmic ratio. Checks cover 45 positive-index coefficients for six rational parameter cases, including the critical endpoint, then compare 150 complex-factor values for five cases. A positive instance with \(ha=1/4\) and negative instance with \(ha=1\) are included.

The strict positivity proof and infinitely-many-signs conclusion are analytical. The checker cannot certify infinitely many coefficients or novelty. Independent review has not been performed.
