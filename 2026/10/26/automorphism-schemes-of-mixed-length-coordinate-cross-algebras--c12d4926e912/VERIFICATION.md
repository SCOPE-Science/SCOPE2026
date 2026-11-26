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

Over R_red the augmentation ideal is exactly the nilradical, so every constant in an image of a generator is nilpotent over R and the linear coefficient matrix B is invertible (its determinant is a unit modulo the nilradical). For n≥2 the linear part of every cross-product equation equals c_i B_h+c_h B_i; multiplying by B⁻¹ kills both constants, without assuming a reduced base. In a long column the coefficients generate the unit ideal and are pairwise orthogonal by the degree-two cross equations. Their principal opens cover the base and are pairwise disjoint; on each open one coefficient is a unit and all others are zero. Two long columns cannot match the same row by invertibility. No matched row can be short, because its square equation would contain a unit times the nonzero degree-two basis vector. The matched power relation requires the source length to be at least the target length; summing over the finite long-branch permutation forces equality throughout. The matched series is a unit times the branch variable, whose annihilator in the branch ring is the top-degree submodule. Thus every off-match entry in a long branch is exactly a top-degree shear; the short-column block below GL_r is unrestricted. Pairwise products of off-match shears vanish, and their squares vanish, so they create no additional power or cross equations. The linear block and the higher filtration quotients are invertible for every such choice. This gives the disjoint clopen patterns, the affine parameter count and smoothness over arbitrary k. For n=1 the linear coefficient must be a unit and the constant nilpotent. Write d=qm with q=p^v_p(d) in divisible characteristic and q=1 otherwise. For p dividing d, Frobenius gives f^d=(f^q)^m; in the other case use f directly. The coefficient of x^((m−1)q) is c^q times a unit: its leading term in c is m times the invertible linear coefficient to the power q(m−1), and every other term in the parenthesis is nilpotent. So c^q=0 is necessary, and then the power has no term of degree below d. The triangular determinant modulo the nilradical proves invertibility. The resulting nonreduced product is a statement about schemes, not the group law. The verification note is analytic; no enumeration or formal certificate is needed.

## originality

PASS

The ordinary mixed-length normal form and finite-field census are already stated in a distinct same-day indexed record. The supported distinct result here is its scheme-level refinement on arbitrary base algebras, including the absence of infinitesimal extra structure for multiple branches and the precise one-branch boundary. No priority claim is made for the ordinary formulas or the elementary dual-number instance.

## value

PASS

This is a complete normal form for a natural mixed-length family of finite local algebras over arbitrary bases. It determines whether the ordinary automorphism geometry hides infinitesimal directions, and locates an exact change at the single-branch boundary, including the full thickness when the characteristic divides the length. The arbitrary-base control is what gives value beyond the existing finite-field count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
