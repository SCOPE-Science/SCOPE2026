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
# Verification record

The standalone `verify.py` checker was executed from the extracted package. Its successful marker was:

`CROFTON_PAIR_ANGLE_OK quadratures=20 inverse_cases=1500 width_weighted_shapes=3 direct_line_shapes=3 pairs_per_shape=110000`

The midpoint quadratures independently integrate directional widths. The inversion trials use independently generated nondegenerate parallelogram parameters. The independent pair-angle simulations employ both width-weighted acceptance and direct line-offset rejection against projected vertices. The latter directly checks the motion-invariant hitting-line convention. Tolerances are deliberately broader than expected sampling fluctuations; the complete all-parameter proof is analytic and is contained in `RESULT.md`.

Only self-review has been performed. No external mathematical audit or certification is claimed. The results are statements for exact population expectations, not finite samples.
