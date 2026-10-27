# Scientific review

**Correctness: PASS.** The complete space of \(5^{10}=9,765,625\) binary five-state transition pairs is exhausted twice. One implementation counts shortest full-set-to-singleton labeled paths forward; the other counts singleton-to-full preimage paths backward. Each is bijective to distinct shortest reset words, both produce the same complete histograms, and direct independent brute force verifies the witness language and 240-element orbit. The classification is finite, not a conjecture for larger automata.

**Originality: PASS on inspected evidence.** Szykuła's 2026 survey and Kisielewicz–Kowalski–Szykuła's 2013/2015 and 2016 studies discuss reset length, algorithms for obtaining shortest witnesses, and slow automata. None of the inspected primary results enumerates all **numbers** of shortest reset words for five-state binary automata. A prior five-state reset-length census does not imply the new multiplicity law. A separate seven-state word-count result is a different domain. An earlier small-automata report was only partially readable, and unindexed equivalents remain possible.

**Mathematical value: PASS.** The exact 14-value multiplicity law characterizes how many optimal synchronizing controls exist, an invariant distinct from their minimum length. Its 64-word maximum is achieved by exactly one 240-member symmetry class, with all shortest words explicitly factorized. The fraction with unique optimal control and contrast between thresholds 13 and 16 are useful nontrivial finite benchmarks.

**Limits.** The scope is limited to ordered binary automata on five labeled states; neither larger-state behavior nor publication priority is certified independently.

Self-review: passed. Independent audit: not yet performed.
