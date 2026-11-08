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

With Python 3 and SymPy available, run `python check.py` in the extracted package directory. The resulting successful run reported `PASS 475 independent rational resolvent and derivative comparisons; six phase witnesses; exact symbolic identities`. The code independently constructs the two-component conditional-coherence matrix and compares its exact inverse against the proposed analytic response on a full Cartesian grid of rational/surd points. It also compares 300 seeded rational derivative samples, verifies the exact rational identity and factorization symbolically, verifies the unique constant-flux response and elastic/inelastic decomposition, and verifies representative maximization/minimization/monotonicity witnesses.

The all-real-parameter assertion is **analytical**: the sign of the derivative is the sign of a product of two affine factors whose slopes and intercepts are classified in the proof. The finite checks are diagnostic and do not prove completeness, uniqueness, physical validity beyond weak excitation, or independence from earlier published mathematics. The environment is required to be ergodic, hence zero switching is handled as a one-sided limit. Independent scientific audit remains unperformed.
