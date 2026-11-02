# Review of the fifth-order binary de Bruijn cross-join metric census

## Correctness — PASS

The objects are exactly binary order-five de Bruijn cycles up to rotation, in bijection with Boolean feedback masks whose successor permutation has one full 32-state orbit. The verified exhaustive table recursion examines all 65536 masks and retains 2048; the independent direct Hamiltonian-cycle DFS also retains exactly 2048 and independently constructs cross-join edges by interlaced conjugate chords. A two-bit legal toggle equals a classical cross join; the parity lower bound and two-cycle split/rejoin descent give the exact metric. The two complete algorithms produce the seven-class pair-distance distribution, 48 centers, 736 vertices of eccentricity seven, and 368 diametral pairs. All BFS roots are checked, not sampled. Source code is included and run from the final package paths.

## Originality — PASS, qualified

The claim is limited to the *complete finite metric distribution, center, and diametral-pair classification* for order five. Mykkeltveit–Szmidt (ePrint 2013/760) already develop cross joins and the essential connectivity/descent argument; Alhakim (arXiv:1805.12059, Table 1) already documents the order-five degree distribution and thus implies its total edge count. Neither inspected primary source reports the exact all-pairs shortest-path distance spectrum, 48 centers, or 368 diametral pairs. Related 2023 work addresses multi-de Bruijn cycles. Targeted semantic research-record searches and accessible earlier records found no equivalent claim. A search cannot prove historical novelty; the residual risk is an unindexed tabulation or another formulation of the same metric census.

## Value — PASS

A shortest-path metric determines the efficiency of converting one complete de Bruijn cycle into another via only valid cross joins. Connectivity and local degrees do not answer the natural worst-case distance, best centers, or full transformation-cost distribution. The exact diameter seven is a sharp global conversion bound for 2048 configurations, the 48 centers identify optimal starting cycles, and the 368 antipodal pairs describe the extreme obstruction. This is a complete, reproducible, nontrivial finite classification of a standard combinatorial reconfiguration graph, rather than an arbitrary subset count.

## Scientific limits

The proven numerical census is order-five only. The general metric reduction is treated as a consequence of earlier cross-join theory, not as original. Independent historical priority and independent scholarly audit remain open.

Self-review: passed. Independent audit: not yet performed.
