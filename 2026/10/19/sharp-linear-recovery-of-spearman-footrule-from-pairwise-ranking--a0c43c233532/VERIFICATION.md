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

For uniform S_n, swapping values x<y between a<b changes footrule by twice the number of cuts t in [a,b) with x<=t<y; other locations are unaffected. Averaging over unordered value pairs gives the stated positive covariances. Two- and three-site orderings give Sigma=(I+B^T B)/12, which is positive definite even at n=2. The cross-covariance is B^T h, so the complete-graph Laplacian puts it in the (n+1)/12 eigenspace of Sigma, yielding the unique affine fit. The residual is for affine prediction only, not a loss of information in the full comparison vector. Independently evaluated the two all-size sums using symbolic power sums: for s_i=i^2-(n+1)i+n(n+1)/2, the double-centered assignment variance is [n^2(n^2-1)/6-2 sum_i(s_i^2)/n+(n^2-1)^2/9]/(n-1). With H_i=i(i-1)(3n+1-2i)/6, the squared cross-covariance norm is [n sum_i(H_i^2)-(sum_i H_i)^2]/[n(n-1)]^2. These reduce to (5) and (6); subtraction verifies (4). The exact forward difference of (3) has numerator 3(2n+1)(23n^4+46n^3-311n^2-334n-504) over a positive denominator. The quartic is negative for 2 and 3 and strictly positive from 4 by its expansion in n-4. R_2^2=1, R_3^2=9/10 and R_4^2=58/65; the leading terms give 51/56. Replay: sum the displayed polynomials over i=1,...,n (or use symbolic summation), then factor R^2(n+1)-R^2(n). The supplied verifier was inspected but not executed; its finite counts are frozen self-reported evidence, not the all-size proof.

## originality

PASS

The supported distinction is the exact footrule cross-covariance and complete finite affine projection, including the sharp worst-size and limiting variance fractions, not comparison precision, footrule moments or asymptotic normality. The closest available statements give ingredients or different projections, not the claimed evaluated projection.

## value

PASS

The uniform null is a natural benchmark for replacing footrule by linear comparison summaries. This solves the complete affine prediction problem and supplies both the exact worst-size performance guarantee and the persistent nonlinear fraction 5/56, a distinction one cannot infer from complete pairwise information or a scalar footrule–Kendall correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
