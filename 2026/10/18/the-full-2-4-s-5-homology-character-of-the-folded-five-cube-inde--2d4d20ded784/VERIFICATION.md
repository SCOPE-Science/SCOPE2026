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

The package contains the standalone Python 3 source `verify_clebsch_character.py` and has no external software dependencies. Execute `python3 verify_clebsch_character.py` in the extracted directory.

The checker reconstructs the sixteen-vertex graph from five binary connection directions. It exhaustively checks all 65,536 vertex subsets for independence; the face-size counts including the empty face are `(1,16,80,160,120,16)`. Mod-two boundary ranks are exactly `(15,65,95,16)` by integer bit-vector elimination. The rank constraints from successive boundary compositions then prove rational degree-three homology of dimension nine and vanishing in all other reduced rational degrees.

Every one of the 1,920 explicit automorphisms is checked. The signed-fixed-simplex trace uses the induced permutation sign on each setwise-fixed independent simplex; independently, a compatible-vertex-orbit recurrence evaluates the same signed Euler sum without consulting the simplex enumeration. The two exact calculations match the closed-form character value for every group element. The computed value distribution is `{-5:20,-3:60,-1:884,1:865,3:80,5:10,9:1}`. Character inner products establish two orthogonal rank-four and rank-five irreducible constituents, whose irreducibility also follows from the proof in `RESULT.md`.

The proof uses exact finite enumeration, not a sample, heuristic search or timeout. It relies on standard facts that signed simplicial traces satisfy the Hopf trace identity and that finite-group representations over characteristic-zero fields are semisimple. It does not determine integral equivariant homology or generalize the calculation beyond this one graph. External independent audit has not been performed.
