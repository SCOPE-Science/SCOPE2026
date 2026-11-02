# Scientific review

## Correctness (C): PASS

For each \(K_{a,b}\), independent vertex-call Poisson splitting gives independent edge contact clocks of rate \(1/a+1/b\). The count-state transition rates and exponential first-infection decompositions then follow from the strong Markov property. Both one-seed initializations reach the same \((1,1)\) state, and their differing first-exponential rates give a strict stochastic order and the exact difference \((a-b)/(a+b)\) in expected times. In the fixed-width limit, a designated initially infected small-part vertex infects order \(a^{2/3}\) vertices rapidly, these infect the remaining fixed-sized part by time \(a^{-1/3}\) with exponentially high probability, and all but \(o_{\mathbb P}(a)\) of the large part remain uninfected at that time. Independent residual exponentials yield the centered Gumbel law; the pre-hub stage for all-large-part seeds contributes an independent limiting \(\operatorname{Exp}(k)\) delay. A second-moment domination and exponentially small bad-event bound justify the stated expectation convergence. A reproducible exact-rational recursion and Monte Carlo diagnostic program reports 526 checks. Numerical tests do not establish asymptotic statements; those have analytic proofs.

## Originality (O): PASS, qualified

Acan et al. (arXiv:1411.0948, 2014) give the independent-edge representation and an exact star analysis; the star case is known and expressly excluded from the claimed novelty. Leskelä and Ngo (arXiv:1806.09568, 2018) prove first-passage and flooding results on sparse configuration models with degree conditions that fail for a fixed-width complete biclique. Doerr and Kostrygin (arXiv:2303.11150, 2023) treat discrete-round epidemic spreading on different graph geometries. Their inspected results do not imply the complete-biclique, degree-normalized, all-fixed-seed Gumbel-versus-convolution classification or the exact finite one-seed source advantage. Searches under push-pull, asynchronous rumor spreading, first-passage percolation, Gumbel flooding, and complete-bipartite synonyms did not identify an equivalent theorem. Search absence is not proof of global priority; uninspected publications remain a residual risk. The one-seed finite ordering shares a general first-jump mechanism with the already-known star case; it is the combination with the new fixed-width limiting source penalty that carries the distinct contribution.

## Value (V): PASS

Complete bipartite core-periphery graphs are a natural testing ground for degree-normalized epidemic contact and strategic source placement. The result identifies a distribution-level, order-one seed-location penalty that survives even as the graph's total population diverges, plus a sharp universal Gumbel law whenever at least one seed lies in the high-degree core. The finite-size stochastic dominance is valid for all deadlines, not just the mean. This gives a usable deadline-dependent distinction between increasing the number of peripheral seeds and reaching the core. It is not a mere numerical table, relabeling, or renormalization of the sparse-graph logarithmic leading order.

## Residual risks and limitations

The studied asymptotic keeps the core width \(b\ge2\) and seed count \(k\) fixed; no theorem is claimed for growing core width or optimal arbitrary multi-seed placements at finite size. The exact star case predates the present work. Full historical priority awaits an independent literature audit, as does independent mathematical verification.

Self-review: passed. Independent audit: not yet performed.
