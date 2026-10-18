# Self-review

## Correctness — PASS

The statement is finite and its universe is explicit: fifteen ordered Petersen edges, \(32768\) orientation masks, \(120\) induced symbol permutations, and \(\binom{15}{9}\) candidate edge subsets. The exact certificate checks all orientations by both Kahn reachability and a separately implemented reversal-plus-DFS test, verifies the seven local-degree coefficients and every symmetry orbit, and counts coherent spanning trees by checking every assignment to each tree's nine edges. The integral incidence basis proves smoothness at simple vertices; chambers with too many walls are non-\(\mathbb Q\)-factorial. Both orientation and coherent-tree approaches give \(1080\) smooth fixed points. `python3 CHECK.py` returned `VERIFY_OK` from the embedded source. Finite exhaustive search is valid here because the theorem concerns one explicitly fixed ten-vertex graph, not an unbounded family.

## Originality — PASS, qualified

The general graphical-zonotope geometry (Postnikov–Reiner–Williams), flippable-tree criterion (Cordovil–Forge) and global face-vector enumeration (Grujić) are prior work and are acknowledged. The global edge total is not claimed alone as new. Those results do not themselves report the local Petersen degree polynomial, all \(168\) \(S_5\)-orbits by degree, or the \(540\) coherent spanning trees split into five symmetry classes. Targeted literature/record searches and direct reading of relevant primary materials identified no covering statement. A differently indexed exact table could still exist; novelty is qualified rather than established by absence of search hits alone.

## Mathematical value — PASS

The Petersen graph is a canonical highly symmetric nonchordal cubic graph, and its normal-fan toric ninefold is a natural finite test case for degeneration and singularity studies. The complete fixed-point curve-degree spectrum distinguishes every smooth fixed chart from the nonsimplicial charts; the exact symmetry stratification reveals structure not contained in global face numbers. The coherent-tree classification supplies an independent and geometrically meaningful corroboration. The proof claims neither a general graph-family theorem nor a complete singular-locus classification.

## Closest literature and limitations

Postnikov–Reiner–Williams, Proposition 5.2, characterizes globally simple graphic zonotopes. Cordovil–Forge, Theorem 3, characterizes flippable trees. Grujić, Theorem 1.1, already covers the total number of zonotope edges via the general face polynomial. Pilaud studies general acyclic reorientation lattices. Neither the primary sections inspected nor relevant accessible research claims included the numerical Petersen degree/orbit census. Unindexed equivalent literature remains a risk. The statement is only about torus-fixed points; nonfixed local singularities are outside scope.

Self-review: passed. Independent audit: not yet performed.
