# Review: dominating induced matching rigidity in \(GP(n,2)\)

## Correctness — PASS

The vertex-state proof is constructive and covers every integer \(n\ge5\). The cyclic outer-white gaps must each have length two or three; the inner-neighbor parity condition at every white outer vertex forces those gaps to alternate, proving \(5\mid n\). Inner states and black matching edges are then uniquely forced, giving exactly five rotations. All five are constructed and checked; the edge partition yields the coloring result. Counting closed edge neighborhoods establishes the saturation statement with the equality case. The independent exhaustive exact-cover and vertex-state programs check orders \(5\)–\(30\) and \(5\)–\(20\), respectively; their logs match the packaged scripts. Finite checks corroborate, rather than replace, the infinite proof.

## Originality — PASS, with residual uncertainty

The strongest nearby source, *Dominating induced matchings and other graph parameters* (2024), Observation 7, already exhibits the periodic DIM and establishes its cardinality, so those are not claimed novel. The new assertion counts and classifies **all** DIMs at every order, rules them out at every other order, identifies **all** minimum maximal matchings, and proves uniqueness of the five-color partition. The Yang–Wu (2018) article's available abstract establishes exact strong edge chromatic indices but does not mention classification of optimal colorings; its full text was inaccessible, which is a specific unresolved risk. The Chen–Miao–Zhou (2020) full text treats the distinct \(k\ge4\) range. Relevant published-finding corpus indexed matching-complex records concern homotopy types on individual graphs, not universal classifications of efficient edge-dominating matchings. Non-indexed equivalent characterizations cannot be excluded.

## Mathematical value — PASS

A natural efficiency-equality problem is upgraded from a known witness to an exhaustive infinite-family rigidity theorem. The classification simultaneously settles the equality cases for minimum maximal matching size and the uniqueness of optimal strong edge coloring. Neither is merely a numerical recomputation: the alternating-gap mechanism is a structural global constraint on local cubic matching patterns.

## Limits

The construction and uniqueness are specific to \(GP(n,2)\). No exact claim for nonmultiples of five beyond the obstruction to strong five-edge-coloring is asserted, and no independent external audit or publication-priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
