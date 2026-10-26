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

# Reproducibility and checked limits

Run `python verify.py --check` with SymPy from the directory holding `verify.py`, `certificate.json`, and `verification-output.txt`. It recomputes exact symbolic quotient polynomials and rational coefficients, checks every certificate monomial and its positive sign, performs twelve direct exact-rational full double-star matrix-inverse tests, and checks the fourth-neighbor Padé obstruction including one exact negative entry. The displayed output must end `ALL CHECKS PASS`. No randomized approximation substitutes for the stated rational polynomial identities.

The mathematical proof also requires independently understanding the four-cell symmetry reduction, the invariance of leaf-class zero-sum subspaces, the eigenvalue-one action there, star spectral projectors, and the unique length-four tree geodesic. The matrix inverse test cases alone are not exhaustive; the symbolic coefficient certificate is a finite identity over arbitrary \(a,b,h\) and supplies the infinite-parameter proof.

External specialist literature might contain unobserved equivalent coverage; the observed search results cannot certify uniqueness. Independent audit is not performed.
