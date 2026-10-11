---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The hyperboloid proof reconstructs the support optimization without using a finite experiment as an infinite proof. For a support normal \(n\), the vertex pairings \(s_i=\langle v_i,n\rangle\) are nonnegative and the maximum hyperbolic distance is attained at a vertex because projective barycentric normalization only increases the Lorentz denominator. Inverting the regular-simplex Gram matrix gives the exact normalization \(1=(q-1)^{-1}(\sum s_i^2-\frac{q}{dq+1}(\sum s_i)^2)\). After dividing by \(M=\max s_i\), minimizing width is equivalent to maximizing a strictly convex quadratic on a union of cube faces. Hence a maximizer is a zero-one pattern. With exactly \(k\) ones the objective is \(F_k=k((d-k)q+1)/(dq+1)\), and the consecutive difference has the stated sign, uniquely maximizing at \(k=\lceil d/2\rceil\). This proves both the closed thickness formula and the complete minimizer classification. The package verifier independently checks the Gram inverse, the difference identity and the tetrahedral specialization.

## originality

PASS

Lassak's primary paper defines this width and thickness, computes a facet-supported width for regular hyperbolic simplices, and in dimension three constructs a narrower edge-supported support to show regular tetrahedra are not reduced. The inspected source does not optimize over all supports in arbitrary dimension and does not classify every minimizing face. Current Resultary search returned the assigned all-dimensional theorem as the exact same-object hit, with no stronger published regular-simplex thickness theorem. The audited result therefore supplies the missing global optimization rather than merely renaming Lassak's tetrahedral example.

## value

PASS

The result closes an explicit geometric optimization left open by the defining source and upgrades a tetrahedral example to an exact all-dimensional formula with a full equality classification. Thickness is the central invariant in Lassak's reduced-body theory, so determining the minimizing support dimension and its multiplicity is a natural structural result rather than an arbitrary special-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
