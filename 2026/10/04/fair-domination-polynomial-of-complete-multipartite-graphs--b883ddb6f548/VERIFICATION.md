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
The proof was checked directly from the literal fair-domination definition. For \(D\subsetneq V(G)\), every outside vertex in part \(V_i\) has exactly \(|D|-|D\cap V_i|\) selected neighbors, so fairness is equivalent to equal selected occupancies among all non-full parts together with positivity of the common outside-neighbor count.

The included `verify.py` exhaustively checks every nondecreasing complete-multipartite profile of total order at most \(9\), every vertex subset, the structural criterion, every coefficient of the displayed fair domination polynomial, and the formula \(\operatorname{fd}(G)=\min\{r,\min_i n_i\}\).

This finite census is a regression check and does not certify the infinite theorem; the infinite theorem rests on the symbolic proof in `RESULT.md`. Literature originality remains subject to the residual search risks stated in `REVIEW.md` and `AUDIT.json`.
