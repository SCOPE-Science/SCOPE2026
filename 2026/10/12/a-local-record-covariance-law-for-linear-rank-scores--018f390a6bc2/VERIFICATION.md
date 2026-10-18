---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Under U_i=1, the first i values form a uniform i-subset, Pi(i) is its maximum with mean i(n+1)/(i+1), earlier coordinate means i(n+1)/(2(i+1)), and later coordinate means (n+1)/2. Multiplication by P(U_i=1)=1/i yields the exact stated arbitrary-real-weight covariance. D=2 sum_j j^2-2 sum_j j Pi(j) gives both Spearman covariance and conditional means. Summing positions produces harmonic Q covariance; classical independent-record law and Var(R)=1/(n-1) yield the exact correlation ~3/sqrt(n log n). Independently brute-enumerated all permutations n=2..7 and 27 (n,i) identities with a nontrivial signed quadratic weight vector; exact Fraction equality in all cases.

## originality

PASS

The classical independent upper-record process and the literature on Spearman metric correlations were compared by exact statistic definitions. Gnedin does not supply joint local record–linear-rank covariance; Jiang’s “record map” is a cycle/one-line correspondence, not these indicator variables. Published semantic hits concerned distinct ordinal/inversion dependencies. Best-of-knowledge formula is not known to be covered by a stronger theorem, with substantial elementary-identity overlap risk.

## value

PASS

Arbitrary deterministic linear rank scores provide a natural complete local record-covariance law; its Spearman specialization identifies position-dependent record effects, exact conditional Spearman biases and the global 3/sqrt(n log n) decay. A future researcher working with record-conditioned nonparametric rank statistics could need these precise dependencies. Elementary proof does not itself make the motivated general formula merely an arbitrary exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
