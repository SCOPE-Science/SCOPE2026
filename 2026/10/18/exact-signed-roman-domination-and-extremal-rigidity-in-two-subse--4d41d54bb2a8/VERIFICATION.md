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

Execute `python3 verify.py` with Python 3 (standard library only). The recorded `verify_output.txt` was reproduced by executing this same file. The checker builds the explicit odd/even labelings for every integer \(9\le n\le80\); for each, it checks the total weight, each of the \(\binom{n}{2}\) graph vertices' closed-neighborhood sum directly, existence of a distinct disjoint label-\(2\) graph neighbor for every label-\(-1\) vertex, the incidence sum identity, and the fixed-ground-element star identity. It also exhaustively evaluates all assignments of labels \(\{-1,1,2\}\) inside an odd extremal small part for sizes \(3,4,5\), reproducing \(1,3,12\) allowed local-balanced assignments. Those sizes admit no negative internal label and hence each admissible balanced assignment has the required Roman defender automatically.

The proof of the unbounded theorem is given in `RESULT.md` and depends on algebraic counting, not on finite cases. The finite checks do not establish the infinitely quantified lower bound, prove original priority, or substitute for independent audit. The odd extremal description includes an explicit internal defender condition; merely checking local sums is insufficient at larger orders.
