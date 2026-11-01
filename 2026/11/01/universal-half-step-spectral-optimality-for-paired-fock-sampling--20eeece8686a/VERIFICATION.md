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

The reproducible checker `verify.py` computes two independent eigenvalue representations of the same finite Gram matrix: a cyclic Fourier-block series and a direct complex Hermitian Gram construction. It ran without error and reported `passed checks 448`. The tested cases include seven polygon orders, four radius pairs (including equal radii), and seven comparison-angle ratios. These are finite checks only.

The proof of all-order spectral optimality uses the established theorem that generalized hypergeometric functions \({}_0F_q(;b;z)\) with all \(b_j>0\) have only negative real zeros, the gamma multiplication identity, Hadamard factorization for order below one, and exact block convexity. Independent audit: not performed.
