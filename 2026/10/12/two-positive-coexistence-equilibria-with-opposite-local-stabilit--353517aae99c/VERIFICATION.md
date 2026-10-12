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

# Exact computational verification

Run `python verify.py` with Python 3 standard library. The script computes rational bisection enclosures for positive roots of \(\phi(x)=h/10\) and \(\psi(y)=3h/10\), with monotonicity arguments supplied in `RESULT.md`. Every exponential bound uses a 70-term rational Taylor polynomial with a rigorous positive remainder majorant, valid on every argument encountered here. It checks \(F(49/10)>26>F(5)\) and \(F(9)<26<F(19/2)\), then computes narrow prey brackets and interval enclosures of the full Jacobian and characteristic polynomial.

The first branch's five Jury expressions are proved strictly positive. The second branch's \(\det(I-J)\) is proved strictly negative; the monic cubic therefore has a real root exceeding one. Successful replay ends with `VERIFY_OK`. All inequalities are checked as exact fractions, not trusted printed decimal approximations. The underlying analytical IVT, Schur/Jury, and implicit-function arguments are supplied in the proof rather than inferred from finite enumeration.

No globally attracting state, complete fixed-point census, population-data estimate, external independent validation, or higher-dimensional bifurcation classification is demonstrated. Independent audit has not been performed.
