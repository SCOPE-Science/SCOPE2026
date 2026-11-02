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

# Reproduction and limits

Run `python3 check_petersen_4cut.py` under Python 3 with no nonstandard dependencies. The checker performs exact bitset enumeration, an exhaustive acyclicity topological sort, mod-two boundary elimination, orientation-aware Lefschetz character computations on all 120 permutations, and Murnaghan–Nakayama irreducible-character reconstruction with orthogonality tests. Its verified terminal marker is `PETERSEN_4CUT_26_S5_120_FULL_CHARACTER_MORSE_OK`.

Observed complete finite counts: 140 maximal facets, 765 nonempty simplices with face vector \((10,45,120,210,240,140)\), 369 matching pairs, 27 critical simplices consisting of one zero-cell and 26 five-cells, and 3,330 Hasse incidences. Mod-two boundary ranks in dimensions one through five are \((9,36,84,126,114)\).

The mathematical use of these checks is explicit: a complete acyclic matching establishes the integral homotopy type by Forman's theorem; the Hopf trace formula on oriented rational simplicial chains establishes the character. The checker does not compute any nonexistent independent certification or infer a general theorem from a finite experiment. A separate independent audit has not occurred.
