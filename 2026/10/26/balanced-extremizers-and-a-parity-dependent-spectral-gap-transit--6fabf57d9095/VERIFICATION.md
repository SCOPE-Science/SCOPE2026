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

# Reproducibility and limits

The exact operator on homogeneous holomorphic polynomials is diagonal in the monomial basis. The proof gives two different conditional-beta integrals that must agree, one using the independent aggregate \(V=X+Y\) and proportion \(U=X/V\), and the other integrating the marginal \(X\) and conditional \(Y/(1-X)\). These are implemented separately in `check.py`.

Run `python check.py` in a directory containing the supplied source. The script requires Python 3, NumPy and SciPy. The expected run transcript is the included `verification_output.txt`, reporting 5190 passed assertions. Tests cover the explicit eigenvalues, independent integration, strict top ordering in several dimensions and degrees, the odd and even second-eigenvalue formulas, odd-degree branch differences at two thresholds, beta-binomial rational identities, and convergence to the chi-square edge limit.

The finite tests do not establish any universal inequality on their own. The infinite-degree and continuum-threshold assertions are proved analytically in the accompanying theorem. Independent scientific audit: not performed.
