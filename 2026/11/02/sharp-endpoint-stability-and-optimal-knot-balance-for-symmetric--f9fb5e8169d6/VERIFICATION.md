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

Integrating nodal hats gives the positive-definite Gram matrix in RESULT; each kernel evaluation row is represented by the corresponding coordinates of the inverse. For an arbitrary evaluation point the row is a convex combination of the adjacent nodal rows. The alternating nodal signs hold on the full open parameter interval by the displayed coefficients. An independent symbolic reconstruction used the signed integral 1 (the projector fixes constants) plus twice the negative triangle areas to recover E, S and C. E−S has a strictly positive numerator after removing the common positive denominator, and E−C changes sign once with 2ε²+11ε−5. C strictly decreases; the endpoint derivative has the stated all-positive numerator after factoring its positive denominator. This gives the switch and unique minimizer (√161−11)/4 with norm 4/3+√161/21, limits 7/3 and 22/9, and C>2 iff ε<1/3. At each maximizing knot the input sign of the kernel attains the norm; continuity identifies the output essential supremum with its true maximum, including at endpoints. Even interior evaluation points cannot add norming locations because each mesh interval has at least one strictly submaximal shoulder endpoint.

## originality

PASS

The inspected general sharp bound 3 is a worst-case bound across partitions. The same-day metric-graph stability bound contains the path geometry but does not fix the parameter-dependent norm. Exact periodic, star and single-refinement calculations are distinct. The supported distinct feature is the explicit finite-path branch and active-knot classification including the sharp minimax knot placement, not the hat-kernel method itself.

## value

PASS

The symmetric path permits clustering at either the center or both boundaries. A uniform stability constant cannot decide the best mesh or even whether the boundaries or center dominate. Their competing monotone branches, below-two optimal amplification, and distinct above-two clustering limits answer a concrete, minimal mesh-design question for the standard least-squares projector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
