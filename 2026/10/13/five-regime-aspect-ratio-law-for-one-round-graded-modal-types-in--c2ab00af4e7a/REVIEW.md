# Self-review

## Correctness — PASS

The theorem fixes both the Bernoulli parameter and polynomial aspect exponent, and distinguishes convergence in probability from identity for individual matrices. The exact depth-one signature is \((X_{ij},D_i,E_j)\); both degree counts can be tested by finite graded thresholds, and all depth-one formulas factor through that triple. Binomial degree-alphabet sizes are derived in three regimes: sparse samples, critical Gaussian occupancy, and polynomially dense occupation with a moderate-deviation boundary. For the saturation \(K_1\sim2RC\), the proof independently verifies that every row sees both colors at each degree in a central almost-complete column-degree interval when \(a<2\), and symmetrically when \(a\ge2\). The one-column exact distribution conditioned on a marked or unmarked entry is explicit; a polynomial-size union bound absorbs its exponentially small failure probability. The formulas at critical \(a=1/2\) and \(a=2\) correctly replace one dense-occupancy factor by the nontrivial Gaussian integral. Multiplying the two degree-alphabet limits yields all five constants. Direct graded-formula evaluation against the signature on 9,418 small matrices, nine exact critical occupancy expectations, and 32 random rectangular sanity checks corroborate the semantic and numerical steps. They do not prove the asymptotic theorem independently.

## Originality — PASS (preliminary, same-model)

The complete inspected primary sources establish counting bisimulation, graded multimodal type equivalence, and bipartite degree-sequence enumeration, but do not state a quantitative first-round random-grid type count, the five fixed polynomial-aspect regimes, or the critical Gaussian occupancy constants. Closest existing findings concern qualitative depth-two random square-grid separation, worst-case sparse-marking separation, or ordinary rather than graded modal generation; none implies this limit. Dedicated equivalent-phrase, degree-pair-occupancy, aspect-ratio and counting-message-passing searches of mathematical research literature and records returned no equivalent claim. Both elementary binomial occupancy limits and modal graded types are prior tools and are **not** individually claimed as discoveries. There remains a genuine risk of an implicit earlier treatment in random bipartite color refinement or joint degree-pair histograms.

## Mathematical value — PASS

Quantifying the first-round expressivity capacity of counting-modal observations is a substantive refinement of qualitative early-versus-late separability. The saturation \(K_1/(2RC)\to1\) is a structural result about dependent row/column degree-pairs with both atomic colors. It yields five different growth laws, two sharp aspect-ratio transitions, and new critical Gaussian constants, with the square law \(8p(1-p)n\log n\) as a transparent example. It simultaneously determines the leading base-two logarithm of the definable Boolean algebra's size. These give natural complexity benchmarks for finite graded-modal type systems, rather than an arbitrary small finite census.

## Limits and review status

The statement is restricted to fixed density and fixed exponent, an independent-entry model, and unrestricted finite counting thresholds at modal depth one. Other scalings and fluctuation laws are not addressed. Exhaustive finite tests supplement rather than certify analytic limits. A separate mathematical and historical originality audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
