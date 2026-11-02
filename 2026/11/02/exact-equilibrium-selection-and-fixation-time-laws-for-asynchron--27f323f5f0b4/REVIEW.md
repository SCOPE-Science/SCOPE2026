# Self-review

## Correctness — PASS

The claim is for the unique best-shot binary response on every \(K_{a,b}\) with \(a,b\ge1\), arbitrary initial counts, a uniform one-vertex-with-replacement schedule, and scheduled-tick fixation time including null updates. Every profile with positive production on both sides loses initial producers only until one side is empty. The order of the first updates of all initially producing vertices is uniformly random, proving both the winning-side probabilities and exact suffix survivor weights. Independent rate-one Poisson clocks give the minimum-of-two-maximums commitment time \(H_i+H_j-H_{i+j}\); memorylessness gives conditional completion time \(H_{a-k}\) or \(H_{b-\ell}\), and Poisson event-rate conversion gives the expected scheduled-tick count. The empty and single-occupied-side boundaries are explicitly covered. The balanced asymptotic follows from the geometrically tight conditional survivor count and the harmonic-number expansion.

An exact-rational checker separately solves the Markov first-step equations and evaluates the closed expressions, agreeing for all 1936 count states across the 64 positive side-size pairs with \(1\le a,b\le8\); suffix weights are checked independently. These tests corroborate but cannot substitute for the all-size proof. The proof does not depend on a finite enumeration or inaccessible computation.

## Originality — PASS, with residual priority uncertainty

Klimm and Stahlberg (arXiv:2301.11849, first posted January 27, 2023), in the inspected full accessible text, establish existence and qualitative convergence for decreasing binary public-goods best responses, not the uniformly random scheduling and absorbing-law formulas. Dall'Asta, Pin and Ramezanpour (arXiv:1002.3572) define the same best-shot response and identify maximal-independent-set equilibria, but study a distinct socially controlled simulated-annealing mechanism. Ramazi, Riehl and Cao (DOI:10.1073/pnas.1610244113) show broad almost-sure anti-coordination convergence and bounded numbers of improving switches; a bound on actual switches does not determine the repeated-selection expected time or equilibrium-selection distribution. Jones, Pauls and Fu (DOI:10.1088/1367-2630/ac3319) study graph-coloring anti-coordination, a different local response.

The published random-order greedy independent-set laws on chain and threshold graphs were also inspected in their complete publicly accessible results: these assume an initially empty accepted set and one-pass random inspection. The chain-graph result therefore already covers the empty-start **selection distribution** on a biclique, which is not claimed as novel here. It does not imply the arbitrary nonempty initial active-profile law, the hypergeometric suffix distribution, or the expected stabilization time under repeated uniform updates. No directly implying result was found in targeted mathematical literature and indexed-results searches; residual risk remains that a specialist paper or a differently named stochastic scheduler derived the same law.

## Value — PASS

Equilibrium existence and convergence alone cannot explain selection between the efficient and inefficient public-goods equilibria or the number of uniformly scheduled update opportunities needed to reach one. The exact selection law identifies the initial producer-count ratio as the deciding statistic, independent of community sizes; the complete suffix distribution captures endogenous remaining production; and the exact expected time yields a sharp \(4m\log m\) leading term and linear correction from a fully producing balanced population. This is a natural quantitative decision-dynamics question on an infinite labeled network family, not an arbitrary finite census or a restatement of qualitative convergence.

## Scientific limitations and closest coverage

The theorem does not include nonuniform update rates, noisy responses, different thresholds, or general graphs. The strongest nearby coverage is the qualitative convergence theorem for decreasing public-goods patterns and the exact greedy selection law starting empty. Publication priority cannot be guaranteed by targeted searches alone. The full proof and a standalone, independently implementable exact-rational checker accompany the claim.

Self-review: passed. Independent audit: not yet performed.
