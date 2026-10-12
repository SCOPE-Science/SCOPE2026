# Scientific review: ternary level-four Simon normal-form length

**Correctness — PASS.** The congruence signature is exactly the set of scattered subsequences of lengths one through four; the append recurrence is proved in both directions. Exhaustive breadth-first closure examines every reachable signature and its three outgoing transitions, producing \(334202\) states, a maximum shortest-path length of \(18\), and exactly \(18\) terminal-depth states. The independent position-subsequence oracle agrees for every extremal witness, and the Fleischer–Kufleitner ranker criterion confirms all eighteen are individually length-minimal. The finite computation is a complete quotient enumeration, not a bounded-prefix experiment.

**Originality — PASS, with residual risk.** Pach (online 2017) and Fleischer–Kufleitner (2018) establish canonical shortest representatives and algorithms, but the accessible full 2018 paper does not give this exact ternary/level-four radius and extremal orbit classification. The 2023 Fleischmann–Höfer–Huch–Nowotka paper supplies binary-class and partial ternary theory, not this finite depth spectrum. The earlier reported index \(334202\) is credited and is not the novelty claim. A 2015 Pach level-four normal-form conference paper and the 2017 original have only partially accessible online material here; a coincident enumeration inside them or otherwise unindexed remains possible. Such inaccessible papers are not asserted to be non-covering in full.

**Mathematical value — PASS.** The maximum shortest representative length is an intrinsic worst-case canonical-form complexity and a sharp uniform witness cutoff for level-four piecewise-testable properties over the first nonbinary alphabet. Neither the known total index nor generic normalization algorithms imply the numeric sharp threshold or three extremal symmetry types. This is a natural complete finite extremal classification, not an arbitrary word sample.

All mathematical claims apply only to the stated alphabet and congruence level. The code's exhaustiveness is justified by transition closure and BFS, not by a runtime log alone.

Self-review: passed. Independent audit: not yet performed.
