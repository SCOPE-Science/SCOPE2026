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

The verification replays the structural reduction used in the proof.

For a finite product of local rings, each coordinate is represented only by its position in the local ideal lattice and by whether it is the whole ring. A tuple is a graph vertex exactly when at least one coordinate is whole and not all coordinates are whole. Two vertices are adjacent exactly when every coordinate is whole in at least one of the two tuples.

The checker exhaustively determines total and paired domination minima for nine local-ideal-count profiles. These include two-factor cases with a field factor, three-factor mixed cases, and up to five factors. It also checks the canonical support witnesses for every \(2\le r\le9\).

Exact output:

```text
VERIFY_OK
ideal_counts=(2, 2): vertices=2 gamma_t=2 gamma_pr=2
ideal_counts=(2, 3): vertices=3 gamma_t=2 gamma_pr=2
ideal_counts=(3, 3): vertices=4 gamma_t=2 gamma_pr=2
ideal_counts=(2, 2, 2): vertices=6 gamma_t=3 gamma_pr=4
ideal_counts=(2, 2, 3): vertices=9 gamma_t=3 gamma_pr=4
ideal_counts=(2, 3, 3): vertices=13 gamma_t=3 gamma_pr=4
ideal_counts=(2, 2, 2, 2): vertices=14 gamma_t=4 gamma_pr=4
ideal_counts=(2, 2, 2, 3): vertices=21 gamma_t=4 gamma_pr=4
ideal_counts=(2, 2, 2, 2, 2): vertices=30 gamma_t=5 gamma_pr=6
support_witness_checks_r=2..9_passed
```

The finite checks are corroborative only. The arbitrary Artinian case is proved by the support-union argument and the published ordinary-domination lower bound.
