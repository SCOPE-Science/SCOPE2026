# Scientific review of the cyclic-gap subset-synchronization theorem

## Correctness — PASS

The potential \(F(S)=\min_{(g,t)}[((n-1)\alpha+\beta)(n-g)-\alpha t]\) is a rigorous lower bound by a strict Bellman inequality for each input letter. Exactly one letter attains equality at every nonsingleton set, and the prescribed word repeatedly follows those equalities, increasing the winning gap until it reaches the full cycle. Strict positivity ensures uniqueness; the singleton and two-state collapse boundary cases are treated in the proof. The independently built verifier checks 130,918 nonsingleton state sets for four weights through size 16 and independently computes shortest weighted paths by Dijkstra for all sets through size 12. There is an all-length proof, not a claim extrapolated from experiments.

## Originality — PASS, with stated risk

Eppstein's 1990 Theorem 1 computes shortest words for any starting set of an arbitrary cyclically monotonic automaton, but supplies an interval-state search, not the present closed formula or simultaneous cost independence for positive letter weights. Gusev 2014 analyzes expected pair synchronization; Behague–Johnson 2020 discusses \(k\)-set rendezvous and earlier Černý lower-bound constructions, not pointwise weighted costs; Ruszil 2021 gives general weighted approximation algorithms. These are genuine close mathematical antecedents rather than mere title matches. A 2014 Cardoso thesis on the same family and \(k\)-set bounds could not be inspected in full, and an earlier unpublished or unindexed pointwise derivation remains possible. Thus originality is assessed relative to the actual inspected statements, without claiming absolute priority or independent certification.

## Value — PASS

The result solves an exact, natural control problem for **all** initially possible state sets of the extremal Černý family: it gives a closed form for weighted optimal cost and an explicit unique word independent of letter-cost ratios. Cost independence is uncommon for weighted reset problems and is not delivered by the general shortest-path algorithm alone. The theorem unifies and strictly extends pair-only formulas to every subset, while yielding a linear-time policy in the size of the given subset (apart from output). It makes no unsupported claim for general automata.

## Scientific limits

The conditions \(n\ge2\), nonempty \(S\), exact two-letter transitions, and \(\alpha,\beta>0\) are essential. Finite verification is supplemental. Prior sources were compared by mathematical implications, and the inaccessible dissertation is explicitly recorded as a residual risk.

Self-review: passed. Independent audit: not yet performed.
