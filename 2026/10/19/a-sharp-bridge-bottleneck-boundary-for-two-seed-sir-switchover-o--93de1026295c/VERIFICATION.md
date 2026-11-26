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

For the deterministic one-step rule, preassign an independent open/closed variable for each edge when it is first tested between an infected and susceptible endpoint; no second opposite-direction test can reach a susceptible endpoint after that first attempt. The final set is the union of open components meeting the two seeds. The component hit probability in RESULT.md uses unordered sampling without replacement correctly. Independently, let P sum p^{distance} over unordered vertex pairs and J sum p^{Steiner subtree edge count} over unordered triples. Inclusion–exclusion for connection of each vertex to at least one uniform seed gives U=2+[4(N-2)P-6J]/[N(N-1)] including the cases in which the vertex is itself selected. Counting pairs on the double star gives coefficients (2n+1,n(n+1),n^2) for p,p^2,p^3; counting triples gives (n(n+1),n(n-1)+2n^2+2 binom(n,3),n^2(n-1)) for p^2,p^3,p^4. Symbolic factorization after subtracting U from 2+2np reproduces the precise boxed difference. Q_1=2p; Q_2=6p^2+5p-10 is increasing with sole interior root (sqrt(265)-5)/12; for n>=3, Q_n is increasing and Q_n(1)=2-(n-1)^2<0. The prefactor reverses the sign in (0,1) and enforces endpoint equality. The n^2 coefficient of Q_n is 3p^2-4, yielding the stated fixed-p normalized limit. These counts and the factorization are an analytic replay path independent of the supplied finite enumeration, which was read, not executed. Only expected sizes on the stated homogeneous toy graph are compared.

## originality

PASS

The open-component representation and general switchover question are prior. Prior endpoint sufficient theorems and the closest tree catalogue statements do not cover the complete double-star fixed-two-seed trichotomy, its unique exact crossing, or its nonzero size-normalized gap.

## value

PASS

A symmetric two-star tree with one bridge is a natural exact bottleneck benchmark for open-component sampling. The result determines all branching sizes and all probabilities, distinguishes both strict orderings and a unique crossover case, and shows that the large-size comparison is not a vanishing boundary effect. It is a mathematical benchmark for percolation expectations, not a real-world model or a ranking of outbreak distributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
