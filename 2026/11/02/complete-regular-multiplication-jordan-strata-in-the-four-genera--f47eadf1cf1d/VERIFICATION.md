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

For n=x−a the exterior nilpotence identity n³=0 holds in all characteristics, so ranks r1 of L_n and r2 of L_n² determine Jordan block counts b3=r2, b2=r1−2r2, b1=16−2r1+r2. If degree-one part v≠0, split E=ΛU⊕vΛU and use invertible block multiplication to prove r1=8. In odd characteristic n²=2v b(1+α) for w=v∧α+b, rank2 iff v∧w≠0, giving r2=2; in char2 r2=0. For v=0,w≠0 the independent graded images give r1=2+rho(w), r2=1 precisely when odd char and rho(w)=4; degree3 and degree4 only give ranks2 and1. Plücker Grassmannian counts rank2 altern forms R2=(q−1)(q²+1)(q²+q+1), complement rank4 R4=q²(q−1)(q³−1); remaining strata are vector bundles/punctured spaces. Independent F2 exterior algebra left-multiplication matrix elimination tested 3048 elements, including char2 degeneration, not universal proof.

## originality

PASS

Known matrix representations and maximal commutative subalgebras of Grassmann algebra concern different invariants. The inspected Domokos–Zubor primary paper addresses maximal commutative subalgebra dimensions and assumes odd characteristic, so it does not determine these arbitrary-field left-regular multiplication Jordan strata. Generic rank/Jordan identities and Plücker counts are credited, not new. Priority qualified by inaccessible full Márki et al text and possible specialist preexisting rank stratification.

## value

PASS

The regular multiplication operator is canonical for finite-dimensional algebras. A complete Jordan-partition stratification, including the characteristic-two phase change, geometric irreducibility and field-count polynomials, gives a reusable invariant; exceeds a routine individual rank computation or relabeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
