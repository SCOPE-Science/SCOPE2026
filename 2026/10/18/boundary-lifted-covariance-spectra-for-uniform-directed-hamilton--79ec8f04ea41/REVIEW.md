# Scientific review: boundary-lifted covariance spectra

## Correctness — PASS

For every integer \(n\ge3\), contracting one or two prescribed compatible directed edges gives the exact joint inclusion probabilities \(1/n\) and \(1/[n(n-1)]\) for a random open path, or \(1/(n-1)\) and \(1/[(n-1)(n-2)]\) for a random directed cycle. Shared heads, shared tails, and reversals are incompatible. Summing the resulting covariance entries gives both operators displayed in RESULT.md. The mutually orthogonal constant, symmetric vertex-potential, antisymmetric vertex-potential, symmetric zero-divergence and antisymmetric zero-divergence spaces have dimensions summing to the entire \(n(n-1)\)-dimensional edge space. Each is explicitly an eigenspace; the spectral theorem proves both sharp weighted-path variance bounds and every equality condition. Rechecking boundary \(n=3\) produces a zero-dimensional symmetric zero-divergence subspace but no exception. The separate standard-library implementation exhaustively evaluates every open permutation and directed cycle through seven vertices with exact rational arithmetic, satisfying 47,656 checks. Neither finite computation nor the reported program output is used as a general proof.

## Originality — PASS, with explicit historical uncertainty

Diaconis, Evans, and Graham (2013), *Unseparated pairs and fixed points in random permutations*, study selected originally adjacent labels and a set-level fixed-point correspondence. Introduction and Sections 2 and 5 of their primary full text were examined; their contraction framework is compatible with, but does not state, the complete two-operator eigenspace decomposition, the loss of exactly \(2(n-1)\) modes upon closure, or the all-weight sharp path-variance optimizer classification. Sutcliffe, Solomon, and Edwards (2012) concern symmetric cyclic traveling-salesperson tours; only the abstract was accessible, so stronger indirect coverage cannot be excluded. Alhakim (2004) addresses overlapping blocks of IID symbols sampled with replacement, a distinct stochastic model. General quadratic-assignment second-moment theory may contain specializations of the underlying covariance entries. No inspected primary result establishes the complete spectral and extremal-weight statements; independent priority review is still required.

## Mathematical value — PASS

The full covariance spectrum for all directed path edges gives an exact noise geometry for arbitrary weighted Hamiltonian paths. The deterministic vertex-potential subspaces explain precisely why closing a path into a cycle annihilates \(2(n-1)\) fluctuation directions. The sharp worst-to-best variance ratio \(n+1\), together with attainable equality classes (vertex potentials versus divergence-free antisymmetric circulations), characterizes which signed edge weights are maximally and minimally sensitive to uniform vertex ordering. These are natural structural questions in permutation statistics and random tour costs, rather than isolated numerical evaluations.

## Limitations and residual risks

The result is purely second-order; no Gaussian limit or computational algorithm is asserted. The primary historical risk is possible derivability from general quadratic-assignment covariance identities or an inaccessible full symmetric-tour variance source. The reference paper's adjacency counting is acknowledged as prior, not claimed new. No external independent review is represented.

Self-review: passed. Independent audit: not yet performed.
