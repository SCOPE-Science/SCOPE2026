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

# Reproducibility of joint Hilbert-simplex distance fluctuations

The accompanying standalone `verify.py` uses Python 3.9 or newer and NumPy. Execute `python verify.py` from the directory containing the two files. A fixed pseudorandom seed makes the Monte Carlo sample reproducible.

The program checks: (i) the finite-\(N\) two-numerator, one-denominator probability with exact expression \((1-(1+Nx)^{-1}-(1+Ny)^{-1}+(1+N(x+y))^{-1})^N\) against its Galambos limit; (ii) the independent one-dimensional covariance integral against the analytic value \(\pi^2/9\); (iii) the exact uniform positive and negative tail estimates for centered directed log maxima; and (iv) a sample of \(3{,}000\) trials at \(N=4{,}000\) for four point labels, checking mean, variance, adjacent-edge covariance and disjoint-edge covariance.

All assertions passed at the declared tolerances. The proof of the joint limit is not a numerical extrapolation: it bounds cross-denominator event intersections by \(O(N^{-2})\), computes per-denominator exponents, and uses exact moment bounds and a closed-form covariance integral. The tests establish reproducible consistency only, not uniqueness in the literature or independent theorem certification.
