---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

In independent upper-triangle variables, congruence transformation on Sym_n has determinant (det g)^(n+1), and F transforms by (det g)^2; identity evaluation gives the integral Hessian determinant (-1)^(n-1+n(n-1)/2)(n-1)2^{n(n-1)/2}F^{(n+1)(n-2)/2}. In char2 off-diagonal partials vanish, principal cofactors produce full diagonal projective image; corank-one adjugate has some nonzero diagonal, while invertible alternating matrices in even n form extra base component. At coranks 1,2,>=3, Schur-complement 2-jets give respectively rank n+1/2-or-0, rank 3/2, and 0; full rank uses orthogonal/alternating normal forms. Independent SymPy Hessians of full generic n=3,4 confirm integer polynomial identity n=3 and odd/char2 ranks at identity and corank1/2: n3 I ranks 2,6,6 for p2,p3,p5; n4 I 4,9,10; corank1 n3 p2=2,p3=4; n4 p2=2,p3=5.

## originality

PASS

The characteristic-zero adjugate/Cremona and Hessian factor are classical, while the char2 determinant involution expansion already implies off-diagonal derivative vanishing; those are explicitly not new. The assessed contribution is the all-rank modular base and Hessian rank classification, particularly invertible alternating matrices in the polar base and an odd-characteristic identically vanishing Hessian with birational polar map. Checked same-object primary mathematics does not state the combined classification.

## value

PASS

The determinant of a generic symmetric matrix and its polar geometry are central algebraic-geometric objects. The char2 full-rank alternating indeterminacy component outside det=0 and odd-characteristic birational map despite zero ordinary Hessian are substantive modular phenomena; the exact pointwise rank table across all coranks supplies a natural complete classification, not an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
