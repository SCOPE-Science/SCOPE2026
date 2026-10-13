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

`verify.py` checks the exact integer-polynomial factorization underlying the sharp bound and numerically evaluates the cleared-denominator eigenvalue identities and several points of the large-root parameterization as consistency checks.

The mathematical proof does not infer an infinite statement from the finite evaluations. The global step is the exact identity
\[
\theta y^3-2=\frac{(r-2)^2(r+1)}{r^2-2},\qquad r=y^2>\sqrt2,
\]
whose denominator is positive on the entire stated domain. The eigenvalue ordering follows from the displayed cleared-denominator identities valid for every \(0<\theta<1\) and \(y>0\).

The verification establishes only the stated Kesten–Stigum bound. It does not prove extremality of the Gibbs measure, because Kesten–Stigum is used only as a sufficient non-extremality criterion.
