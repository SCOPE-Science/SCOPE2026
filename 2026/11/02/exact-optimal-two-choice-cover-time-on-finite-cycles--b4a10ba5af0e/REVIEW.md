# Scientific review: exact optimal two-choice cycle cover time

## Correctness (C): PASS
The visited set is always an arc. Immediately after each newly visited vertex the walk stands at an arc endpoint, and the dihedral symmetry ensures the optimal future value depends only on arc size. Therefore no strategy can improve any individual expected first-exit stage by sacrificing a different side. The stated Bellman equation reflects independent offers with replacement (probabilities \(3/4\) and \(1/4\)). Both explicit parity profiles are checked analytically against the interior recurrence, central symmetry, absorbing boundaries, strict boundary-to-center monotonicity and geometric-tail properness. Summing exit values over all phase sizes yields the parity formulas. The extracted checker independently passed 21,972 exact rational assertions. This finite verification is supporting evidence, not an infinite proof.

## Originality (O): PASS, with residual historical risk
The most relevant accessible full primary paper is Georgakopoulos et al., *The Power of Two Choices for Random Walks* (arXiv:1911.05170, first posted November 12, 2019), Sections 2 and 5: Theorem 5.3 proves only order \(\Theta(n)\) for discrete tori, while its general MDP treatment gives no explicit sharp finite-cycle formula. The full ITCS 2020 predecessor describes hitting/cover bounds and computational hardness, again without this exact expression. Avin–Krishnamachari's earlier empirical variant has a different policy and no identified exact optimal cycle result. Three scholarly-record searches for this claim and related formulations returned no equivalent result, while a separate prior mathematical result about complete bipartite choice walks has a different graph family and claim. No checked stronger theorem implies the exact cycle formula. Search and inspection are finite, and older literature using other terminology may conceivably cover it; definitive priority is not independently certified.

## Value (V): PASS
The underlying choice-walk problem is studied as a route to accelerate graph exploration. An exact globally optimal adaptive strategy and exact cover expectation for the canonical one-dimensional torus sharpen a published order-of-growth theorem. The sharp constant, exponentially small parity correction and comparison with quadratic ordinary-cycle cover time are natural finite-graph stochastic invariants, not an arbitrary parameter slice or a textbook normalization check.

## Limits and remaining risks
The scope is two offers with replacement, ordinary undirected cycles, the minimum of expected cover time, not full stochastic domination. The derivation uses no result requiring independent expert certification, and the present record is not an independent audit. The prior-work review, though including full relevant primary papers, does not exclude every possible historical equivalent.

Self-review: passed. Independent audit: not yet performed.
