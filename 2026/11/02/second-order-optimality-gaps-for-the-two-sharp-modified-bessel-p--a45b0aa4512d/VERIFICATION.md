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
# Verification of exact coefficients and asymptotic claim

The standalone script `CHECK.py` requires the packages in `requirements.txt` and prints `CHECK_OK 33` when its symbolic and supplementary numerical checks pass.

The script reconstructs four Debye coefficient polynomials using the published recurrence, checks the first two even product coefficients, and derives both correction functions directly by algebraic inversion and logarithmic differentiation. It then verifies the exact values, second derivatives, derivative-based optimizing shifts, and the two completed-square identities used at global extrema. Numerical optimizations for several moderately large real orders support the asymptotic coefficients but are not a substitute for a proof over all orders.

The analytical proof requires two external mathematical inputs: the established global sharp bounds and differential identities for the modified-Bessel product (Segura--Suzuki, arXiv:2610.07933), and the classical all-orders differentiated Debye expansion on compact subsets of positive rescaled arguments (NIST DLMF Section 10.41). The new logical bridge is the local-maximum barrier implying global-maximizer localization, after which the standard compact asymptotics justify the extremal expansions.

No independent audit has been performed. The result gives no explicit onset value for eventual uniqueness and no effective constant for the order-four remainder.
