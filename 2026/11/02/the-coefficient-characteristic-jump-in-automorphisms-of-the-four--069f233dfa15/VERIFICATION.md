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

PASS: For E=K[R4], e_i e_j=e_(2j-i mod 4), right annihilator W=span(e0-e2,e1-e3) is intrinsic and dimension two over every field. For char K !=2, the U,W product (u+w)y=epsilon(y)u+delta(y)Hw forces block C=0, quotient A either identity or swap, and W-action D diagonal or antidiagonal; hence (K^××K^×)⋊C2. In char2, the exact multiplication (u,w)(v,z)=(lambda(v)u,lambda(v)w+N(u,v)) forces A=D=I or P and permits any lower-left C∈M2(K), giving M2(K)^+⋊C2, C↦PCP. Finite orders 2(q−1)^2 and 2q^4 follow. Reviewed standalone exhaustive F2/F3 enumeration: 576/186624 admissible block matrices and 32/8 automorphisms; bounded checks do not prove arbitrary-field claims, which rest on the explicit product identities.

## originality

PASS

PASS (qualified): Sangare–Ta 2026 give an even-dihedral embedding in characteristic different from 2, not the arbitrary-field R4 full automorphism group, and Bardakov–Passi–Singh 2022 classify the integral coefficient group (C2×C2)⋊C2 only. The given general-field formulas (especially additive characteristic-two group) are not a mere specialization of either exact theorem; an unindexed independent calculation remains a risk.

## value

PASS

PASS: The jump in the coefficient characteristic for a fixed smallest even dihedral quandle algebra is a natural classification problem: the 4-dimensional additive unipotent automorphism family in characteristic two is not visible from integral or characteristic-odd group presentations. Complete matrices and group laws enable downstream ring/algebra representation comparisons without claiming higher-order R_{4m}.

The dated certificate retains the supplied scientific assessment, sources and limitations.
