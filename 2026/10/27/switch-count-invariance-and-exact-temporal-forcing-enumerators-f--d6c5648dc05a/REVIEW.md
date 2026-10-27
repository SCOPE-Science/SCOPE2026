# Research assessment

## Correctness — PASS

The matching closure map is idempotent and union-preserving. On each alternating-cycle component, the reachability interval of an initially occupied first-matching edge grows by exactly one vertex at each end per matching switch, until saturation. The resulting cyclic-gap criterion is necessary and sufficient. Marked occupied edges and bounded cyclic compositions give the integer coefficient formula. Minimum seeds, their multiplicity, and independent-component factorization follow without hidden regularity assumptions, including shared matching edges. The Bernoulli completion law follows from independence of first-matching-edge occupancy, and elementary block/union bounds yield the logarithmic switch threshold. The independent direct snapshot simulator checked 648 schedule/family cases and 257,976 initial subsets. It is not an infinite proof.

## Originality — PASS (qualified)

Full-text inspection of Baste et al., arXiv:2609.29054v1, confirms that their temporal framework and complexity results do not state the two-perfect-matching all-cardinality polynomial, arbitrary-switch invariance, or the Bernoulli switch threshold; their structural sections are on stars and bounded-degree trees. Boyer et al. supply an established static zero-forcing-polynomial framework and do not provide this temporal statement. Searches of mathematical research records under temporal matching closure, cyclic gap counting, periodic zero forcing, and switch-separated forcing found no directly equivalent claim; the nearest record concerns paths with distinct one-time edge activation, not a two-matching repeated schedule. A separate indexed archive explicitly mentions **exact minima** for alternating even cycles, which may subsume the bare extremal number and is credited. Its detailed manuscript was inaccessible, leaving a genuine priority risk for possible additional enumerative assertions. The claim does not rest on a novelty assertion about ordinary bounded-composition identities or the bare cyclic minimum.

## Mathematical value — PASS

The result supplies a complete all-cardinality enumerator, sharp minimum multiplicity, an exact characterization of every successful initial set, and a time-change invariance for an entire natural class of schedules with arbitrary run lengths on any union of even alternating cycles. It also yields a finite-time infection reliability distribution and a sharp logarithmic random-seed switching scale. These are structural and distributional data beyond a minimum cardinality, and they distinguish switching activity from elapsed snapshots in temporal propagation.

## Limits and closest literature

The principal initiating source is Baste et al. (2026), arXiv:2609.29054v1, fully inspected. Related static enumeration appears in Boyer et al. (2018), arXiv:1801.08910. A relevant independently indexed archive by K. Harish mentions exact minimum values for alternating cycles but was accessible only via repository summary; the risk that its full version contains some equivalent count remains unresolved. The construction assumes two fixed perfect matchings and does not extend unchanged to three matching colors or arbitrary temporal graphs. Independent audit is absent.

Self-review: passed. Independent audit: not yet performed.
