# Scientific review

## Correctness (C): PASS
The size-four lower bound follows from sixteen unique length-four factors, each requiring a crossing mark and each mark crossing at most four of their unique windows. Equality forces the unique mark set \(\{3,7,11,15\}\); this argument holds for all cycles and cuts. Because hitting every length-four window also hits every longer factor occurrence, factors through length four suffice for a full attractor. `verify.py` exhausts the entire \(2^{16}\)-word domain, identifies all \(256\) rooted unfoldings and \(16\) rotation classes, checks full factor cover for both stated mark sets, and independently recomputes the \(16\)-row `CENSUS.csv`. The checker ran successfully with the printed counts in `VERIFICATION.md`. This is a finite complete proof; the claims do not depend on unbounded experimental extrapolation.

## Originality (O): PASS, with priority risk
The nearest relevant treatment by Mantaci et al. gives asymptotic bounds in §6.2 and a single size-four binary order-four example in Proposition 41, not the all-roots distribution. Whittington explicitly asks about general de Bruijn unfoldings in §5, and Theorem 29 resolves a chosen construction only for *prime* orders. Thus neither compared claim implies the classification at composite order \(4\), the exact \(192/64\) split, the \(4/8/4\) orbit distribution, or a universal five-mark set. Relevant semantic-result and published-literature searches were performed for the exact cycle, parameter, and synonym formulations. Absence of an indexed covering result is not absolute priority proof; an earlier unpublished or differently described exhaustive census remains a residual risk.

## Value (V): PASS
The question is directly motivated by a published open investigation of how the attractor optimum depends on the cyclic de Bruijn word and its unfolding. The first composite binary order is a natural complete test case: all sixteen cycles and all their cuts are classified, not an arbitrary isolated instance. The result both exhibits bad cuts (where the minimal sharp four-hitting set is not a full attractor) and proves that each cycle has many good cuts, giving exact extremal incidence counts and a uniform five-position certificate. The known single good example does not determine these facts.

## Limitations
No claim is made for larger order, larger alphabet, circular attractors, online choices, or general conjectures. No independent human or external audit has been performed. Source-specific publication priority remains open to further checking.

Self-review: passed. Independent audit: not yet performed.
