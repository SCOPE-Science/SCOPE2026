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

# Reproducibility

Execute `python3 verify.py` using Python 3 and its standard library. It uses only exact modular arithmetic and explicit finite-field quotient rings. Successful output ends in `VERIFY_OK`.

The script recomputes the characteristic-seven coefficients of \((x^5+ax+b)^2\) and \((x^5+ax+b)^4\); reproduces the two Cartier blocks and \(2a^2(a^5-b^4)\); verifies the nilpotent exceptional chain; checks the seven-element-field discriminant parameter census; counts points for \(y^3=x^5+1\) over \(\mathbb F_7,\mathbb F_{49},\mathbb F_{343},\mathbb F_{2401}\); and derives the unique degree-eight Weil numerator from its first four coefficients and the functional equation.

Results: \((8,50,344,2094)\) and \(L(T)=1-77T^4+2401T^8\). The \(7\)-adic polygon has slopes \((1/4)^4,(3/4)^4\). Finitely many point counts alone do not establish the all-extension parameter census: its proof is the explicit cusp parametrization and Cartier determinant. The independent-audit channel has not been performed, and literary originality is qualified by the access limitation described in the review.
