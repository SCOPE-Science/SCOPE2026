---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Stationary resetting resolvent π_r(f)=r∫exp(-rt)(P_t f)(S)dt follows from memoryless independent reset and irreducibility. r→0 yields uniform k-subset moments and C= -k(n-k)/(n²(n-1)). At high r use U=1-η_x,V=1-η_y. Their first departure derivatives are d_x,d_y; exactly two jumps to distinct initial empty neighbors give second Taylor coefficient d_x d_y-c and no other two-jump routes end with both x,y vacant. Exponential-age integrals multiply by 2!, giving r² Cov(U,V)=d_xd_y-2c. Explicit three-state generator on K_(2,m) has rates 0->1:4, 1->0:m-1, 1->2:1, 2->1:2m and reset 0,1->2:r. Solving π gives C=m((m-2)r-4)/((m+r+2)^2(2m+r+2)), yielding exactly one positive root r=4/(m-2) iff m>=3. Four-cycle specialization and even-block boundary coefficient follow. Independent symbolic rational generator calculation reproduced the K_(2,m) formula; limit claims fixed graph.

## originality

PASS

Basu–Kundu–Pal 2019 establish symmetric exclusion with stochastic resetting and renewal; their inspected full article treats densities/integrated currents. Sadekar–Basu 2020 correlations concern dichotomous rather than single-configuration resets; ordinary bipartite spectrum without resetting does not imply the exact signed covariance threshold. General Markov resolvent formulas are common, so genuinely new portion is the two-hop geometry and all-m bipartite phase.

## value

PASS

Non-equilibrium stationary covariance changes sign despite equilibrium exclusion anticorrelation; the local combinatorial obstruction predicts reversal, and K_(2,m) demonstrates an exact, sharp vacancy coordination threshold with unique sign crossing. This informs finite-network exclusion correlations without requiring a thermodynamic limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
