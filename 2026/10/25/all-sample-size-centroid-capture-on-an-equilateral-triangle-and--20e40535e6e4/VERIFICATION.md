---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For every integer m>=1, normalized perimeter arclength on the equilateral triangle gives an atomless cyclic angular measure at the centroid. A failed convex-hull capture is equivalently a single cyclic gap of at least pi (unique outside null antipodal configurations). Counting its first sample produces p_m=m E[q(X)^(m-1)]. Direct opposite-ray barycentric intersection gives Q(t)=(1-t)^2/(2-3t) on [0,1/2] and q(t)=1-Q(1-t) on [1/2,1]. A Laurent-polynomial substitution z=2-3t yields the supplied finite Q+Q log2 formula, including p_2=1 and p_3=25/27-(20/81)log2. Differentiation verifies the unique strict angular-mass maximum q(2/3)=5/9 with q''=-2; the interior Laplace estimate yields 3 sqrt(pi m/5)(5/9)^m, with strictly subleading cusp/endpoints. Independently computed m=1,2,3,4,5,10,20 integrals and a fresh 30,000-sample geometric Monte Carlo agree. The integrals, not the finite experiment, establish the all-m law.

## originality

PASS

Earlier Wendel symmetric-direction convex-hull formula does not apply to the nonsymmetric triangle perimeter direction law; Berele–Catoiu establishes only the 4/9 minimal halfplane perimeter mass, not the full angular law for every sample size. The prior 3-sample centroid probability is a specialization but does not imply the all-m integral or rare-failure prefactor.

## value

PASS

The all-m exact event probability for the fixed natural centroid and normalized arclength triangle, including the asymptotically sharp polynomial factor, is independently useful in random-polytope containment and geometric probability. Recovering the previously known exponent 5/9 alone would be a routine restatement; the complete distribution and second-order tail are substantive additions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
