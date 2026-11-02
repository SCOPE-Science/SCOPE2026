# Scientific review: exact terminal jamming laws

## Correctness (C): PASS

The exact finite law is supported by a direct competing-clock proof. The first accepted particle occupies one part with one species. Only two decisive outcomes are possible: the opposite species accepts inside that part, permanently excluding all other parts; or the same species accepts in another part, excluding the opposite species everywhere. The independently thinned Poisson streams give the conditional integral and finite binomial sums without independence assumptions between terminal occupancies. For fixed positive limiting part proportions, the rescaled first outside arrival time and bounded convergence yield the mixture weights. In the symmetric balanced bipartite case the binomial representation and a fourth-moment-controlled rational expansion give the coefficient \(3/8\) and the stated \(O(n^{-2})\) remainder.

The independent exact-rational state recursion in `check_jamming.py` matched 290 finite graph/parameter cases with 1,169 assertions. This computation checks implementations and corner cases but is not the proof of an all-size or asymptotic statement. Endpoints \(p\in\{0,1\}\) are treated separately; the finite formulas themselves require \(0<p<1\).

## Originality (O): PASS, with residual priority risk

The closest same-dynamics source is Martins, Dickman and Ziff, arXiv:2211.04622 (first posted 2022-11-09). Its full text studies one- and two-dimensional lattice adsorption, perturbative jamming coefficients, and percolation; its model agrees on repeated attempts and incompatible species but does not present a complete-multipartite terminal distribution, the dense-graph mixture, or the balanced \(3/(8n)\) correction. Dhara, van Leeuwaarden and Mukherjee (2016) study different threshold/frequency RSA rules on sparse Erdős–Rényi graphs. Krivelevich, Mészáros, Michaeli and Shikhelman study single-species, single-pass greedy independent sets. Equilibrium Widom–Rowlinson partition enumerators do not determine the irreversible history-dependent absorption probabilities. The actual comparisons concern stochastic rules, geometry, and implication strength, not mere title similarity.

Targeted searches of accessible mathematical research records and primary literature did not find an implication-equivalent terminal law. Neither the absence of a match nor the graph-family restriction proves priority. Broader historic work on exactly solvable irreversible multitype adsorption or competing nucleation processes could still cover this case; a published but only abstract-accessible early graph-RSA paper remains a lesser risk. Independent source-by-source historical review is still needed.

## Value (V): PASS

The result gives a complete probability law for a natural and entire dense graph family, rather than a small enumeration or a routine expected value. It identifies the only possible macroscopic jammed configurations, gives finite probabilities under arbitrary species bias, and shows that symmetric density has a strictly positive limiting variance even as the graph size tends to infinity. The sharp finite-size correction resolves the direction and first scale of the finite bias in the balanced benchmark. These facts provide an exactly solvable comparison geometry for studies of antagonistic adsorption and distinguish irreversible stochastic jamming from equilibrium occupancy counts.

## Scope and remaining risks

The theorem assumes independent per-site Poisson attempts with revisiting, no desorption, a complete multipartite graph, and two species. It does not characterize jamming on sparse lattices, graphs with missing cross-edges, or single-attempt colored random-order models. The first-order thermodynamic mixture fixes the number of parts and assumes positive limiting proportions; the second-order expression concerns only \(K_{n,n}\) at equal species rates. Correctness and novelty assessments are confined to the stated result and inspected evidence.

Self-review: passed. Independent audit: not yet performed.
