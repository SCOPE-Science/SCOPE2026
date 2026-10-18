# Independent mathematical audit

## correctness

PASS

For the fixed irreflexive four-node Kripke target r->c and c->t,c->f and any monotone NAE3 incidence source with nonempty clause set, every surjective p-morphism necessarily sends unique root rho to r: sink variables cannot map to r/c by back and clause nodes cannot map r because a sink successor would need image c. Forth then sends every clause to c, variables to t/f; back at each clause requires both colors, exactly monotone NAE3. Conversely every satisfying assignment uniquely defines a surjective forth/back p-morphism, including repeated-variable clauses and isolated variables. Thus the reduction is parsimonious from #NAE3, not incorrectly claimed parsimonious from #SAT. Enumerating a candidate map is polynomial so problem belongs to #P; Creignou-Hermann counting CSP dichotomy yields #P-hardness since NAE3 has six tuples and is not affine. Independent exhaustive map vs satisfying-assignment counts for representative 1..3 variable incidence frames corroborate the bijection. General proof is the explicit forced-level argument.

## originality

PASS

Takahashi (2026) already uses this exact target and monotone-NAE incidence picture for decision existence, leading to a modal Jankov validity coNP-hardness conclusion; graph locally surjective homomorphism literature also has related decision/parameter complexity. Counting valid p-morphisms, however, requires exact witness correspondence and #P-hardness in the fixed-target directed frame class; it is not a stated conclusion of the accessed decision source. The source decision reduction is credited as starting point and the improvement rests on a complexity jump and parsimonious proof, not a new construction. Full Takahashi text inaccessible creates a real risk of an implicit counting statement.

## value

PASS

Exact fixed-target #P-completeness for bounded-height rooted irreflexive frames is a motivated counting complexity classification directly relevant to modal p-morphic image witnesses and local-surjectivity constraints. The parsimonious bijection is an explicit transfer tool, not an isolated small-instance enumeration; it upgrades known satisfiability-based decision hardness to a quantitatively stronger problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
