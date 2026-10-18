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
# Reproducible mathematical checks

Run `python verify_cube_matching.py` after installing the versions specified in `requirements.txt`.

The verifier derives the cube and matching complex from the three-bit coordinates, confirms face vector \((12,42,44,9)\), constructs signed integer boundary matrices and verifies their compositions vanish, and checks boundary ranks \((11,31,9)\). It exhausts all \(4096\) subsets of twelve cube edges and reports the exact smallest homology supports. It verifies one four-pair elementary collapse certificate, every surface vertex link, and transitivity of the full symmetry group on the six spheres.

The integer lattice check computes the Smith normal form of the \(44\)-by-\(13\) matrix consisting of all nine third-boundary columns and four induced two-sphere cycles; every invariant factor is one. It then verifies all forty-eight signed simplicial Lefschetz traces and the two rational group components. The code additionally checks two explicit homology relations between the six generators. The results concern this finite combinatorial complex, not any unspecified infinite family.

The check is deterministic. The claimed scientific conclusion rests on exact integer arithmetic and complete finite enumeration, together with the standard topological facts about elementary collapses and closed connected surfaces. No outside data files are needed. Independent review has not been performed.
