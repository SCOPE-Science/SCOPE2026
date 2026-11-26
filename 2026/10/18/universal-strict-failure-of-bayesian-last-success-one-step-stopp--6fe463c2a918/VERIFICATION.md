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

At the first success after f_m failures the Beta posterior has shapes A=alpha+1 and b_m=beta+f_m, with m trials left. Relative to the all-failure word, any single specified success word has probability ratio A/B_m, where B_m=b_m+m-1=mA+delta_m and 1<=delta_m<2. This gives the strictly smaller one-step value. Given that the first later success occurs at k, selecting it wins on the one-success word; skipping it and choosing the next wins on one of m-k two-success words, each with relative weight (A+1)/(B_m-1) versus the one-success word. This independently recovers the positive-part expression and is also valid for k=m (zero waiting reward). Its positive-part sum divided by m^2 tends to the integral of (1-(A+1)x)_+ over [0,1], namely 1/[2(A+1)]. Hence the conditional relative improvement tends to 1/[2A(A+1)] despite strict myopic stopping. The first-success history is reachable under myopic play. Multiplying the current winning probability g_m by its history probability q_m gives exactly Beta(alpha+1,b_m+m)/Beta(alpha,beta). Since b_m+m~mA, the Gamma ratio gives m^(alpha+1)q_m g_m -> alpha Gamma(alpha+beta)/(Gamma(beta) A^(alpha+1)). Multiplication by the relative gain proves the claimed regret lower bound. The modified strategy agrees with myopic off the specified history; N_m is strictly increasing and f_m is nonnegative for sufficiently large m.

## originality

PASS

The supported contribution is the explicit first-success family for every fixed proper Beta prior, with strict one-step acceptance, a feasible at-most-two-later-success policy with its limiting gain, and the quantitative global regret lower bound. The existence of a strict finite counterexample, the posterior recursion, and adaptive improvement at the odds equality line are already covered and are not credited by this pass.

## value

PASS

The exact one-step rule is a natural computational shortcut, so it matters whether its failure is isolated, a tie artifact, or persists for every prior. The reachable strict counterexamples resolve this distinction. The two-future-success policy and explicit lower bound also separate conditional policy improvement from unconditional regret on a rare history; this is more than another finite counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
