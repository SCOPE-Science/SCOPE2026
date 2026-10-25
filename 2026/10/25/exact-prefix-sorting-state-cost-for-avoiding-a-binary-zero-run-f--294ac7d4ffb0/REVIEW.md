# Self-review

**Correctness — PASS.** The proof explicitly distinguishes all \(r+1\) ordinary right languages using \(0^{r-j}1\), establishes pairwise co-lex incomparability by strict triples, and gives a correct \(2r+1\)-state Wheeler order with all transitions checked. The matching convexity lower bound separates both words in each of the \(r\) nonterminal suffix classes and adds the final suffix class. A Python checker passed for \(1\le r\le10\), independently testing 218358 exact binary inputs and all edge-pair axioms. Finite checks are not a proof beyond their range.

**Originality — PASS with explicit residual risk.** Closest theory is Alanko et al. (2019) on Wheeler convex partitions and Cotumaccio et al. (2022) on colex width. A 2025 stronger source already implies that this locally testable language is Wheeler, so *existence is not novel*. The exact simultaneous ordinary-DFA state count, maximal colex width, and minimum Wheeler-DFA state count are not identified in inspected material or consulted mathematical records. General algorithms supply methods but do not themselves state this parametric identity. Uninspected appendices, unindexed work and inaccessible historical parts could reduce originality.

**Mathematical value — PASS.** Exact family-dependent cost of prefix sorting quantifies the conflict between minimization and Wheeler sorting on a natural one-pattern forbidden-factor language, with arbitrarily large width of the minimum DFA yet only linear state refinement to a Wheeler DFA.

The result uses trim partial DFAs, fixed \(0<1\), and forbidden factor \(0^r1\), for all \(r\ge1\). Independent auditing is outstanding.

Self-review: passed. Independent audit: not yet performed.
