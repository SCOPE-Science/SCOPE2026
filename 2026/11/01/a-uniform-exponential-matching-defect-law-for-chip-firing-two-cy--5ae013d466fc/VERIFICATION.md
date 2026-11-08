---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Summing the two-step chip changes gives Lf=0, so connectedness and primitivity force exactly one firing per vertex across the two phases. A nontrivial first-phase shore A supports exactly prod_v c_v(A) first-phase states, where c_v is its number of neighbors across the cut. Division by two counts temporal orbits. Deleted matching edges each affect two cross-degrees and yield the displayed binomial sum by splitting-pair count s, intact-pair count p and unmatched-vertex count t. Under complete-graph cut weights binom(N,a)b^a a^b, central cut sizes have exponential concentration; conditional split indicators give E[S|a]=2kab/[N(N-1)] and exactly E[S(1/a+1/b)|a]=2k/(N-1). Their conditional variance is O(N), so second-order exponential Taylor and the O(1/N) logarithmic replacement deliver a constant uniform in k. I independently enumerated all shores for N=4..9 and reproduced samples of finite counts and uniform scaled errors. Finite enumeration is not the proof of the uniform asymptotic.

## originality

PASS

The cut product and some complete-graph period-two counting principles are known; the accepted contribution is the exact matching-deletion specialization together with its uniform, parameter-sensitive relative exponential loss. The cited complete-graph Levine paper employs a self-loop convention in the inspected introductory discussion, while firing-pattern/period-length theorems do not count weighted two-cycles. A previous bounded-degree deletion law for complete bipartite graphs has a different base weighted-cut measure and does not imply this complete-graph constant.

## value

PASS

Deleting only O(N) edges from K_N is a natural sparse structural perturbation, yet it produces the nonvanishing limiting e^{-1} count ratio for a perfect matching. The exact orbit census and uniform error quantify a dynamical effect not visible in a mere existence-of-period theorem or a single finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
