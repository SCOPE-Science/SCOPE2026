# Scientific review: priced pineapple resistance allocation

## Correctness — PASS

For every integer \(k\ge2\), \(m\ge1\), and positive budget/price \(B,t\), the claim concerns all independent eligible edge conductances, not just symmetric candidates. Strict convexity of the all-pairs effective-resistance objective and graph automorphisms force a unique three-orbit optimum. On a weighted pineapple graph, the hub-to-core and core-to-core effective-resistance decomposition gives
\[
\mathcal K=\frac{m(N-1)}b+\frac{m+1}a+\frac{(k-1)N}{a+kc}.
\]
The Cauchy–Schwarz lower bound with transformed variable \(v=a+kc\) is feasible exactly below the stated chord-price threshold. Above and at the threshold, the star candidate passes the chord-boundary Karush–Kuhn–Tucker inequality; strict convexity gives uniqueness. The stated fixed-leaf asymptotic follows directly by retaining the leading \(k^{3/2}\) term in the exact normalization. A standalone checker confirms the resistance identity by independently constructed rational Laplacians and evaluates small unrestricted competitors. The analytical proof, not those finite checks, covers all integer sizes and real parameters.

## Originality — PASS, with bounded residual risk

Ghosh–Boyd–Saberi (SIAM Review 50, 2008, DOI:10.1137/050645452) supply the general convex design framework, strict uniqueness, a star solution, and worked examples for wheels and barbells. An existing general price-screening result for chords of a weighted tree already gives the chord-free price boundary in this star-backed instance; that boundary alone is **not** treated as original. The present claim adds a complete exact positive-chord allocation, its all-price closed optimal objective, and an explicit dimension-independent support regime for this natural pineapple family. Haritha–Chithra (arXiv:2309.02704, Proposition 3.2) calculate unweighted pineapple resistance distances but optimize no conductances. Tovar et al. (arXiv:2610.03627) study general cost-convexity and edge screening, but the inspected material supplies no exact pineapple-family optimizer. Searches found no identical formula. The unresolved risk is a differently indexed specialization, not a demonstrated stronger prior theorem; independent bibliographic review remains unperformed.

## Value — PASS

The theorem answers an exact, natural network-design question rather than a single arbitrary parameter instance: how to allocate a costly set of redundant clique links versus essential spokes and bridges to minimize all-pairs electrical resistance. It simultaneously classifies every edge's optimal activity, provides explicit weights and optimal objective for an infinite two-parameter family, and shows that one sharp price threshold depends only on total network order. The fixed-leaf large-clique asymptotic gives an explicit quantitative benefit for purchasing optional links. Its usefulness does not depend on claiming a new general SDP or a larger downstream theorem.

## Limits

All costs are linear and two edge families have unit price; only clique-internal nonhub edges carry common relative price. Pendant edges remain bridges, and disconnected assignments are inadmissible. Statements do not extend to arbitrary graph attachments or nonlinear material laws. An equivalent published formula in unindexed sources cannot be excluded by searches alone. Finite verification neither exhausts parameter space nor constitutes independent audit.

Self-review: passed. Independent audit: not yet performed.
