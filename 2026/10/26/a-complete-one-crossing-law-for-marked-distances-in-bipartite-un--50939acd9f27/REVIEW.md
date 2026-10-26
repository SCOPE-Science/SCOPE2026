# Scientific review

## Correctness — PASS

The source theorem [1, Theorem 1.4] gives an exact probability for an embedded fixed path. Counting and subtracting its disjoint possibilities yields a properly normalized exact marked-distance law. The key difference identity factors explicitly as a positive denominator times a decreasing bracket. That identity proves global domination or a single tail reversal, with the one equal-support exception handled by a positive lower bound of two. The finite threshold and limiting sign follow from exact polynomial bounds. A standalone exact-rational checker passed 89,613 assertions, including independent small-graph spanning-tree enumeration; this checks calculations, not the infinite proof. The analytic argument covers every allowed integer parameter.

## Originality — PASS (historical priority not certified)

Prior work [1,2] already supplies the path-inclusion formula and, after summing, the exact distance distribution. It is not new. The claimed addition is the full order trichotomy for *different bipartition sizes with fixed graph order*, including the exception, the single-crossing law, first incomparable order eleven, and the macroscopic transition. Direct reading of the relevant sections of [1,2,3], mathematical-result similarity queries, and title/formula/alias searches did not identify an implication establishing the classification. Other nearby results concern vertex degree–distance dependence on uniform Cayley trees or bipartite spanning-tree vertex degrees; these do not order the same-part marked distance tails. A general pre-existing monotonicity or likelihood-ratio result could subsume the new conclusion and remains a historical-priority risk.

## Value — PASS

The natural question is how a fixed graph order and a changing part imbalance affect distance between two marked vertices in a random spanning tree. The answer is not a simple monotonicity assertion: the more-imbalanced law can dominate, be dominated, or be incomparable, depending on a sharp integer inequality. The first finite obstruction and its two exact opposite-sign tail gaps are structurally motivated. The at-most-one-crossing and asymptotic phase boundary make the comparison reusable for threshold-level properties of graph distances; this is not a random parameter slice or a mere restatement of an existing enumeration.

## Sources and limitations

The counted-subtree input originates in Ge–Dong (arXiv:1904.07766), with a broader forest formula in Dong–Ge (arXiv:2103.05294). Archer–Shalev (arXiv:2301.00461) studies a different, scaling-limit level of description. The result only compares two fixed marks in the larger part of a complete bipartite uniform spanning tree; the case of other graphs and opposite-part marks is not covered. The novelty comparison cannot guarantee exhaustive historical priority. Independent validation is not performed.

Self-review: passed. Independent audit: not yet performed.
