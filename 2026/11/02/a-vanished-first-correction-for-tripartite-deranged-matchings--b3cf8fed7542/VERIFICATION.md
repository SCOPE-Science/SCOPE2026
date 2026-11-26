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

Each perfect matching has m edges of each cross-part type, and the part-preserving relabelings are transitive on these matchings. After prescribing i,j,k edges, the residual part sizes are 2m-i-j, 2m-j-k, 2m-k-i up to order, and the residual cross-part counts are m-i,m-j,m-k. Partitioning the residual vertices and pairing them gives the product of the residual size factorials divided by the product of the three residual cross-part factorials. Dividing by the same count at i=j=k=0 and multiplying by the inclusion–exclusion multiplicities gives (1). Each R_m(a,b) is the binomial ratio binom(2m-a-b,m-a)/binom(2m,m), between zero and one. Log Taylor expansion inside the m^(1/10) cutoff has uniform error O((1+i+j+k)^4/m^3); exponentiation gives error O((1+i+j+k)^6/m^3) inside the 4^(-i-j-k) factor. The absolute factorial weights sum against that polynomial, and the exact and expanded tails fall faster than any power of m. For an independent moment calculation, write P=sum_r (r)_2 and Q=ij+jk+ki, so A=(Q-P)/2. Under the signed factorial moment functional with parameter lambda, let Y_r=r-lambda and Z_r=(r)_2-2 lambda r+lambda^2. They have zero means, square moments lambda and 2 lambda^2, and mixed moment zero. Then Q-P=sum_{r<s}Y_rY_s-sum_r Z_r, giving E[A]=0 and E[A^2/2]=9 lambda^2/8. The square-sum S_2(r)=(r)_3/3+(r)_2/2 has mean lambda^3/3+lambda^2/2, with parameter 2 lambda for r+s, so the sum of log second-order terms has mean -3 lambda^2/4. At lambda=-1/4 the combined coefficient is 3/128. This verifies the absolute O(m^-3) remainder and the matching-uniform claim. The finite verifier was inspected, not executed; its small-m checks are not evidence for the remainder.

## originality

PASS

The exact finite identity and the e^(-3/4) limit are prior results. The independently supported distinction is the vanishing first-order term, exact positive second-order coefficient, and O(m^-3) remainder for the scalar zero-overlap probability. None of the compared statements supplies that expansion.

## value

PASS

The zero-overlap event is the original deranged-matching observable, not a post hoc choice of a rare coefficient. The cancellation shows why a first-order correction is absent for this event and the explicit positive term gives its leading error relative to the known limit, distinguishing it from generic distributional convergence estimates. The result is narrow but useful for precise asymptotics of the tripartite benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
