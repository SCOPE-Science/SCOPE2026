---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: For uniform spanning tree T of labelled K_{a,b}, sum of B-side degree excess is a−1, so at most a−1 B-vertices are nonleaves and removing all other B leaves gives a unique connected acyclic skeleton on A and the core. Conditional on this exact skeleton, all omitted B vertices attach independently and uniformly to one of a A-neighbors. For two independent trees, union of core B labels has size r<=2(a−1); the b−r double leaves contribute independent Bernoulli(1/a) overlaps, independent of all core overlap conditional on skeletons. For b>=2a−2 factor out Bin(b−2a+2,1/a) from every conditional PGF, leaving a mixture with nonnegative coefficients; maximal total overlap a+b−1 bounds residual degree by 3(a−1). For K_{3,n}, I/II skeleton types of a 3-star or two 2-stars are exhaustive. Enumeration by core sharing and edge overlap gives the stated Q_n(t) nonnegative correction polynomial, exact edge-disjoint ordered pair count and mean/variance. Independent direct tree enumeration matches full polynomial at n=4,5: 432 and 2025 spanning trees, 186624 and 4100625 ordered pairs, and zero-overlap counts 216 and 6480.

## originality

PASS

PASS, qualified: Bóna, Burghart and Wagner (2026, full paper section 5) establish asymptotic/approximately binomial overlap for fixed small side, not exact finite semiring divisibility or explicit K_{3,n} distribution. Dong and Ge give a generic count of spanning trees containing a fixed forest; extracting an exact common binomial factor and positive residual from pairs is not an immediate stated corollary. The exact Q_n polynomial and ordered disjoint-tree census are specialized novel content relative to inspected originals. Possible unindexed exact enumeration remains a risk.

## value

PASS

PASS: Exact positive binomial-factor extraction is a natural structural feature of uniform spanning-tree intersections on bipartite graphs; an explicit K_{3,n} overlap law and ordered tree-packing census are reusable finite exact invariants, not a recomputed single small case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
