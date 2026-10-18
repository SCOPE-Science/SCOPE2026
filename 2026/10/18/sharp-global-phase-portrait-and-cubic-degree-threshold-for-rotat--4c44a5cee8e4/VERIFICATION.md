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

# Mathematical verification

The claim was checked by rederiving the rotation-weight normal form, independently differentiating the real Cartesian cubic, analyzing the exact discriminant and sign of the squared-radius polynomial, and proving that a strictly increasing proper radius map gives a global smooth inverse. All quantifiers are for all real \(s\ge0\), all starting \(z\in\mathbb C\), all positive integers \(q\ge2\), and all rational or irrational circle angles as appropriate.

The standalone `verify.py` uses only Python's standard library. Executing `python verify.py` returned `VERIFY_OK`: exact Fraction arithmetic checks the Cartesian-vs-radial Jacobian identity at multiple independent rational parameters and states; the \(q=2\) coefficient invariants are exactly \(m=d=5/16\), \(c=3/16\), and \(Q(1)=2\). Samples for periods \(3\) through \(18\) confirm the analytic formulas to numerical tolerance, but are not used to prove the all-period assertion.

The determinant criterion and uniqueness of the invariant circle are proved directly in RESULT.md, so no finite samples, floating-point outputs, source abstracts, or logs substitute for the infinite statements. The strict boundary excludes the singular-Jacobian equality case. The results do not require external formal certification, and no independent audit has yet been conducted.
