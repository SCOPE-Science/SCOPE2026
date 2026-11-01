# Research review

## Correctness — PASS

The exact scope is a finite simple tree on at least four vertices and synchronous open-neighborhood Boolean NOR on its complement. The antitone-symmetry argument proves \(F^3=F\) on every finite undirected graph; the tree closed-neighborhood intersection lemma then enumerates each possible image and its inverse fiber. The proof separately treats stars, for which the complement contains an isolated center. Counting those fibers yields every basin, and the increasing discrete increments of \(2^{e+2}-2e-4\) yield sharp path/broom/star extremizers. Actual, distinct Python and C++ state-space checkers reproduce the predicted counts, but the proof—not finite enumeration—establishes the theorem for arbitrary order.

## Originality — PASS, with residual risk

Aracena–Richard–Salinas (arXiv:1507.06141, Proposition 1) establishes the general fixed-point/maximal-independent-set correspondence and therefore implies the tree-complement fixed-state count; this is expressly excluded from the claim of novelty. Aledo–Martínez–Valverde (DOI:10.1155/2015/594294) surveys parallel Boolean dynamics with a self-inclusive homogeneous NOR convention and general period behavior; it does not determine individual open-neighborhood basin sizes or sharp tree extremizers. Aledo et al. (DOI:10.1155/2020/9708347) counts periodic states for their self-inclusive system, not the stated basins. Related mathematical findings on joins, rook graphs, leaf coronas, and matching-deleted bipartite graphs do not imply the whole connected-tree-complement family. A plausible 2012 maxterm/minterm paper (DOI:10.1016/j.mcm.2011.08.040) was inaccessible in full; remaining unindexed historical overlap is possible. The assessed new contribution is solely the combined exact individual-basin classification and sharp extremality.

## Mathematical value — PASS

The family of complements of trees includes arbitrarily many nonisomorphic graphs and varying complement connectivity. The complete nonasymptotic, degree-sensitive basin classification resolves which oscillation dominates, determines consensus/fixation probability exactly, and establishes three rigid extremal shapes (star, path, broom). Neither the general period bound nor a fixed-point count yields these comparisons. The sharp structural optimization is natural because attraction-basin size, unlike periodic-state count, measures robust response to uniformly random initial configurations.

## Evidence and limitations

The supplied computation exhausts 433 nonisomorphic trees through 11 vertices and 18,744 tested labelled trees, including all labelled trees through seven vertices. These are distinct implementations of the finite checker, not an independent audit. The primary inaccessible 2012 paper remains a historical-originality uncertainty; no assertion of universal literature novelty follows from database absence. The four key comparisons are (i) different update conventions, (ii) general period bounds versus exact basins, (iii) fixed states versus complete attraction orbits, and (iv) strict tree complement family versus unrelated graph-family specializations.

Self-review: passed. Independent audit: not yet performed.
