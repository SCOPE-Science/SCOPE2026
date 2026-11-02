---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For p=7, the hyperelliptic Cartier-Manin matrix coefficients are those of f(x)^3 at x^(7i-j). All exponents of (1+a x^6+x^12)^3 are multiples of 6, forcing diagonal 5x5 matrix diag(3a,3(a²+1),a(a²-1),3(a²+1),3a). Its semilinear Frobenius iterates preserve the vanishing positions, so stable p-rank is count of nonzero diagonal positions and a-number counts zeros. The degree-two involution x->-x gives Q_a:y²=t^6+a t³+1, whose differential block is diagonal 3(a²+1)I2; prime-to-7 isogeny J(Q)xP->J(C) preserves 7-divisible group and complementary three-dimensional Prym block. Smoothness exclusion a²=4 is exact; sign-change x->lambda x with lambda^6=-1 identifies a with -a; different strata distinguish isomorphism classes. Independently expanded polynomial cube and all prime-field strata; a²=-1 class in F49 is an algebraic specialization; finite checks corroborate parameter-wide polynomial identity.

## originality

PASS

Standard Cartier-Manin method and dihedral-involution genus-five family are acknowledged; the claim is the complete four-locus char7 p-rank and a-number stratification plus complementary quotient/Prym superspecial switch. Gutiérrez–Shaska treat extra involutions, Achter–Pries general hyperelliptic rank loci, and Suresh studies polynomial-shape Galois specializations. Related Jacobian decomposition literature establishes structural isogenies but does not, from checked mathematical statements, yield this exact char7 table. The accessible 2026 general superspecial genus-five enumeration does not classify this Prym pencil. Best-of-knowledge PASS with explicit historical-full-text risk.

## value

PASS

A full stratification of a natural symmetric genus-five dihedral pencil and two opposed superspecialities supplies exact arithmetic data useful in Prym geometry and small-characteristic Jacobian moduli. The zero-locus polynomial classification is a complete natural one-parameter calculation, not an arbitrary isolated numeral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
