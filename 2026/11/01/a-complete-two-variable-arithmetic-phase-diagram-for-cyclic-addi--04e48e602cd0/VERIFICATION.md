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

The proof's critical finite invariants were cross-checked by two standalone programs included in the same package. `verification/verify_types.py` refines exact unary types using all substitutions of two variables into the ternary addition relation (not a function-term language), and compares every pair of cyclic moduli from 1 to 160. It reports 12,720 pair comparisons and no disagreement. `verification/verify_palette.py` separately builds full first-order two-pebble one-step support palettes for each element, compares class palettes for all moduli in that range and tests representative equivalences and separations; it reports 1,378,160 ordered pairs examined and zero disagreements. Both scripts use only Python 3 standard-library modules. Their output snapshots are provided next to the code and can be replayed with `python3 verification/verify_types.py` and `python3 verification/verify_palette.py` from the package root.

The universal logical equivalence is not certified by these bounded enumerations; it depends on the structural doubling-tree lemma, the all-vertex atomic support lemma, and the permanent two-pebble strategy proved in the result. The proof also supplies formulas distinguishing every unequal invariant. There is no external machine-checked certificate and no independent mathematical audit.
