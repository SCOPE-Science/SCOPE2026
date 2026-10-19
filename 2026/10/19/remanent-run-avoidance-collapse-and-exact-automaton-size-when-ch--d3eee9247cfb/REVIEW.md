# Scientific review

## Correctness — PASS

The proof establishes a full-language sandwich using a fixed \(k\)-clique and a proper \(k\)-coloring, correctly covering all orientations. A tournament containing a directed cycle reads all signed words, whereas an acyclic tournament is transitive. The run-by-run construction in the transitive tournament gives sufficiency even when run lengths vary; the forbidden-run argument gives necessity. The complete DFA has \(2k\) reachable states, with explicit separating suffixes covering every state-pair type. The composition bijection supplies the enumerator. No computational enumeration is used to infer an unproved infinite step. The checker exhaustively examines its stated bounded cases; it independently verifies the boundary orientation of the five-cycle.

## Originality — PASS within examined evidence

The closest source is Pujol, arXiv:2609.08843v1. Its Definition 32 supplies the invariant, Proposition 4 supplies the cycle observation, Corollary 34 detects chromatic number with monotone words, and Theorem 36 supplies exactly the already-covered \(k=2\) bipartite case. The present all-sign-language equality for \(\chi=\omega\) graphs, its generalized-Fibonacci word enumeration, and exact \(2k\)-state minimal complete DFA (in particular for all \(k\ge3\)) are not stated in the inspected relevant portions of the primary text. The new claim is not inferred merely from the monochromatic path criterion: the proof compares every alternating signed word through a clique–colouring sandwich. Research-record searches for remanent languages, perfect graphs, transitive tournaments, and deterministic state complexity returned no covering record, and accessible prior owned claim ledgers had no matching statement. Residual risk: the sandwich is short and could have appeared implicitly in older graph-homomorphism work; no independent priority certification is asserted.

## Value — PASS

This is a structural classification of a newly investigated graph-language invariant over a large natural class (including all finite perfect graphs), answering whether the full orientation-intersection language retains more graph information than chromatic number when clique and chromatic number agree. It identifies the exact forbidden-factor language, complete minimal state complexity, and all-length word counts, and shows on the five-cycle that dropping the invariant-equality hypothesis can change the language. The result is not merely a restatement of the known bipartite case or a new name for an arbitrary finite table.

## Source relationship and limits

Primary source: Cyril Pujol, *Graph-based automata*, arXiv:2609.08843v1, §§2 and 5.2. The general direction is already related to established graph homomorphisms and run-avoidance DFAs. Unindexed equivalent statements are a historical risk. No converse, characterization of imperfect graphs, or independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
