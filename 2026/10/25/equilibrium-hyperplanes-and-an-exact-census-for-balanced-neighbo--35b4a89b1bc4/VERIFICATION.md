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

# Verifiable calculations and limits

Run `python verify_swap.py` with a standard Python 3 interpreter. The program enumerates every binary placement for the seven displayed \((h,m)\) instances, computes each moving agent's pre- and post-swap utility using **explicit open-neighborhood neighbor lists**, and compares every oriented opposite-type cross-part swap with the integer criterion. It separately computes the tripartite count by binomial-weighted part profiles and checks the closed-form inclusion--exclusion identity.

Observed run: `PASS 42816 configurations; 1468544 ordered red-to-blue cross-part cases`. The tripartite equilibrium counts printed were \(52,458,3196,28568\) for part sizes \(2,3,4,5\), respectively. This is exhaustive only for the stated finite sizes, not for arbitrary size, all preference functions, or alternative graph families.

The all-size criterion, potential decrease, exact census and asymptotic expansion are proved in `RESULT.md`. The asymptotic uses a standard lattice local central limit theorem plus the stated \(O(m^{-1})\) two-constraint bounds. Neither its infinite range nor originality is certified by the finite checker. Scientific limitations and closest-source comparisons are recorded in `REVIEW.md` and `RESULT.md`.
