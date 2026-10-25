---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The tree-edge polynomial is F_m=sum_i a_i b_i product_(j!=i)(a_j+b_j). Gauss induction uses gcd(F_(s-1),product u_j)=1. Partition singular points by zero count of u_i: zero zeroes has nonzero derivative of sum v_i/u_i; one zero forces a_i=b_i=0 and remaining F_(m-1)=0; two zeroes force two zero coordinate pairs; at least three u_i=0 gives L_I. All components are irreducible, same dimension and distinct on explicit dense opens. Nondegenerate Hessians of local equations st U+(s+t)w and sum_(pairs) v_i u_j u_k give generic 3-variable nodes. Hypersurface is S2 and R1, hence normal. Independent full projective GF(5) m=3, GF(3) m=4 and GF(2) m=5 enumeration reproduced Jacobian/component incidence exactly on respectively 3906, 3280 and 1023 projective points, with singular counts 121, 652, 671; m=3 used only as boundary corroboration. This is not an all-m proof; the symbolic argument is.

## originality

PASS

General matroid configuration rank degeneracy identifies underlying singular support but does not give the complete uniform m>=4 decomposition with degrees and local quadratic models. The m=3 four-component prism example is already published and explicitly excluded. Denham–Schulze–Walther Example 3.17 and 5.1 was read at full HTML, contrasting exact polynomial and m=3 strata. Search of published Resultary matched graph/matroid polytopes and a distinct four-wheel degeneracy example but did not find this theorem; unsuccessful discovery is not absolute novelty proof.

## value

PASS

An explicit irreducible-component/degree and transverse-singularity classification of a natural infinite family of graph-configuration hypersurfaces extends the known prism example and supplies concrete local models beyond general determinantal support. m=4 has eight components of total degree twenty; the arithmetic of components is not a routine direct corollary of the general rank criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
