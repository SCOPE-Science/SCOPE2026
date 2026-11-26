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

The marginal count chooses the unique occupied incident edge; the joint count correctly separates use of the common edge from independent choices of the two incident edges from their disjoint edge classes, allowing the same third vertex. Factoring the joint count as binom(B+1,m−1)L_m/(B+1) verifies the quotient on every adjacent pair including the upper boundary. With K=n−2, t=N−m and 0<x=b/a<1, the quotient is the product of 1+x/((m+1)(m−x)) and 1−(K²−t)/(t−K)²; on 2K≤t≤N−1<K² both factors are positive and strictly decrease with m. This proves strict log-concavity at every interior positive index. The exact replay /workspace/reproductions/3.py verifies all four shifted crossing polynomial identities by equality at nine integers and a degree bound of eight, and verifies the three n=8 covariance fractions. The positive coefficients after shifting r=z+3 give strict opposite signs on either side of ceil(n/2), so the global maximum is unique. The strict shape makes the superlevel set above 1 contiguous or empty; q_m vanishes beyond B+2 and then covariance is −p_m², including zero when p_m=0. For n=8 strict unimodality and the checked neighbors of m=4 imply the asserted strict signs throughout. The packaged finite checker was read, not rerun.

## originality

PASS

Inspected sources do not yield the finite-edge-budget ratio's strict log-concavity and exact unique mode. The elementary joint-counting identity is not credited as new; the added theorem is the shape of the normalized ratio over its full positive range and the resulting sign-window constraint.

## value

PASS

Normalizing by the marginal square isolates dependence of two leaf events as the common edge budget changes; a shared edge competes with the effects of sampling without replacement. The exact peak at ceil(n/2) and strict shape control where positive dependence can occur at each finite n, information not given by marginal concentration or asymptotic normality. The eight-vertex calculation illustrates the window but is not the main contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
