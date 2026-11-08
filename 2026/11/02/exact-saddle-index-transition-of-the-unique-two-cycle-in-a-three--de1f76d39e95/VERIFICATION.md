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

Every primitive two-cycle alternates (u,v,u),(v,u,v); subtracting orbit equations forces u+v=b-1, with discriminant 4(a-a_birth), giving existence/unique unoriented cycle iff a>a_birth. Monodromy J(u)J(v) characteristic p(lambda)=lambda^3+2(b-1)lambda^2+4[b(b-1)-a]lambda-b^2, so p(1)=-4(a-a_birth)<0 gives a real root>1. The characteristic polynomial factors at birth and at a_flip=(5b^2-6b+3)/4; p(-1)=4(a-a_flip). Nonreal unit pair would require other root b^2 and a_pair-a_birth=b(b+2)(b^2-1)/4<0, impossible in existence domain. At flip -1 is simple and crosses outward, while other roots are >1 and in (-1,0). Thus unstable index exactly 1 then 2. Actual Sympy verification source read and direct algebra reconstructed; numeric tests are not proof of unrestricted b. No four-cycle bifurcation inferred.

## originality

PASS

The family and near-onset period-two instability are established by earlier literature; the complete global primitive-two census and exact index-one to index-two threshold were not located in materially examined mode-locking and fixed-point sources. Qualified priority because 2002 Richter and other historic same-family treatments may imply it.

## value

PASS

A complete parameter-uniform spectral and orbit census for the first nontrivial periodic branch in a canonical three-dimensional quadratic diffeomorphism, with exact saddle index jump and impossibility of attracting two-cycle. This sharp bifurcation boundary is intrinsically useful even without a higher-cycle theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
