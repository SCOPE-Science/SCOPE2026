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

# Verification scope
The file `verify_projection.py` uses Python's standard library only. The command `python3 verify_projection.py` returned `VERIFY_OK wedge_pairs=3750 curved_cone_expansions=12`.

The planar tests evaluate the exact piecewise projection formula at 3,750 deterministic pseudorandom point pairs, comparing their quotient with the analytic rank-one operator-norm expression. The curved-cone tests produce 12 strictly expanding pairs with positive normal displacements for four non-Hilbert exponents and three positive apertures. The checker also verifies that the rank-one formula is one precisely on sampled Hilbert or symmetric-aperture regimes.

# Logical limits
Finite tests cannot establish an infinite collection of exponent/aperture claims, global sharpness, uniqueness of a minimizer, or absence of historical coverage. The self-contained proof in `RESULT.md` supplies those mathematical deductions (except the explicitly unclaimed historical exclusivity and unclaimed higher-dimensional exact Lipschitz constants). No external independent audit is claimed.
