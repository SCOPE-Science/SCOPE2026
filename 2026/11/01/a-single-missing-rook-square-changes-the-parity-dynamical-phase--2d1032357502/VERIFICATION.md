---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At frozen RESULT.md and check_linear.py, the line-graph identity F=B^tB over characteristic 2 is exact: B is incidence of K_{a,b} minus one edge. The rank of B onto even vertex-coordinate vectors and the parity-core decomposition of Q=BB^t into (2,2), (3,2), (3,3) cores and scalar sectors establish all a,b>=2, q=2^h. Core rank sequences determine J3/J2/J1, J5 and the unique J2(1) as stated; finite-field kernel counting yields exact time layers. Independently constructed a GF(2) adjacency matrix and computed power ranks at (2,2),(2,3),(3,3),(4,4),(3,8),(7,6),(9,9), matching [E,a+b-2,1,0], [E,a+b-2,stable], or [E,o+s-1,s+1,s,s-1,s-2,s-2] as appropriate. Finite cases corroborate, not prove, the all-size decomposition. The line-graph diagonal cancellation depends critically on characteristic 2.

## originality

PASS

Best-of-knowledge originality from actual published mathematical searches and inspected primary scientific material; relevant exact known cases and stronger-coverage risks are compared, not merely title-matched. No directly implication-equivalent theorem identified in inspected statements; not a historical priority guarantee.

## value

PASS

Deleting one vertex from a natural rook/Hamming graph is a minimal structural perturbation. The universal Jordan classification exposes a genuinely qualitative dynamical bifurcation: in mixed parity the intact period-two behavior disappears and a sharp five-update nilpotent chain replaces it, with dimension-free final-shell probability 1-1/q. All finite-field orbit/entry census follows from motivated algebraic structure rather than an arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
