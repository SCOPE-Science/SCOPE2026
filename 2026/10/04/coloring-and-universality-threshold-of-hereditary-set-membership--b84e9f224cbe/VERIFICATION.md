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

The infinite-cardinal proof is symbolic and rests on four checks.

1. **Closure.** For regular \(\kappa\), fewer than \(\kappa\) many hereditary-\(<\kappa\) sets have a union of hereditary size below \(\kappa\), so \(B\) and \(A\cup\{B\}\) lie in \(H(\kappa)\).
2. **Exact extension witness.** For \(z=A\cup\{B\}\), every \(a\in A\) is adjacent to \(z\). If \(b\in B\), then \(b\in z\) would force \(b=B\) and hence \(B\in B\), while \(z\in b\) would create the membership cycle \(b\in B\in z\in b\). Foundation excludes both.
3. **Coloring-number order.** In an increasing-rank well-order, the earlier neighbors of \(x\) are exactly the elements of \(x\), hence fewer than \(\kappa\).
4. **Sharp lower bound.** The ordinals below \(\kappa\) form a \(K_\kappa\), so the chain \(\omega\le\chi\le\chi_\ell\le\operatorname{Col}\) collapses to equality at \(\kappa\).

Run `python3 artifacts/check_finite_membership.py`. It constructs \(V_4\), verifies the finite rank-order identity, checks the four-vertex ordinal clique, and exhaustively checks the finite extension witness for all disjoint \(A,B\subseteq V_2\). It prints `VERIFY_OK`.

The finite script is a bookkeeping replay only. It does not certify regular-cardinal closure or transfinite recursion; those are established in `RESULT.md`.
