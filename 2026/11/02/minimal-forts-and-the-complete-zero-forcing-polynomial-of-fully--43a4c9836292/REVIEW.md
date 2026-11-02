# Review of minimal forts and the complete zero forcing polynomial

## Correctness — PASS

For each fort, the subdivision of every cut edge between its selected and unselected original vertices must be selected. The proof exhausts the five possibilities for the number of original vertices: zero produces minimal cycle forts; one yields a proper all-subdivision fort; intermediate sizes contain a proper complete-cut fort; one missing original gives the minimal forced star-cut fort; all originals give the last minimal fort. It checks inclusion minimality and counts unoriented cycles with the correct reflection factor. The fort-hitting equivalence is proved via stalled zero forcing. The seed criterion, forest exponential formula, unique excluded centered star per singleton original, and the spanning-tree count then follow with all boundary cases n >= 3.

The standalone direct-adjacency and direct-forcing verifier enumerated all initial sets and all forts for n=3,4,5, and compared independent Prüfer-code counts through n=7. It returned VERIFY_OK. These finite checks corroborate, rather than replace, the all-n proof. Cayley's labeled-tree count is the only substantial standard enumerative input.

## Originality — PASS, with explicit priority risk

Becker et al., arXiv:2404.05963v1 (2024), study minimal forts and count them for other graph classes; the inspected text does not present this incidence-graph classification. Boyer et al., arXiv:1801.08910v1 (2018), define the zero forcing polynomial without the displayed polynomial for fully subdivided complete graphs. Barrett et al. (2009) and Catral et al. (2012, Theorem 1.9) cover the scalar minimum via Hamiltonian base graphs; that scalar is explicitly not new. In contrast, the proved fort classification implies an all-coefficient spanning-forest enumerator and the exact classification and count of optimum seeds. None of the inspected source statements implies the enumerator directly. Equivalent formulations via incidence graphs of complete graphs, cycle-hitting sets, graphic-matroid forests, or coforest subsets were considered; all permit potential earlier priority not detected in the inspected references. No global novelty guarantee or literature-exhaustiveness assertion is made.

## Mathematical value — PASS

The natural family of full edge subdivisions is central to zero forcing; the already known optimum number alone says nothing about the distribution of all seed cardinalities. The theorem determines every minimal forcing obstruction, the entire size distribution through classical labeled forests, and an exact \(n(n^{n-2}-1)\) classification of smallest configurations. The cycle/star-cut obstruction dichotomy is structural rather than a numerical parameter substitution. The scope and stated exclusions are meaningful to subsequent forcing and fort-hypergraph work.

## Closest literature and limitations

The 2009/2012 Hamiltonian-subdivision theorem gives the minimum only. The 2018 polynomial paper supplies the general framework. The April 2024 minimal-forts paper supplies the motivating object and other graph families. Earlier equivalent incidence-graph or forest-code literature cannot be ruled out by these searches. Valid only for n >= 3 and ordinary zero forcing. The direct verifier checks finite orders; independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
