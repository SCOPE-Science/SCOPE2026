# Same-model review

## Correctness

**PASS.** Atoms are intrinsically definable as covers of \(0\), and orthogonality is intrinsically definable by \(p\le q^\perp\), so every logic automorphism acts on the atom orthogonality graph. For an atom \((x,y)\), its closed non-orthogonality set is exactly
\[
(X\setminus\{\bar x\})\times(Y\setminus\{\bar y\}).
\]
Pairwise intersection sizes recover the rook relation “same \(x\) or same \(y\).” Maximal rook cliques recover the two coordinate systems, up to their global interchange when \(N=M\). Orthogonality within one recovered row or column then recovers the binary-output perfect matching, forcing the coordinate permutations to lie in \(C_2\wr S_N\) and \(C_2\wr S_M\). Every resulting operational relabeling visibly extends to the generated concrete logic. The standalone checker replays all finite structural invariants for \(2\le N,M\le5\).

## Originality

**PASS, with a narrow claim.** The primary box-world papers construct the logic, determine its atoms and disjointness relation, and study composition, but the inspected text does not classify its automorphisms. Bell-scenario literature treats permutations of parties, inputs, and outputs as a standard relabeling group, but the inspected material presents these as operational symmetries rather than proving that the relabeling subgroup equals the *full* automorphism group of the Tylec--Kuś propositional logic.

Targeted published-finding corpus and web searches for box-world logic automorphisms, the symmetry group of the \(82\)-element logic, hidden symmetries, and automorphisms of the full binary event orthogonality graph found no covering statement. The accepted claim is only the no-hidden-symmetry theorem for the binary two-party propositional logic.

A genuine residual risk remains because the atom graph is a natural Bell-event exclusivity graph, and an equivalent automorphism theorem may exist in graph-theoretic Bell literature under different terminology.

## Value

**PASS.** Symmetry reduction is central in the classification of Bell inequalities, behaviors, and finite propositional structures. The theorem proves that the physically obvious relabelings are not merely a convenient subgroup: they are all abstract logical symmetries. This gives an exact quotient group for every binary \((N,M)\) scenario, validates symmetry reduction performed using operational relabelings, and rules out hidden logical identifications that could otherwise change orbit counts.

Same-model review: passed. Independent audit: not yet performed.
