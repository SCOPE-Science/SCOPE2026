---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For random labeled tournaments every edge orientation is independent and fair. For i≠j write (Di,Dj)=(A+E,A’+1-E) with independent A,A’~Bin(n-2,1/2), common opposite Bernoulli E. Direct conditioning yields covariance of score functionals = -(1/4)EΔφ(A) EΔψ(A). For B~Bin(n-1,1/2), the binomial shift identity Cov(φ(B),B)=(n-1)/4 EΔφ(A) and Var(B)=(n-1)/4. Summing i=j and i≠j terms proves exactly Cov(Sφ,Sψ)=n[Cov(φ(B),ψ(B))-Cov(φ(B),B)Cov(ψ(B),B)/Var(B)]. Indicator functions give Σ=n diag(b) - n bb^T -(4n/(n-1))((k-(n-1)/2)b_k)((l-(n-1)/2)b_l). White normalizing yields n(I-uu^T-vv^T), u,v orthonormal for every n≥2, rank n-2, spectrum n repeated n-2 and zeros twice. Taking trace yields E Pearson Qn=n-2. Complete exact-rational enumeration of all 2^{n choose 2} tournaments for n=2..6 independently checks every covariance entry; infinite theorem follows from Bernoulli conditioning, not enumeration.

## originality

PASS

The nearest inspected Cohn–Godbole–Harkness–Zhang source (2015) uses shared-edge conditioning to analyze Seymour-vertex count thresholds but does not present a universal covariance bilinear form or flat whitened histogram spectrum. Alspach–Reid (1978) is closely title-matched but accessible abstract concerns deterministic degree-frequency realizability; the full 1978 text remains inaccessible, so cannot assert whole-document NOT_COVERING. Aldous–Kolesnik concerns attainable mean score vectors, not empirical histogram covariance. Shared-edge probability and two deterministic sum constraints are prior facts; the full exact projector/expectation law is the surviving mathematical result with genuine older-literature risk.

## value

PASS

All score-frequency bins are a canonical empirical distribution for independent fair tournaments. The exact covariance projector completely characterizes second moments of any sum of score functions, identifies exactly two deterministic null directions, proves otherwise flat normalized variance spectrum, and corrects the Pearson discrepancy mean from the multinomial n-1 benchmark to n-2. This is a natural whole-family stochastic invariant with direct statistical interpretation, not an isolated cheap variance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
