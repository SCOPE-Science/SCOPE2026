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

The unrestricted proof is contained in RESULT.md, steps 1--6. Reproduce finite checks by running `python3 verify_crown_closed_neighborhood.py` with Python 3 and no dependencies. Expected terminal lines include `FINITE_CHECK_OK` and `CHARACTER_CHECK_OK`.

Actual computations: full augmented boundary matrix elimination over \(\mathbb F_2\) for every \(3\le n\le8\); signed Lefschetz-character comparisons for all permutations at \(n=5\), and a deterministic subsequence of permutations at \(n=6\), both with and without side exchange. Facets are constructed from the defining graph adjacency, not copied from the proof. Computations corroborate integral ranks and characters but cannot certify integral torsion absence or arbitrary \(n\); those come from the integral homotopy-pushout and Mayer--Vietoris proofs.

The basepoint and cofibration hypotheses of the homotopy pushout are verified by the graph's connectedness and by the inclusions of finite simplicial subcomplexes. The infinite claim does not rely on extrapolation from the computed range. Literature novelty remains subject to independent checking.
