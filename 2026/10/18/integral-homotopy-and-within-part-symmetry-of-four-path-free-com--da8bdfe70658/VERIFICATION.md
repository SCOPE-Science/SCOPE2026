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

Checked complete occupancy classification: permissible faces occupy one part, two parts with at least one singleton, or precisely three singleton parts. Any other pattern contains an explicit four-vertex simple path. X contains full 2-skeleton and is simply connected. The contractible star cover U_i has pairwise one-dimensional intersections; Mayer–Vietoris induction yields H_j(Z)=0 above degree2 and torsionfree H2, and attaching only rainbow triangles to form X preserves these properties. Integral Euler characteristic from exhaustive face enumerator yields β, and Hurewicz+Whitehead gives ∨βS², including degenerate singleton cases. Signed fixed-simplex Lefschetz traces depend only on per-part fixed points f_i, yielding the proposed polynomial and semisimple rational representation with multiplicities choose(m−1,3), choose(m−1,2), m−1,1. Independently enumerated all actual length-3 simple paths and checked classification/Euler counts for nine size tuples including (3,3,3) β38, (2,2,2,2) β35; package contains broader 64 tuple mod2 and 123 class-character checks. Finite samples are corroboration, not the all-parameter proof.

## originality

PASS

Deshpande–Goyal–Sawant arXiv:2607.05358 closely studies these vertex-subset path-free complexes and provides general decomposition plus a complete bipartite homotopy classification, which are expressly credited. According to the accessible abstract, no all-m≥3 t=4 homotopy formula or W-equivariant character is stated; the full body was inaccessible, so hidden special cases cannot be excluded and priority is qualified. Distinguish directed-edge path-missing complexes of Grinberg–Katthän–Lewis from the vertex-subset construction. Resultary searches targeted path-free multipartite all-parameter sphere formula and did not locate a direct duplicate, but search absence alone is not proof.

## value

PASS

This is a uniform integral homotopy and equivariant representation classification for every complete multipartite graph with ≥3 parts, a natural forbiddance complex at the first nontrivial four-vertex-path threshold. The exact β and W-character are useful invariants, with a nontrivial topological Mayer–Vietoris mechanism; neither arbitrary slice nor textbook substitution. No general statement for other forbidden path sizes is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
