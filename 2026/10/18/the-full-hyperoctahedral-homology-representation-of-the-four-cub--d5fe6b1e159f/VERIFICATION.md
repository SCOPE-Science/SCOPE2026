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

Execute `python3 verify_q4_character.py` with standard Python 3. The code uses no downloaded datasets, external packages or auxiliary files. It enumerates all 65,536 vertex subsets and verifies exactly 742 nonempty independent faces. It reconstructs the greedy acyclic matching on 742 faces, checks 367 distinct pairs, reconstructs and topologically sorts all 2,816 oriented cover relations, and verifies critical-cell profile one in degree zero and seven in degree three. It then enumerates all 16 translations times 24 coordinate permutations, checking the derived character through both the independent orbit-conflict evaluation and direct oriented fixed-face Lefschetz sums, plus the full formula and exact Fourier projections.

Expected successful output:

`VERIFY_OK vertices=16 faces=742 matching_pairs=367 critical=1x0+7x3 acyclic_incidences=2816 group=384 rank_H3=7 translation=3+4 all_character_checks=384 globally_fixed=0`

An observed successful execution produced this output. The acyclic matching implies the integral nonequivariant homotopy claim; the character computations prove the claimed rational action, not an integral representation lattice. Neither completeness of global mathematical literature nor independent external scientific validation is asserted.
