# Scientific review

**Correctness — PASS.** The exact automaton follows by intersecting all 32 opposite-labelled orientations of the five-cycle. The standalone verifier independently constructs the transition relation, exhaustively reaches 23 nonsink subset tuples and one sink, and obtains 18 stable Myhill–Nerode blocks, all reachable. The displayed 18-state table agrees exactly. Exact coefficients through degree 26 and the bound on the numerator degree prove the rational generating function identically, not merely on tested lengths. Direct word testing provides a separate check, not the proof of infinitude.

**Originality — PASS with a documented unresolved literature risk.** The motivating 2026 work introduces the remanent orientation-intersection language. Its accessible abstract emphasizes language models, duality and chromatic information, without these particular 18-state or rational-series values. The full paper was not accessible, so a same-paper formulation cannot be excluded. Related 2024 work on reversible automata and 2020 work on oriented cycle homomorphism duality concern distinguishable questions in their accessible abstracts. Searches of mathematical records and publicly indexed research records found no matching minimal quotient or enumeration; failed searches are not proof of novelty.

**Value — PASS.** The first odd cycle beyond the triangle is a natural basic test object for a newly introduced graph-language invariant. The result gives its entire infinite regular language in minimal-state form and exact word-count growth, with an explicit triangle/pentagon distinction invisible to ordinary chromatic number. The resulting finite specification can be used as a reproducible benchmark for larger graphs; no unproved downstream consequence is claimed.

**Residual limitations.** The complete motivating preprint could not be inspected; unindexed equivalent statements remain possible. Scope is precisely the complementary direction-label convention and the five-cycle. No independent review is claimed.

Self-review: passed. Independent audit: not yet performed.
