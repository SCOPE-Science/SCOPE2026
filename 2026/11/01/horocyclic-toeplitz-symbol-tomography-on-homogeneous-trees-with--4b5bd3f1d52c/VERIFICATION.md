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

# Verification and boundaries

The argument uses a previously published complete orthogonal basis [1, Theorem 14], but independently proves the stronger levelwise Gram cancellation needed for Toeplitz diagonalization. Each wavelet has total squared amplitude \(q^{m-1}c_m^2\) on the \(m\)-th descendant level; after weighting, this yields precisely the positive coefficients \(r^m(1-s^m)^2\). The convolution inverse is an identity between bounded bilateral-shift operators because every geometric-series factor has norm parameter less than one. The inverse norm is attained by the alternating sequence. For \(q=2\), \(\alpha=2\), the exact benchmark is \(\kappa=75/7\).

Execute `python checker.py` with SymPy installed. It checks the rational generating-function identity, the alternating-rational inverse norm, direct finite-tree wavelet cancellations, and sixteen parameter checks including the near-endpoint case \(\alpha=1.05\). Its output is a PASS line. The proof, not the finite tests, establishes the infinite-dimensional statements. The statement does not claim spectral-set-only inverse recovery, results for non-horocyclic symbols, or a complete assessment of historical publication priority.

References: https://arxiv.org/pdf/2309.15047 and https://arxiv.org/pdf/2505.03479.
