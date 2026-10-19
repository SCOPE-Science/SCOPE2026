# Scientific review

## Correctness — PASS

The statement is for all integers \(m\ge2\), all noise-intensity ratios \(\rho>0\), and every gain budget \(B>0\). Positive definiteness over the whole simplex, strict convexity with a positive definite noise weight, and uniqueness without symmetry assumptions are proved directly. Leaf symmetry follows *after* unrestricted uniqueness. A Schur complement gives the precise rational cost; both endpoint derivatives were reconstructed symbolically, and the sign criterion follows from strict convexity. A single-variable derivative has one positive zero, producing the exact golden-ratio cusp. The theorem's two asymptotic scales follow from endpoint expansions, not extrapolation. The standalone checker passed 3,371 exact-symbolic and numerical assertions; these do not replace proof.

## Originality — PASS, with residual risk

The closest foundational source is Lin–Fardad–Jovanović (arXiv:1302.0450), whose read model and optimization sections use equal-noise covariance and selection of fixed-gain Boolean leaders; its convex relaxation does not state the heterogeneous-noise, continuously divisible-budget threshold. Fitch–Leonard (arXiv:1407.1569) treats fixed equal-gain leader sets and unit-intensity noise. Patterson–Bamieh (DOI:10.1109/CDC.2010.5718151) addresses noise-free designated leaders, but only its abstract-level description was checked. Previous uniform-noise complete-bipartite allocation is close: the \(\rho=1\) star case is not independently claimed as novel. No checked reference implies the exact two-parameter variance-ratio phase diagram, the tangency at \(B_*(m)\), or its large-star asymptotic pair. An equivalence buried in broader A-optimal-design literature remains possible, so novelty is best-knowledge rather than exhaustive.

## Value — PASS

In a network with a single high-degree hub, it is not evident when to invest feedback at the hub rather than in redundant leaves, especially when noise intensities differ. The theorem classifies the optimizer for an infinite graph family and all noise ratios and budgets, including exactly how a support interval appears, collapses to one point, and disappears. The golden-ratio critical parameter, three-vertex example, and separated small-/large-budget scales provide structural design information beyond a generic convexity statement or another fixed-parameter computation. The proof identifies why increased budget can both suppress and restore hub feedback.

## Limitations and comparison

The result is confined to unit-edge stars, one noise intensity at the hub and a common intensity at leaves, and linear pinning costs. The interior optimizer is characterized by a unique root rather than a radical expression. General weighted A-optimal-design results, other unindexed network-control work, or a more complete version of an abstract-only source may contain equivalent consequences. Neither finite tests nor a negative literature search prove novelty. Full detail, references, and reproduction are in the result and verification files.

Self-review: passed. Independent audit: not yet performed.
