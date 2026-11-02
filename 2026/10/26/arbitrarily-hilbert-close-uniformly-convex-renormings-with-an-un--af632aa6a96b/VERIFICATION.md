---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The supremum γ(s,x)=sup_{u>=0,||u||≤1}|s+<x,u>| equals max(|s+||x_+|||,|s-||x_-|||), a continuous seminorm bounded by √2||(s,x)||_2. Thus Nβ²=||(s,x)||²+βγ² is a complete norm with 1≤Nβ/||·||_2≤√(1+2β), permitting arbitrarily small distortion β>0. Convexity of γ² plus Hilbert parallelogram proves the 2-uniform-convexity modulus δ(ε)≥ε²/[8(1+2β)]; Browder–Göhde–Kirk provides the bounded-set fixed-point property. The fixed positive affine slice C={s,x>=0:s+<w,x>=1}, w_j=2^(-j), is unbounded via (0,2^j e_j). For p=(1,0), any y=(b,v)≠p has d_y=1-b>0. If z_n=(s_n,x_n) in G_C(p,y) escapes, then ||x_n||=r_n→∞, g_n=x_n/r_n weakly→0 by coordinatewise x_n,j≤1/w_j. The explicit norm-one support functional at z_n-p has F_n(p-y)→βd_y/√(1+β)>0, contradicting Nβ(z_n-y)≤Nβ(z_n-p). So every G_C(p,y) is bounded; Kirk–Ray localization applies for every nonexpansive C→C, giving a fixed point. Independently checked the support limit for escaping points j=15,20,25 and β=.037. The argument relies on exact strict β>0; at β=0 Hilbert Ray theorem forbids the conclusion.

## originality

PASS

Japón–Laguna-Ricart (2026) already construct the same positive affine slice and a different renorming with unbounded-set nonexpansive FPP; that existence theorem is expressly credited. The new result quantitatively strengthens the geometry to a 2-uniformly convex norm of arbitrarily small Hilbert distortion while keeping the same C. Saejung 2010 treats firmly nonexpansive-like operators on smooth, strictly convex, reflexive spaces, not all nonexpansive maps for this nonsmooth norm. The original six-page Japón–Laguna-Ricart complete text was unavailable despite arXiv/OA attempts and authorized institutional check (VPN disconnected), so exact relative norm properties remain a material historical-priority risk, not grounds for automatic failure.

## value

PASS

The fact that unbounded nonexpansive fixed-point sets exist in uniformly convex Banach norms arbitrarily Banach–Mazur-close to Hilbert, but are impossible at the exact Hilbert norm, is a sharp geometric stability boundary. Power-type-two modulus and same explicit unbounded slice make this a meaningful fixed-point/renorming result, not a routine reparameterization of existing bounded-set theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
