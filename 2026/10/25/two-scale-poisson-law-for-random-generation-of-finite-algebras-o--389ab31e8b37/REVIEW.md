# Review of the two-scale Poisson generation theorem

## Correctness — PASS

The finite Boolean-filter representation decomposes every finite ADA into two- and three-element coordinates. Explicit crisp tests construct selectors for pairwise distinct generator words, with undefined values obtained only where present. Independent falling-factorial assignment counts follow. Collision factorial moments give Poisson(a²/2), missing-U words give Poisson(b), and ternary collisions vanish as O((3/4)^k). The standalone exhaustive checker reproduces twelve finite counts. Full generality follows from the written proof, not finite testing.

Boundary cases include \(k=0\), pure binary products, pure ternary products, and empty coordinate blocks. The proof establishes all asymptotic limits symbolically. The checker covers only twelve finite configurations. Nonuniform sampling is not claimed.

## Originality — PASS in inspected evidence

The 2026 Ledda--Graziani--Vergottini article supplies the representation, and Sipoş's 2023 posted normal-form theorem covers substantial deterministic expressivity. The exact factorial count is credited as an elementary bridge and not asserted to be new in isolation. Targeted literature and prior-finding semantic searches did not uncover the independent two-scale Poisson window or its random generation conclusion. Residual risks include older term-equivalent formulations of the same stochastic limit and unindexed literature; absence of matches is not a uniqueness proof.

The closest sources are Ledda--Graziani--Vergottini, DOI 10.1002/malq.70026, Theorems 6–7, and Sipoş, arXiv:2304.00288, Theorem 2.4. The first proves the structural representation; the second contains term-function normal forms that substantially anticipate the deterministic generating-count mechanism. Neither inspected article formulates the simultaneous birthday/missing-undefined Poisson law. This is a bounded evidence assessment, not an absolute priority guarantee.

## Value — PASS

The result answers a natural average-case generation question for recently unified three-valued algebraic semantics. It distinguishes the Boolean birthday obstruction from a qualitatively different ternary missing-undefined obstruction, identifies two competing exponential coordinate scales and the full nondegenerate limiting law. These features are useful in random generation, finite-model sampling and benchmark design beyond deterministic generator rank.

## Limits and risk

The newest source was inspected through its publisher-indexed full HTML content but not through a direct PDF file. An equivalent older stochastic theorem, particularly under term-equivalent algebraic language, remains possible. Only independent uniform generators in the specified finite variety are treated.

Self-review: passed. Independent audit: not yet performed.
