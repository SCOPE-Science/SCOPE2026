# Independent mathematical audit

## correctness

PASS

For distinct one-head Horn updates, a one-way cross-dependency u in A_v but v not in A_u is witnessed by X=(A_v\{u}) union A_u: u fires and enables v in one order, not the other. If cross-dependencies are both absent or both present, neither firing can newly enable the other, giving iff symmetry. Hence undirected graph G has premises N(v), and every initially disabled rule remains disabled while missing adjacent heads block each other; one pass yields C_G(X)=X union {v:N(v) subset X}. A set is fixed iff its missing-vertex induced subgraph has no isolated vertices. Exchange across an edge forces equal neighborhoods outside the pair and hence a union of cliques; conversely each clique induces U_(b-1,b) and the direct sum is a matroid. Boolean-valued submodularity for the closed-set failure indicator is equivalent to union closure of closed sets; a vertex with two neighbors creates a union-closure counterexample, and matchings preserve unions. Closed-set generating polynomials then follow blockwise. An independent exhaustive test on all premises and all subsets for n<=3 reproduced commuting-system counts 1,2,8; symbolic arguments cover all n.

## originality

PASS

General Horn closure and matroid connections predate this work, including the broad Bérczi–Boros–Makino characterization and Lozin–Zamaraev's union-closed Horn study. Their identified themes do not provide the particular pairwise one-head commutation iff symmetric dependency, combined graph representation, and simultaneous matching-versus-clique thresholds. Counts B_n, involutions and labelled graphs are explicitly inherited, not new. Residual priority risk persists in database dependencies, confluent rewriting, and one-head closure systems.

## value

PASS

The natural class of one-rule-per-head Horn updates admits an exact commutation normal form, with exchange and Boolean submodularity separating two familiar graph classes. This pinpoints when order-independent rule execution exhibits matroid closure and union-closed fixed systems, useful for logic, closure computation and constraints. The familiar Bell/matching counts are a corollary, not the sole value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
