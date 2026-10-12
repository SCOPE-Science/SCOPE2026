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
# Verification
The proof was checked by two complementary same-model methods. First, the Gaussian-cell expansion was derived by Taylor-expanding the exact interval integral, and the binomial entropy term was reconstructed from Stirling's formula together with exact centered moments. Second, `verification.py` computes the finite-sample KL divergence directly from binomial masses and Gaussian cell probabilities in the log domain.

The checker verifies numerical evenness \(D_n(c)=D_n(-c)\), tests that the midpoint phase is smaller than several nonzero phases, and checks convergence of the scaled quantities toward \(1/9\), \(1/2\), and \(-1/18\). The output file records `VERIFY_OK`.

The finite computation is not an exhaustive proof over all \(n\) or \(c\); the global finite-sample minimization is instead established analytically by strict convexity and symmetry. The asymptotic statement is likewise analytic, with tail control supplied by a binomial Chernoff bound. No claim is made for phases growing with \(n\) or for nonsymmetric parent laws.
