# Scientific assessment

## Correctness — PASS

The claim fixes the graph, simultaneous three-state rule, temporal orbit convention, and page-label convention. Pages initially in the same one of nine ordered pair states have identical trajectories; the hubs depend only on the existence of an excited first/second page coordinate. Consequently the support-state reduction is exact for every integer \(k\ge1\), not merely for a bounded graph census. All \(9(2^9-1)=4599\) initial hub/support cases were enumerated from the included source (`code/verify_symbolic.py`) and compared with their full CSV witness. Every case enters a period-one, -three, or -four orbit by time five and obeys the face-circulation sign criterion. The fixed-period support counts, local phase classification, and inclusion–exclusion supply the closed orbit and basin formulas. The explicit one- and two-page configurations attain the announced entry-time bounds. Separately, the included C++ verifier enumerated every labelled configuration with one through six pages (5,380,830 configurations), matching the exact claims. Mathematical risk: the universal entrance bound is a fully reproducible finite-state computer-assisted lemma, not a hand-reduced table-free proof; the nine-type reduction and transition code are critical.

## Originality — PASS, qualified

The closest primary result, Gravner–Lyu–Sivakoff (arXiv:1610.07320v1, 2016-10-24), gives a general cycle-circulation criterion and excitation-rate characterization. It does **not** state the exact primitive orbit counts, global iterate identity, or uniform sharp transient bound for quadrilateral books. Doba (2018, *Complex Systems* 27) gives general winding/rate criteria, again without this complete graph-family census. Historical studies of square bouquets **sharing a vertex** and triangular books **sharing an edge** concern genuinely different edge sets; their counting results do not imply the present statements for \(k\ge2\). Research-record searches included the precise graph family, its alternate names (four-cycle book, edge-glued square bouquet), three-state excitation, primitive periods, orbit counts, and basin parameters. Returned work on matching complexes of the same book graph and binary parity dynamics uses different dynamics/invariants. Residual risk: exhaustive priority checking against unindexed historic publications is impossible; the existing general circulation theorem is credited explicitly.

## Value — PASS

The classification explains an intrinsic dynamical competition on an unbounded, natural family: the first three-phase oscillator requires at least two edge-glued squares; period-three orbit *counts* overtake period-four counts at exactly four pages, while their attraction-basin fractions tend to one third and two thirds. Both exact labelled recurrent-orbit counts and all-state basins are nontrivial functions of the page count. The uniform sharp five-step entrance bound is independent of graph size. This distinction between orbit abundance and basin prevalence is not a routine substitution into a general period theorem. Scope stays restricted to the stated rule and graph family.

## Closest literature and limitations

Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, 2016 arXiv v1 and 2018 journal text; Nobutaka Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, 2018, Sections 6–7. The finite support-class proof and independently implemented direct-state census are supplied, but there has been no independent external audit. Equivalent work may exist under other terminology; neither bounded numerical tests nor absence of database hits proves novelty.

Self-review: passed. Independent audit: not yet performed.
