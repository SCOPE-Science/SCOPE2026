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

The standalone script `verify.py` uses only the Python standard library and requires Python 3.8 or newer. Run `python3 verify.py` in this directory. `verification_output.txt` records a successful execution.

The program independently implements the full graph-level one-point-extension recurrence for quantifier rank one on pairs, rank two on roots, and rank three on unpointed graphs for every dimension from one to nine. It compares the resulting isomorphism-invariant exact types, rather than only checking formula samples. It separately computes coordinate-orbit pair types for dimensions one through thirteen, tests the exact six separating sentences, and checks that all large-distance pair orbits share one pointed type from dimension seven onward.

Expected lines include `FULL_RECURSION_OK dimensions=1..9 classes=7 stable_from=7`, `ORBIT_REDUCTION_OK dimensions=1..13 stable_from=7`, `SEPARATING_SENTENCES_OK thresholds=2,3,4,5,6,7`, `SHARP_MINIMUM_REPRESENTATIVE_OK order=64`, and `VERIFY_OK`.

The bound of thirteen dimensions in the program is an implementation test, not a statement about all dimensions. The all-dimensional theorem is proved in RESULT.md by the explicit, exhaustive extension-support table and the three-round game argument. No external independent scientific validation has been conducted.
