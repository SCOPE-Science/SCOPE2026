# Scientific review: sharp crossover in random-direction parking

## Correctness

**PASS.** The exact finite last-preference formula is explicitly taken from the primary paper and algebraically expressed as an Abel--Cayley weight plus a signed cumulative term. The Borel total-progeny factorization, Stirling asymptotics, uniform endpoint bounds, central finite differences, compact-uniform interior convergence and boundary/interior decomposition yield the limiting total-variation functional. The elementary one-variable integral gives the crossover and the fixed-parameter constant. The separate executable exact checker confirms 704 finite identities and probes. Enumeration is not used to justify any infinite assertion.

## Originality

**PASS, with historical-priority uncertainty.** The most relevant source, Durmić et al. (2022), gives the exact law and only \(\Theta(n^{-1})\) and \(\Theta(n^{-1/2})\) total-variation rates. Its Theorems 3, 5 and 6 and the proofs were examined to distinguish this from sharp constants and a simultaneously tuned critical window. Bellin (2021) addresses classical parking marginals and multivariate bounds; Diaconis--Hicks (2016) treats classical parking probabilities; Harris--Ribeiro--Yin (2025) treats fewer-car models. Searches of mathematical records for critical windows, total-variation prefactors, aliases and Borel-derived distributions found no matching stronger result. A hidden derivation from published exact identities cannot be categorically excluded. No absence-of-results assertion rests on search results alone.

## Value

**PASS.** The original work exhibits a genuine change in convergence exponent when the directional bias equals zero, but does not resolve the parameter-dependent crossover. The result supplies a complete nondegenerate transition profile and both matching sharp constants. This gives a precise distinction between an exactly symmetric protocol, vanishing directional asymmetry, and fixed directional asymmetry. This finite-statistical limit is intrinsically motivated by the existing established open asymptotic gap; it is not an arbitrary numerical refinement.

## Closest literature and limits

Principal same-model source: Durmić, Han, Harris, Ribeiro and Yin, *Probabilistic Parking Functions*, arXiv:2211.00536 (2022), Theorems 3, 5, 6, and their proofs. Other sources: Diaconis--Hicks, arXiv:1611.09821 (2016); Bellin, arXiv:2108.08661 (2021); Tian--Treviño, *Generalizing Parking Functions with Randomness* (manuscript dated 2021); Harris--Ribeiro--Yin, arXiv:2502.00269 (2025). The new result has no claimed independent priority certification, multi-coordinate conclusion, fewer-car conclusion, or finite convergence-rate bound.

Self-review: passed. Independent audit: not yet performed.
