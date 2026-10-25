# Scientific review

## Correctness — PASS
The first-colour dichotomy is exhaustive: its two vertices can straddle the bipartition only if they are a deleted matching pair; if a second same-side vertex obtains the colour, all future vertices of that side retain it and the opposite side uses just one further colour. Peeling a paired first class preserves FirstFit on the induced smaller crown graph after shifting its colours by one. Consequently, using at least \(t+2\) colours is equivalent to having exactly the first \(t\) classes be deleted matching pairs, and the displayed cross-side precedence poset is necessary and sufficient. The base poset probability is \(1/n^2\), and a complete first-two-/first-three-vertex case split gives the factor-three recurrence. Every factorial and quantifier in the probability law follows from disjoint ordered choices of the paired classes. Exhaustive computations for 3,669,864 labelled arrival orders across four graph orders and independent 28-poset dynamic-programming tests agree with the formula. These finite checks supplement, rather than replace, the infinite proof.

## Originality — PASS, qualified
The nearest primary result is Ye et al., arXiv:2608.29603, Section 3.1, which proves a loose expectation bound of \(2.5+O(1/n)\) rather than an exact probability law. Li and Li, arXiv:2610.15468, explicitly cite that bound without obtaining the present distribution. Kordecki and Łyczkowska-Hanćkowiak, arXiv:1601.00252, Table 1 report random-order simulation values; their formulas in Section 3.1 address a buffered, fixed-alternation model and are not the same distribution. The new theorem obtains the full tail law, its poset linear-extension counting mechanism, the exact optimal-colouring probability and the worst-order count. Targeted semantic research-record searches and own-claim checks identified no covering formula. Residual priority risks include unidentified Johnson-graph/Grundy-colouring literature or unpublished work.

## Mathematical value — PASS
This calculation resolves a specific quantitative gap in a recently researched canonical extremal example of online colouring: an adversarial ordering uses \(n\) colours, whereas a uniformly random order uses exactly two with probability \(1-1/n\). The sharp expectation asymptotics replace an asymptotically slack constant bound, the all-cardinality formula explains previously published empirical means, and the clean recurrence \(L_{n,t}=3L_{n-1,t-1}\) exposes the underlying structural reason. The result is an infinite-family distribution theorem, not merely a textbook computation or a short numerical census.

## Remaining limits
The result is restricted to unbuffered FirstFit, uniformly random vertex orders and labelled crown graphs. Neither arbitrary bipartite graphs nor all arrival distributions are classified. Independent historical-priority and proof assessment have not been performed.

Self-review: passed. Independent audit: not yet performed.
