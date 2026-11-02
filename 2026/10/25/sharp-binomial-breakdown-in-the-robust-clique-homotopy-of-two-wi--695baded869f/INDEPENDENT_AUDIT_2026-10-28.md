# Independent mathematical audit

## correctness

PASS

Independence-number recursion alpha(s)=max(alpha(s without lowest bit),1+alpha(s without closed neighborhood of lowest bit)) is exact on *all* 2^(3n) subsets for both specified finite graphs. Each k-face is exactly one with alpha(s)<k; the deterministic greedy element-toggle matching pairs codimension-one incident faces, leaving one critical 0-cell and b critical cells only in dimension 2k−3 (or only critical vertex). Crucially, an independent C++17 reconstruction (different memory and graph implementation from the supplied Python verifier) enumerated the full face posets for k=4,5,6,7,8 on n=5 and k=4..9 on n=6, reversed each matched incidence, and fully topologically sorted every oriented Hasse digraph, with visited count exactly total face count in each case. Example: n5 k5 12826 faces, 67 critical 7-cells; n6 k5 38417 faces, 206 critical 7-cells; n6 k8 249408 faces, 33 critical 13-cells. All 11 nontrivial/high boundary cases matched the submitted multiplicities; the audited original code separately handles known k2,3 and high trivial k. A finite discrete Morse matching is exhaustive for the *two finite grids* and Forman’s homotopy theorem upgrades the critically homogeneous CW complexes to integral sphere wedges. It is not extrapolated to arbitrary strip length.

## originality

PASS

Filakovský (arXiv:2602.11365v4) studies exactly these grid robust-clique complexes: Theorem 1 gives k=2,3 and Corollary 3 covers all k only for edge-glued square sequences; both width-three grids have corner attachments. Example 10 already shows a binomial failure at a different grid and the top-k maximal-independent-set result is old, so the audited novelty is not first failure anywhere. Theorem 1 and the general k≥4 corner-gluing challenge remain a conjectural direction in that paper, and the inspected statements do not determine the specific 3×5/3×6 full k≥4 homotopy spectra. Chandrakar et al grid total-cut work gives total 3-cut for width three, not higher k. Published Resultary search produced a general k3 bipartite graph theorem and unrelated finite grids, not the new parameters.

## value

PASS

The two adjacent width-three rectangular grids are the first small substantial corner-gluing test cases beyond established low-k theory, showing exact homotopy types (not just ranks) through the full parameter range and pinpointing initial low-parameter binomial-count breakdown. This finite census answers sharply motivated cases of an explicit open structural wedge-conjecture without pretending to prove an infinite grid family; the complete integral certificate is independently useful for future generalizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
