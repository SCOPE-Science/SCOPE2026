# Self-review

## Correctness — PASS

The domain consists of distinct-spectrum symmetric positive-definite \(2\times2\) matrices, independent unnormalized Gaussian probes, integer even budgets, and exact one-node or two-node Lanczos inverse-trace quadrature. One-node and two-node outputs and matvec costs were reconstructed from the orthogonal Lanczos definition. The two angular integrals follow from a tangent substitution and differentiation of the exact first integral. Gaussian radial moments give the complete one-node bias and variance. Gaussian fourth moments give the deep variance. Substituting the square-root eigenvalue ratio yields the explicit MSE difference, whose derivative has strictly negative sign. The special budget bound and unique crossing then follow for every spectrum and each admissible budget. Exact algebra was checked symbolically; numerical diagnostics were separately replayed from the embedded package. The use of exact arithmetic excludes roundoff and breakdown at repeated eigenvalues. Finite experiments are not treated as proofs.

## Originality — PASS, with residual priority risk

Full-text comparisons examined the original SLQ inverse-trace algorithm and estimates (Ubaru–Chen–Saad 2017), Gaussian trace tails plus Lanczos (Cortinovis–Kressner 2020), uniform quadrature bounds (Chen–Trogdon–Ubaru 2022), and the optimized depth/sample error-budget theory for logdet (Li–Huang–Zhu 2023). The closest established resource-allocation work optimizes bounds for logdet rather than exact inverse-trace Gaussian MSE in a \(2\times2\) spectrum. Antithetic two-point logdet coupling and Hutch++ variance results do not imply the new depth/probe crossover. Meaningful overlap searches for equivalent formulations, stronger theorems, databases, and implication coverage did not reveal this exact statement; this is not a proof of absolute novelty. The main remaining risk is an unindexed exact-special-case formula or unpublished computation.

## Value — PASS

A central practical design choice in stochastic matrix-function estimation is whether a fixed matrix–vector-product budget should be used for additional probes or greater Krylov depth. These two choices have different sources of error: shallow quadrature retains systematic bias, while deeper quadrature reduces approximation bias but averages fewer random directions. This calculation gives the exact point where the tradeoff reverses, proves that the usual intuition that deeper is invariably superior is false at fixed cost, and gives a simple independent benchmark for allocation heuristics. It is not merely a numerical optimization of an arbitrary parameter: the two pure allocations are canonical SLQ choices. The \(2\times2\) scope prevents claims of large-dimensional optimality; deterministic two-query exact recovery is explicitly acknowledged.

## Remaining scientific limitations

This is a fully analytic two-dimensional benchmark, not an optimality theorem for general matrix-free algorithms. Probes must be independent standard Gaussians and \(B\) even. Eigenvalue multiplicity, finite precision, normalized-sphere conventions, different matrix functions, and non-pure allocations require separate analysis. A matching earlier specialized result may exist outside the searched sources; independent literature and mathematical audit remain to be performed.

Self-review: passed. Independent audit: not yet performed.
