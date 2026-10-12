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

The theorem is proved symbolically in `RESULT.md`. The critical invariant is that deleting a matching removes at most one neighbor from any vertex. Therefore, if at least three vertices on one bipartition shore are white, every blue vertex on the opposite shore still sees at least two of them, so that white count can never decrease. This reduces all forcing lower bounds to the cases with at most two white vertices per shore.

The three deletion regimes are then exact: with no deleted edge, at most two vertices can remain white; with one deleted edge, at most three can remain white; with at least two deleted matching edges, at most four can remain white. Explicit forcing chains attain each bound. Domination is checked on minimum forcing witnesses, with separate impossibility arguments for \(G_{2,2,1}\), for \(m=2,t=2,n\ge3\), and for \(m=n=3,t\in\{2,3\}\).

The standalone script `artifacts/verify.py` independently implements adjacency, domination, and the color-change rule. It exhaustively computed both minimum parameters on 58 connected profiles of total order at most ten within \(2\le m\le5\), \(m\le n\le7\). It also replayed the explicit symbolic witnesses on 681 connected profiles with \(2\le m\le12\) and \(m\le n\le15\). Its output is:

`ALL CHECKS PASSED; exhaustive_connected_profiles=58; witness_profiles=681`

The finite replay is corroborative and does not certify untested orders. The proof, not the enumeration, supplies the quantification over all admissible \(m,n,t\).
