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

The distance-two condition suffices: on a geodesic minimizing selected internal vertices, replace any selected midpoint by an unselected common neighbor. The resulting walk is still a geodesic, since it has the same minimum length. Fibonacci-cube distances are Hamming distances by removing differing ones before inserting new ones. Thus a pair of neighbors of a given word has a unique midpoint exactly when their flips insert ones at two adjacent positions; a simultaneous deletion or mixed flip cannot introduce adjacent ones. This excludes the all-zero word for n>=2, leading/trailing zero runs of length at least three, and internal runs of at least four. Distance-two pairs with two midpoints give exactly the opposite-corner conflicts, so feasible sets are precisely the independent sets in the claimed graph. The length enumerator follows by multiplying the two end-run choices and summing over internal gaps. In the factorization (1+z)(1-z-z^3) the positive cubic root r is simple; the other cubic roots are a conjugate pair with modulus r^(-1/2)>1, so the next contribution is bounded. Greedy independence and maximum degree at most binom(n,2) preserve the exponential rate. A fresh exhaustive check for n=2 through 6 matched direct all-pairs visibility for every eligible subset and matched eligibility for every singleton, with maxima 2,3,5,5,9. Replay recipe: enumerate no-11 words, connect Hamming-distance-one words, and for each pair remove the selected vertices other than the endpoints and compare restricted and original BFS distances.

## originality

PASS

The supported distinct content is the explicit eligible-word and conflict characterization in Fibonacci cubes, its enumerator, and the resulting exact exponential growth rate. Hamming-graph square criteria and general singleton criteria are credited. The closest public same-family abstract announces results and a closely related method, but the exact available wording gives neither bounds nor a rate and supplies no demonstrable implication of the frozen result.

## value

PASS

The result replaces an all-pairs geodesic set optimization by explicit forbidden words and a sparse conflict graph for every dimension. It quantifies exponential separation between the eligible census and the unrestricted size of the Fibonacci cube and identifies the exponential growth of the actual visibility optimum. Those structural and asymptotic conclusions are materially more useful than a list of finite maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
