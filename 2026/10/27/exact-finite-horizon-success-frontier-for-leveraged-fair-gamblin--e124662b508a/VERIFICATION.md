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

The substantive guarantee follows from the self-contained Bellman induction in `RESULT.md`. For a current wealth \(z\), a leverage \(L\), and remaining horizon \(k\), its critical point is \(z(M/z)^{1/k}\). The affine majorant is global on the entire legal interval, not just on sampled stakes; equality and uniqueness follow from the derivative's strict sign change.

Run `python check_finite_leverage.py` after installing the package in `requirements.txt`. Actual execution passed 15,375 sampled dual inequalities, rational finite-horizon examples, self-financing mean identities, Bellman recursion identities, strict monotonicity checks, and symbolic derivative/Taylor coefficients.

Checks of finitely many parameter grids do not establish the universal theorem; the paper's analytic argument supplies it. No independent audit or independent experimental certification is claimed. The checked program only depends on the attached files and PyPI SymPy.
