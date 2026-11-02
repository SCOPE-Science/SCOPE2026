# Scientific review

## Correctness

**PASS.** The conclusion is a finite exhaustive theorem with an explicit complete search domain: all \(8!=40320\) row-column permutations, of which exactly \(92\) obey both diagonal constraints. All \(4186\) unordered solution pairs are compared by the number of changed occupied squares. All-source breadth-first search on the exactly constructed graphs proves the component structure, radii, diameters, and distance enumerators; full symmetric-square transformations establish the orbit claim. An independent bitboard implementation reproduces the enumeration and graph statistics from a different representation. The exact finite certificate and both standalone checkers are supplied.

## Originality

**PASS with residual risk.** The \(92\)-solution census and the \(12\) square-symmetry classes are prior knowledge. Zhang and Ma's 2008/2009 swap Monte Carlo chain traverses all rook placements and permits diagonally conflicting intermediate arrangements. The present graph keeps every intermediate *full solution* and allows simultaneous changes of up to five queens; neither the threshold nor its metric profile follows from the Monte Carlo sampling results. The 2013 and 2014 papers of Chaiken, Hanusa and Zaslavsky enumerate placements rather than classify paths between them. Searches for exchange, transposition, Hamming-distance, swap, reconfiguration, and exact mobility formulations in published research records and indexed literature found no covering statement. The Bell–Stevens survey was available primarily through its abstract and bibliographic record; an older German genealogy of eight-queens solutions was also not read in full. Those uninspected sources and unindexed equivalent representations remain residual risks. Independent human novelty verification remains outstanding.

## Value

**PASS.** The eight-queens puzzle is a canonical exact constraint-satisfaction benchmark. Knowing the number of feasible configurations alone does not describe their mobility when *every intermediate state must remain feasible*. The sharp four-versus-five batch-size boundary, the symmetry-coherent exceptional set, and the complete distances quantify this obstruction. A sharp, exhaustive solution-space connectivity benchmark can inform feasible-state local-search and reconfiguration test cases; no larger-board theorem or practical algorithmic improvement is claimed.

## Limits and closest literature

C. Zhang and J. Ma (arXiv:0808.4003) use single swaps on a larger state space admitting constraint violations. S. Chaiken, C. R. H. Hanusa, and T. Zaslavsky (arXiv:1303.1879; arXiv:1402.4880) study enumeration and inside-out polytopes. J. Bell and B. Stevens (Discrete Mathematics 309, 2009) survey the classical puzzle. The new finite claim is not implied by the quoted results; the full-text coverage limitations above remain. Exact computational completeness is for eight queens, not all \(n\).

Self-review: passed. Independent audit: not yet performed.
