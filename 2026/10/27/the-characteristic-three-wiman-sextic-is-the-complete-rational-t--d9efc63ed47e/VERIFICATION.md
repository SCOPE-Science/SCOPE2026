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

In characteristic three, with C=X^2+Y^2+Z^2, the sextic is C(C^2+X^4+Y^4+Z^4). Multiplying the four sign lines gives -sum X^4+2 sum X^2Y^2, which is the residual quartic. The smooth conic has exactly the four points whose coordinates are all nonzero over F_3; the indicated sign lines are their polar tangents. Their six distinct pair intersections have two nonzero coordinates, lie off the conic, and are transverse. At a tangent contact there are two smooth branches with intersection multiplicity two; completing the square in a transverse coordinate and changing a unit gives the formal form y^2-x^4. Its Tjurina quotient has basis 1,x,x^2 since 2 and 4 are units, and its delta is the branch intersection multiplicity two. This gives the full singular basket, sums 14 and 18, and genus 0+14-5+1=10. The conic and each line are rational over the base field. There are exactly ten double-counted rational points and no triple intersections over any extension, hence 5(q+1)-10 and the asserted zeta function. Any geometric projective automorphism permutes the four lines, with trivial kernel since they form a dual frame. Conversely the plane representation of PGL_2(F_3) on the split smooth conic gives 24 such automorphisms. No computation over F_3 alone is used to bound the stabilizer over the algebraic closure.

## originality

PASS

The scoped increment is the full description of the literal characteristic-three fiber, especially recognition as the complete rational tangent arrangement and the resulting geometric incidence and full projective group. The 2018 paper publishes the equation and explicitly notes reducibility in characteristic three, but its characteristic-three statement is not this classification. A distinct later Resultary entry gives equivalent coverage of all the salient claims, and some consequences there are verbatim mathematical matches; its documented record date is later than the frozen record, not evidence of earlier publication or priority. No independent novelty is credited to the genus, local-invariant sums, or zeta conversion once the arrangement is known.

## value

PASS

A complete structural description of an explicitly excluded bad-characteristic fiber of the standard Wiman plane model is a natural boundary problem, not an arbitrary point count. Identifying the entire reduced fiber as the four rational tangents to the conic explains exactly how it degenerates and gives its embedded projective symmetries and arithmetic. Those are useful for comparing this model with good-characteristic models; the numerical corollaries are bookkeeping, not independent contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
