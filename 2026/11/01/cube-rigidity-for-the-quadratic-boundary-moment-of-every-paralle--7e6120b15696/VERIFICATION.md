---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Represent a parallelepiped by centered edge vectors u,v,w with lengths a,b,d and facet areas F_1=|v×w|,F_2=|u×w|,F_3=|u×v|. Direct integration of six affine facets gives I=(1/6)Σ_i(T+2F_i)a_i² with T=ΣF_i, S=2T. The desired ratio is Σ_i(T+2F_i)a_i² >=(5/3)T². On the relaxed box 0≤F_1≤bd, 0≤F_2≤ad, 0≤F_3≤ab, the negative deficit H=(5/3)T²-Σ_i F_i(a²+b²+d²+2a_i²) is convex, so its maximum is attained at a vertex. At zero H=0; the six one/two-positive vertices have strictly negative H; the all-positive vertex has 3(-H)=1/2Σ_cyclic (a-b)²[5ab+d(a+b)]≥0, with equality only a=b=d. Independently expanded this exact polynomial identity symbolically, and confirmed the two-face vertex expression exactly. Equality at a physically nondegenerate point F_i>0 forces all F_i maximum and equal lengths; cross-product equality then forces pairwise orthogonal equal edges, exactly a cube. No sampling is used to prove all real triples.

## originality

PASS

Freitas–Laugesen–Liddell prove the same sharp 5/72 ratio and cube equality for orthogonal rectangular cuboids only. The audited convex-relaxation proof establishes the bound for every oblique Euclidean parallelepiped. The equal constant is a known calibration; the extension across skew parallelepipeds is the claim.

## value

PASS

Extends a famous sharp cube inequality from rectangular cuboids to all skew parallelepipeds, a natural geometric class with three extra angle degrees of freedom. The proof supplies a transparent convex relaxation and exact rigidity. The same coefficient is a calibration, not a tiny numerical gain; adding all shears is a qualitative extension. Not an unmotivated slice, because the unrestricted convex-surface optimum is different and the parallelepiped class is canonical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
