# Scientific review: Klein-quartic flex-tangent intersections

## Correctness — PASS

The point list is the explicit complete cyclotomic list of Fisher (2001) and is checked against both the quartic and its Hessian by exact arithmetic. The exact coefficient ring is \(\mathbb Z[\zeta_7]\); the 21 nonrational tangent coefficient vectors are all divisible by \(7\), and dividing by that factor is harmless away from characteristic seven. The complete 2024-triple norm census finds only the prime divisors two and seven, so its all-prime nonconcurrency assertion is proven, not extrapolated from examples. Smoothness follows from the determinant-28 gradient system, and Bézout ensures that the 24 distinct smooth Hessian intersections exhaust the inflection locus. The Galois fixed-pair counts, orbit decomposition and finite-prime formula are verified by independently enumerating projective Galois permutations. The standalone verifier was executed successfully.

## Originality — PASS, with historical-computation risk

Fisher's modular-cusp description and the splitting field of the 24 flex points are prior art; they are not treated as new. Pacini–Testa (arXiv:1711.05776, Example 1.9) give the 24-point inflection scheme in the dual plane, which does not assert the absence of any collinear triple of its points or calculate Galois orbits of pair intersections. Pokora–Roé (arXiv:1803.06411) study a different, 21-line Klein arrangement; its 24-point count is of flex contact points, not intersections of 24 flex tangent lines. Dimca et al. (arXiv:2301.01117) mention the ordinary Klein flex count without classifying the tangent arrangement. Relevant exact-phrase searches and the public mathematical-results index disclosed no logically equivalent or stronger incidence-and-arithmetic classification, but cannot establish novelty absolutely. Elkies' historical survey could be read only at the abstract/metadata level in the accessible interface; this is noted as residual risk.

## Value — PASS

The 24 inflection lines are the intrinsic ramification-line configuration of a canonical, exceptionally symmetric genus-three curve. That **all** their pairwise intersections remain ordinary in **every** good prime characteristic despite their cyclotomic coordinates is a structural, all-prime incidence theorem, not a generic-position assumption or a small finite-field census. The exact 276-point Galois orbit profile and three rational-point regimes are complete natural arithmetic invariants of this geometric configuration; they are not entailed by the source's count of flexes. The result supplies a reusable arithmetic benchmark for comparing line configurations and their reductions.

## Limitations and closest literature

The result is model-specific and restricted to primes at least five different from seven. It does not establish external novelty certification, reconstruct an arbitrary quartic, or classify special-characteristic flex schemes. The closest publications are Fisher (2001), Pacini–Testa (2018), Pokora–Roé (2018), and Dimca–Ilardi–Pokora–Sticlaru (2023). A historical survey by Elkies (1999) remains an incomplete full-text comparison.

Self-review: passed. Independent audit: not yet performed.
