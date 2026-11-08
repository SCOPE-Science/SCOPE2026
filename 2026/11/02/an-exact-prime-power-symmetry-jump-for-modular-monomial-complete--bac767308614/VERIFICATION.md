---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For n=p^e Frobenius sends every nonconstant monomial to zero, so every substitution in the maximal ideal respects the exponent relations; invertible tangent matrices give automorphisms by nilpotent inverse-function/Nakayama and count of free higher coefficients. For n=h+1, the degree h+1 part of f^(h+1) forces every nonzero tangent generator to be on one axis, hence the tangent matrix monomial. Writing f=x_j u+b with b free of x_j, the lowest degree of nonzero b contributes uncancellable x_j^h b_s to f^(h+1), forcing b=0. Counting distinct elements of (x_j) with nonzero x_j coefficient gives the formula without unit-representative overcount. Independent direct full F2,d=2 enumerations return 24 and 2048 for n=2,3.

## originality

PASS

Díaz–Liendo–Manzano-Flores–Regeta arXiv:2408.02197 and Díaz–Lucchini Arteche study finite monomial-algebra automorphisms over characteristic zero; the positive-characteristic Frobenius-induced GL-to-monomial adjacent exponent jump is outside their theorem hypotheses. Published Resultary coordinate-cross algebras kill mixed monomials, unlike the examined complete intersections where mixed products survive. The complete formulas may still be implicit in older positive-characteristic formal-automorphism literature; no full text of char-zero paper could be obtained and institutional access was blocked.

## value

PASS

The complete automorphism-group and order classification for all finite fields, numbers of variables and adjacent prime-power truncations reveals a sharp structural rigidity transition, a natural invariant not mechanically supplied by characteristic-zero theory or unrelated coordinate-cross algebra formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
