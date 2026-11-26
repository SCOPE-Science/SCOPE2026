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

The exact scope of RESULT.md lines 4–12 is the cyclic-vertex count (all cycles, including loops) and each fixed indegree d, not the number of cycles or a growing-degree estimate. Conditional on the cyclic set of size c, its restriction is a uniform permutation of that set, not necessarily one cycle. Peeling the least nonroot leaf gives n−c−1 freely chosen parent letters in [n] and a final parent in the root set; the inverse successively removes the least nonroot absent from the remaining word, which exists because the final letter is a root. Each root gains indegree one from the permutation and the distinguished final root one more. This yields the stated conditional mean, with the c=n permutation case handled separately, and counting words and permutations yields P(C_n=c)=c(n)_{under c}/n^{c+1}. Direct mapped-orbit and indegree enumeration at n=2 through 5 confirmed this conditional formula and mass function (python3 /tmp/opencode/frozen_math_reproduction.py); the supplied checker was inspected, not run. For j>=0, log of j! times the binomial mass expands to −1+(1−j)c/n−(j/2)(c/n)^2+(1+j−j²)/(2n), with error O_j((c/n)^3+c/n²+n^−2) uniformly up to c=n^{3/5}. Exponentiating and using d!/((d−1)!)=d and d!/((d−2)!)=d(d−1), with the missing masses zero for d=0,1, gives zero linear term and conditional regression coefficient e^−1(−d²+3d−1)/(2d!) times (c²/n−1). The error is uniformly o(1) on that range; outside it the falling-factorial tail bound makes its contribution vanish even after multiplication by any fixed power of n. The same product bound and a Riemann sum imply Rayleigh convergence with polynomial moments, and Cov(X,X²)=sqrt(π/2). Conditioning gives the claimed covariance limit and strict eventual signs. The two profile sums are zero by the Poisson(1) moment identities; convergence for growing d or termwise summation of arbitrary n-dependent errors is not needed.

## originality

PASS

The exact cyclic-set/degree law and the zero-indegree coordinate are established antecedents. The supported distinct claim is the full fixed-degree second-order asymptotic for the cyclic-vertex covariance, including its nonzero-degree coefficients. A component-count profile with the same polynomial is not that covariance. The comparison explicitly credits the conditional-forest regression as recoverable from the stronger published exact law, rather than treating it as new.

## value

PASS

The cyclic core and the entire degree histogram are canonical global and local statistics of the same random structure. At their natural scale the evaluated covariance profile supplies the leading size and sign for every fixed class and identifies a second-order Poisson mode orthogonal to both conservation laws. This explains more than the earlier leaf coordinate or a sign observed in numerical sampling; no inference about growing degrees or joint fluctuations is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
