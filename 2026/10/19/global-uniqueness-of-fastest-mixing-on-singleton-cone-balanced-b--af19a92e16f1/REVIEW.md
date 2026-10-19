# Self-review

## Correctness — PASS
For all integers \(m\ge2\), automorphism averaging is legitimate because the feasible kernel polytope is convex and the centered operator norm is convex. The invariant spectrum follows from the constant, hub-contrast, class-contrast, and two zero-sum spaces. The elementary sharp two-constraint bound forces the invariant weights and proves exact attainment; the hub residual eigenvalue is within the bound precisely for the stated domain. For an arbitrary optimal kernel, positivity of \(\mu I-P+J\) and its averaged nullspace forces the entire \(2m-2\)-dimensional zero-sum space into its nullspace, which in turn forces equality of all periphery probabilities and global uniqueness. Independent exact rational spectra were computed for \(m=2,\ldots,9\), and 1,331 numerical full-matrix comparisons were run. No finite test is used as the infinite-family proof.

## Originality — PASS, with residual risk
The closest relevant full-text prior result is Boyd–Diaconis–Parrilo–Xiao, arXiv:0709.0955, Section 5.3.2, which explicitly gives the general complete-multipartite symmetric-block reduction. That prior result is acknowledged as stronger in graph scope for the *reduction*, so the mere eigenvalue calculation is not advanced as independently new machinery. It does not characterize **all**, potentially non-automorphism-invariant optimum kernels of the singleton-cone balanced bipartite graph. Jafarizadeh arXiv:1008.2588 studies equal-sized path/cycle partite arrays rather than the classes of sizes \(1,m,m\); the clique-lifted graph result (arXiv:2501.02421) concerns different substitutions. Searches of mathematical records, plausible aliases and accessible previous results did not identify a theorem entailing the global uniqueness. Because literature search is nonexhaustive, the risk of unindexed equivalent uniqueness remains.

## Value — PASS
The design question is whether the symmetry-averaged fastest-mixing Markov kernel on a hub-enhanced bipartite communication network is the only optimum or whether unequal local edge allocations can tie. This is not settled by generic symmetry reduction. The theorem answers it for every network size and shows every hub edge must be used at its capacity-saturating weight, while the exact gain from adding the hub is \(1/(6m)\) compared with the balanced bipartite graph. This full optimizer rigidity is a structural statement beyond re-solving the already-known reduced SDP.

## Limitations
The general multipartite spectral blocks were previously available and are not claimed as new. No independent mathematical audit or exhaustive literature census was conducted. Scope excludes \(m=1\), directed or nonsymmetric kernels, nonuniform stationary probabilities, other multipartite class sizes and different mixing criteria.

Self-review: passed. Independent audit: not yet performed.
