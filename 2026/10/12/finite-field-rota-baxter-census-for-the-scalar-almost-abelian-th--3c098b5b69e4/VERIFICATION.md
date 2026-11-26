---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For R(s,x)=(as+f(x),su+Ax), the (t,v) identity gives f(A+aI)=0 and A²=−u⊗f. On V×V the t-component cancels and both V-components equal f(v)Aw−f(w)Av; the (t,t) identity is automatic. This reduction works in characteristic two. If f≠0, A preserves ker f and squares to zero there, hence vanishes there since ker f is a line. Thus A=w⊗f, f(w)=−a, u=aw, and R is the rank-one map (1,w)⊗(a,f). For every nonzero f there are q choices of a and q choices of w, giving q⁴−q² rank-one maps. For f=0 there are q² square-zero A, counting the nonzero ones by their common image/kernel line and a nonzero quotient-to-line map. For A=0 the free first column gives one zero and q³−1 rank-one maps; each nonzero A gives q rank-one maps (a=0 and u in the image) and q³−q rank-two maps. Summing yields the stated ranks and total, with rank three impossible by the same argument over every field. Substitution q→q^m in the counts and the defining exponential series give the zeta function. A separate basis-pair bracket enumeration of all 512 matrices over F₂ gave (1,25,18,0); the uploaded artifacts/verify.py was inspected, not run. This enumeration checks F₂ only, not the arbitrary-field identity or general count.

## originality

PASS

The surviving contribution is the finite-field census by rank in all characteristics (and its zeta function), not first classification of the complex algebra or novelty of the Rota–Baxter defining equations. The exact polynomial match found in the catalogue belongs to a different algebra. The strongest primary complex classification could not be inspected in full despite lawful alternate retrieval attempts; the decision reflects actual comparisons and leaves the risk of an equivalent parameterization explicit.

## value

PASS

The finite-field count resolves the natural exceptional scalar-action member of a studied Lie-algebra family without carrying over divisions or normalized complex families. The rank census separates the geometric constraint f≠0 forcing rank one from the entire rank-two locus and covers small characteristic as well as extension fields. It is a complete readily reusable invariant of the weight-zero operator variety, not a sporadic table entry or an isolated parameter calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
