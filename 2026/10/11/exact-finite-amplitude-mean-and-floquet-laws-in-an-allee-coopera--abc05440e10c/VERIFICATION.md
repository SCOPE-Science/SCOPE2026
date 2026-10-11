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

The analytic verification checks the following identities for the stated positive-domain system:

1. For \(H(y)=y+\beta\log y\), direct differentiation gives \(\dot H=-e+\varepsilon c x\).
2. For \(G(x)=\log x\), direct differentiation gives \(\dot G=a-bx-m/(x+\alpha)-cy\).
3. The reciprocal identity used after centering at \(x_*\) is exact and turns the predator-mean difference into a nonnegative weighted square.
4. The divergence equals the derivative of \(\log x+\log(y/(y+\beta))\) plus \(x[-b+m/(x+\alpha)^2]\), so both logarithmic pieces vanish over any positive period.
5. The bundled `verify.py` uses exact rational arithmetic to check these algebraic reductions at multiple rational values and verifies the Example 4 constants \(x_*=5/9\), \(y_*=143/280\), and defect coefficient \(1863/3920\).

The checker does not establish existence or uniqueness of periodic orbits and does not numerically certify the sign of the Floquet exponent. Those are outside the proved claim.
