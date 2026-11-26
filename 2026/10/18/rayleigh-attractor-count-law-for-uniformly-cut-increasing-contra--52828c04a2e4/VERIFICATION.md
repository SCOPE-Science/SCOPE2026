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

With the stated common slope 0<lambda<1 and equally spaced branch anchors, the jumps are all positive, so f is strictly increasing on its entire domain. Iteration is monotone after deciding the sign of f(x)−x and bounded away from 0 and 1 after the first step. A limit at a cut would require the neighboring branch fixed point to coincide with the cut, a null event. Thus every orbit converges to an interior branch fixed point, which is attracting by lambda<1, and periodic points are fixed. The i-th anchor is fixed exactly when there are i−1 cuts to its left. With N=n+1, k specified anchors split the N subintervals into k+1 blocks of positive lengths a_j/N; the requisite multinomial counts are a_0−1, a_1,…,a_(k−1), a_k−1. Using a^(a−1)/(a−1)!=a^a/a! at both ends yields the displayed coefficient formula for k≥1. An independent check of the limit and full law follows by setting A=(N−2)!/N^(N−2), letting T(z)=z exp(T(z)) be the rooted tree series, and using G=zT'=T/(1−T). The probability generating function in w is 1+A[z^N](T/(1−wT)−G), by summing the factorial moments for k≥1 and treating k=0 as 1 separately. Lagrange inversion gives Pr(K_n=j)=(j+1)(N−2)!/[(N−j−1)! N^j] for 1≤j≤N−1, with the constant coefficient zero. Its telescoping tail at j is the product of (1−l/N) for l=2 through j. At j of order x sqrt(N), the log tail tends to −x²/2; using log(1−u)≤−u gives a Gaussian tail bound uniform in N on this scale, sufficient for all fixed moment convergence. The Rayleigh mean, variance and scaling by sqrt(n) follow. At j=n the PMF reduces to (n−1)!/(n+1)^(n−1), with Stirling asymptotic sqrt(2 pi n) exp(−n−1). The common slope drops out of the counting law, even along a sequence of slopes in (0,1). The packaged finite occupancy verifier was inspected as source only; it does not assert a finite computation proves the limit.

## originality

PASS

Pass for deriving the exact finite and asymptotic attractor count in the specified uniform-cut contraction ensemble. The probability law itself is a classical random-mapping law in disguise: K_n has the law of C_(n+1)−1 conditional on C_(n+1)≥2, where C counts cyclic vertices of a uniform random self-map. The law, Rayleigh constant, and rare upper tail are therefore not new as random-mapping facts. The distinct result is the exact identification for the random interval dynamics, through the joint occupancy of branch anchors. The checked matching mapping sources and deterministic contraction theorem do not establish that link.

## value

PASS

The uniform simplex of cuts and equally spaced anchors give a natural solvable contrast between the deterministic sharp n and a typical random count of order sqrt(n), with fluctuations of that same order. The exact count law and its maximum-event probability answer a distinct question about the interval dynamics. They transfer a precise classical discrete probability structure to this ensemble, rather than purporting to improve the classical mapping law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
