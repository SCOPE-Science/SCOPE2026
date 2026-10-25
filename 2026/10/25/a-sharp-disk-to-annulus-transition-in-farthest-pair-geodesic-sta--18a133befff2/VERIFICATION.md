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

# Reproducibility and verification notes

The companion `verify_annulus.py` uses Python 3 and NumPy. It computes the tail probability by integrating, with Gauss–Legendre quadrature, the exact angular-measure condition given the endpoint radii; the angular threshold switches at the tangent-circle joining length. The program evaluates 12 critical-hole-scaling scenarios and 6 fixed-hole scenarios and checks their ratios to the stated leading asymptotics. All 18 scenarios passed; the largest observed relative deviation was below 1.75% for the crossover cases and below 1.17% for the fixed-hole cases. These are finite numerical diagnostics, not rigorous error enclosures. The integral defining the crossover coefficient was also independently integrated in SymPy; symbolic simplification confirmed the stated piecewise expression and agreement at the transition value.

The mathematical proof is contained in `RESULT.md`: it specifies the exact path geometry, distribution normalization, endpoint localization, radial and angular rescalings, limiting integration domains, and monotonicity required for inverse recovery. The checker does not establish the endpoint limits for every parameter or prove that no alternative historical result exists. No third-party proof verification or independent audit has been performed.
