# Scientific review

## Correctness
**PASS.** The exact two-opportunity cycle decomposition yields Bernoulli gap steps and specifies both coalescence boundaries. The honest cycle clock has mean \(n/p+O(1)\) and variance \(O(n)\). Coupling to a lazy gambler's ruin walk shows that early terminal phases shift the hitting count by \(O(n)\) in expectation; Donsker's principle and a uniform law of large numbers supply the distributional limit. Brownian exit ODEs yield the Laplace transform, moments, and optimal bias. Exhaustive macro-case checks and a separate full-state finite Markov solution support the proof but cannot establish the infinite limit.

## Originality
**PASS against inspected accessible literature, with residual risk.** Gusev's arXiv:1404.6731 Section 3 studies the same Černý automaton with biased random input, but gives expected synchronization lengths rather than an all-gap Brownian first-exit law or its Laplace transform. Gonze--Jungers arXiv:1410.4034 studies a different game-theoretic probability function and deterministic triple rendezvous. The accessible finite-pair fair-input variance result does not determine an entire probability law. Targeted mathematical-record and primary-literature searches identified no equivalent claim; indexing gaps and alternate formulations remain possible.

## Mathematical value
**PASS.** The limiting first-passage law is a natural latency invariant of random-input automata, where higher fluctuations and upper quantiles are not determined by mean synchronization time. The diffusion constant \(p^2(1-p)\) provides a structural stochastic scaling theorem and identifies the same optimal input bias for every limiting quantile. This goes beyond numerical approximations or a routine parameter restriction.

## Sources and limits
Sources: V. V. Gusev, *Synchronizing automata with random inputs*, arXiv:1404.6731 (2014); F. Gonze and R. M. Jungers, *On the Synchronizing Probability Function and the Triple Rendezvous Time for Synchronizing Automata*, arXiv:1410.4034 (2014). Standard Donsker and gambler's ruin results supply known probabilistic ingredients. The theorem assumes fixed \(0<p<1\) and a normalized gap with limit inside \((0,1)\); it concerns pair coalescence only, with no finite-size convergence-rate claim.

Self-review: passed. Independent audit: not yet performed.
