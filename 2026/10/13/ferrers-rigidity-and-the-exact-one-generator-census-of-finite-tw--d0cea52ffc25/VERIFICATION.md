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

# Reproducible finite checks

Run `python3 verify.py` with Python 3.9+ and assertions enabled. The program requires no packages beyond the standard library, no network access, and no external datasets. It computes modal partitions by iterative set-of-successor-types refinement, independently from the Ferrers test it compares against; it also verifies a saturation-based nontrivial bisimulation certificate without using the oracle's final labels and separately computes Boolean-algebra closures on small universes.

The executed verifier terminated successfully, emitting:

```
VERIFY_OK exhaustive_matrices 74954 rectangular_parameter_cases 16 explicit_bisimulation_core_checks 648 direct_boolean_algebra_closures 7 random_large_matrices 1680 generator_counts {'1x1': 2, '1x2': 2, '1x3': 0, '1x4': 0, '2x1': 2, '2x2': 8, '2x3': 12, '2x4': 0, '3x1': 0, '3x2': 12, '3x3': 72, '3x4': 144, '4x1': 0, '4x2': 0, '4x3': 144, '4x4': 1152}
```

All 74,954 valuations of every rectangle with one to four rows and one to four columns were exhausted; the 1,680 other matrices were reproducibly pseudorandom (fixed seed), plus explicitly planted canonical markings. Thus tests establish exact finite agreement only within the enumerated domain; they do not prove the theorem beyond four-by-four. The infinite family is covered by the structural argument in `RESULT.md`, not finite enumeration. No independent mathematical audit has been performed.
