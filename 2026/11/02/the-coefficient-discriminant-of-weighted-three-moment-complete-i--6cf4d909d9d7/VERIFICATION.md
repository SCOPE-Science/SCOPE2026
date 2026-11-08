---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Jacobian columns a_i(1,2x_i,3x_i^2) have rank<3 iff the coordinates take <=2 values (p>=5). For a two-value point u on S and v on T, the first two moment equations force either one value zero and A_S=0 or both A_S=A_T=0; all-equal points require W=0. For W!=0, at [e_S] the F1/F2 linear tangent constraints split into two weighted hyperplanes; the Hessian of F3-(3/2)F2 has one scaling radical on S and no radical on T. The projective transverse quadratic form of dimension n-3 is nondegenerate; the odd-characteristic formal Morse lemma yields ordinary double points and reduced singular scheme. Isolated singularities in CI dimension n-4>=2 and R1/S2 give normality; projective connectedness and generic regularity give integrality. Independent exhaustive projective F5/F7 rational point singular-support enumeration for 3 six-variable weight vectors gave respectively 6,6,8 matches; finite checks do not prove the general theorem.

## originality

PASS

Best-of-knowledge novel coefficient-space subset-sum arrangement and exact nodal stratification under variable weights. Earlier papers study power-sum varieties or finite-field diagonal systems, but cited primary material does not establish this full coefficient-discriminant theorem. A newer uninspected appendix or more general discriminant geometry may subsume it.

## value

PASS

The precise discriminant and multiplicity-free node classification gives a meaningful geometric wall crossing for a natural weighted complete-intersection family, determines smoothness and normality parameters, and identifies explicit degree-six K3 nodal degenerations; it is not merely a type check or isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
