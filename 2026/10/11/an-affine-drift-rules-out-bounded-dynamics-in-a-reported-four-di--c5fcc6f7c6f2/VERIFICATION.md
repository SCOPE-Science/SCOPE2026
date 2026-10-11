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

The exact vector field checked is
\[
\dot x=-x-4y,\qquad \dot y=x+z^2+a w,\qquad \dot z=1+x,\qquad \dot w=-b y.
\]
For \(F=w-\frac{b}{4}(x+z)\), direct substitution gives
\[
\dot F=-by-\frac{b}{4}((-x-4y)+(1+x))=-\frac b4.
\]
`VERIFY.py` encodes the relevant polynomials with exact rational coefficients and verifies coefficient-by-coefficient that the Lie derivative equals exactly \(-b/4\). It uses no floating-point arithmetic or external package.

The logical consequences were checked separately. If a forward-complete trajectory were bounded, the affine function \(F\) would be bounded, contradicting its nonzero linear drift for \(b\ne0\). A nonempty compact positively invariant set would contain such a trajectory. For an invariant probability measure with compact support, invariance of the integral of \(F\) contradicts the exact translation \(F\circ\phi_t=F-bt/4\).

Limits: the check does not address \(b=0\), finite-time blow-up versus asymptotic escape, numerical discretizations, the altered 2022 fourth equation, or coupled/controlled extensions.
