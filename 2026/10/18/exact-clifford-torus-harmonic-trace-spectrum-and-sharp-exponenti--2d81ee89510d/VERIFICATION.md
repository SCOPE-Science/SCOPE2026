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

# Reproducibility and limits

The finite checker `check_exact.py` evaluates two mathematically independent formulas with exact rational arithmetic: the normalized Jacobi-mode restriction sum and the torus Fourier coefficients of the three-sphere addition kernel. The checker verifies all admissible Fourier modes for \(1\le L\le9\), and the exact trace, dimension, rank and minimizer multiplicities. Execute `python check_exact.py` from the extracted package directory. All identities for arbitrary \(L\ge1\) are justified symbolically in `RESULT.md`; finite computation alone does not certify them for every \(L\).

The Hilbert measures in this package are probability-normalized. The domain is the strict degree-\(L\) low-pass scalar harmonic space, the codomain is the Clifford-torus \(L^2\) space, and the inverse is the minimal-domain-norm right inverse restricted to the exact range. No independent external audit, experiment, or proof certification is asserted.
