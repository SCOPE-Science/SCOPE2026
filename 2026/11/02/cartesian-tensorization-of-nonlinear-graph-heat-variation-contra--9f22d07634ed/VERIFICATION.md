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
# Verification performed

The executable `verify.py` is self-contained and requires only Python 3 standard libraries. Run `python verify.py`. Exhaustive three-valued inputs were tested on three Cartesian product examples for three integer exponents, with 393,660 exact derivative comparisons and no failures; the four-leaf-star lifted counterexample returned exactly 2. This is supporting finite evidence, not universal verification.

The general result instead follows by the edgewise monotonicity/Kato argument and a convex directional derivative inequality, as proved in RESULT.md. Ties and zero gradients are included by taking all allowed absolute-value subgradients. Product converse uses coordinate-lifted solutions. No independent scientific audit has been conducted.
