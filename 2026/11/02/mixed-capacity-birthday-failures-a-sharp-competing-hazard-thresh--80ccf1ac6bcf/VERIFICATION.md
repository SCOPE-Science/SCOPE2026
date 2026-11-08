---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The exact finite law follows by multiplying truncated occupancy exponential generating functions and marking a bin already at its capacity at the next arrival. Independent rate-1/N Poisson processes for each bin give Gamma(2,N) and Gamma(3,N) first-rejection clocks. At scale N^(2/3), class-one survival log -> -alpha*x^2/2 and class-two -> -x^3/6 whenever a_N/N^(2/3)->alpha; differentiation yields the claimed marked densities. When a_N is much larger, N/sqrt(a_N) instead yields Rayleigh law and negligible class-two risk; when smaller, pure cubic-Weibull. Independent exponential waiting times and the maximal martingale inequality justify de-Poissonizing the time without changing the failing-bin mark. Coupling independent Exp variables gives strictly increasing class-one win probability and unique alpha*≈0.5521857197206905. The Poissonized fixed-alpha O(N^-1/3) log-survival is not misrepresented as a discrete clock error. Independent exact occupancy recursion agrees with all coefficients for N<=5.

## originality

PASS

A sharp mixed-capacity first-rejection crossover, exact capacity mark and finite enumerator seem additional to common-capacity urn overflow work. The ingredients Poisson thinning, independent Gamma arrival times and competing hazards are classical and are not separately claimed as original. Broad heterogeneous occupancy literature may already derive a more general version; qualified best-of-knowledge PASS after object/implication comparison.

## value

PASS

The first failure of a heterogeneous storage system is a natural reliability/birthday statistic. A vanishing population of capacity-one bins changes its limiting scale at sharp order N^(2/3); the complete two-clock marked law and unique half-risk constant give information unavailable from homogeneous capacity models. This is a motivated exact first-event classification, not mere relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
