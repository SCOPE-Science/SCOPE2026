---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

PASS: The finite simple prism C_n square K_2 and natural commuting layer swap are precisely defined for all n≥3; the action preserves independent faces. Oriented setwise-fixed faces contribute (-1)^(cycles−1), including the empty simplex, so reduced Lefschetz is minus the signed fixed orbit-set polynomial. The 3-state transfer T has exact characteristic polynomial (z−1)(z²+1), giving cyclic Q_m=1+2cos(mπ/2); the open transfer P_m=(-1)^floor((m+1)/2) follows from its T² action. Rotation orbit quotient has gcd(n,j) columns (self-conflicting when 1); reflections fold to path length (n−1)/2 for odd n and n/2+1 for even n, with the opposite odd-axis orbit self-conflicting; the rung layer-swap fixes only empty face. Their traces are −Q_gcd, −P_path, and −1. Agarwal--Basak Theorem 15, read directly in complete arXiv HTML, proves homology only in stated degree with rank one or three. Multiplying reduced Lefschetz by (−1)^degree yields generator traces; semisimple rational finite-group representations and group relations force the claimed matrices. For 4k, rotation traces give 1⊕Q(i), reflection has zero trace on Q(i) and stated line sign, while commuting swap is +I on Q(i) and −1 on the line. For n odd and n≡2 mod4, the one-dimensional generator signs follow. Independent exact fixed-face enumeration checked all 208 group elements at n=3..10 without running package code, and independently verified the transfer spectrum and 24 Q/P values; source-tree Git hash reconstructed exactly. All-n scope is analytic and relies on the cited independently read nonequivariant classification.

## originality

PASS

PASS, best-of-knowledge qualified: arXiv:2608.30601v2 supplies only nonequivariant homotopy ranks and degrees, not rotation, reflection and layer-swap traces. Full published Möbius-ladder dihedral classification and the cycle matching-complex character are for genuinely different simplicial complexes and group actions. Three targeted Resultary searches found only the assigned identical published record (excluded as priority evidence), related ladder graph complexes, and the different-graph representation records; public web searches found no dominating exact theorem. The new contribution is complete closed rational D_n×C2 module structure for every n≥3, including the 4-divisible square plane with t=+I and complementary t=−1 line; group character data cannot be inferred from nonequivariant sphere multiplicities. Some general fixed-face machinery is standard, and unindexed equivalent calculations remain possible.

## value

PASS

PASS: An infinite natural family of cubic prism graphs and its canonical full dihedral-plus-layer-swap symmetry has a genuinely motivated equivariant-topological question beyond the known wedge-of-spheres classification. The theorem determines the entire rational representation for every width and a sharp mod-four transition, with the rank-three space splitting into a quarter-turn plane fixed by layer swap and a sign-reversed line. These symmetries are invisible to total Betti number or sphere dimension and can support symmetry-invariant homology questions. The result does not claim integral lattices or equivariant homotopy; all claims remain proportionate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
