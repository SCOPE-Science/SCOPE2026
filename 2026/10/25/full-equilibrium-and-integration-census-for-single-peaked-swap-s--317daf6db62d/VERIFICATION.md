---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

At peak Lambda=1/2 the closed-neighborhood payoff has exactly two levels: each agent is positive iff at least one adjacent vertex has the other color. A mutually strictly beneficial opposite-color swap exists iff both colors have an interior vertex of a length >=3 monochromatic run: those vertices are nonadjacent, and swapping makes both integrated. Thus an equilibrium has all runs of at least one color of length <=2. For k paired cyclic runs, a short run has S(t,z)=tz+t^2 z^2, an unrestricted run has T(t,z)=tz+t^2 z^2/(1-t), and inclusion-exclusion gives S(x,z)^k T(y,z)^k+T(x,z)^k S(y,z)^k-S(x,z)^k S(y,z)^k. Marking a blue run yields the exact n/k coefficient, so P_{n,b}(z) counts vertex-labeled colorings, not individually distinguishable agents. Extremal support is [b+ceil(b/2)+1,min(n,3b)] for n>=3, 1<=b<=r, attained continuously by distributing 1..2 minority runs and majority excess. Independently brute-enumerated all b<=floor(n/2), n=3..10, comparing direct profitable swaps with independently implemented run polynomial for 24 parameter pairs; the result E_{6,3}=14 agrees. The general claim is proved by cyclic-run argument, not finite tests. Required actual files inspected: RESULT.md blob eb0f3082..., verify.py b4630dba..., METADATA, AUDIT, SLOGAN, VERIFICATION.

## originality

PASS

Best-of-knowledge new full run-refined equilibrium integration census and attainable welfare spectrum, conditional on published game definition. Bilò et al. prove existence and approximate price-of-anarchy bounds, not the exact (n,b,j) polynomial in inspected manuscript. The other jump model allows unilateral moves into vacancies, so its superficially similar extremal ratios do not cover pair-swap counts.

## value

PASS

A natural complete classification of equilibria and exact multiplicities at each integration value, over every cycle size and population balance, improves qualitative existence and efficiency bounds and permits welfare-weighted equilibrium comparisons. The PoA extremum is a byproduct and not claimed alone as the discovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
