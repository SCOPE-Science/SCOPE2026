# Independent mathematical audit

## correctness

PASS

With uncovered row/column sets I,J, domination is exactly I×J contained in the deleted matching. If exactly one side is fully covered, every selected edge must be private on that side; if both sides are covered, each edge must be private on both sides or deletion preserves full coverage of one side. If the only missed row and column are the same hole index, deletion is obstructed exactly when it reveals a new missing row or column; this is the minimal edge-cover condition on the reduced board. This includes edgeless K_{1,1}-M_1 and disconnected K_{2,2}-M_2. For balanced deletions, the full and reduced cyclic shifts give different sizes except when the reduced 1×1 board is empty. For a<b the unmatched column gives size a, and the two-row column cover for a≥4 misses at least two rows, so its b edges are essential. With a=3 and t<3 the full third row supplies size b; with t=3 the two-row column cover cannot be minimal: the edge in the omitted row's diagonal column must be private in its used row, leaving the other used row to cover its own missing diagonal. A reduced 2×(b−1) full two-hole board has no doubled selected column in a minimal cover (both chosen edges would need row privacy), so the other size is b−1. With a=2,t=1 the reduced row gives b−1, and a full-column star with the holed row omitted is not minimal; with t=2 no such star exists and the reduced board has an isolated column. These cases give precisely the five clauses. Independent bounded check: number line-graph vertices by surviving edges, compute closed-neighborhood unions for each mask, and retain whole-cover masks for which deleting any set bit destroys coverage. This agreed on all 39 triples with 1≤a≤4, a≤b≤5 and ab≤16, including all small exceptions. This finite check does not certify the theorem; the case proof above supplies the infinite quantifiers. The bundled script was inspected, not executed.

## originality

PASS

The undeleted and star clauses are known, the disconnected two-edge boundary is immediate, and most balanced exclusions follow from the connected perfect-matching theorem. The supported distinct claim is the complete matching-deletion classification, in particular the unbalanced positive regimes together with the exclusion of all other unbalanced parameters. The strongest related Resultary edge-domination census located covers only a balanced subfamily and is later; the distinct same-day records inspected measure other invariants.

## value

PASS

A natural dense bipartite graph family has a complete WED classification with an infinite unbalanced positive subfamily and two isolated unbalanced exceptions. The support reduction explains these cases via minimal edge covers, rather than reporting a small census or restating the perfect-matching case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
