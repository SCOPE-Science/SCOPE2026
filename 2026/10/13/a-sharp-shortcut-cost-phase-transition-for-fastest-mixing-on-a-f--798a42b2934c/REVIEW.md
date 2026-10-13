# Scientific review: sharp four-cycle mixing-rate allocation

## Correctness — PASS

The statement is a complete, normalized optimization problem over four nonnegative edge rates and a positive relative cost. For \(0<t\le9\), two explicit orthogonal test vectors and nonnegative Rayleigh multipliers express the entire rate budget as a weighted sum of energies; their norms yield the global ceiling \(4/(t+2\sqrt t+5)\). The displayed feasible rates meet it, with the trace yielding an additional strictly larger nonzero eigenvalue. Strict positivity of both Rayleigh multipliers when \(t<9\) forces two exact eigenvector equations, giving uniqueness. For \(t\ge9\), a fixed vector yields the bound \(1/5-(t-9)q/5\). Equality gives the unique exterior solution, and at \(t=9\) gives precisely the affine family whose remaining two eigenvalues impose \(0\le q\le1/15\). Boundary cases and spectral multiplicities are proved analytically. The independent exact-rational characteristic-polynomial checks supplement the proof; they are not treated as exhaustive tests over real parameters.

## Originality — PASS with residual risk

Sun, Boyd, Xiao, and Diaconis (2006), §§5.2–5.3, explicitly solve arbitrary-cost **paths** and equal-cost **cycles**, and formulate a general SDP for rate optimization; their only stated general arbitrary-cost cycle result concerns two-dimensional optimal embeddings. Those results cover the single equal-cost point of this theorem but do not state the entire heterogeneous-cost formula, threshold \(t=9\), or the full critical optimizer segment. Boyd et al. (2004) concern discrete-time randomized gossip. Shakeri et al. (arXiv:1510.06785) optimize interlayer weights with fixed underlying layers and do not allocate four freely varying cycle rates with a heterogeneously priced edge. Targeted searches over algebraic-connectivity/cycle-cost terminology found no matching formulation. Since equation-level equivalences can be hidden in older eigenvalue-optimization sources, independent literature review could still identify prior coverage; the searches do not prove novelty by themselves.

## Value — PASS

A natural, nontrivial budgeted edge-activation question has an exact policy: use a costly shortcut strictly below price ratio nine, delete it strictly above nine, and expect continuum nonuniqueness exactly at the boundary. The result also explains when the mixing eigenvalue is double. These distinctions supply a directly usable resource-allocation rule and a testable boundary case for spectral optimization, beyond a numerical SDP solve. The four-cycle is a small, natural benchmark with a removable shortcut and a connected spanning path; its one-cost-parameter structure is motivated rather than an arbitrary parameter slice. It is a limited special-family classification, not a claim of a generic algorithm or a general large-graph theorem.

## Closest literature and limitations

1. Jun Sun, Stephen Boyd, Lin Xiao, Persi Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), §§1, 5.2–5.3, doi:10.1137/S0036144504443821.
2. Stephen Boyd, Arpita Ghosh, Balaji Prabhakar, Devavrat Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, IEEE CDC 2004.
3. Heman Shakeri et al., *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:1510.06785, especially its problem formulation with fixed network layers.

The theorem excludes asymmetric generators, cycles of other lengths, and arbitrary four-edge cost vectors. Prior-special-case risk remains, and the result has not received independent validation.

Self-review: passed. Independent audit: not yet performed.
