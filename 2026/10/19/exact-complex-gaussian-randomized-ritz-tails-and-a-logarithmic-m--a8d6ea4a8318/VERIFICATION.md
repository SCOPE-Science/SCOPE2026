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

# Verification of the exact randomized Ritz distributions

The analysis proves a lower-triangular compressed pencil and invokes Haar invariance of its null line to represent the two random correction coefficients as ratios of independent circular complex-normal variables. A second independent-Gaussian linear combination proves the \(qV/U\) reduction; the exact CDF, expectation and radial tail follow from elementary exponential integrals. Divergence of the raw eigenvalue second moment follows by integrating the exact \(1/t\)-order tail in its squared magnitude. The small-angle coefficient follows analytically from \(q\sim (b/a)^2\theta^2\) and \(\Phi(q)=-q\log q+O(q)\).

Run the included standalone script with `python verify.py` (Python 3, NumPy and mpmath). The script was executed successfully. It checked six high-precision integral identities; the special uniform law at resonance; four small-angle asymptotic sanity cases; and direct batched Gaussian compressed matrices at four trial-space angles, with 110,000 independent sketches per angle. For each angle it checked the exact triangular structure, mean, five normalized-angle CDF cutoffs, and four radial eigenvalue-tail cutoffs. All programmed assertions passed. The direct simulation sample size and tolerance are finite; neither the universal CDF nor the infinite-moment conclusion is certified by Monte Carlo.

There has been no external audit. The statements are limited to the exact square complex-Gaussian pencil and the specified diagonal Hermitian trial-space model. See RESULT.md for definitions, steps, the explicit output branch, and the previously known results.
