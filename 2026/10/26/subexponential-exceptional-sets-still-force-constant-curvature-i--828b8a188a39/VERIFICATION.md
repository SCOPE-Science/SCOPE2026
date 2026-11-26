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

Use a smooth ambient norm on the tangent bundle. On the one-dimensional unstable line, the log expansion is an additive cocycle whose derivative at time zero depends Hölder-continuously on the base point, since the unstable line is Hölder. Its integral over an orbit is the log expansion; dividing by the period gives the exponent. To make the specification counting step precise, suppose a primitive orbit has nonzero centered average c. Reverse the sign of the potential for this argument if necessary so c>0. Fix a tracing scale sufficiently small that the change in potential is <c/4, and also smaller than a fixed positive-entropy separation scale. For a sequence of lengths n, take exponentially many separated n-segments and use bounded-gap periodic specification for the mixing Anosov geodesic flow to append to each a Cn-segment of the chosen periodic orbit and close up. The chosen periodic block contributes at least (3c/4)Cn−O(1), the arbitrary segment costs at most n times the sup norm, and the gaps cost O(1). A fixed sufficiently large C makes each closed orbit a mismatch. Counting primitive orbits is valid: the least period is at most (1+C)n+O(1) and iteration does not change its average. For a given primitive orbit at most O(n) of the separated free segments can be assigned to it: divide its initial tracing phases into bounded-size bins small enough that two phases in a bin give synchronized traces closer than the separation scale, using the uniform bound on the flow speed. The exponential count thus survives passing to primitive orbit classes. This contradicts the assumed zero exponential growth of the exceptional complement. All primitive exponents, hence all periodic-point unstable exponents, are α. Nina Zarate–Romaña's Theorem 1.3 then applies to the compact smooth negatively curved surface and gives K=−α².

## originality

PASS

The supported difference is that an exceptional family of zero exponential counting growth is allowed in a surface unstable-exponent rigidity hypothesis. The all-periodic curvature theorem and the hyperbolic-dynamics tools are not new. A more general orbit-counting route follows from standard specification and entropy, but an existing stronger theorem directly covering this Lyapunov-potential and curvature conclusion was not located in the statement-level checks.

## value

PASS

The result makes a complete periodic-data rigidity test insensitive to omitting any subexponentially counted family of primitive closed geodesics. It shows that a single discrepancy from the candidate common exponent, if it exists, forces exponentially many discrepancies. That is a meaningful change in the admissible data for a geometric conclusion, not a new proof of the complete-data theorem alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
