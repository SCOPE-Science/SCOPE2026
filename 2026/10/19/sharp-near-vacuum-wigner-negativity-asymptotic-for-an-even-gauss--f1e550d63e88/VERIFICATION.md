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
# Verification notes

The analytic verification is the full proof in `RESULT.md`: the Gaussian Wigner normalization, exact negative-region edges, removal of higher fringes by Gaussian tail estimates, scaling limit with an integrable majorant, exact gamma integral, and third-order angular-edge expansion collectively imply the asymptotic.

Reproduction: run `python checks/check_cat.py` with Python 3 and `mpmath`. At 75 decimal digits, the script tests the exact Wigner expression against three independently evaluated defining oscillatory integrals, then evaluates the two nearest symmetric negative lobes by exact integration over the transverse position coordinate. The ratios of this first-pair mass to the claimed asymptotic at \(a=0.35,0.25,0.20,0.15\) were approximately \(0.828432180137\), \(0.888463324694\), \(0.915728890810\), \(0.940715014276\), respectively, increasing toward one. All script assertions passed.

The checker does **not** sum the infinitely many distant lobes. Its finite results alone establish neither the full integrated-volume asymptotic nor publication priority; higher-lobe negligibility and the unrestricted limit are proved in `RESULT.md`. No independent mathematical audit has been performed.
