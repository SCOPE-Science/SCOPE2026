# Independent mathematical audit

## correctness

PASS

The complete-graph race at k≥2 gives singleton probability q_k=2ε/(k−1+2ε), with a deterministic final singleton at k=1. The decreasing vacancy path cannot skip both members of {2j,2j−1}; the first member visited is selected using only uniforms in higher states. Its uniform is fresh, so the shared-threshold comparison indicators with probabilities ε/j are independent. Subtracting the thresholds and summing gives first-visit error at most 2ε(ζ(2)−1). A second voluntary monomer in a pair contributes at most q_{2j}q_{2j−1}; summation gives at most 4ε²(1−log 2). The initial unpaired odd state and vacancy two contribute at most (5/2)ε together. Adding the Bernoulli-to-Poisson error ≤2ε²(ζ(2)−1), the coefficient after division by ε is at most 4.420 for ε≤1/4. Parity repairs the voluntary count pathwise and deterministic pushforward contracts total variation. The harmonic sum, Poisson mean coupling and a rounding error of at most one give the critical window, PGFs, parity-minimal regime and CLT. For convergence of the actual means, total variation alone is insufficient, but the same uniforms give K_n^{mon}≤1+Σ_{k=2}^n 1{U_k≤q_k}; the independent sum has mean bounded by 2εH_{n−1} and bounded second moment in the critical window. This gives uniform integrability and justifies the stated mean limits. Vertex permutation symmetry yields the uniform label set conditional on every positive-probability count. Frozen exact and numerical tests were inspected, not rerun; the uniform 5ε bound follows analytically.

## originality

PASS

Best of current knowledge for the irreversible terminal count and its uniform upward-rounded Poisson approximation. Published kinetic and equilibrium results, exact complete-graph catalogue results, and same-date weak-rate Poisson phenomena were compared at their model and observable level. None of the inspected results states or was shown to imply this bound.

## value

PASS

The terminal monomer count is intrinsic to the competitive irreversible process. The uniform error across n isolates a genuinely different parity mechanism from conditioning and identifies the logarithmic crossover (including its zero/one probabilities) and both adjacent regimes. The complete graph is a useful mean-field kinetic case rather than a reparametrization of Gibbs matching fluctuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
