# Review

## Correctness
PASS. The proof fixes the complete-DFA convention, excludes the unique dead sink from the state count, uses a topological ordering of the non-dead states, and bounds the accepted suffix count by the chain completion. The case split for final-state patterns and the first deviating transition gives the exact gap. Explicit constructions attain every case. The finite checker is supplementary and is not treated as an infinite proof.

## Originality
PASS on the reviewed evidence. The closest literature enumerates minimal or acyclic automata and studies their structural ranks, but the reviewed material does not state the conditional accepted-language cardinality spectrum or its exact second-largest gap. published-finding corpus searches returned no direct match. Search failure is not a proof of novelty; the earlier conference precursor to the acyclic-automata enumeration literature and unmaterialized historical records remain residual risks.

## Value
PASS. The result gives an exact capacity bound and the first discrete gap below it for a natural finite-language automaton model, with explicit extremizers. The gap is a structural stability invariant, not merely a finite table or a computational novelty claim.

## Closest literature and limitations
The closest sources are the enumeration of minimal acyclic automata via generalized parking functions (arXiv:1411.4757) and Liskovets's exact enumeration of acyclic deterministic automata (2006). Their reviewed parameters concern automata counts and structural ranks, not the number of accepted words conditional on both state and accepting-state counts. The theorem is limited to complete deterministic automata, finite languages, alphabet size at least two, and at least two non-dead states.

Self-review: passed. Independent audit: not yet performed.
