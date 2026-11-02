# Scientific review

## Correctness — PASS

The claim gives a complete all-size block-matrix factorization for degree-weighted DeGroot learning on cones over any finite regular base. The hub–constant subspace has eigenvalues \(1,-p\), while the peripheral zero-sum subspace inherits the remaining adjacency eigenvalues. Detailed balance proves an exact weighted-\(L^2\) contraction rate. Independent equal-variance errors produce the stated stationary variance; derivative and piecewise-affine comparison prove unique optima and the complete Pareto interval. The regular adjacency trace and disconnected/bipartite eigenvalue criteria justify all endpoint inequalities. The supplied checker passed 145 exact algebraic instances; none substitutes for the symbolic general proof.

## Originality — PASS, with residual literature risk

The inspected originating paper [1] already defines the degree-weighted DeGroot rule and derives general stationary influence, reversibility and spectral control. Its stochastic-block-model speed formulas and comparative statics do not state the arbitrary finite regular-base cone spectrum, exact nondominated parameter interval or unbounded variance-penalty law. The windmill study [2] computes the unweighted walk's Kemeny constant and related spectrum, not the optimally biased speed–variance frontier. Generic fastest-mixing work [3] optimizes a different transition family. Santini [4] studies target-degree power bias in Barabási–Albert networks but, on the accessible abstract, considers exploration speed rather than this exact spectral learning/variance problem; the article full text was unavailable. Search coverage included degree-biased random walks, friendship/windmill graphs, cone spectra and Pareto optimization. The full text of Santini [4] could not be inspected; an institutional retrieval attempt could not proceed without a network connection. A specialist exact result not identified in the inspected literature could still imply the claim; this is a remaining bibliographic priority risk, not a proven absence of coverage.

## Value — PASS

The contribution goes beyond a computed eigenvalue: it establishes the complete two-objective efficiency frontier for a natural infinite, topology-variable graph family. It identifies opposite-sign optima for statistical wisdom and convergence speed and shows an asymptotically unbounded \(\Theta(N)\) loss in estimation accuracy when speed is optimized on standard network families. This gives a mathematically motivated boundary for choosing popularity bias in repeated social learning.

## Sources and limitations

[1] Cheng et al., *Degree-Weighted Social Learning*, arXiv:2311.07010, especially Proposition 1, Section 4 and Appendix C (https://arxiv.org/html/2311.07010v3).

[2] Kooij and Dubbeldam (2020), *Kemeny's constant for several families of graphs and real-world networks*, https://doi.org/10.1016/j.dam.2020.05.033 .

[3] Olesker-Taylor and Zanetti, *Geometric bounds on the fastest mixing Markov chain*, arXiv:2111.05816.

[4] Simone Santini (2025), *Popularity-driven random walks on a class of scale-free graphs*, https://doi.org/10.1103/PhysRevE.111.054303 (abstract inspected; full text inaccessible).

The theorem assumes a regular base, one universal hub, a common degree exponent, a loopless linear averaging rule, and independent equal-variance unbiased initial signals. The reported efficiency criterion concerns long-run variance versus weighted-\(L^2\) contraction, not every possible social-learning loss. Independent publication-priority verification and external audit have not occurred.

Self-review: passed. Independent audit: not yet performed.
