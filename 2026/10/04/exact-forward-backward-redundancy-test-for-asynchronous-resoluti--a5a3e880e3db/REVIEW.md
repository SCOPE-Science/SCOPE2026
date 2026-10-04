# Review

## Correctness

PASS. The published recursion implies that a resolution group replaces every participant's current view by the union of all participant views. These updates preserve componentwise unions, so any suffix is exactly a contributor map: the final view of agent \(a\) is the union of the prefix views indexed by \(\operatorname{see}_a\) of the suffix.

This gives the exact formula with and without the chosen occurrence. Equality of final views is sufficient for equality of current accessibility relations in every model. Necessity is proved by the explicit coordinate-equality model on \(\{0,1\}^A\), in which different index sets yield different intersections of base equivalence relations.

The immediate-repetition corollary and the \(n(n-1)\) compression bound follow directly. Exhaustive finite replay agrees with every step.

## Originality

PASS. The primary paper explicitly leaves redundant resolutions as future work. It gives the view recursion and notes that equal views do not imply history equivalence, but it does not supply an arbitrary-occurrence deletion criterion.

Pairwise gossip literature contains notions of redundant or productive calls, stuttering results, and sharp bounds for ordinary telephone calls. Those results are not the same statement: the accepted theorem treats arbitrary resolution groups, separates prefix and suffix effects, and gives a necessary-and-sufficient model-independent test for preservation of the 2026 semantics' current accessibility relations.

## Value

PASS. The result turns an explicitly posed semantic redundancy question into a finite set-theoretic test. It can detect a resolution that was informative when executed but becomes irrelevant to the final current relation state because later resolutions subsume its contribution. The contributor factorization also yields a finite compression bound for arbitrary asynchronous resolution histories. This is useful for state-space reduction and clarifies the exact distinction between current information and remembered event history.

## Closest literature and limitations

Balbiani, van Ditmarsch, and Lerouvillois (2026) are the closest source and explicitly pose redundancy as future work. Brouwer, Draisma, and Frenk (2015) give a sharp irredundant-length theorem for pairwise ordinary gossip. Van Ditmarsch, Kokkinis, and Stockmarr (2017) study redundant calls in pairwise gossip protocols.

The present theorem is deliberately about current accessibility relations, not full asynchronous history semantics. A history-sensitive formula may still distinguish two histories whose current relation tuples agree.

Same-model review: passed. Independent audit: not yet performed.
