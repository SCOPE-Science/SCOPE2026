# Independent mathematical audit

## correctness

PASS

Trimming preserves the language and graph restriction. A state on successful paths cannot occur at depths i and j with i≠j, because one common successful suffix would yield two accepted lengths. All surviving transitions increase depth by one (any transition between trim states lies on a successful computation). Every middle state contributes the rectangle of its first and second labels; their union is exactly R. Hence the unrestricted minimum is b(R)+2. Three different middle neighbors of one final yield two four-cycles sharing an edge at the start, so each final serves at most two middle states. Pairing the middle states from an optimal cover attains the resulting bound as a bipartite cactus, including a singleton when needed. For inequality, sets of rectangle indices containing each row symbol constitute an antichain because every ordered off-diagonal pair must be covered; equal-size subsets give the converse. Any null rectangle in the converse would reduce the number below the proved Sperner lower bound. Nonemptiness and k≥2 are used in the respective statements.

## originality

PASS

The supported distinction is the exact cactus state cost for arbitrary nonempty length-two relations. The unrestricted rectangle construction, the classical Sperner bound, and the already covered diagonal specialization are not separate originality claims. The nearest inspected primary theorems do not give this general constrained state cost.

## value

PASS

This is a complete sharp answer for a natural class of languages, relating a graph restriction on nondeterministic representations to a well-defined Boolean-rank invariant. It separates the reachability labeling cost from the exact cost of grouping finals, and shows that restricted-state overhead tracks the relation rather than the alphabet size (linear for equality versus logarithmic for inequality). This is a constrained optimization result, not a new claim for the standard Sperner calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
