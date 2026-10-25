---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

A P5 subgraph in Kmn exists exactly for selected part sizes (a>=3,b>=2) or (a>=2,b>=3), with no induced-path qualification. Subcomplex B of sets a<=1 or b<=1 is union of two contractible joins meeting in Kmn, so integral H2(B)=H1(Kmn)=I_m tensor I_n, others vanish. Exactly (2,2) faces lie in X\B, one relative 3-cell per left/right 2-subset, so relative C3=Λ²E_m tensor Λ²E_n. Oriented tetrahedral boundaries map under Mayer–Vietoris to rectangles (e_j-e_i) tensor(f_q-f_p), i.e. d_m tensor d_n, which is split-surjective as abelian map via pairs to each chosen final vertex. Exact pair sequence identifies H3 with integral kernel and others zero. Rational permutation module splitting E=1+U identifies three irreducible outer products; wedge-square trace identity gives formula. Independently enumerated sample (3,3),(3,4),(4,4) with reduced H3 of ranks 5,12,27 and zero other Betti over F2 and F101, confirming formula for sample only, not general proof.

## originality

PASS

Best-of-knowledge original only for the precise additional integral/equivariant/multiplicative result; explicit known portions carved out. Two targeted indexed semantic searches plus specified primary comparisons do not show a stronger implying theorem; absence of hits is not a proof of novelty. See each named mathematical implication check and named residual risks.

## value

PASS

For path-free complexes on complete bipartite graphs, the known nonequivariant wedge count omits how color-class permutations act. The explicit canonical integral kernel lattice for every m,n is an intrinsically useful equivariant refinement, with complete irreducible character/representation across a natural two-parameter family. A known sphere-wedge rank would not determine integral module or character.

The dated certificate retains the supplied scientific assessment, sources and limitations.
