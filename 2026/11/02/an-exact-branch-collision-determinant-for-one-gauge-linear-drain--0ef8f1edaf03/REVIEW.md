# Review of the one-gauge drainage-tree determinant

## Correctness

**PASS.** The model uses known, strictly positive depletion and transfer rates on a topologically ordered rooted tree, with a zero-input linear differential equation. The full formula is derived from exact resolvent-path numerators, a unit-triangular change from outlet derivative jets to numerator coefficients, and a leaf-deletion determinant recursion. The same proof handles rate equality, arbitrary topology, and the one-store boundary. Cayley–Hamilton proves that singularity gives indistinguishable complete outlet trajectories, including distinct positive initial stores. Exact symbolic and rational checks substantiate, but do not replace, this proof.

## Originality

**PASS within accessible comparisons; historical priority remains provisional.** The quantitative all-tree determinant factors were not located in the targeted literature and published-result searches. Nash's series-reservoir model and Pan–Wood's inverse-routing model motivate the question but do not give this exact factorization. Older compartmental observability results include structural criteria and treatment of repeated eigenvalues; the Fagarasan–DiStefano (1986) generalized-tree analysis is especially plausible prior coverage of the qualitative observability criterion. Its full paper could not be read, so this is a material residual priority risk. The asserted additional result is the explicit determinant polynomial, not merely the observation that generic rates are observable.

## Value

**PASS.** A single outlet gauge is a natural monitoring bottleneck in branching drainage networks. The all-network-size product isolates precisely which timescale collisions erase independent stored-volume information, while distinguishing branch collisions from harmless repeated rates in a series. It also exposes algebraic sensitivity to nearly equal branch rates and identifies the minimum exact output-derivative count. The theorem is an idealized structural result, not a noise-robust hydrological inversion procedure.

## Limits and closest literature

Only known-coefficient passive linear routing after inputs cease is analyzed. Other source terms, unknown routing rates, stochastic errors, nonlinear retention, and numerical conditioning are outside the theorem. Closest literature: Nash (1957), Pan and Wood (2013), Cobelli et al. (1979), and Fagarasan and DiStefano (1986). The last work was accessible only by abstract. The result has not undergone independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
