# Independent mathematical audit

## correctness

PASS

For a minimal accessible permutation DFA A with N states and |F|=m, the generated finite group G acts transitively. The reverse subset DFA has an orbit B of t distinct translates of F, pairwise distinguishable using accessibility and forward minimization. The assumption exactly two reversed accepting states implies each original state belongs to exactly two orbit blocks, so 2N=tm. Forward minimality forces an injection from Q to unordered pairs of B via each state's incidence signature, hence N≤C(t,2), m≤t−1 and N≥m(m+1)/2. Equality requires t=m+1 and bijects Q with all unordered pairs of B, turning transitions into a 2-homogeneous edge action with vertex-star final states. Conversely any 2-homogeneous edge action is forward minimal, has m final edges and reversed accept count exactly two; a full cycle and adjacent transposition give binary alphabet witnesses. The argument is all m≥2, not a bounded DFA census. Independent edge-star orbit checks verified witness incidence for m=2..6.

## originality

PASS

Rauch–Holzer (2022) already establish uniform incidence in reverse subset orbits (Lemma 23), exclusion of one reversed final state, and initial spectrum results. German (2026) establishes exact accepting-count spectrum for reversal with an m+1 choose 2 star-family witness when reversed count is two. The new assessed statement is a universal forward state minimum among all permutation DFAs satisfying the pair of final-state counts plus complete 2-homogeneous equality rigidity. The existing witness is an upper bound only; exact possible-state optimization and equality classification were not proven in the materially read works.

## value

PASS

State-size optimization under simultaneous accepting-state constraints is a natural automata-complexity invariant. A sharp universal lower bound and classification of every equality case strengthens existence constructions and exposes 2-homogeneous group geometry, providing more than a routine reformulation of the existence spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
