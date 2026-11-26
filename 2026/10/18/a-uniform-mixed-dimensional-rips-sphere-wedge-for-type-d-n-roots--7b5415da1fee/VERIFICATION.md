---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Squared distance is 4-2 times the inner product, so the only eligible distinct pairs on [sqrt(2),2) have inner product 1. Precisely, the coordinate supports must be distinct and share an index with matching sign. Line 27's initial wording about sharing one signed coordinate needs this qualification (e1+e2 and e1-e2 are not adjacent); the next sentence explicitly excludes coincident supports and the proof uses that exclusion. Pairwise-intersecting distinct two-supports have a common index, or form the three edges on three indices: once {i,j},{i,k} and a support avoiding i are chosen, that support is {j,k} and no fourth support works. Sign agreement gives a signed star in the first case and 8*C(n,3) exceptional triangles in the second. Each star is a join of n-1 two-point sets; pairwise intersections are single vertices for distinct indices and empty otherwise, with no triple intersections. In a disjoint-copy model join each pair of identified vertices by an interval and attach the exceptional triangles along the lifted boundaries; collapsing the pair intervals, which are disjoint contractible subcomplexes, recovers the frozen complex by homotopy equivalences. Instead collapse spanning trees inside the stars. The intervening star paths are then based loops in simply connected spaces and may be homotoped away when attaching the triangles. The resulting crosspolytope 2-skeleton has 2n spheres of dimension n-2 attached at points; connectedness gives the wedge splitting. The 2-skeleton itself is simply connected (the full boundary is S^(n-1) and attaching higher-dimensional cells does not change π1). Euler characteristic gives H2 rank 8*C(n,3)-2n(n-1)+2n-1. Hurewicz and the simply connected homological Whitehead theorem give the wedge of that many 2-spheres. The two dimensions are distinct from n=5 onwards. Independent exact squared-distance face enumeration gave (40,240,400,160) and (60,480,1120,960,384), with 80 and 160 exceptional triangles at n=5 and 6. Replay: python3 -I /tmp/opencode/frozen_audit_small_checks.py, rips(). The frozen verifier was read, not executed.

## originality

PASS

The closest primary and catalogue topology comparisons use half-cubes or ordinary line graphs, not the root graph. The latter is a proper spanning subgraph of L(K_{2,...,2}) and is clawed. The frozen line-graph discussion should name K_{2,...,2}, not the complete graph on 2n signed vertices, to have the claimed common vertex set; this imprecision does not alter the graph distinction or topology theorem. The strongest root-filtration matches use a different root family or an excluded scale and rank.

## value

PASS

The first nontrivial Rips scale of the canonical D_n root configuration already has two genuinely distinct sphere dimensions. The proof identifies their separate geometric sources, a crosspolytope 2-skeleton and signed-coordinate star spheres. This yields an integral homotopy classification uniformly at all assigned ranks, not a Betti table or a mere variation of the ordinary line-graph formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
