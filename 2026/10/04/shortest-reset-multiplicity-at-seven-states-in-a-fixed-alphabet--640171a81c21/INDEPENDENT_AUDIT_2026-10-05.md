# Independent mathematical audit

## correctness

PASS

The displayed seven-state transition maps match the specialization of the source construction. An independent exact subset-BFS replay gives first singleton distance 32 for both alphabets. For {a,e} it gives 331776 shortest words, all to state 4; for {a,b,e} it gives 663552 to state 3 and 663552 to state 4, total 1327104. The inspected package verifier implements the same complete shortest-path recurrence over the finite power automaton and replays the published length-32 witness. Thus the factor-four multiplicity statement is exhaustive, not sampled.

## originality

PASS

The primary Theorem 3 was inspected through the construction and threshold proof. It states the same reset threshold for the three-letter restriction and notes the two-letter restriction has the same threshold, but it does not enumerate shortest words at seven states. Targeted Resultary and web searches for shortest-reset multiplicity, the exact family, and the exact counts found no prior equivalent enumeration.

## value

PASS

The source explicitly studies how alphabet size changes slow synchronization and uses finite census data for critical small automata. At the first state count beyond that census, the exact comparison isolates an effect invisible to reset threshold: adding one letter preserves optimum length but quadruples optimum-word multiplicity and adds an optimum target. This is a motivated finite invariant under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
