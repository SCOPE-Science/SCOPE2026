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

The proof has two independent exact components. First, the upper bound is obtained from the positive combination \(\cos(\pi/9)T(\pi)+T(7\pi/9)\), in which the \(\cos(4\theta)\) and \(\cos(5\theta)\) coefficients cancel. Sum-to-product identities reduce the resulting bound to \(2\cos(\pi/18)/\sqrt3\).

Second, with \(r=\cos(7\pi/9)\), the proposed extremizer is converted to a polynomial in \(x=\cos\theta\). The checker verifies the factorization modulo the exact relation \(8r^3-6r-1=0\), checks the contact and derivative identities, reduces the sharp coefficient to \(3A^3-3A-1=0\), and verifies that the residual quadratic has discriminant \(-64(80r^2-62r-13)\). On the intended root \(r\in(-1,-3/4)\), this discriminant is negative and the leading coefficient and denominator are positive, proving global nonnegativity.

The replay command is `python artifacts/verify.py`. The expected terminal line is:

`VERIFY_OK r=-0.766044443118978 A=1.137158042603257 B=0.313660917291061 C=0.176502874687803 cubic=3A^3-3A-1 factor_mod_p=1`

The numerical decimals identify the intended real root only; no finite sampling is used as proof of nonnegativity or optimality.
