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

In characteristic 2, involution cancellation makes every off-diagonal determinant variable occur with even exponent, so partial derivatives are exactly diagonal cofactors. On det=0 the adjugate rank-1 formula at corank one forces a nonzero diagonal cofactor, while all cofactors vanish at corank≥2; support equals the reduced corank-two locus. On a rank-(n-2) Schur chart detM=detA(uv+w²); the exact hypersurface Jacobian quotient is (u,v,w²), yielding a square-zero rank-one nilradical and generic length two. Under kernel frame G the residual w transforms by detG (char2), and projective scaling supplies O(-1), identifying detK⊗O(-1). At corank one gradients are λ(v_i²) in diagonal slots, giving the kernel-line map followed by Frobenius with image the entire diagonal P^{n-1}. Independently exhaustively checked all 1,024 symmetric binary 4×4 and 32,768 symmetric binary 5×5 matrices: support/adjugate gradient and corank-one vector identities agreed. All-n proof uses Schur algebra, not finite extrapolation.

## originality

PASS

The determinant involution expansion is established; complex-characteristic symmetric degeneracy studies do not settle the characteristic-two intrinsic Jacobian nilpotent-line structure. Best-of-knowledge originality resides in global gluing of the exact corank-two square-zero thickening and cycle multiplicity two; the Frobenius Gauss collapse is classical/elementary and not independently credited as new.

## value

PASS

Computes a canonical scheme-theoretic structure invisible to reduced rank stratification in an algebraically natural universal symmetric determinantal hypersurface. The nilpotent line and multiplicity determine a meaningful obstruction/cycle contribution, while explicitly avoiding any deeper-corank primary decomposition claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
