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
# Numerical and analytic verification

The reproducible `verify.py` uses NumPy and SciPy and was run from its actual location. It checks 800 seeded random vectors across dimensions one through eight and five nonnegative ridge parameters, including the unregularized case. It compares the direct one-column least-squares Anderson update with the independently rearranged half-sum identity and requires agreement at stated numerical tolerances. Six additional integrations test the dimension-one \(\varepsilon^{-1/2}\) coefficient and dimension-two logarithmic-increment coefficient at ridge scales \(10^{-5}\), \(10^{-7}\), and \(10^{-9}\). The recorded verifier output is `PASS 806 fixed-input update identities and asymptotic checks`.

The proof itself does not depend on a Monte Carlo tail estimate. The sharp moment integrability and divergence use full polar integration near the nondegenerate Gaussian denominator's origin. Leading small-ridge constants follow from explicit singular radial integrals and a separate error-bound argument. The code does not certify statements outside the displayed assumptions, and no independent review or independent formal certification is represented.
