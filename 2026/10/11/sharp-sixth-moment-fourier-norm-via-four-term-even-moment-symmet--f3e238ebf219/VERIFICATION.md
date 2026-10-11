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
# Verification and limits

The analytic certificate has four parts: (i) coefficientwise majorization after expanding the integer even moment; (ii) monotonicity of the Laurent constant term in nonnegative autocorrelations; (iii) the four elementary autocorrelation comparisons under pair root-mean-square symmetrization; and (iv) an exact sixth-moment polynomial with derivative factored by a quintic having one positive root. Equality uses strictness in the autocorrelation comparisons and the phase alignment of the coefficients of degrees two and three in the cubic polynomial.

Run `python3 artifacts/verify.py` from the extracted file bundle. It independently checks the coefficient polynomial and derivative coefficients using integer arithmetic, exact rational autocorrelation identities and Cauchy--Schwarz inequalities, and deterministic grid tests for complex vectors. All exact tests are finite algebraic checks and do not constitute an exhaustive search over coefficients or an independent audit.

The result is restricted to frequency support \(\{0,1,2,3\}\) on the continuous circle; there is no implication for finite cyclic grids with aliasing or exponents not covered in the theorem. A potentially equivalent earlier low-degree exact-constant calculation remains a documented originality risk.
