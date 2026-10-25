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
# Reproducibility checks

The attached `verify.py` may be run with Python, NumPy and SciPy. The code independently builds finite monomial-basis weighted-composition matrices using gamma functions; checks Hilbert–Schmidt coefficient orthogonality for complex nonmonomial polynomials; checks the singular-value perturbation inequality; and samples the predicted norm, all-\(p\) Schatten scaling (including a quasi-norm exponent), an exact Gaussian Fock Hilbert–Schmidt series and the two real Lambert-branch level counts.

The packaged `verify.py` completed 42 finite checks. These are supplementary consistency checks, not an exhaustive computation over all parameters or proof of an infinite-dimensional limit.

The proof's decisive steps are the exact gamma-ratio monomial singular values, their uniform envelope, Riemann-sum convergence, and \(o(\varepsilon^{-k/m})\) lower-degree operator-norm error together with the corresponding Schatten quasi-norm bound. Published source comparisons remain provisional because the 2013 and 2015 journal texts were not fully accessible.
