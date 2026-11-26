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

By irreversible occupancy a rejected start cannot become acceptable later, so first exponential clocks suffice. For an empty interval of length n>=2, an intersecting start lies from two sites left of its first site through its last site; conditioning on the union being empty gives exactly the hierarchy of lengths n,n+1,n+2, with the two parity-specific end rates and the stated interior sums. For a single site there are three possible covering starts, giving the stated derivative of v after averaging over parities. Factor out the interior hazard: exp(−(m−1)(1+epsilon)t) for length 2m and that factor times exp(−lambda_s t) for length 2m+1. The resulting three ODEs give a bounded hierarchy solution on every finite interval. Uniqueness follows by integrating factors for the nonpositive, possibly large diagonal rates and iterating the uniformly bounded off-diagonal integral operator, with factorial decay. Thus the ODE solution represents the actual interval probabilities; all three coefficients are nonnegative and, from the reduced equations, at most one. At epsilon=0 all three equal exp(−2(1−e^(−t))) and the integrated fast term is (1−e^(−2))/2. For epsilon>0 the fast term has the same limit by dominated convergence. Integrating the third equation up to u/epsilon shows that the epsilon-z term is uniformly O(epsilon), whereas the e^(−t)A term converges to its zero-rate integral for each u>0. Hence B_1(u/epsilon) tends to e^(−2), and a second dominated convergence with weight e^(−u) gives the limiting integrated slow term e^(−2). The sign and jump follow after multiplication by 3/2, and finite-time continuity explains noncommutation of the two limits. In the homogeneous case the symmetric explicit solution gives the quoted quadrature.

## originality

PASS

The supported distinct claim is the period-two exact transient trimer law and its finite jump from suppressing one arrival channel, not generic discontinuous RSA or the known homogeneous lattice law. The local catalogue has a demonstrably equivalent stronger finding that resolves parity and reduces three equations to two, but its stated date is later than the frozen record. This exact overlap is credited and does not establish older coverage or independence. The accessible earlier singular-perturbation paper changes the spatial support and hence the conflict geometry rather than the intensity on fixed integer starts. The very plausible older bipartite-chain paper could not be compared beyond bibliographic and reported abstract-level evidence after reasonable lawful attempts; that neither shows nor rules out prior implication.

## value

PASS

Switching on arbitrarily rare odd starts changes jammed vacancy by a finite, explicit amount and beats homogeneous coverage in the limiting regime. This exposes a real order-of-limits effect and identifies a class of gaps that survive the fast stage and fill on the slow time scale. The exact finite-dimensional transient reduction shows how the macroscopic effect arises in a standard irreversible deposition model, rather than just fitting simulations or computing a known homogeneous constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
