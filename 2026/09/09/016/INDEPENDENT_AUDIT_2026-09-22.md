# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/016`  
**Audited source tree:** `e1068f2b906d3387572a9d902d445632e20f5a10`  
**Date:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS. Independently encoded AG(4,3) as four base-3 coordinates and used third(p,q)=−p−q. The specified D0 blocks 41 of the other 71 points, leaving exactly 30 possible extension points. An independently written lexicographic backtrack with no symmetry pruning found precisely the six listed 20-point sets. For every set, all triples were checked line-free and all 61 outside points were checked against secants; all are complete caps. All 15 pair intersections have exactly 12 points, including D0 and one extra antipodal anchor-0 line. The claims about 240/2880 stabilizer orders were not independently recomputed here; the exact intersection theorem does not depend on those auxiliary orders.

## Originality

PASS, narrow. Awan et al.'s open full text establishes the demicap definition and six maximal caps per demicap (Proposition 3.6) and displays six caps associated with a chosen demicap; its theorem about a 6×6 grid concerns partitions with another cap. It does not state the 15 pairwise overlaps of caps sharing a fixed demicap. Follett et al. study disjoint cap pairs and 1/2/6-completability, not this overlap. The number six alone does not force the intersection size 12.

## Scientific value

PASS, limited. The singleton overlap spectrum {12} is a precise incidence invariant for a natural demicap fiber. The all-demicap interpretation uses Awan et al.'s equivalence theorem; the record itself certifies one representative. It is a small finite-geometry lookup and rigidity lemma, not a new general cap-set bound.

## Prior work

- https://arxiv.org/pdf/2106.14141
- https://arxiv.org/pdf/1302.4703

## Scope

The independent enumeration supports the six-set fiber and overlap theorem. Stabilizer orders are auxiliary reported checks, not independently certified by this audit.
