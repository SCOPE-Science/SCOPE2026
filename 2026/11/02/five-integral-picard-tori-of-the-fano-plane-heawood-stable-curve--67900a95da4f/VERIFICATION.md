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

For the split nodal 14-component, 21-node stable curve p_a=21-14+1=8. Three distinct 0,1,infinity marks permit an honest GL_3(F_2) action in all characteristics and Frobenius twisting. The normalization sequence identifies X*(Pic^0) integrally with H_1(Heawood,Z), not merely rational H_1. Directly examined the integral 8x8 fundamental-cycle construction and four explicit determinant-±1 matrices A satisfying U A=A W in verify_heawood.py for representatives of orders 2,3,4,7; these check permutation/regular plus cyclotomic integral modules, yielding G_m^8, R_2^4, R_3^2 x N_3, R_4^2, G_m x R_7. The 168 group actions split into orders 1,2,3,4,7 with counts 1,21,56,42,48. The normalization product Z=prod_d(1-T^d)^(e_d-v_d)/(1-q^d T^d)^(v_d) follows from each rational component and the 2 preimages of each node, no edge reversal. Fixed vertex/edge data yield #Fq points 14q-7,6q+1,2q+2,2q+1,0 respectively; order-seven and only order-seven twists are Fq-point-free, for every q including q even. A separate F_2^3 group-action program recounted all 168 group elements and their vertex and edge orbit profiles; finite computation supports the integral identities but does not prove general descent.

## originality

PASS

A complete integral Frobenius-character module classification and all-extension zeta spectrum for the canonical Heawood stable curve is distinct from standard graph-curve normalization and from homology of Heawood simplicial complexes. No inspected published theorem determines these specific five isomorphism classes; best-of-knowledge, with priority risks disclosed.

## value

PASS

The Heawood graph is canonical incidence geometry of the Fano plane and its genus-eight stable graph curve naturally has a Picard torus. Determining all five integral rather than mere isogeny types, including a nontrivial cubic norm-one factor, together with all extension-field point counts and an exact zero-rational-point stratum, is a useful complete arithmetic classification of a natural geometric object; no arbitrary q-slice is selected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
