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

Use Python 3 standard library: `python3 verify.py`.

The checker implements the unit-group multiplication law for the radical-square-zero quiver algebra independently, computes conjugates of each unit under all other units, partitions them into true conjugacy orbits, and builds the resulting integer class-size histogram. A separate graph-support counting implementation predicts the histogram and compares coefficients exactly. Test cases span 17 quiver/field settings over the fields with 2, 3 and 4 elements, including directed cycles, four-cycles, loops, parallel arrows and disconnected vertices. Separate tests check three forest formulas and eight cycle formulas.

The saved `verify_output.txt` records all counted histograms and ends with `ALL_QUIVER_UNIT_TUTTE_CLASS_AND_SPECTRUM_CHECKS_PASSED 17 forest_3 cycle_8`.

These are finite exact checks only. General correctness rests on the algebraic proof given in `RESULT.md`, not on extrapolation from computations. The multiplicative class-size factor degenerates at field order two and must be aggregated when reading the ordinary numerical histogram. No independent audit has been performed.
