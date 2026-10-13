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

# Verification of the two-mode Legendre-copula theorem

Run `python3 verify.py` from the directory containing the attached script. No third-party modules, external data, external network, or external proof system are required. On the reviewed script, execution terminated successfully with the exact final message `VERIFICATION_OK`.

The script builds rational bivariate polynomials for the copula, its mixed derivative, and its distributional integrals. It verifies the Spearman/Kendall formulas at six parameter nodes, uniquely determining a polynomial of total degree at most two in \((\lambda_1,\lambda_2)\), checks exact marginal integrals, and checks endpoint cases and the algebraic critical polynomial for the Kendall extremum. It then checks 33,371 deterministic numerical positivity/necessity cases spanning \(-1\le b\le2\), including the singular endpoints.

These checks confirm algebraic normalization and detect many implementation mistakes, but finite numerical samples do not prove all-real nonnegativity. The continuum proof in `RESULT.md` uses the exact feasible interval \(2\le s/t+t/s\le st+(st)^{-1}\), minimizes separately for nonpositive and nonnegative second-mode parameters, and compares boundaries analytically. No computer-assisted global optimization or omitted certificate is required. Source comparison and priority are not independently certified. No claim is made about statistical testing performance or other copula families.
