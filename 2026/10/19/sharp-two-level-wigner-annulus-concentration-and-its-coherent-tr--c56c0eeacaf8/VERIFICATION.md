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
# Reproduction and checks

The artifact `check_wigner_annulus.py` uses Python 3 with NumPy and SciPy and contains no data dependency. Run `python check_wigner_annulus.py` from the extracted package directory. The recorded execution returned `ALL CHECKS PASS` after 36 direct Wigner Fourier integrations, 24 independent physical-annulus integrations, 400 random domain optimizer checks against five competitors each, and 20 comparisons with thin-shell limits. At \(s=1\), \(t=3\), the optimal excited population was approximately \(0.457976476333779\), and the strictly positive gain over the better pure Hermite state was \(0.200152423538054\).

The analytic proof, not the finite sampling, establishes all claims for arbitrary \(0<s<t<\infty\). The key identities to check are the cross-Wigner Gaussian integral, the polar Jacobian \(2\pi r\,dr=du/4\), the quadratic derivative values \(4U\) and \(-2V\), and the thin-shell expansions. Numerical quadratures use finite tolerances and do not constitute rigorous interval enclosures. No independent audit has been performed.
