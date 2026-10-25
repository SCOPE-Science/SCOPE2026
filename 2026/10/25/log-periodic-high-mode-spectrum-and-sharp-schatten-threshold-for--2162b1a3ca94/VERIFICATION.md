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

# Verification details

The finite-stage operator eigenvalues are beta-prime integrals of the Cantor intervals. The infinite measure's normalizations were checked on nested intervals: \(\nu([0,3^j])=2^j\), and its dilation identity is \(\nu(3B)=2\nu(B)\). The rescaled density limit and both tails are established analytically in the proof. Positivity, logarithmic periodicity and strict nonconstancy are all derived rather than inferred from graphs.

A reproducible standard-library diagnostic is supplied as `checks/numeric.py`. It uses the exact beta CDF for \(\alpha=1\) and finite Cantor-cylinder quadrature to compare \((3/2)^m\lambda_{\lfloor r3^m\rfloor}\) to the explicit limiting profile for \(m=3,4,5\), several \(r\), and a fixed larger Cantor truncation. Such finite comparisons do not prove convergence or the nonconstancy claim. No independent audit or validation is asserted.
