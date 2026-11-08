---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For finite connected simple triangle-free cactus G with at least one edge, K=N[L(G)]=union over original uv of Delta(S_u union S_v), and T=Cl(L(G))=union_v Delta(S_v). All nonempty star intersections are simplexes; no triple intersection, so the nerve gives T ≃ G and its integral H1 cycle-block basis. At a one-vertex sum G1 ∪_v G2, define J=K1 ∪ K2 ∪ Delta(A ∪ B) with A,B the two disjoint half-stars. Every F in K minus J has witnesses b in B and x in E(G1)\A (or vice versa); a generating uv must lie on the side of x and be incident to x. Two distinct such uv would make a forbidden triangle, hence unique center e(F), distinct from witnesses. Toggle e(F) pairs exactly all exterior faces, preserves the center and exterior status. Removing in descending lower-face size makes each lower face free, since any other remaining coface has the same center and was paired at higher size; explicit elementary collapse K searrow J fixes T. J has contractible connecting simplex meeting K1 and K2 in nonempty disjoint full A and B simplexes, so J ≃ K1 wedge K2. Iteration over cactus block-cut tree yields K(C4)=boundary of tetrahedron=S2, K(Cm>=5) collapses via unique free diagonals to S1, and bridge gives a point; hence K(G) ≃ wedge_q S2 wedge_r S1. Because collapse fixes T and T(Cm)→K(Cm) is H1 iso for long cycles and Z→0 for squares, Mayer–Vietoris splits H1 map by blocks and the primitive kernel is precisely square-block cycle basis. Independent direct face-set program reconstructed 16 vertex sums C4–C7 with unique generator, 384 elementary free-face pairs and final exact J; independent GF(101) homology checks for bouquets [4,5], [4,4,5], [4,5,5], [5,6,7] match predicted Betti. Universal and integral result rests on proof, not finite checks. Source tree re-hashed from seven actual Git blob SHA identities with result f74ab1dab625612bf00a5c0634a63999d2fd6ba3.

## originality

PASS

Qualified best-of-knowledge priority judgment for the mixed square/long-cycle cactus closed-neighborhood line-graph theorem and primitive integral flag-to-neighborhood kernel, not for definition of the complex, C4=S2, girth>=5 case, or the flag complex's homotopy type. Direct full-text comparison with the same-object high-girth line-graph Čech theorem shows its explicit exclusion of squares; Goyal–Shukla–Singh Cor. 3.3 covers only the flag complex and Cor. 3.7 its vertex-sum pushout; Matsushita introduces the closed complex and 2k-fundamental group but does not state the mixed-block collapse or H2 wedge formula in its relevant inspected material. The published block-graph result concerns Lovasz OPEN neighborhoods, not the closed complex. A reusable one-vertex mixed-face collapse and its inclusion map distinguish the present claim from these antecedents. Resultary searches and web searches found no published exact mixed-block theorem, which is not conclusive proof of novelty.

## value

PASS

The closed-neighborhood topology of line graphs is a natural graph-Čech thickening; a single square changes the homotopy degree relative to the high-girth graph-recovery theorem. In arbitrary triangle-free cacti, the classified mixed S1/S2 contributions and the primitive integral flag-to-neighborhood H1 kernel answer a specific unresolved interface between graph cycle blocks and thickening, not an arbitrary parameter slice. The one-vertex gluing elementary collapse is a reusable structural lemma allowing branching and many square/long cycles. Known isolated square and high-girth pieces alone do not determine the mixed-block topology. No paper-sized generalization, full persistence or all-graph classification is needed for this infinite natural family to be a worthwhile exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
