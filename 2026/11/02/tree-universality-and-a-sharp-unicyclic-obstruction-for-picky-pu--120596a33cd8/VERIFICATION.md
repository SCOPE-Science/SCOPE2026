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

Run `python3 verify.py` with Python 3.10 or later. The verifier uses no external dependencies. It exhaustively constructs all labeled spanning trees using Prüfer sequences, adds every possible missing edge, deduplicates exact edge lists, and checks all binary profiles on every connected unicyclic graph of orders three through six for the response rule \(T_3\). It also tests the tree inductive states against brute-force equilibria for all labeled trees up to six vertices and \(q\in\{2,3,4,5,6\}\), and verifies the explicit obstruction family for \(q\in\{3,4,5,6,7,8\}\).

The finite checks do not certify the infinite tree existence theorem or the entire all-parameter obstruction family; those are proved by induction and a complete four-case argument in `RESULT.md`. The finite minimality statement for \(q=3\) is exhaustive because the Prüfer/tree-plus-edge generation covers *every* labeled connected unicyclic graph up to six vertices. The program checks existence and nonexistence exactly, not approximate equilibrium or welfare.
