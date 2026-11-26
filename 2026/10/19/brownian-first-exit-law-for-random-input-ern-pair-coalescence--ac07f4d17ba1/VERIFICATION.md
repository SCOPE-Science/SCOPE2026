---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Keep the state labels fixed and cut into cycles at the times the first label returns to zero. Starting with clockwise gap d, the second label reaches the reset state at first-label phase n-1-d. A reset on the first letter there pushes the gap up by one; once pushed it cannot return to the reset state within that unabsorbed cycle. At the final first-label phase a fresh reset pushes the gap down by one. The two Bernoulli(q) first-letter flags are independent conditional on the past, since their sampled phases are distinct; one may hypothetically complete a truncated terminal cycle. The reflected labeling of coalescence as gap 0 or n is consistent: the only mismatch with macro-increment gambler's ruin is early killing at n-1 if both flags equal 1. The remaining expected lazy-walk lifetime on this mismatch is (n-1)/(2pq), negligible on the n^2 cycle scale. The invariance principle yields the Brownian exit limit because the limiting paths cross the hit boundary immediately. Cycle durations have mean 1+(n-1)/p and variance (n-1)q/p^2; a maximal bound at deterministic O(n^2) horizon and tightness justify the clock despite within-cycle dependence on the gap flags. The terminal-cycle truncation and arbitrary initial partial passage are negligible. The physical-time generator is therefore p^2q times the second derivative. Solving the boundary problems for the Laplace transform and the first two moments reproduces the displays. Since the exit law is a positive time scale times one fixed nondegenerate law with positive mass in every nonempty subinterval of (0,infinity), maximizing p^2(1-p) uniquely minimizes its positive-time tails and interior quantiles. A separately written true pair-state calculation checked representative finite means and discounted transforms; the uploaded script was inspected, not executed.

## originality

PASS

The supported distinct claim is the complete first-exit distribution for every fixed bias and macroscopic starting gap, with exact physical-time scale and distribution-wide bias optimality. Credit Gusev's exact finite midpoint-pair means and the corresponding leading optimizer, and credit the independent catalogue's exact second-moment coverage in fair-input cases. Neither comparison gives the full exit law or the reduction needed to pass from pair transitions to it. No priority is asserted for the shared mean or the optimizer regarded as a mean optimizer.

## value

PASS

A mean for a distinguished pair does not predict tail risk, quantiles or dependence on the starting separation. The cycle reduction explains the cubic time scale and isolates the exact bias-dependent constant, yielding a single explicit model for all macroscopic separations and a stochastic-order result. These are substantive additions beyond standard moment or worst-case synchronization calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
