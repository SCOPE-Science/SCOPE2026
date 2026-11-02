---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Differentiating individual concave payoffs gives b(y)=sqrt(y)−y and F_c(y)=sqrt(b(y)/c)−b(y), valid for positive rival efforts. For c>4/25, F maps (0,1) into itself. Unique Nash y*=1/(1+c)^2 has F'(y*)=−(1−c)^2/(4c), yielding exact local threshold 3−2sqrt(2). F²−id is positive near 0, negative immediately left of the repelling Nash, positive immediately right, and negative near 1, so IVT gives interior genuine two-cycle. Independent Fraction/isqrt outward interval arithmetic verified for c=1/6, J=[0.26299,0.26300], F(J) in (0.97447,0.97455), opposite endpoint signs and (F²)'(J) in (0.17,0.18), rigorously establishing attraction. No global attractor classification.

## originality

PASS

Best-of-knowledge claim is not established by the sources actually recovered: Old reset or different strictly convex-cost cycle does not entail smooth strictly positive linear-cost 4-move cycle, and continuous/damped learning theorems do not control undamped alternating exact replies. Priority is qualified by incomplete full-text access.

## value

PASS

A concrete unresolved behavioral boundary in undamped lottery-contest learning: nonconvergence can occur without opponent-zero resets even just beyond earlier 4/25 examples, and Nash loses local stability at an exact cost threshold. A certified nontrivial attracting orbit is meaningful dynamics evidence and mathematical structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
