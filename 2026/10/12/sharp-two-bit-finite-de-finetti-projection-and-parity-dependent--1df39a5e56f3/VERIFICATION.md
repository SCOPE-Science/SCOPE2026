---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

On exchangeable pairs with endpoint masses (a,c), TV to (A,C) is one half the sum of |A−a|, |C−c|, and |A+C−a−c|. Negative covariance is equivalent to √a+√c<1: both endpoint deviations from the product at the original mean equal the covariance. A de Finetti competitor satisfies √A+√C≥1 by the L² triangle inequality. If A<a, the product at √a strictly improves on the competitor's error on cell 00; the reverse case is symmetric. In the remaining quadrant the endpoint sum is the objective. A point with √A+√C>1 dominates a product law at any parameter in [√a,1−√c]∩[1−√C,√A], which is nonempty and lowers at least one endpoint strictly. This reduces the problem to a strictly convex quadratic, giving the clamped half and uniqueness. Equality in the L² bound forces a constant directing variable (including degenerate endpoints). For nonnegative covariance, mixing the deterministic parameter at the original mean with the {0,1} distribution of the same mean realizes the needed variance; means 0 and 1 are immediate. Finite exchangeability is the convex hull of the fixed-count urn laws, so convexity of distance reduces the maximum to them. With z=(N−m)/N≥1/2, the endpoint branch 2z−2√[z(Nz−1)/(N−1)] decreases in z, since (2Nz−1)²−4(N−1)z(Nz−1)=4z(Nz−1)+1>0; the central branch grows with m through N/2 and joins continuously. Thus the balanced integers are extremal. Substitution yields the claimed parity formulas; N=2,3,4 give 1/2, 4/3−√(4/3), and 1/6 respectively, in half-L¹ TV.

## originality

PASS

Credit the exact TV projection onto all infinitely extendible binary pairs, including uniqueness and the nontrivial odd-N extremal value. The fixed-count urn reduction and finite de Finetti type bounds are known; the symmetric even value alone is readily obtained from standard urn computations plus a diagonal-event lower bound. The inspected general results do not give the unique clamped parameter, or the odd-N optimum when the mean may change.

## value

PASS

The projection answers how much any negatively dependent binary pair must change to become infinitely extendible, not merely how well a prescribed sampler approximates it. It shows exactly when moving the one-bit marginal improves the fit and identifies a unique product even among all product mixtures. The first nontrivial odd urn already distinguishes the optimized and empirical parameters; the parity formulas give the sharp finite-extension benchmark. The value is the projection geometry and sharp optimization, not the size of the small asymptotic improvement alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
