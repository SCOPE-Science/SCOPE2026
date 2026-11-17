---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Conditional on fair unary colors, let B be signed color imbalance; B/sqrt(n) -> N(0,1). The row signed sums D_v are independent differences of two binomials with edge probability r=1-epsilon. For root children, excluding its self-loop, the balance difference T_n is conditional sum of n-1 i.i.d. {-1,0,1} terms with probabilities r q_(-1)(B), r q_0(B); the omitted root self-term is nonzero with probability O(n^-1/2). In epsilon>=c/log n, an exponentially tilted lattice local CLT at deviations B=O(sqrt n) yields q_j~(2pi n r epsilon)^-1/2 exp(-(rB-j)^2/(2nr epsilon)), j=0,-1, so the expected number of balanced children M_n has log M_n/log n->1/2-Z²/(2a) when epsilon log n->a>0. The conditional sign is 1/2 below |Z|<sqrt(a), and zero-event true with probability 1 above that threshold, producing 3/2-Phi(sqrt(a)); Bernstein handles a=0, CLT a=infinity; subsequence compactness yields moving-parameter o(1). Finite independent row convolution for n=5, K=2, r=3/4 gave q0=149/512 and q-1=87/1024. This finite check does not validate the local-CLT asymptotic.

## originality

PASS

Ghosh–Schwarzentruber Section 6.1 studies the same syntactic formula but on deterministic regular rooted trees and shows parity oscillation. It does not cover random independent directed edges, fair random colors or the 1/log n near-complete window. Benedikt–Zhukovskii studies undirected aggregate concentration and other density regimes. A similar Resultary mixed-Poisson balance theorem concerns two simultaneous independent balance predicates on fixed-density directed graphs rather than this single balance threshold under epsilon->0.

## value

PASS

A natural formula previously known for nonconvergence on trees develops a sharp, continuous probability transition on near-complete directed random graphs. The exact Gaussian crossover isolates a semantically meaningful missing-edge scale; it is not a textbook substitution or random unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
