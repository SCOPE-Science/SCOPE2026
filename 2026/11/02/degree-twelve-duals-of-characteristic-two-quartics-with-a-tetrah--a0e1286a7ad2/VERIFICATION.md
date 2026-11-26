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

With the four diagonal coefficients nonzero, the primal gradient vanishes only on the coordinate lines, and the restriction to each line is the square of a nonzero binary quadric. Thus the singularities are isolated; reducibility or a repeated factor would force a positive-dimensional singular locus. On the projective torus, C(C(x))=P(x)^2 x and G(C(x))=P(x)^8(P(x)+Q(x)^2); these are scheme-level identities with unit factors on the torus. Every coordinate-plane restriction is a nonzero b_i^2 times the fourth power of the product of the three remaining coordinates, so no additional factors or multiplicities are lost in passing to the torus. The derivative P(u)^2 C_i(u) gives the inverse Gauss map on the torus and vanishes exactly on the boundary of V(G), which consists of the six lines. A generic line has a nonzero order-two initial form of Q(C) (the two squared transverse variables cannot cancel), while P^3 starts in order six. At a vertex the three distinct degree-four square monomials in Q(C) survive all cross terms, while P^3 starts in order nine. This proves orders four and eight and nonnormality in codimension one.

## originality

PASS

Credit the earlier explicit Cremona dual and degree on the primitive Heisenberg subfamily, including the same substitution and exclusion of boundary factors. The distinct result supported here is the uniform dual for independent allowed coefficients and, in particular, the exact reduced dual boundary and its multiplicities throughout that family, including primal coefficient walls. No inspected result covers that full claim.

## value

PASS

This is the complete reduced dual-boundary geometry for an established characteristic-two quartic family. Identifying the six nonnormal lines, quantifying how local order rises at the vertices, and computing the nonreduced plane sections gives information for studying normalization and degeneration that neither the Gauss-map degree nor a count of primal nodes provides. The result applies unchanged on cross-coefficient walls, rather than being a calculation at an isolated sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
