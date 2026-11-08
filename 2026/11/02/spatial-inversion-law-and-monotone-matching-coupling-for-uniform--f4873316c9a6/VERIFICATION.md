---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Uniform k-two-cycle involutions are sampled by a uniformly chosen moved set r=2k and uniform perfect matching on it. For positions a<b, d=b−a, both moved contributes r²/[2n(n−1)] (direct partners always invert, others by exchangeability); mixed fixed/moved contributes r(n−r)(n−d−1)/[n(n−1)(n−2)], both fixed contributes zero. Substitution gives 2k²/[n(n−1)]+2k(n−2k)(n−d−1)/[n(n−1)(n−2)] for n≥3; n=2 is checked separately. Gap slope and k-monotonicity follow by endpoint convex interpolation. Coupling consecutive classes by pairing a uniformly selected pair of current fixed positions preserves uniformity because each (k+1)-cycle target has k+1 predecessors and each k source has C(n−2k,2) choices. Exact inversion increase is 1+2#{t between a,b whose pi(t) lies between}, so strictly positive for every transition and gives strict stochastic increasing h(I) and conditional covariances. Sum over gaps produces known mean k(2n−k)/3. Independent exact all-involution enumeration n=2..8 checked local probabilities.

## originality

PASS

Best-of-knowledge originality PASS for the precise stated claim, not a priority certificate. Potential aliases include class-conditioned Coxeter length distribution, q-Hermite polynomials, random partial matchings, and stochastic ordering under adding disjoint transpositions. Univariate length generating functions identify marginals but do not specify individual event probabilities P(pi(a)>pi(b)) by gap. Désarménien 1982 q-Hermite inversion polynomials and Dukes 2004 / Hart–Rowley 2014 length generating polynomials cover the global first moment and full univariate distribution. Pinsky 2025 concerns all permutations with fixed point counts, a larger but differently conditioned distribution; it does not imply the restricted uniform class of involutions without additional conditioning. Resultary cycle-count versus gap law for unrestricted permutations has a different statistic and measure. Principal residual risk: An older stochastic-order or matching-growing coupling proof might already imply strict monotonicity.

## value

PASS

While global inversion generating polynomials are classical, this complete affine position-gap profile is a distinct local observable and the explicit all-class monotone coupling gives an actual stochastic order rather than only increasing mean. Both are natural reusable facts in random permutation/matching studies; no trivial substitution from the univariate generating polynomial yields the coupling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
