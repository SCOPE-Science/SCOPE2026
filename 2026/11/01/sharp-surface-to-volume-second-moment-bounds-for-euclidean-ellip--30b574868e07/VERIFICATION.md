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

# Reproducibility and verification

Run `python verify.py` with Python 3 and NumPy. The verifier independently calculates the surface covariance by deterministic spherical quadrature of the Euclidean surface Jacobian and through the Gaussian mixture. It reports eight example ratios, all inside the proved sharp bounds; it also checks 99 exact weighted-angular identities in dimensions \(2\) through \(100\), 48 exact ball equalities, and 48 exact comparisons of upper and lower constants.

The proof reconstructs all normalizations explicitly: ellipsoid surface Jacobian \(|\det A|\|A^{-1}u\|\), interior covariance \(A^2/(d+2)\), weighted spherical second moments \(2/(d+1)\) and \(1/(d+1)\), and positive-definite Gaussian weight matrix of unit trace. The critical inequality is proved through strict convexity of the logarithm of a Gaussian mean norm, not inferred from sampling.

The code covers selected dimensions two and three numerically. Its exact rational comparisons check finite identities but are not a machine proof of the integrals or of the universal theorem. The published-source overlap comparison is provisional; independent validation has not been performed.
