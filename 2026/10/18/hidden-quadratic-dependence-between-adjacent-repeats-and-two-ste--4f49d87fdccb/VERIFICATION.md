---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For independent uniform letters U_1,...,U_n with q>=2 and n>=3, the two edge families each form forests, hence A~Bin(n-1,1/q), B~Bin(n-2,1/q) and each cross edge pair is independent. Conditioning on the entire adjacent equality vector gives P(b_i=1 | a_i,a_{i+1}) equal to 1, 0, 1/(q-1) in cases (1,1), mixed, and (0,0). Hypergeometric sampling of the k successes conditional on A=k proves E[B|A=k]=[k(k-1)+(L-k)(L-k-1)/(q-1)]/L, L=n-1. The centered degree-two Krawtchouk polynomial equals twice the sum of independent centered pair products, whose orthogonal variance gives eta^2=2/((q-1)L). An explicit triangular centered mixed third moment is 2(n-2)q^-2(1-q^-1)>0; Cov(A,B)=0. Independently enumerated all q^n words for 12 (q,n) with 2<=q<=4 and 3<=n<=6 using rational arithmetic; every conditional mean, covariance and ratio agrees. The universal result follows from the symbolic proof, not finite experiments.

## originality

PASS

The precise all-(q,n) quadratic conditional regression and nonzero correlation ratio concern two jointly defined local equality counts. Neither single-pattern occurrence asymptotics in Mansour et al. nor a count of distinct adjacent pair types in geometric words logically determines their joint conditional expectation. An equality-forest argument itself is standard and not claimed new. Resultary semantic search returned no equivalent mixed A,B regression; an unindexed transfer-matrix or run-statistics identity might still imply it.

## value

PASS

A and B are canonical local pattern counts in random strings. Exactly zero covariance would ordinarily conceal their dependence; the exact nonlinear conditional predictor and its sharp explained-variance coefficient for every alphabet and length provide a useful structural and statistical diagnostic. It is not a mere renaming of binomial marginals or an isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
