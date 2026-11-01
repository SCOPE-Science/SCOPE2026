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

# Verification of the stated finite-band theorem

The theorem is proved analytically in `RESULT.md`. It first changes variables to \(y=x^2\) in each parity sector, then uses exact Cauchy–Binet expansions for all elementary symmetric functions of the concentration matrix. The leading coefficient equals a Jacobi complementary Hankel minor times a Selberg integral. Scaling the characteristic polynomial at \(b^{\alpha+2k-1}\) isolates a simple nonzero root at every rank; the error in the elementary symmetric functions is \(O(b)\), and \(b=T^2\). No numerical extrapolation is needed for the general statement.

To reproduce supplementary checks, install the packages in `requirements.txt` and execute `python CHECK.py` in the directory of the extracted files. Execution with Python 3, SymPy and mpmath yielded `CHECK_OK 525`. It compares direct and product-form Hankel determinants for the Laguerre/Jacobi weights, checks the leading coefficients of every elementary symmetric function in representative matrix sizes and parameters, checks individual eigenvalues at three shrinking radii, and performs independent symbolic coefficient extraction for a three-dimensional Laguerre example.

An additional direct substitution into the closed-form constants, for the published generalized Gegenbauer example with \(N=12,\mu=1,\beta=1,T=1/16\), predicts the first eigenvalue \(0.0419934\) against the paper’s \(0.0386973\), the seventh \(6.88365\times10^{-18}\) against \(6.98\times10^{-18}\), and the twelfth \(2.86758\times10^{-35}\) against \(2.94\times10^{-35}\). These are asymptotic leading terms at a finite window, so agreement is indicative only, not exact identity.

The finite checks do not establish asymptotic validity for every \(N\) or every real weight parameter; those statements rely on the complete proof. The older reproducing-kernel literature was not entirely accessible, so the self-review originality assessment remains subject to potential earlier equivalent results. No independent audit or validation has been performed.
