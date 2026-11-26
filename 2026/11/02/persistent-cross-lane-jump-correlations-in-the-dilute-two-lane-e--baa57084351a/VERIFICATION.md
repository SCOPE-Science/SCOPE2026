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

Direct application of the endpoint occupancy rule gives the two directed rates c_d and c_{d+1} in the relative coordinate, with c_0=c_1=p+a/2 and all other edges p. Reverse rates match across each relative edge, and the two-position in- and out-rates balance for uniform product initialization. The total-count Poisson corrector has flux differences J_d-J_{d+1}=c_d+c_{d+1}-2(p+a/N) and the zero-circulation condition sum J_d/c_d=0. Substitution verifies the stated fluxes, including the symmetry-paired special edges and the single ordinary edge at N=3. The total-count martingale bracket averages to 2(p+a/N)+2E_N: linear terms cancel by stationarity and the gradient squares contribute twice per undirected edge. The signed lift corrected increments are N/(R_N c) on each forward edge, so its bracket average is 2N/R_N. The endpoint corrections are bounded for fixed N and do not change linear variance growth. Taking one quarter of the difference gives C_N; strict arithmetic–harmonic mean inequality gives positivity unless a=0, and E_N tends to a^2/(3p). For the reverse limits, bound the integrated first-disagreement intensity by |a| times the occupation of {0,1,N-1} by the unconditional stationary baseline walk, whose expectation is 3t/N; no uniformity conditional on agreement is needed. Bounded-rate Poisson domination makes all fixed-degree mixed moments uniformly integrable. Thus the two limits differ for a nonzero coupling, without extending to t growing jointly with N. Independently reproduced exact values by the per-lane mixed martingale bracket (15 cases across N=3,4,5,9,17, both signs and zero coupling); e.g. 11/420 for N=3, p=1, a=-3/4. Replay: python3 -B /workspace/branches/frozen_review_replay.py 3. Frozen script inspected, not executed.

## originality

PASS

The rate family, product law and stationary mean currents are already known. The checked papers and catalogue entries do not give or directly imply the stated finite-sector two-count mixed cumulant and its order-of-limits boundary. No claim of exhaustive priority is made.

## value

PASS

This is a minimal canonical sector that cleanly distinguishes independent stationary positions from dynamically correlated integrated counts. The exact size-dependent law identifies a persistent covariance from a vanishing fraction of interaction states, with a different fixed-time limit. That boundary matters for dilution arguments and gives a reproducible fluctuation benchmark without assuming finite-density or crossover-scale results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
