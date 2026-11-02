# Scientific review: triangular-graph width-depth coincidence

## Correctness
PASS. Two separate back-and-forth strategies preserve a partial bijection of root-point supports under \(p\) pebbles for unlimited moves, and under \(p\) nonrecycled moves for quantifier rank \(p\). At most \(2(p-1)\) root points remain selected before a move, leaving room for two new points at root size \(2p\). The lower-bound existential sentences use path forests whose line-graph adjacency pattern uniquely forces all \(s\) root points. Special cases \(p=1\), \(s=4\), and reused pebbles are addressed. Orbit and forest verification programs reproduce the predicted small cases, but the general result is proved symbolically.

## Originality
PASS, with qualified historical priority. The surveyed finite-model-theory literature supplies games and generic variable-width/depth notions. Work on \(L(K_n)\) by Harvey and Wood concerns treewidth rather than logic. A prior rank-bounded support theorem proves only the eventual equivalence half; it does not establish the exact exceptional classes, unrestricted-depth bounded-variable equivalence, or the joint sharp width/depth threshold. Searches for Kneser-complement, Johnson \(J(n,2)\), triangular-graph, and line-graph formulations did not reveal this exact theorem. A broad unpublished or historical result could still imply it; that residual risk is recorded.

## Mathematical value
PASS. The result is a complete classification for every finite variable width, not an isolated low-rank example. It establishes an exact width-depth coincidence (both minimum distinguishing resources equal \(\lfloor m/2\rfloor+1\)) and a sharp representative bound \(p(2p-1)\). The uniform family is a standard graph-theoretic test case and the path-forest characterization explains why its apparent ground-set size becomes invisible beyond the cutoff. The unbounded-depth result does not follow from merely knowing one finite quantifier-rank threshold.

## Closest sources and limits
The closest primary material is Pikhurko–Verbitsky (arXiv:1003.4865; logical depth and width), Grohe–Otto (arXiv:1204.1990; general pebble equivalence), and Harvey–Wood (arXiv:1210.8205; the same line graphs with different invariants). The result excludes counting quantifiers and more expressive signatures. A direct historical-priority guarantee and independent validation are unavailable.

Self-review: passed. Independent audit: not yet performed.
