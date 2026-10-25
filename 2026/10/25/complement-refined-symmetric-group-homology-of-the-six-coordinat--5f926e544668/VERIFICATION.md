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

# Reproducible checks and limits

Run `python3 verify.py` in the directory containing this document. The checker uses Python 3 standard library only; it reconstructs all subsets, adjacency, clique faces, binary boundary matrices, group actions and irreducible characters. It prints `REPRODUCIBLE_RIPS_S6_C2_CHARACTER_PASS` on successful completion.

Observed exact completion data: `EXHAUSTIVE_SCALE_TWO_F_VECTOR (30, 210, 520, 480, 132, 20)`; `MOD_TWO_BOUNDARY_RANKS [29, 181, 339, 112, 20] BETTI [1, 0, 0, 29, 0, 0]`; `ALL_JOINT_GROUP_TRACES 1440`; `S6_TIMES_C2_DECOMPOSITION {(3, 1, 1, 1): (1, 0), (2, 2, 1, 1): (0, 1), (2, 1, 1, 1, 1): (1, 1)}`; `SCALE_FOUR_CROSS_POLYTOPE 15 ANTIPODAL_PAIRS`.

The rational degree concentration is justified by the published scale-two wedge theorem of Feng–Nukala for the exact two-rank input. The exhaustive binary rank verification is an independent finite corroboration; it does not alone certify all integral invariants. The integer Lefschetz counts and finite-group character inner products give an exact rational module calculation. This does not verify any homology representation at unlisted ranks or for a larger coordinate set. Independent mathematical audit: not performed.
