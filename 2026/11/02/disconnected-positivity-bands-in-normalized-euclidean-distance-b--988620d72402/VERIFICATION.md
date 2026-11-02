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

The proof derives the normalized coefficients from actual Euclidean-distance beta moments and establishes their locally normal continuation in the parameter. The crucial necessity-of-positivity step uses a circle Fourier-mode test, not a sampling heuristic. Even-prefix factor signs supply a complete classification for all nonintegral negative parameters; zeros of finite rising factorials supply the exact rank at every negative integer. The strict positivity statement additionally invokes finite Vandermonde invertibility.

Run `python3 kernel_check.py` to reproduce exact rational coefficient comparisons and selected finite-rank calculations. These finite calculations are supplemental consistency checks, not an exhaustive computation or an independent mathematical audit.

Normalization is essential: all negative-parameter assertions concern the continuation of \(K_t/K_t(0,0)\), uniquely defined originally for \(t>-1\). The continued kernels are not claimed to be Bergman kernels of positive nonintegrable weights. Earlier hypergeometric literature may implicitly contain equivalent coefficient-sign criteria.
