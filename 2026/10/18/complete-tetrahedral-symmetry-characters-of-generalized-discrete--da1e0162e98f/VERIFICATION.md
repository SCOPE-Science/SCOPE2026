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

Both standalone standard-library scripts were run from their supplied contents. `gm_character.py` reconstructs the \(15\)- or \(14\)-vertex face poset and enumerates every matching by a disjoint-edge recursion. It finds \(14{,}720\) and \(5{,}096\) nonempty simplices; for every one of the \(24\) tetrahedral label permutations it computes the signed trace of setwise-fixed simplices, including the reduced empty-face correction. Character values are constant on each cycle type.

`gm_orbits.py` independently enumerates admissible Hasse-edge orbits, constructs the orbit-conflict graph, evaluates the independent-set polynomial at \(-1\), and confirms the same five character values for both generalized complexes. It also checks Specht multiplicities \((2,5,2,6,0)\). Compare reproducible standard output with `gm_character_output.txt` and `gm_orbit_output.txt` using the commands `python3 gm_character.py` and `python3 gm_orbits.py`.

The scripts verify the finite combinatorial portion of the proof; Scoville's theorem is an explicitly cited topological premise, not re-proved by these computations. The conclusion is limited to rational symmetry characters and rational homology of the full geometric orbit quotients. No external or independent audit has been performed.
