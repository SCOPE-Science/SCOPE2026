---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For n>=6, the noncover complex of the tight 3-uniform cycle is the ordinary 3-cut complex of complement C_n. Kim–Kim Theorem 3.4 provides the nonequivariant concentration in d_n=2k−2 with rank3 for n=4k, otherwise d_n=2k−1 rank1. Equivariant combinatorial Alexander duality gives χ(g)=(-1)^(c(g)+d_n)F(g), with F the signed orbit-subset sum over cyclic words avoiding 111. The 4×4 rotation transfer matrix has characteristic x(x−1)(x²+1), independently reconstructed exactly; the reflected half-path sums satisfy T_L=(-1)^floor(L/2) (checked to L=34 and supported by transfer recurrence). This yields χ(r^j)=3 if n=4k and 4|j else −1 in the n=4k case; χ(sr^j)=(-1)^(k+1+j), with 1 and (-1)^k for nonzero residues. Fresh independent direct orbit-sum enumerations verified every dihedral element at all n=6..15, not an all-n substitute.

## originality

PASS

The exact hypergraph and nonequivariant homotopy are known from Kim–Kim; this part is not new. Bayer et al. 2023/2024 equivariant cut-complex results concern Δ_k(C_n), not Δ_3(complement C_n). Another published result treats cyclic actions on 3-cut complexes of cycle powers, different graph and only cyclic rather than full dihedral. No earlier exact rotation/reflection character for these noncover complexes was found; possible equivariant reductions remain residual risk.

## value

PASS

The full D_n homology representation on a canonical infinite tight-cycle hypergraph family contains the reflection-axis signs and a quarter-turn plane invisible to existing ordinary homotopy calculations. It produces an exact mod-eight invariant-space dichotomy and natural rational representation classification for every n≥6, not a small arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
