# Scientific review: finite-support period exclusions for rule 115

## Correctness — PASS

The universal spatial statement reduces exactly to a finite directed graph whose alphabet consists of temporal columns. The rule-115 truth table yields the degree-three Boolean polynomial used to define admissible graph edges. A time-periodic finite-support state produces a spatial path eventually equal to the homogeneous period-three background on both tails. Such a path can visit only the root's forward/reverse reachability intersection; conversely every rooted finite walk corresponds to a finite-support periodic state. The exact enumerations for periods 3, 6, 9 and 18 show that the period-9 and period-18 rooted components are precisely threefold temporal repetitions of their lower-period analogues. The attached independently implemented exact traversals agree, including every enumerated edge, and both nontrivial boundary examples pass their local-rule checks. The graph enumeration is exhaustive for the exact temporal periods, not a bounded spatial scan. Residual correctness risk: software implementations may share a misunderstood mathematical reduction; the full proof and elementary graph specifications make that reduction independently checkable.

## Originality — PASS

The full motivating article (arXiv:2606.13159v1, Sections 2–7 and its associated nine-page PDF) proves general finite-configuration periodicity and the divisibility-by-three requirement, but labels finite-support period 9 unachieved and period 18 unresolved. Neither observation implies the claimed impossibility. Searches for period spectra, finite configurations, the rule number, the authors, and temporal-graph equivalents located no public statement of these fixed-set equalities. General cellular-automaton and de Bruijn graph techniques are established prior methods, not claimed as new. Residual risk: an equivalent unpublished argument, unindexed later manuscript, or specialized period-spectrum theorem could already imply the result; absence from search results is not proof of priority.

## Mathematical value — PASS

The two natural periods are singled out by an explicit unresolved question and computational barrier in the source. The exact no-period result excludes whole families of finite-support orbits, and the rooted temporal-column compression replaces a purportedly impractical graph by 973 admissible time words and 27 root-component vertices at period 18. The fixed-set equalities are stronger than the mere nonexistence of primitive periods and are not an arbitrary small table entry. Their value is finite-support dynamical rigidity for one specific reversible rule; they do not settle the complete period spectrum.

## Closest literature and limitations

Formenti–Kamilya, *The Curious Case of Reversible Elementary Second Order Cellular Automaton 115*, arXiv:2606.13159v1 (2026), in particular Theorem 1, Lemma 1 and §7. Only this rule and these two questioned temporal periods are addressed. The exhaustive finite-state certificate is provided for reproduction, while independent scientific validation remains outstanding.

Same-model review: passed. Independent audit: not yet performed.
