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

# Reproducibility and proof boundaries

Run `python3 verify.py` with NumPy installed. The script evaluates the cycle Laplacian for \(3\le n\le40\), including both parities, at six ratios \(h/h_n^*\in\{1.00001,1.01,1.1,2,5,100\}\), and checks that the constructed quotient Jacobian has exactly one negative and no zero eigenvalues. It also checks positive orientation at the zero configuration. The expected program output is `VERIFY_OK negative_orientation_samples=228 ring_sizes=38`.

An additional exact-arithmetic spot check for the triangle at \(h=1\) and edge cosines \((-1/2,-1/2,1)\) gives the full vertex Jacobian eigenvalues \(1,5/2,-1/2\), illustrating the single negative quotient orientation.

The numerical check verifies only sampled finite cases and uses standard floating-point eigensolvers. It does not validate arbitrary graph sizes, parameter values or the topological-degree argument. The exact proof instead relies on the strict inequality for sine secants, the explicitly known cycle Laplacian Fourier spectrum, the rank-one positive-semidefinite decomposition at the critical cosine, and degree \(+1\) on the connected quotient torus. A separate independent audit has not been performed.
