---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Final claim and proof checked in repairs/4/RESULT.md. The original Step 4 claimed uniform convergence of the denominator factor on a fixed relative neighborhood of L=log N. At t=(1−ε)L with fixed ε>0 it instead tends to 1/(1−α/(1−ε)), so that step was not justified as written. The replacement uses [L−sqrt(L),L], on which k/(t−log W) tends uniformly to α, and an explicit exponential upper bound on the complementary power mass. The claim and scope are unchanged. In the simultaneous gap representation S_l−log l converges almost surely by summable centered gap variances; l exp(−S_l) has the exponential limit by the exact maximum law, giving the same W across all coordinates. For m=j−1, k=m−1, the tail series divided by its last term converges uniformly to the geometric sum when k/S_l is bounded below 1. Choose α<δ<β=α(1−log α) so l≤N^δ contributes o(b_N) and the other l stay in that uniform tail regime. The repaired cell derivative bound and window estimate give conditional mean b_N W^(1−α)/(1−α) to relative o(1) almost surely; conditional variance ≤ mean and a finite union bound give the asserted convergence in probability. As a cross-check, conditional on the largest first-arrival time t=L+g, each nonlast type is missing independently with probability Pr(1≤Pois(t)≤m)/(1−e^(−t)); dividing the conditional mean by b_N gives exp(−(1−α)g)/(1−α)+o(1) uniformly for compact g, matching the shared Gumbel amplitude. For expectations the repaired proof sums the Gamma(m,1) arrival tail against the S_l laws, getting E[M_N^m]/m! exactly. The bound Pr(M_N−L>x)≤e^(−x) and pγ<1 for some p>1 and α<γ<1 give uniform integrability. The mean Γ(1−α) and the marginal CDF then follow by the exponential law. This replay is analytic; frozen verify.py was inspected, not executed, and its finite checks alone do not test the growing-index conclusion.

## originality

PASS

The repaired result retains the distinct subcritical logarithmically moving-index joint limit. Fixed-index coupling and means are recognized inputs, not contributions. Neither the exact expectation formula nor the critical-window fluctuation theorem supplies the shared Weibull-power distribution at fixed subcritical ratios.

## value

PASS

The subcritical logarithmic scale is a natural moving threshold in the sibling model: its Poisson cutoff is a fixed fraction of the completion-time scale. The final theorem gives the exact normalizer and a nonexponential law, with the same latent amplitude but different powers across sibling levels and matching mean. That is a useful regime classification between fixed indices and the critical window, rather than a finite-binomial recomputation or a normalizer change without a distributional effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
