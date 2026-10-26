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
# Verification of the balanced collective-risk theorem

`RESULT.md` supplies the complete analytic argument. In the attached `verify.py`, the symbolic check confirms that the displayed gradient of the first integral has vanishing dot product with the vector field and has commuting mixed partials, for formal positive parameters and exponent. The general equilibrium Hessian is checked against two explicit positive diagonal formulas, without treating finite integer samples as proof.

For the admissible illustrations with \(a\in\{1,2,3\}\), \(b=1\), and \(c=\varepsilon=1/10\), the program solves the ODE at high tolerance, detects the first same-direction section return, and uses adaptive quadrature over exactly that computed physical-time period. It checks the mean-cooperation identity, the inverse-gain mean-risk identity, and the strict risk-variance inequality. Illustrative numerical return times are approximately \(9.93487185\), \(10.37701979\), and \(10.77704919\), respectively. These checks corroborate but do not establish the infinitely many cases in the theorem.

To reproduce, use Python 3 with NumPy, SciPy, and SymPy installed, from the directory containing this file and `verify.py`, and execute `python verify.py`. The analytic proof needs no numerical quadrature, no database table, and no external certificate. Priority verification beyond the documented literature comparisons and independent scientific review have not been performed.
