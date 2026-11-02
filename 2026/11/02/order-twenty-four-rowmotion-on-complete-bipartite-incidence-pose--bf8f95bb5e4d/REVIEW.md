# Scientific review

## Correctness: PASS

The stated theorem has one defined poset family, one classic rowmotion action, six claimed cycle formulas, and exact permutation order 24. Its Boolean local recurrence follows by identifying precisely the minimal complement in an incidence poset. Any labelled ideal with a given left-bit pair and set of distinct column types evolves with the same period as the canonical support representative, because only type presence controls the global updates and copies of a type evolve identically. This reduces the infinite family to exactly 48 nonempty supports. The direct minimal-complement certificate `verify_support.py` checks the full table. Independent labelled-state enumeration `verify_direct.py` verifies n=1,...,6 and reconciles all counts. The surjection formula counts every labelled state once and includes all boundary cases n=1,2.

## Originality: PASS with residual risk

Striker–Williams, *Promotion and Rowmotion* (arXiv:1108.1172, first public August 4, 2011) supplies the classical definition and promotion framework, but its investigated classes do not establish this family-specific cycle census. Grinberg–Roby, *Iterative properties of birational rowmotion* (arXiv:1402.6178), covers classical rowmotion on skeletal posets and other structured families; the connected incidence poset in this theorem is not a height-two skeletal poset. The previously available rowmotion census of the rank-one/rank-two Boolean poset (complete-graph incidence) has no length-24 cycles and neither specializes to nor dominates this different induced-poset action. Targeted graph aliases, exact sequences, published-finding corpus searches, and OEIS-oriented searches did not reveal a covering result. Full global novelty cannot be certified: unindexed manuscripts or database tables may contain an equivalent theorem.

## Value: PASS

The problem is natural classical rowmotion on vertex-edge incidence posets of complete bipartite graphs. A uniform order 24, a sharp primitive-period threshold at three right vertices, and six exact all-parameter orbit formulas are a structural periodicity and enumeration result for exponentially growing state spaces. The 48-support automaton is an explanatory invariant of multiplicity-free column types, not an arbitrary parameter slice or a purely numerical census.

## Reproducibility and limitations

Only classical rowmotion on labelled incidence posets is covered. The proof uses a finite 48-case table, with complete direct code and corroborating brute-force enumeration attached. Independent scholarly review and exhaustive novelty verification remain unperformed. The actual checks and their limits are specified in `VERIFICATION.md`.

Self-review: passed. Independent audit: not yet performed.
