# Scientific review of the finite-family EF1 minimax theorem

## Correctness — PASS

The argument distinguishes the two information states in the input family. Without an injective allocation of the common prefix, every short input has a zero EF1 score. With a unique initially empty agent, each other target creates a short-versus-long conflict: assigning its special good away from the empty agent loses on the short horizon, while assigning it to that agent gives at most a \(K^{-1}\) EF1 factor on the long horizon. The explicit opposite-horizon action choices achieve one exactly fair outcome in either case; they achieve both when the target equals the initially empty agent. This proves the arbitrary-distribution best-response identity.

The uniqueness argument is exact: expressing the formula through total target masses and within-target short/long imbalances yields two inequalities whose simultaneous equality characterizes the uniform law. The low-threshold construction checks all relevant directed pair comparisons. Exact-rational exhaustive verification of 90 weighted decision games with up to four agents, along with 280 separate equalizer cases, successfully corroborated the stated formulas. The verifier cannot establish the infinite-parameter theorem alone. The analytical argument does.

## Originality — PASS (with residual risk)

Chen and Long, arXiv:2609.23577, Section 4.2 and Theorem 4.3, introduce this input family and prove the upper bound \((n+1)/(2n)\) via a uniform short/long distribution. This is *not* claimed as new. Their theorem is an upper bound on unrestricted online allocations and does not prove that any randomized algorithm meets that bound on every input in their particular finite family. Nor does it give the exact response to arbitrary nonuniform priors, prove uniqueness of the least-favourable prior, or identify the abrupt \(K^{-1}\) threshold of this finite game. The new construction and optimization independently supply all these missing implications.

Neoh and Teh, arXiv:2609.05310, obtain general online-fairness impossibility and approximation results under different objectives and assumptions; its relevant abstract and introductory setting do not state this finite minimax classification. Multiple targeted searches of mathematical research records and published literature (including equivalent game-theoretic terms such as minimax, hard distribution, Yao tightness, and least-favourable prior) produced no mathematically matching record. This is evidence of a current gap, not a guarantee of global novelty. A differently formulated or unindexed treatment remains possible.

## Value — PASS

The paper's probabilistic impossibility bound is derived from a concrete finite adversarial distribution. The natural unresolved diagnostic is whether that distribution and finite input collection are genuinely extremal, or whether changing their weights could strengthen the obstruction. The theorem answers this precisely: the uniform law is uniquely optimal for the adversary, a simple online rule equalizes all inputs, and the finite game's feasibility jumps at a sharp factor threshold. This identifies exactly what the existing hardness certificate can—and cannot—prove, without claiming a new bound for the unrestricted online problem. The arbitrary-prior best-response equation is additionally a complete decision-theoretic description of the finite family rather than an isolated numeric example.

## Closest literature and limitations

1. T. Chen and J. Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, arXiv:2609.23577, 2026, especially Theorem 4.3, proof and Section 5. The prior upper bound and input family are explicitly credited.
2. T. Y. Neoh and N. Teh, *Closing Gaps in Online Fair Division*, arXiv:2609.05310, 2026; related global impossibility theory rather than an exact finite-game solution.

The classification concerns one specified \(2n\)-input family, not the unrestricted worst-case randomized EF1 guarantee. The full EF1 threshold, information assumptions, quantifiers, finite checks, and unproved extension boundaries appear in `RESULT.md` and `VERIFICATION.md`. No independent mathematical audit has taken place.

Self-review: passed. Independent audit: not yet performed.
