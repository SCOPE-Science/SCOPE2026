# Independent mathematical audit

## correctness

PASS

For intersection sizes 3, 0, 2 and 1, the O_4 distances are 0, 1, 2 and 3: a common disjoint triple exists exactly when two distinct triples have intersection 2, and for intersection 1 a length-three path exists by relabeling the example {a,b,c}–{d,e,f}–{b,c,g}–{a,d,e}. Johnson distance is 3 minus intersection size. The two metrics separate the same vertex pairs relative to each landmark, hence induce identical basis families and identical single-exchange graphs, not identical underlying graphs. Independently enumerating unions of 595-pair separation masks on every 4- and 5-subset gave 0 of 52,360 and 149,184 of 324,632 resolving, so by upward closure the dimension is 5. I generated the exchange edges as cliques of bases with a common four-subset, which counts each distinct pair at most once, and got 6,331,500 edges. Applying all 5,040 permutations on ground symbols to one unseen basis at a time gave 48 orbits and the same full orbit-size histogram. Every representative's unweighted sparse graph traversal reached all bases; the weighted eccentricity counts were 146,160 at 5 and 3,024 at 6, coming at 6 from one size-504 and one size-2,520 orbit. This proves radius 5, diameter 6, and connectivity; both specified pairs were also independently at distance 6. Private exact replay: /workspace/branches/replay/odd.py and odd.txt. The frozen C++ and Python certificates were inspected, not executed.

## originality

PASS

Supported for the count and orbit census of minimum bases and the complete labelled exchange-graph geometry. The minimum cardinality and the Johnson/Odd equivalence are expressly prior facts or equivalent formulations, not additional discoveries.

## value

PASS

For an established landmark-optimization problem on the fourth Odd graph and its equivalent Johnson representation, the metric dimension says nothing about the availability or mobility of optimal landmark choices. The exact census and six-step worst-case guarantee give that information for fixed labels; the disjoint distance-six witnesses show a genuine resolving-set constraint detour beyond the five direct replacements possible without the constraint. The small ground set permits a complete, replayable analysis, including the extent and symmetry types of the exceptional eccentricity-six bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
