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

The exact self-contained script `CHECKER.py` was executed using a Python standard-library environment. It enumerated *all* box-slice vertices by fixing all but one coordinate at a bound, then compared them with the two closed vertex formulas. The bounds were rational, with \(\epsilon=1/(3n)\), and arithmetic was exact. The complete domain \(4\le n\le9\), \(2\le k\le n-2\) and both orientations produced 42 successful checks of the full vertex sets, comprising 7540 vertices.

The same checker verified that each perturbed vertex has exactly \(n-1\) active coordinate facets, that the upper and lower resolutions have respectively \(k\binom nk\) and \((n-k)\binom nk\) torus-fixed points, and that these distribute as \(k\) and \(n-k\) per old vertex. These computations do not establish general fan regularity, semigroup normalization, or birational crepancy for all dimensions; the mathematical proof in `RESULT.md` supplies those arguments.

All code uses the Python standard library and can be rerun with `python CHECKER.py`. Results are recorded in `CHECKER_OUTPUT.txt`.

No external or independent mathematical audit has occurred; no certification is asserted.
