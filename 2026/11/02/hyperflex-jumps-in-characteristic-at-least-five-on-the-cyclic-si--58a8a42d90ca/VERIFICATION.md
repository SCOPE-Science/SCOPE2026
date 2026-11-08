---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For algebraically closed k, p>=5, r not in {0,2,-2}, tangent restriction of x^3+y^4+ry^2+1 gives E2=3(6u+r)(u^2+ru+1)-4u(2u+r)^2 and E3=2u(2u+r)^3-27(u^2+ru+1)^2 with u=y^2. Exact independent resultant is 324(r^2-4)^3(11r^4-1080r^2+3888), and the linear subresultant determines u=N/A; resultant(P,A)=2^34*3^10*11^2 and the special p=11 case A=4 ensure this works uniformly. Substitution numerators vanish modulo P; u and G are nonzero. The two y choices and three x cube roots give exactly six further hyperflexes, alongside [1:0:0]. Exact discriminant 2^32*3^15*11 proves 4 reduced exceptional parameters for p!=11, whereas p=11 gives a separable quadratic r^2=8; geometric isomorphism quotient uses the published r^2-invariant. Independent symbolic arithmetic and modular prime tests corroborate, but no finite prime test proves the all-characteristic case.

## originality

PASS

PASS best of knowledge for the explicit positive-characteristic hyperflex stratification including the p=11 degree drop; existing normal-form, Hasse-Witt and characteristic-zero bitangent/hyperflex results are distinguished. Earlier unindexed contact-polynomial calculations remain a priority risk.

## value

PASS

The sharp 1-versus-7 jump and exceptional geometric isomorphism classes on a natural cyclic-order-six genus-three family classify a meaningful inflection stratum, including a positive-characteristic degeneration not determined by automorphisms or Hasse-Witt invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
