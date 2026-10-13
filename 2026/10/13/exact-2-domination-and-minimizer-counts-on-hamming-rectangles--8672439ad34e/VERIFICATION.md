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

The theorem is proved analytically in `RESULT.md`. The bundled checker is a finite stress test only.

`verify.py` constructs \(K_m\mathbin{\Box}K_n\) directly and checks ordinary 2-domination from adjacency. For every \(1\le m\le n\le4\), it enumerates every vertex subset, finds the exact minimum, counts all minimum sets, and compares both quantities with the formulas in the finding. It also verifies the explicit constructions and their domination property for every \(1\le m\le n\le40\).

The finite enumeration is not used to infer the result for arbitrary dimensions. The infinite claim rests on the row/column-count dichotomy in the proof: no empty column forces at least \(n\) choices; an empty column forces at least two choices in every row and hence at least \(2m\).

The literature comparison has a stated access limit: the 2009 square-rook predecessor was inspected only through its abstract/metadata and citation context, not full text. This remains a residual originality risk.

Actual replay from the bundled path:

`ALL CHECKS PASSED; exhaustive_cases=10; subset_candidates=3681; construction_cases=820; exhaustive_range=1<=m<=n<=4; construction_range=1<=m<=n<=40`
