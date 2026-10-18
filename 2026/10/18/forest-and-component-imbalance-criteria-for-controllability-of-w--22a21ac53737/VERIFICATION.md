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

Run `python3 verify_rook.py` with a standard Python 3 installation. The complete run executed successfully and printed `ALL CHECKS PASSED: 11378`.

The checker builds the four exact integer eigenspace bases, constructs weighted Laplacians directly and verifies every basis eigen-equation at two concrete positive weight assignments for each tested board. It independently computes the bipartite forest and component-ratio predicates and the modular ranks of the selected restrictions. Every one of the \(2^{pq}\) selected-cell masks is checked, both resonantly and nonresonantly, for boards of sizes \((2,2),(2,3),(2,4),(3,3),(3,4)\), in total 4,944 masks and 9,888 predicate comparisons. Minimum sizes are exhaustively verified for these boards. Further deterministic selection tests and explicit optimal constructions are evaluated on \((4,4),(4,5),(5,7),(7,3)\).

The rank routine works modulo the prime \(2^{61}-1\), and all tested basis entries are in \(\{-1,0,1\}\). The exhaustive boards have interaction rank at most six and merged main-effect rank at most five, so their square minors are bounded by \(6^{3}=216\) under Hadamard's inequality; reduction is therefore exact on those boards. Larger-board modular ranks are corroborative because an exceptionally large determinant could be divisible by the chosen prime. The unbounded classification depends only on the paper proof.

There are no external data inputs or numerical optimization solvers. Source identifiers and mathematical limitations are in `RESULT.md`. Independent validation has not been performed.
