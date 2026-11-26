---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Writing the leaf images as b_i c+w_i, their squares are all T(c), so b_i² is constant; their distinct cross-products give b_i b_j=0 by independence of c and s. Since m≥2, all b_i=0. This forces T(c)=ac, a≠0. The products then give exactly WᵀW=aI and Ws=a²s, sufficient as well as necessary. If m≠0 in the field, the norm of s forces a³=1; dividing W by a² gives an isometry fixing s, with arbitrary restriction to s⊥. The Gram matrix I+J of the differences v_i−v_m has determinant m. If m=0 in the field, choose t with (s,t)=1 and subtract half its norm times s to make it isotropic. The resulting hyperbolic plane has determinant −1, leaving a nondegenerate K of determinant class −1. Pairing Ws with Wt gives the t-coefficient a⁻¹; the t-coefficient in Wu for u∈K vanishes. If g is its K-block and z the K-component of Wt, pairing Wu with Wt and taking the norm of Wt force the s-coefficients −a(gu,z) and −a(z,z)/2 respectively. These formulas preserve the form with multiplier a and allow every z. In odd dimension the determinant identity forces square a and scalars realize each; in even dimension hyperbolic planes and the field norm model for an anisotropic plane give all multipliers. Thus each available multiplier gives q^(m−2)|O(K)| maps, and the standard odd-field orthogonal orders with the stated determinant signs give the claimed formulas and examples. The modular case starts at m≥3, so the listed orthogonal formulas cover all needed dimensions, including dimension one.

## originality

PASS

The supported contribution is the full odd-field star automorphism calculation and explicit count through the isotropic transition. The group orders and the structure of an orthogonal parabolic are standard ingredients. Published twin-class derivation statements, graph-symmetry actions, and a diagonal example do not supply this full classification. The strongest matching Resultary complete-bipartite theorem uses related equations but expressly excludes a singleton part.

## value

PASS

This natural twin-class example distinguishes full algebra automorphisms from permutations of the graph. The exact calculation reveals an isotropic case with a full additive parameter and, depending on dimension, multipliers not restricted to cube roots. The distinct behavior is controlled by characteristic dividing the number of leaves, not apparent from either graph symmetries or the standard order formulas alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
