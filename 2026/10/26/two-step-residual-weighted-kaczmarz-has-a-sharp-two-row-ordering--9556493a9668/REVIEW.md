# Scientific review

## Correctness — PASS

The two-row identity \(F_{12}-F_{21}=c^2(d^2-a^2)\) and the monotonicity of the residual-power mixing weight establish universal two-step ordering. Uniform sampling can repeat a row, never improving upon taking the other row as its second projection. The three-row matrix has unit rows and determinant \(13/27\); exact rational projection gives the table, uniform expectation \(65572/6561\), and the rigorous finite-\(p\) lower bound \(\mathbb E_{40}\|e_2\|^2>21/2\). A standalone exact-arithmetic checker recomputes the certificates. The stochastic statement concerns only two steps, with the zero-residual termination convention explicitly fixed.

## Originality — PASS (best-knowledge, residual priority risk)

The strongest direct predecessor is Steinerberger (2020), which gives improvement of global geometric rate *bounds*, and one-step conditional progress, but does not establish exact finite-horizon stochastic dominance. Zhang et al. (2023) incorporate the same row probabilities into a Bregman/sparse method whose \(\lambda=0\) specialization is our setting; its results are also convergence-rate estimates. Nutini et al. (2016) treat greedy rules and multi-step graph-dependent rate bounds, not this exact ordering boundary or specific counterexample. Targeted research-record and literature searches found no implication covering both pieces. Independently unindexed or equivalent special-case results remain possible.

## Value — PASS

Choosing a power exponent to interpolate uniform and greedy sampling is central to these algorithms. The result shows the first row count at which better one-step selection can reverse the actual two-step expected error, directly distinguishing a rate bound from finite-horizon risk. It provides a small exact benchmark for theory and implementation, with no unsupported long-run, high-dimensional, or sparse-regularization claims.

Self-review: passed. Independent audit: not yet performed.
