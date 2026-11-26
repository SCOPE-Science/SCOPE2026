---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

RESULT.md lines 43–131: the Kirchhoff index is 2^d times the trace for connected support; the disconnected objective is explicitly infinite. With M=L+Π and Z=M^(−1/2)HM^(−1/2) the trace-inverse second variation is 2 tr(M^(−1/2)Z²M^(−1/2))>0 for H≠0. Edge weights inject into L; connected feasible weightings form a convex domain and the objective diverges on approach to disconnected support. Compactness, at least one feasible connected weighting, and strict improvement by scaling to a tight budget give existence and uniqueness. Bit flips and permutations preserving the price classes force two weights; zeroing either entire class disconnects the cube. Walsh characters give 2(ky+εx), with binomial multiplicity. There are 2^N edges in each direction, giving exactly the stated x,y and F_N times 2^(N−1)/B. The ratio parametrizes the open tight-budget line monotonically, so the strict convexity on that line proves uniqueness of the derivative zero even without assuming convexity in the ratio. Rewriting the derivative as P A_N+sum_(k=0)^N binom(N,k)(Pk−NQ)/(k+r)² confirms the singular k=0 term. Binomial concentration (exponentially small tails) and a second-order Taylor estimate near N/2 give the first two inverse sums 2^N(2/N+O(N^(−2))) and 2^N(4/N²+O(N^(−3))), with third sum O(2^N/N³). For P>Q the fixed-r derivative scaled by N/2^N tends to 4(P−Q)>0, forcing r_d→0. At r_d the nonsingular part is asymptotic to 4(P−Q)2^N/N by the inverse-moment bounds, balancing NQ/r_d² and giving the claimed premium constant. For P<Q, r=Nρ gives limiting derivative 2P+(P/2−Q)/(ρ+1/2)²; its unique sign change brackets the ratio divided by N and yields the stated positive coefficient. Full coordinate symmetry gives r=1 at equality, including the smallest dimension d=2. All limits fix both prices and the budget.

## originality

PASS

The supported distinction is the two-price resistance-optimal cube solution, particularly the opposite asymptotic scales and their constants. General strict convexity, price-aware KKT conditions, Walsh spectral methods, and the isotropic optimum are not new. The strongest same-day analogue optimizes the tree enumerator on the same priced graph and has different asymptotics, so it does not cover the claimed rates. The inaccessible Liu et al. passage leaves a bounded coverage risk, not negative evidence.

## value

PASS

Single-direction pricing is a natural minimal symmetry breaking of a standard optimal design problem. The result explains how an indispensable class can receive an exponentially vanishing relative weight even under connectivity, while a discount produces a ratio increasing linearly instead. The constants and the finite root equation give useful comparison targets for optimizing the same objective numerically. This is a quantitative distinction beyond the known symmetry argument and fixed-weight trace, not a claim about all price classes or budgets approaching parity with dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
