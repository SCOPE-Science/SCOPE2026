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

Distinct exact deletion vectors give distinct residual multisets. Counting inputs above d gives B(n−t,q); for ordered pairs d,e the sum of their coordinatewise maximum is t+m for m=||d−e||₁/2, so Theorem 9's pair count gives the second moment, including zero contributions if n−t−m<0. At t=3 the only deletion shapes give counts binom(K,3), H(K−1), J. Once the nested sets of sizes k,h,j are chosen, all surplus above k+h+j goes to the j coordinates already of size at least three; at j=0 the only allowed mass is k+h. This gives precisely the histogram. Independent finite checks matched both moments in 104 cases, the coefficient formula in 80 (q,t,m) cases, and the histogram in 28 (q,n) cases, including the two exact rational examples; the supplied transcripts do not establish the infinite assertions. For the limit, K is hypergeometric with (population, marked, draws)=(n+q−1,q,n); its variance is asymptotic to p²(1−p)q under the stated regime. Nonsquarefree deletion vectors give a deterministic count error O_t(q^(t−1)). Taylor expansion of binom(K,t) at the exact mean has first derivative asymptotic to (pq)^(t−1)/(t−1)!; the remainder is bounded by O_t(q^(t−2)(K−μ)²), of L² norm O_t(q^(t−1)) by the sampling-without-replacement fourth-moment bound. Thus both the CLT and convergence of rescaled variance follow, with coefficient p^(2t)(1−p)/((t−1)!)². Keeping the exact μ avoids assuming a rate for n/q→λ. This is not the multinomial occupancy law, and t is fixed in the Gaussian claim.

## originality

PASS

The distinct supported result is the exact t=3 one-sided histogram and the growing-alphabet fixed-t Gaussian and variance laws for uniform multisets. The mean is routine incidence counting, and the exact second moment is a direct corollary of the prior pair-distance enumerator; neither gets independent originality credit. Inspected same-level and ordered-word results do not cover the histogram or Gaussian law on the stated probability space.

## value

PASS

The channel's one-sided volume varies with the center; an average or a fixed-radius metric ball does not describe that variation. The complete t=3 frequencies and the leading Gaussian variance for every fixed t in a genuine growing-alphabet regime supply precise finite and asymptotic benchmarks on the natural uniform multiset model. The value rests on these volume distributions and scales, not on reusing the pair enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
