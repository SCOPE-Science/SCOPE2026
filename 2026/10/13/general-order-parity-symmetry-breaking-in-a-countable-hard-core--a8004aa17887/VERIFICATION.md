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

The proof was checked at the level of the exact two-mass equations induced by the parity adjacency graph.

1. Dividing the two mass equations gives \((M_1/M_2)^{1/k}=(1+M_1)/(1+M_2)\); solving this relation with \(r=e^{2s}\) gives the stated reversible formulas for \(M_1,M_2\).
2. Direct hyperbolic identities reduce \(D\) and \(1+M_1\), and substitution reconstructs \(\Lambda_{k,\ell}(s)\) exactly.
3. The \(s\downarrow0\) expansion gives the stated \(L_c\) and quadratic coefficient. Its sign is negative precisely when \(\ell>(k+1)(k+3)/(3(k-1)^2)\).
4. The large-\(s\) asymptotic is \(\Lambda_{k,\ell}(s)\sim e^{2s}\). Together with the local decrease, this proves existence of a lower global minimum and two distinct positive branch parameters for each intermediate level.
5. The symmetric equation has a positive root by the intermediate value theorem, so each such level has at least five fixed points.
6. `verify_parity_branch.py` was replayed from the packaged bytes and reports `VERIFY_OK cases=44 worst_residual=6.395e-14 k2_specialization=1 two_root_orders=2..12`. These finite calculations are corroborative only.

The result does not assert an upper bound of five fixed points for general \(k\), nor does it classify unequal parity activity totals or Gibbs-measure extremality.
