# Review of exact first absorption on a finite quantum path

## Correctness — PASS

The stated claim includes the full integrated survival operator, all localized-state means and rate optima. The Hamiltonian, jump normalization, generator and boundary conditions are specified; strictly negative generator spectral real parts ensure certain absorption and Lyapunov uniqueness. An entrywise finite-difference calculation verifies every case of the closed kernel. Two implementations passed 39 exact rational Lyapunov residual tests and 33 numerical solves over independent parameters. Risks: no implications for nonuniform or infinite chains; finite tests alone are not an all-size proof.

## Originality — PASS within checked sources

Varbanov–Krovi–Brun (2008, arXiv:0803.3446) address a distinct Poisson-measured protocol and short-path examples. Chia–Paterek–Kwek (arXiv:1608.05510) give a powerful **general** jump-moment superoperator inversion which formally represents this observable, but their inspected results do not perform the all-size homogeneous-path inversion or derive its two-term rate polynomial and size-independent minimizer. Riberi (arXiv:2605.08056) solves the autonomous boundary-loss problem on the semi-infinite chain rather than a finite reflected path. The nearest inspected mathematical records concern different graphs or detection schemes. Residual risk: a path-specific formula could exist in differently indexed physics literature; the Ranjith–Kumar (2013) paper was compared only at abstract level. Novelty cannot be established from unsuccessful searches alone.

## Mathematical value — PASS

The exact entire matrix of mean absorption times and coherent-state cross terms makes a physically natural non-Hermitian hopping problem directly solvable without inversion of an increasingly large Liouvillian. The universal sitewise optimizer is independent of remote path length, while the uniform-source optimizer depends on length and converges to a different profile. This distinction is useful for controlled loss and transport benchmarking. A small-instance formula or a generic numerical inverse would not supply this uniform structural result.

Self-review: passed. Independent audit: not yet performed.
