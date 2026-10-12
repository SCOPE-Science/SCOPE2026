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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

For every \(1\le a\le8\), it enumerates all subsets of the \(2a\)-vertex graph, computes the complete independence polynomial directly, identifies every maximal independent set, and compares both outputs with the closed formulas.

It separately checks the independence number, the number of maximum independent sets, the well-covered criterion, and the independent domination number.

The verifier also constructs representative annihilating-ideal graphs directly from divisor ideals in integer residue rings and tests zero products by divisibility, independently checking the algebra-to-graph reduction.

Exact replay output:

```text
a=1: polynomial=[1, 2, 0], facets=2, max_sets=2, well_covered=True, i=1
a=2: polynomial=[1, 4, 3, 0, 0], facets=3, max_sets=3, well_covered=True, i=2
a=3: polynomial=[1, 6, 8, 3, 0, 0, 0], facets=4, max_sets=3, well_covered=False, i=2
a=4: polynomial=[1, 8, 16, 13, 4, 0, 0, 0, 0], facets=5, max_sets=4, well_covered=False, i=2
a=5: polynomial=[1, 10, 26, 31, 18, 4, 0, 0, 0, 0, 0], facets=6, max_sets=4, well_covered=False, i=2
a=6: polynomial=[1, 12, 39, 63, 56, 26, 5, 0, 0, 0, 0, 0, 0], facets=7, max_sets=5, well_covered=False, i=2
a=7: polynomial=[1, 14, 54, 108, 126, 86, 32, 5, 0, 0, 0, 0, 0, 0, 0], facets=8, max_sets=5, well_covered=False, i=2
a=8: polynomial=[1, 16, 72, 174, 256, 236, 134, 43, 6, 0, 0, 0, 0, 0, 0, 0, 0], facets=9, max_sets=6, well_covered=False, i=2
Z/6Z direct ideal-product graph OK: vertices=2
Z/12Z direct ideal-product graph OK: vertices=4
Z/80Z direct ideal-product graph OK: vertices=8
Z/1215Z direct ideal-product graph OK: vertices=10
Z/875Z direct ideal-product graph OK: vertices=6
VERIFY_OK
```

The finite checks are corroborative. The arbitrary-exponent result follows from the symbolic classification by the largest selected \(B\)-index.
