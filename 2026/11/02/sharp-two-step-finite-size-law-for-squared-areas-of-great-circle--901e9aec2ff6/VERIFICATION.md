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

Execute `python3 verify.py` using Python 3.9 or later; only the standard library is required. It reconstructs exact rational Dirichlet polynomial moments, the three planar integral normalizations, and the coefficients in the claimed expansion. The expected final line is `ALL_EXACT_MOMENT_IDENTITIES_PASSED`.

## Checked versus unchecked

The executable checks the explicit finite algebraic sublemmas: normalized simplex moments \(4/21\), \(32/165\), \(14/33\), the resulting integrals \(I_0=4\pi^2/7\), \(I_R=32\pi^2/11\), \(I_T=8\pi^2/11\), and the coefficients \(-10\), \(65\), and \(-28\pi^2/11\). The proof in `RESULT.md` separately establishes the three-probe Crofton identity, the geometric distance expansion, and integrability of the remainder. Numerical quadrature comparisons for three finite values of \(n\) were supplemental and do not certify the asymptotic remainder. Neither historical uniqueness nor independent mathematical audit is certified.
