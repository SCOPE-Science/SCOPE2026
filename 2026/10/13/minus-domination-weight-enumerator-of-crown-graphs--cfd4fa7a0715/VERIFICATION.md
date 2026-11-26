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

For d_i=x_i-y_i, the two closed-neighborhood sums at index i are B+d_i and A-d_i, yielding precisely A>=1+M and B>=1-m. The five pair factors partition all nine label pairs, and inclusion-exclusion extracts the exact two attained extrema before the feasibility truncation; specialization then records total weight. Weight two forces m=M=d, A=1+d, B=1-d, and nd=A-B=2d. Hence for n>=3 the labels are diagonal and the common vector has sum one; the stated multinomial counts all such vectors. A direct labeled-neighborhood enumeration against an independent extrema-state recurrence at n=2,3,4 confirmed the bivariate coefficients, with 6 and 16 diagonal minima at n=3,4 and two extra off-diagonal minima at n=2. The universal conclusion uses the proof, not this finite comparison.

## originality

PASS

Best of inspected evidence: the two-extrema feasibility criterion and bivariate/all-weight census apply to the deleted matching, not to intact complete multipartite adjacency. The scalar regular-graph lower bound is already a direct double count and is not credited as original. The closest same-graph diagonal minimum census concerns a different label alphabet and rule, and neither it nor the multipartite census implies the ternary crown enumerator.

## value

PASS

The crown is a natural highly symmetric graph where the missing matching obstructs the intact bipartite formulas. Tracking the two side sums gives a genuine complete distribution (not just an optimum) with a constant-size alphabet of pair extrema and only polynomially many side-sum states. It also identifies which minimizers realize the universal lower bound and why the small matching boundary behaves differently. These outputs are useful for exact enumeration and comparison with other domination rules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
