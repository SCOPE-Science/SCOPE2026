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

# Verification of the regular-hexagon covering profile

The proof in `RESULT.md` certifies the full continuum of orientations and translations using an explicit six-facet Minkowski gauge, a convex triangle-cover lemma, two exact witness configurations, and elementary trigonometric inequalities. No finite calculation is used to infer an unproved universal conclusion.

To repeat the executable numerical diagnostics, run `python3 verify.py` with the Python standard library. The observed output is:

`PASS: 119356 deterministic covering-profile diagnostics`

The checker validates both closed-form constants; evaluates the active covering/empty-point certificates at 2,001 evenly spaced orientations; checks distances to every integer point in a fixed neighboring box; verifies 31 complete \(61\times61\) fundamental-square sample grids; and checks strict monotonicity of both branches on 2,000 sample angles. These are independent finite consistency checks only. The continuum coverage, global lattice exclusion, exact equality and optimal-angle classification rely on the symbolic steps detailed in the proof.

The covering radius applies to the full plane and the fixed square lattice. An independently audited mathematical proof, exhaustive historical-priority certification, and an extension to other lattices have not been performed.
