---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n>=3 uniform independently oriented tournament and directed r-cycle count C_{r,n} modulo cyclic rotation, conditioning on occurrence of any directed r-cycle fixes exactly one incoming and one outgoing incident edge at each of its r vertices. Its score law becomes 1+Bin(n-3,1/2), while all other vertices retain Bin(n-1,1/2). Summing over cycles yields covariance (n)_r/2^r times [Q_{n,k}-B_{n,k}], with Q/B=4k(n-1-k)/((n-1)(n-2)), exactly the asserted square-root sign polynomial [n-1-(2k-(n-1))^2]. Integer zeros iff n-1=s², s>=2, at k=(s²±s)/2. The ratio to the triangle covariance is a_{r,n}=(n-3)_(r-3)/2^(r-3). The deterministic identity T=binom(n,3)-sum_k binom(k,2)N_k proves centered T in the linear score-span, hence residual orthogonality to every N_k identifies the exact L² *linear projection*; it is not full conditional expectation. Independently enumerated all labeled tournaments for n=3..5 (2^3+2^6+2^10=1096 orientations) and checked 26 exact rational covariance pairs; all matched. General proof follows from conditioning, not finite cases. Evidence: Source text in assigned RESULT.md §§Finding, Assumptions and scope, Proof, Verification, Relationship to prior work; repository Git tree 49f0c8c021d774e34ca06bd8a2c5fd7cf2b9634e

## originality

PASS

Best-of-knowledge novelty of the exact final quantitative claim, with classical proof mechanisms and expressly credited subcases excluded. Genuine broad/theorem and full-text comparison risks retained; inaccessible full texts alone do not dictate failure.

## value

PASS

The covariance of directed cycle counts with a natural random-tournament degree-histogram statistic has an exact all-n, all-length arithmetic zero/sign phase, including the square-root thresholds and an exact projection rigidity onto an entire nontrivial linear statistic span. These finite-size identities give finer fluctuation structure than asymptotic Hamilton-cycle normality and are natural mixed combinatorial moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
