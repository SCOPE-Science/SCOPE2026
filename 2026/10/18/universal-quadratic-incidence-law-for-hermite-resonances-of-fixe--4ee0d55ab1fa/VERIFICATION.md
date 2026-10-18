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

# Mathematical verification

The eigenvalue identity is derived using the normalized Gaussian and Hermite basis. The pairwise ratio is a conditional moment of a strictly increasing power; differentiation of both moving endpoints supplies strict positivity for every finite inner radius. Poisson tails at the zero inner radius and the divergent large-radius ratio supply existence. The exact adjacent difference forbids triple resonance. The lattice count is rigorously sandwiched between two identric-mean geometric-mean counts differing only by a fixed horizontal shift; the limiting planar area is evaluated by a two-variable substitution.

Numerical check (not an infinite proof): `python check_annulus.py` with Python, NumPy and SciPy. The checker solves 15 crossing equations across three widths and five index pairs, checks strict brackets and nearby ratio signs, integrates the limiting constant and reports geometric-mean incidence lower/upper brackets for radii 20, 40, 80, 160 and 300. It prints `All specified finite checks passed; infinite theorem proved analytically.` when all assertions hold.

The script's incomplete-gamma and floating-point operations are not a proof or certified enclosure of the universal constant. The exact analytic integral is the theorem's authoritative constant, and the decimal digits are approximate. No claim concerning distinctness of unrelated pair-crossing radii, an effective error term, or arbitrary non-Gaussian symbols has been established. Independent mathematical audit has not been performed.
