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

# Exact certificate and its scope

Install SymPy, then run `python checker.py` from this directory. The checker reconstructs the full real twelve-by-sixteen intensity-measurement matrix, checks that it has rank twelve, checks that the displayed Hermitian pencil belongs to the kernel, and computes the real and imaginary parts of its sixteen three-by-three minors. An exact rational Gröbner basis is recomputed and four explicit ideal-membership residues are checked to vanish. These implications force the rank-two determinantal variety to intersect the kernel only at zero, proving universal cubic phase retrieval without numerical experimentation.

It also checks equality of two non-phase-equivalent cubic polynomials on the unique lower-radius twelve-site Gaussian-integer three-square configuration. All comparisons are exact symbolic expressions over rationals, Gaussian integers, and radicals. The implementation is a reproducible computational proof certificate rather than independent scientific validation. The initial source date refers to the 2024-03-24 posting of arXiv:2403.16255; older literature is cited only as background.

The asserted radius optimum is confined to three distinct complete fourfold nonzero Gaussian-integer orbits. No optimal stability coefficient, full-spectrum uniqueness, or global cardinality minimum for arbitrary measurement vectors follows.
