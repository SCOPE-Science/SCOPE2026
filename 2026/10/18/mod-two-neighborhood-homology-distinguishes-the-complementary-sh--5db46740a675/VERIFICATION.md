---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Both 16-vertex Cayley Shrikhande and 4×4 rook graphs have degree6 and common-neighbor count2, so their simple complements have nine-point open neighborhoods. Independently enumerated all 65536 vertex masks as subsets of one of the 16 complementary neighborhoods, obtaining full face vectors (16,120,528,1292,1728,1296,576,144,16) for S and (16,120,560,1332,1728,1296,576,144,16) for R. Exact augmented mod2 boundary matrix bit-rank elimination gives (1,15,105,423,869,848,448,128,16) and (1,15,105,453,879,848,448,128,16). Rank-nullity f_d−r_d−r_(d+1) yields only reduced H4(F2)^11 for N(complement S), vs H2(F2)^2 plus H4(F2)^1 for N(complement R). The computational domain is entirely finite and exhausted, and the result does not assert integral homotopy.

## originality

PASS

Best-of-knowledge statement-level comparison of the precise functor, object and parameter with relevant full-text primary sources and published mathematical results. N(complement G) is the non-dominating complex of G and combinatorially Alexander dual to the dominance complex, not N(G). Complement operation changes facet sizes from six to nine in these graphs. Matsushita–Wakatsuki supply general neighborhood/dominance Alexander duality, without the displayed Shrikhande/rook chain ranks; Cioabă et al treat clique-complex spectra/cohomology, which is a different simplicial functor. The Kummer biplane result N(S)≅N(R) concerns original open neighborhoods of size six, not nine-point N(complement S) or N(complement R). Published exact homotopy of N(S) and N(R) as RP2∨55 S2 and separate ordinary independence complex profiles were explicitly inspected, but neither table lists N(complement) binary profiles. Direct Alexander-dual computation of known domination homology could imply these values if discovered. Equality N(S)≅N(R) for original graphs gives no equality for neighborhood complexes of their complements: complement changes common-neighbor block system. Cliques and independence complexes carry different face definitions, and none of their cited exact values determine these boundary ranks. Any remaining bibliography uncertainty is retained as residual risk, not presented as novelty proof.

## value

PASS

The two canonical nonisomorphic cospectral strongly regular (16,6,2,2) graphs provide a motivated exact test case: a natural topological invariant of their complementary neighborhood complexes distinguishes them even with identical adjacency spectra and parameters. Full mod2 degree profiles—not just unequal face counts—are useful for neighborhood/dominance-complex and Alexander-dual comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
