---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

On normalized Bergman monomial bases for -1<alpha<0, beta>alpha+2, the differential Hilbert coefficient B_ij=(i+1)/(i+j+1) sqrt(w_i(beta)/w_j(alpha)) has strictly positive Cauchy exterior minors. Dividing the kth compound by product of first k target row weights leaves row factors q_I decreasing and log convex, and positivity of maximizing vectors yields strict norm decrease; Holder gives log convexity. Fixed compact compound operator plus strong convergence of diagonal row weights to the first-row projection yields operator-norm convergence, whose selected exterior row norm equals k! sqrt(det G_k(alpha)) by Cauchy–Binet and the binomial moment kernel. Positive definite G and w_m(beta)~m! beta^{-m} imply the sharp fixed-k s_k~k sqrt((k-1)!) sqrt(det G_k/det G_{k-1}) beta^{-(k-1)/2}. At alpha=-1/2, k=1 constant 2sqrt(log 2). Independent finite-section SVD verified decreasing first three normalized singular-value products across beta=3,8,20,80; finite truncation not asserted to certify the limiting constants.

## originality

PASS

Li–Zhou provide the differential Hilbert operator’s monomial coefficient matrix, boundedness, compactness, trace class and weighted norm framework, but the inspected full paper does not calculate large target-weight fixed-rank singular asymptotics, exterior-product log convexity or the evaluated Gram determinant hierarchy. Classic exterior-power and total positivity identities are ingredients, not newly claimed theorems. Best-of-knowledge noncoverage is qualified by operator-spectrum literature risk.

## value

PASS

All fixed approximation-number levels of an established two-weight differential Hilbert operator acquire exact beta-decay powers and positive Gram-determinant constants; this distinguishes persistent constant mode from rapidly suppressed higher ranks. It is a useful full hierarchy, not a routine reparameterization of a single norm estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
