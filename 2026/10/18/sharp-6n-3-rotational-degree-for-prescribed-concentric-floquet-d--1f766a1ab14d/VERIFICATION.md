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

With s=r², uniqueness for the scalar radial ODE makes every periodic trajectory constant in s; positive angular speed makes every positive root of Q into a circle with physical period 2π/Ω(s_i). In angular time, differentiate ds/dθ=2sQ(s)/Ω(s) at the root and evolve for angle 2π. This gives log μ_i=2s_iT_iQ′(s_i), so hyperbolicity is simple-root multiplicity and the exact absence of extra circles forces Q/A to have one constant nonzero sign on (0,∞). For the converse, squared Lagrange cardinal functions interpolate both the positive signed radial quotient values and the positive angular speeds; their common zero set is empty since the original cardinal functions sum to 1. This proves strict positivity, node values and the upper degrees max(deg Q, deg Ω)≤3N−2. For any fixed radii and periods, choose signed quotient values (1,ε,…,ε). If there were qualifying degree ≤2N−3 positive quotients for arbitrarily small ε, bounded coefficient sequences would have a nonnegative limit with N−1 double interior zeros and value 1 at the first node. Unbounded sequences have a nonzero limit after coefficient normalization, with N double interior zeros, since all original node values remain bounded. Both cases contradict the degree cap. There is no cancellation of radial and angular leading terms (restrict to y=0, where they are separate Cartesian components), so degree is precisely 2 max(deg Q,deg Ω)+1. N=1 requires a nonconstant Q and permits degree 3 for every admissible datum. The two-circle witness independently gives the root 13/3 of the unique affine radial quotient and multiplier exponents −12π and 24π/5. The all-N proof is analytic; the frozen rational checker was inspected, not executed. No claim holds here about unrestricted planar fields or forward completeness.

## originality

PASS

The supported distinct claim is the complete exact compatibility condition and sharp 6N−3 worst-case degree for arbitrary N in the stated rotational class, uniformly for every fixed choice of radii and periods. General polynomial realization of periods and qualitative stabilities is established prior work. One distinct Resultary entry fully covers and refines the N=2 slice, but does not establish the all-N minimum worst-case degree. No covering general statement was identified in the inspected evidence.

## value

PASS

Periods and multipliers are natural independent invariant data of a hyperbolic cycle; the theorem specifies exactly which lists can coexist without spurious invariant circles. Quantitative stability and the sharp degree price at every fixed geometry and period list are substantive, even though the rotational restriction is essential and small N has finer individual degree information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
