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

# Analytical and supplementary verification

The polynomial-core identity was derived directly using the orthonormal basis \(e_n(z)=\sqrt{m!/(n+m)!}\,z^n\) and \(Je_n=\sqrt{n+m+1}e_{n+1}\). The proof separately establishes the high-energy necessity and closure sufficiency. No numerical experiment is used as evidence of positivity for all matrix sizes or levels.

The standalone `verification/verify_affine_fock.py` (Python 3; requires NumPy) can be run from any directory with `python verification/verify_affine_fock.py`. It reported `supplementary finite assertions passed: 3789` on actual execution. It tests random complex matrix coefficients in dimensions 1, 2, 3 and Sobolev indices 0, 1, 3, 7; exact interior block formulas; trace cancellations; and a genuinely nonnormal example. It intentionally omits artificial top truncation boundaries. Exact symbolic calculation for the example also gave \(P=\begin{psmallmatrix}5&-1\\-1&5\end{psmallmatrix}\), \(G=0\), and \(K=0\), with eigenvalues 4 and 6.

Limits: finite truncation is not an infinite-dimensional proof, and numerical `allclose` assertions are not exact algebraic certificates. The analytical trace cancellation, packet limit, polynomial domains, and closure argument provide the infinite-dimensional reasoning. No independent audit or external validation has been performed.
