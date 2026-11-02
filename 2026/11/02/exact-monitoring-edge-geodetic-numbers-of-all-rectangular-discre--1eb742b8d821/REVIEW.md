# Scientific review: exact rectangular torus monitoring

## Correctness — PASS

For \(m,n\ge3\), the claimed monitoring number is proved by an established, directly inspected Cartesian-fiber characterization, the cycle three-point lower bound, and an explicit construction that saturates it for every \(5\le m\le n\). The floor-stretched columns have three selected vertices; row gaps are bounded by \(\lceil\lfloor(m-1)/3\rfloor n/m\rceil+1\), which is strictly less than half the row length except for two checked small cases with explicit replacement arrays. Exact integer arithmetic verifies the 36-case finite reduction, and independent edge-deletion BFS checks 1,318 edges. Finite verification is not substituted for the proof.

## Originality — PASS, subject to publication-priority uncertainty

The closest paper is Haslegrave's *Monitoring edge-geodetic sets: hardness and graph products* (arXiv:2210.08955, Theorem 4), which proves the square case, not the arbitrary rectangle. His general product lower bound is sharp for the new unequal-factor range but its matching upper bound is not established there. Dev and coauthors (arXiv:2210.03774) already determined the one-factor cycle values; those are used and credited. The 2024 product-networks paper (DOI:10.1080/17445760.2024.2301929) has an accessible abstract naming other products, but not an accessible full article for definitive exclusion. Searches did not identify a stronger exact rectangular classification; absence of a search hit is not novelty proof. An inaccessible plausible source and unindexed literature remain risks.

## Value — PASS

The result completes the exact monitoring number of every rectangular discrete torus and supplies an optimal pattern for arbitrarily unequal circumferences, extending a published square example to all aspect ratios. The constructive arithmetic bound shows why the Cartesian-product lower bound remains sharp even when simple square-circulant symmetry is unavailable. This has mathematical significance as an exact extremal graph-product family and as explicit fault-monitor placement. It makes no claims about strong products, twisted tori, or a classification of all optimum sets.

Self-review: passed. Independent audit: not yet performed.
