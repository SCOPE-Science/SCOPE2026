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

# Verification of the stated triangular-bipyramid formula

The mathematical proof is contained in `RESULT.md`, especially the six-facet table and the Minkowski normalization. To reproduce finite independent checks, run `python verify_bipyramid.py` with Python 3, NumPy and SciPy installed. The script does not call outside services or fetch literature.

The source computes 247 parameter instances using exact rational arithmetic. For each, it independently reconstructs the six reflected facet support values; obtains the difference-body convex hull from all pairwise vertex differences; triangulates its boundary with SciPy's convex-hull routine; and evaluates all signed simplex determinants exactly as fractions. It compares both independent routes with the closed formula and checks sharp endpoint sample cases. The verified output on the supplied script was:

`BIPYRAMID_GODBERSEN_VERIFY_OK cases=247 exact_facet=247 exact_hull=247`

The hull facet selection is floating-point geometric computation, so close-to-degenerate input could in principle trigger numerical combinatorial errors; all tested rational instances passed. Exact fractions remove floating-point volume accumulation errors once facets have been identified. Tests do not establish an infinite theorem, nor do they establish originality; the proof and the prior-work comparison are the relevant arguments. There is no independent external scientific audit.
