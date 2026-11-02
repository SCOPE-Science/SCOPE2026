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

# Reproduction and verification

The theorem has a self-contained analytical proof in `RESULT.md`. In a radial sector of nonnegative angular degree \(m\), form the \(q\)-by-\(q\) positive Gram matrices \(H_m(1)\) and \(H_m(s)\) from the formulas in that document. Their positive generalized eigenvalues are the complete eigenvalues in that sector. This construction avoids needing a global spectral truncation.

Run `python checker.py` with a standard Python installation. The observed output was `PASS: 126 exact rational determinant and factorial identities`. It compares exact rational determinants of the full and truncated sector Gram matrices for several orders, degrees and rational cutoffs, and proves no claim about infinitely many parameters by finite enumeration. The reciprocal-factorial matrix identity is also established for every order algebraically in the proof.

Optionally install `mpmath` and run `python asymptotic_probe.py`. The observed output ended `PASS: 24 high-precision determinant and asymptotic-ratio checks`; the script prints all evaluated branchwise eigenvalue/prediction ratios at the specified orders, squared radii and Fourier degrees. Near-singular Hilbert-type Gram matrices require high working precision. These comparisons support debugging and normalization only; they are not a substitute for the all-order limits.

The key proof checks are: (i) exact change of variable relating subdisk mass to a degree-limited dilation operator; (ii) convergence of the bounded list of transformed moments to factorials and of orthonormal polynomials to signed Laguerre polynomials; (iii) unique highest-degree exterior-power minor and its nonzero falling-factorial determinant; (iv) division of consecutive exterior-power norms to obtain every singular-value constant; and (v) inversion of logarithmic eigenvalue asymptotics and cancellation of integer branch coefficients. The claim does not rely on an external certificate or an unverified infinite enumeration.

Independent mathematical audit and validation have not been performed.
