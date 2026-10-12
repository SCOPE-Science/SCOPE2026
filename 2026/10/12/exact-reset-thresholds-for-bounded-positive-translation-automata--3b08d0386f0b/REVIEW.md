# Scientific review

**Correctness — PASS.** The endpoint \(n-1\) is absorbing; every initial distance must be a subset sum of the command lengths. The sorted-coin missing-integer argument bounds consecutive coverage by \(\sum_{j<k}\min(m,2^j)\). Conversely, the largest-first greedy denomination word reduces every residual distance to zero by a rigorous invariant. Boundary values \(n=2\), \(m=1\), and \(m\ge n-1\) are included. A separate exhaustive power-automaton BFS confirms all 105 small pairs, without standing in for the symbolic proof.

**Originality — PASS, with priority risk.** Bradshaw–Clow–Stacho (arXiv:2405.00826, Sections 3–4) defines difference DFAs and gives bidirectional diameter bounds; the positive-only interval class here is *not* bidirectionally connected. General synchronizing-automaton results and the earlier Sidon embedding do not imply the exact bounded-command tradeoff. Published research searches, the relevant primary text, a semantic research index, and prior locally recorded claims identified no statement that covers the two-parameter formula. This is not proof that no unindexed antecedent exists.

**Value — PASS.** Limiting jump lengths is a natural resource constraint on location-independent reset commands. The theorem identifies the exact minimum number of commands for every number of states and maximum allowed step, constructs optimal words, and quantifies the transition from linear to logarithmic reset time. Unlike an arbitrary finite census, this establishes a complete infinite-parameter classification tied to the new geometric difference-automata setting.

Limitations: the result requires the entire positive alphabet through the bound and the stated self-loop rule; it is not a theorem about all difference DFAs. Known coin-denomination covering principles are used rather than claimed as original. Some unindexed literature may contain equivalent results.

Self-review: passed. Independent audit: not yet performed.
