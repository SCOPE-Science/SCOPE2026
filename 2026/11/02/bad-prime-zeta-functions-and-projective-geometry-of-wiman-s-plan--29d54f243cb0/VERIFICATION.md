---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Direct exact coefficient arithmetic verified F mod 2=((X+Y)(Y+Z)(Z+X))^2, mod 3=Q times four sign hyperplanes, and mod 5=2Q^3+(XYZ)^2. The p=2 reduction is three concurrent doubled lines, hence 3q+1 points. At p=3 the smooth conic meets four rational tangent lines at four tacnodes, and the four lines have six distinct pairwise nodes: 5(q+1)-10=5q-5. At p=5 the partial derivatives exhaust six coordinate cusps and four sign-vector ordinary nodes; independent symbolic expansion at [1:1:1] gives 2u^2+3uv+2v^2 with nonsquare discriminant 3 mod 5. Bezout rules out geometric splitting because cusps are unibranch and four nodes supply at most four cross-component intersections, below the minimum five for a reducible degree-six curve. Delta-invariant 4+6=10 forces genus-zero normalization. Four rational nonsplit nodes exchange their branches under odd Frobenius and split under even powers, yielding q+1-4(-1)^n; p=3 and p=5 projective stabilizers inject into S4 of four special points and contain signed coordinate permutations of order 24. The three all-extension zeta functions then follow. Independent verification covered coefficient identities and tangent discriminant; extension universality rests on geometry, not finitely many fields.

## originality

PASS

Full low-prime point counts and zeta functions, including p=5 Frobenius correction, complete singularity geometry and scheme-projective S4 stabilizers were not entailed by the inspected Wiman sextic primary source. Its explicit statements already cover reducibility at 2,3 and rationality at 5; those basic facts are excluded from new content. Residual risk is an older equivalent low-characteristic arithmetic table or explicit plane-model analysis.

## value

PASS

Arithmetic zeta functions and reduction-type geometry at every exceptional prime of a classical genus-six plane sextic are intrinsic, reusable scheme-specific invariants. Nonsplit nodal branches versus geometric cusps explain the genuinely arithmetic alternating point counts; distinction between projective stabilizer and normalization automorphisms matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
