# Review: Minimum zero forcing sets and contrasting reconfiguration distances in the Pappus graph

## Correctness — PASS
Finite exhaustive proof on the explicit 18-vertex incidence graph. Independent C++ and Python implementations enumerate every subset of sizes 1–7, reproduce 6912 minimum configurations with no smaller forcing sets, reconstruct each legal jump/slide and both connected graphs. C++ breadth-first search from all 6912 roots verifies radii, diameters and eccentricity distributions. Python independently verifies 216 base automorphisms, 35 orbits and BFS from all orbit representatives, reproducing every graph invariant. Four packaged source/output artifacts can be replayed; finite proof does not imply any result for larger graphs.

## Originality — PASS
General minimum-rank/zero-forcing introductions, girth lower bounds and full-text primary work on zero-forcing reconfiguration give definitions, inequalities and algorithms; none of the inspected source statements covers or implies the exact minimum-set multiplicity and both exchange-graph centrality spectra for the Pappus graph. Actual published-finding corpus semantic searches and available own-ledger historical claim comparisons found no covering claim. These search results are not a proof of global novelty; unindexed publications and tables are residual risks.

Closest literature: Davila–Kenter (arXiv:1406.0482, girth bounds); Gentner–Rautenbach (arXiv:1608.00747, girth lower bounds); Geneson–Haas–Hogben (arXiv:2009.00220, zero-forcing exchange-graph definition, generic results and enumeration complexity). The latter shares the jumping definition but gives no Pappus-specific state count, move count, diameter or eccentricity census in its inspected full text. A graph database entry fixes the underlying graph but not its forcing invariants. Residual risk: an unindexed paper or table could independently contain these numbers; database nonretrieval does not establish universal priority.

## Value — PASS
The 18-vertex Pappus graph is a canonical cubic symmetric incidence graph, and minimal zero forcing concerns matrix nullity and propagation/controllability. The exact 6912-state structural census answers a natural optimal-seed mobility question beyond the minimum seed number. In particular, unrestricted exchanges preserve distance-homogeneity of eccentricity seven, while local slides retain connectivity but create diameter eighteen and three eccentricity classes. Exact finite classification and a verified 216-automorphism reduction are substantial object-specific results, not arbitrary numerical slices or a textbook deduction.

## Verification limits
The finite exhaustive procedures justify the specific eighteen-vertex claim. They do not establish new general graph-family laws; a separate external independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
