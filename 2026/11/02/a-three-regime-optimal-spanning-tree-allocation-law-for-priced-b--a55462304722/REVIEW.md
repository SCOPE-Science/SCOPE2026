# Scientific review

**Correctness: PASS.** The proof covers the unrestricted edgewise budget, uniqueness, positivity of both optimal classes, normalized scalar stationarity and all three fixed-price asymptotic regimes. Its critical components are injectivity/strict concavity of reduced Laplacian log-det, Walsh-spectrum product, and binomial concentration with the zero-binomial cell separated in the expensive-price limit. An independent exact-determinant routine and scalar-root comparisons in `verify.py` completed 566 grouped checks. Finite checks are corroboration rather than proof of a limit.

**Originality: PASS with stated priority risk.** Martin–Reiner (2003) and Bernardi (2012) already give the weighted tree product, which is not claimed as new. Khosoussi et al. (2016) treat edge selection with given weights and discrete/cardinality constraints, including continuous relaxations, not the unrestricted paid-conductance allocation and its three dimension laws. Related priced-cube effective-resistance minimization has different scaling and does not imply the tree-entropy optimum. An equivalent unlocated D-optimal design theorem remains possible.

**Value: PASS.** The exact optimum for every cube dimension and fixed two-price pattern has a meaningful design consequence: the expensive-direction optimal ratio is of order dimension times an exponential, while the cheap-direction ratio is of order dimension. This characterizes a structural change between two natural purchases and cannot be inferred from the weighted tree product alone without nontrivial optimization and asymptotics.

**Scope limits.** No arbitrary per-edge pricing, robustness to pricing error, or control-energy claims. The finite-dimensional optimum is given by a unique implicit scalar root, not an elementary radical expression. Bibliographic coverage does not guarantee universal priority.

Self-review: passed. Independent audit: not yet performed.
