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

The complete all-parameter proof is in `RESULT.md`. The two principal external inputs are the published \(\bigvee^{B_q}S^3\) homotopy equivalence for the categorical triple product and the \(\bigvee^{(q-1)^2}S^1\) homotopy equivalence for the two-factor product. Neither external homotopy equivalence is asserted to be equivariant.

The critical new steps can be checked independently: verify that each coordinate-transpose orbit is wholly contained in one bipartite sheet; construct the cross-sheet orbit incompatibility graph; confirm that every off-diagonal symbol is adjacent across the sheets to every off-diagonal symbol; enumerate the four cases for the first sheet's selected diagonal cardinality and off-diagonal nonemptiness; derive \(-1+q-\binom q2\), \(-(q-1)\), \(0\), \(-1+q-\binom q2\) and their sum \(-(q-1)^2\). Check at the lower boundary \(q=2\).

Run `python3 check_klein_character.py` in a standard Python 3.8+ environment. It uses only the standard library. `klein_character_checks.txt` contains the exact recorded stdout. The first enumeration considers all \(2^{2q^2}\) vertex subsets at \(q=2,3\), filters independent faces, and counts signed invariant simplices for all four automorphisms. The second programmatic route enumerates first-sheet orbit subsets at \(q=2,3,4,5\). Formula integrity checks cover all integer parameters \(2\le q\le100\).

The finite enumeration does not verify the infinite-family assertion beyond these parameters; the proof rests on the explicit inclusion–exclusion argument and cited published homotopy theorem. No independent audit has been performed.
