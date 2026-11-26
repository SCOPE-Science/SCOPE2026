# Independent mathematical audit

## correctness

PASS

In the synchronous product on Q×Q, advance along any pair S⊆T; a reachable state in F×(Q\F) is precisely a failure, since only equal-length words are compared. Reachability in this implicit product is in NL: store two states and a counter bounded by |Q|², and scan the explicit table for successors. NL=coNL gives membership also for monotonicity. DFA nonemptiness with a nonaccepting start is NL-hard by reachability from a fresh start: use edge choices as transition labels, other moves to a sink, and the target as final. Complementation gives source emptiness NL-completeness. In the stated reduction every valid block has length m>=2 and precisely one occurring predicate. The parser needs only the simulated state, the position in the block, and the seen predicate position (or none), so its explicit transitions are streamed in logspace and there are O(|Q|m²) states. A nonempty accepted source word has a coded block in which flipping one bottom letter to top makes a rejected block; the empty source language maps to the empty language. The nonaccepting start is essential to this proof because the empty word has no upward perturbation. Larger fixed powerset alphabets can reject unused letters; k=0 gives equality of all equal-length words. No finite sampling was needed.

## originality

PASS

The published unrestricted-alphabet NL-completeness result and the upper-bound mechanism are known. The supported increment is hardness in the fixed two-letter chain, and thus the exact least nontrivial predicate count, rather than the general classification. The closest checked published proof uses an extra alphabet letter and does not establish the binary threshold by specialization.

## value

PASS

One predicate is the smallest nontrivial ordered vocabulary. Resolving it distinguishes hardness due to the state reachability structure from hardness due to a growing alphabet and makes the dichotomy with zero predicates exact. This is a meaningful restriction of the complexity theorem, not a repetition of the known product upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
