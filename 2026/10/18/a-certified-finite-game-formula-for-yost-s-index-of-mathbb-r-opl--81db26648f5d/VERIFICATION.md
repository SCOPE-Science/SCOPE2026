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

# Verification record

The formula concerns the real space \(X=\mathbb R\oplus_2 c_0\) and every integer \(N\ge1\). The mathematical verification is internal to the proof: (a) for a finite source list, send a response into a fresh \(c_0\) coordinate; (b) reverse it with equal-weight \(\pm e_1\) source pairs and a convexity inequality; (c) optimize over weakly compact scalar source distributions; (d) symmetrize and discretize an angular game whose payoff is \(1\)-Lipschitz in both arguments.

A floating-point LP computation using the displayed matrix yielded representative outputs \(V_{128}\approx1.2403134\), \(V_{512}\approx1.2403169\), and \(V_{2048}\approx1.2403171\); these are **exploratory numerical values, not exact optimizer certificates**. The exact theorem has the solver-independent error \(\pi/(4N)\), which applies to the exact \(V_N\), not automatically to rounded solver output. Any independent numerical reproduction may construct the \((N+1)\)-square coefficient matrix from the two radicals in \(K\) and solve the stated finite LP with controlled solver error.

The strict lower bound uses a symmetric \(\{0,-1,1\}\) source and a perturbing symmetric \(\{\pm1/\sqrt2\}\) source. The upper bound uses two special responses; both are proved for the whole sphere rather than sampled test points. Neither grid enumeration nor software output is used to certify the infinite-dimensional reductions.

No third-party verification or independent audit has been performed. Bibliographic originality is based on inspected accessible literature and genuine search comparisons; the unavailable full 1998 article remains a residual risk.
