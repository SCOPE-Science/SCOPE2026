---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For a one-way n-cycle CTMC with positive r_i, linear budget Σ_{i<n}r_i+q r_n≤B, stationary weights are π_i∝t_i=1/r_i; direct clockwise hitting times give K=e_2(t)/Σt. Fix two ordinary rates a,b with sum s; K as a function of v=1/a+1/b has strictly positive derivative [R²+H+2R/s]/[2(R+v)²], so averaging unequal equally priced rates strictly improves K. This proves unrestricted reduction to k=n−1 identical ordinary rates, not an assumed symmetry. With u=r_n/r_1, K=k(k+q u)((k−1)u+2)/(2B(ku+1)); derivative has sign q[k(k−1)u²+2(k−1)u+2]−k(k+1), increasing on u>0. Below q_c=k(k+1)/2 its unique root is the formula in RESULT.md and the sole global positive minimizer; at or above q_c, strictly increasing K gives unattained inf k²/B as u→0+, r_i→B/k. At q=1 the unique solution is uniform. SymPy differentiation and n=3,4 rational hitting-time checks are independent; 12516 saved tests alone are not proof.

## originality

PASS

PASS, qualified: novelty is the exact unrestricted one-price positive-rate optimizer with sharp existence threshold, not stationary-cycle Kemeny identity or general discrete-time Kemeny optimization.

## value

PASS

Stationary-target expected hitting time is a standard stochastic-network quality measure and edge purchase cost a natural resource constraint. A sharp n(n−1)/2 transition distinguishing attained rate allocations from reducible-boundary limiting designs is a useful exact network design result; unrestricted symmetry proof matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
