# Scientific review: local de Bruijn factor covariances

## Correctness — PASS
The two indicator events prescribe four distinct edges of the order-two de Bruijn graph and two disjoint transitions through a common central vertex. Contraction gives an exact bijection of cyclic Euler tours; the BEST factorial ratio, directed Matrix-Tree cofactor and \(2\times2\) determinant lemma reconstruct the joint probability without probabilistic independence assumptions. Independent one-shortcut counting gives both marginals. Exhausting all injective equality-pattern types gives the four covariance formulae and all signs for every integer \(q\ge3\). Boundary alphabet sizes are addressed, and a standalone checker enumerates every cyclic tour at \(q=3,4\) and independently computes contracted cofactors through \(q=6\).

## Originality — PASS within examined evidence
The claim is the sharp *uniform covariance-sign classification*, not the joint factorial moment formula. Rødland (2006), Theorems 1 and 3, explicitly provides general joint-pattern counting and therefore subsumes raw joint probabilities; this prior coverage is acknowledged rather than presented as a novelty. Cowan (1991) provides marginal counts; Sawada and Gabrić (2025) provides the uniform sampling model. No inspected primary paper or searched research record states the sharp four-class sign transition at \(q=5\), the unique zero class there, or the exact negative-class changes at \(q=3,4\). General prior joint-count identities can be algebraically specialized, so potential earlier implicit derivation remains a material risk; the claim asserts that the all-alphabet sign synthesis is the contribution, not a new enumeration framework.

## Value — PASS
The sign of correlation determines whether observing one next-order motif increases or decreases the chance of seeing another, a relevant issue for coverage properties of sampled de Bruijn cycles. The sharp alphabet threshold and complete equality/negative-case classification expose a qualitative dependence transition across the entire family rather than reporting a single small computational count. The closed forms and independence class are usable directly without evaluating general high-dimensional pattern-count formulae.

## Sources and limits
Primary material inspected: Sawada–Gabrić (2025), arXiv:2510.16545, original full sixteen-page preprint, in particular the uniform-sampling theorem and algorithm; Rødland (2006), full eighteen-page article, especially its general Theorems 1 and 3 and determinant appendix; Cowan (1991), seven-page author-archived version, especially individual pattern expectations. Relevant indexed research-record hits treated as comparisons, not proof of uniqueness. Limits: only order-two cycles and the four-distinct-edge, common-center motif class; no independence or originality certification from another researcher.

Self-review: passed. Independent audit: not yet performed.
