# Scientific review

## Correctness — PASS

The pair-coordinate definitions handle ordinary and even-antipodal pairs without duplication. Explicit transition formulas establish the two coordinatewise potential lower bounds for every \(n\ge2\), including wrap and complementary-arc cases. A displayed word meets both bounds, and a unique rank-decreasing outgoing edge at every nonsingleton pair proves uniqueness for all strictly positive costs. Disjoint consecutive intervals prove the shortest-distance spectrum without a finite extrapolation. Replayed transition tests cover all pairs for \(2\le n\le50\) and independent weighted reverse Dijkstra enumerations through \(n=17\), not an external independent audit.

## Originality — PASS, with residual priority risk

The closest full primary source is Gusev's 2014 analysis of the Černý pair automaton (arXiv:1404.6731v1, Section 3). His Lemma 1 gives a representation of the pair transition graph for odd \(n\), and his Theorems 3–4 evaluate expected merging times under random inputs for odd and even sizes. The present mathematical claim instead concerns deterministic shortest words for **all** pairs and both parity classes, their separate letter-count minima, simultaneous positive-cost optimality, uniqueness, and the exact multiplicity-one distance spectrum. This is not implied by the probabilistic expectation formula alone; the available graph could serve as a starting point for a further derivation, which is a genuine residual priority risk. General shortest-reset algorithms and weighted-automaton work do not state or dominate these particular exact formulas. Targeted research-record and literature searches found no covering assertion; absence of a match is not a proof of novelty.

## Value — PASS

The problem of merging a specified pair under nonuniform input costs is a natural basic synchronization/automata-control optimization problem. A single word simultaneously optimizing two competing resource counts for every starting pair is stronger than a scalar shortest-path table or a fixed choice of costs. The result also exhibits a rigid bijection between starting pairs and shortest-merging lengths, and includes the nontrivial antipodal parity boundary. This is a structural exact classification across an unbounded automaton family, rather than an isolated small census or trivial restatement of the full-state reset threshold.

## Closest literature and limitations

Primary: Gusev, *Synchronizing automata with random inputs*, 2014, arXiv:1404.6731v1, Section 3, full author-uploaded manuscript inspected. Context: Kisielewicz–Kowalski–Szykuła (2013) on general shortest reset algorithms; Ruszil (2021) on general weighted synchronization algorithms. The theorem does not address subsets larger than two, general automata, or state-dependent costs. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
