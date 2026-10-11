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

# Verification of the three-piece classification

Run `python3 verify_odometer.py` with standard Python 3. The script uses only `fractions` and `itertools`; there are no external datasets or downloads.

The checker enumerates all six permutations, builds the deterministic \(12\)-cell transition graph exactly, follows each of the three possible first-quarter entry cells, tests the complete partition into finite towers, verifies the induced permutation and return lengths, and checks the high-quarter scaling and return identity at exact rational test points. It finishes with the exact marker `EXACT_CELL_GRAPH_OK` when all checks succeed.

The twelve-cell enumeration is exhaustive for the first-return combinatorics because on each of the first nine output cells the map acts by exact translation and on the last three cells the same scaled adding map applies. The separate proof in `RESULT.md` uses self-induction to exclude *all* periodic trajectories; a finite computation does not prove that infinite step. Unique invariant probability additionally depends on the already-published conjugacies for the two cyclic types (arXiv:2101.00868, Proposition 8.4) and the exact finite-tower measure reconstruction. No independent audit has been performed.
