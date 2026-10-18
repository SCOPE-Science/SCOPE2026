# Scientific review: principal-angle phase transition for two-level boosting

## Correctness — PASS

For every real SPD two-eigenvalue system and equally ranked approximate subspace in the stated domain, the cosine-sine principal-angle decomposition produces two-by-two blocks with determinant \(\kappa\gamma\) and a trace monotone in squared principal angle. The largest angle supplies both global eigenvalue endpoints. Minimizing the trace normalized by its determinant yields the unique scalar boost; an exact discriminant identity gives the piecewise sharp condition number. The high-contrast boundary follows without extrapolating experiments. The supplied deterministic checker compares explicit matrices, the formulas, and the optimum on 50 configurations/300 boosts; tests alone are not a proof.

## Originality — PASS, qualified by residual bibliographic risk

The source result of Sun–Qi–Han–Xie (arXiv:2605.29304v1, inspected §§1, 3.2) studies *orthogonal constrained projection* in randomized iterations, not positive scalar projector boosting. Benanti–Han–Qin (arXiv:2601.20174v1, inspected §§4 and Appendix A) use multilevel coarse corrections and learned approximate subspaces, not this exact spectral tuning. Kahl–Rittich (arXiv:1209.1963, full text including Proposition 4.3 inspected) bound an effective condition number for singular deflated CG; this does not entail exact scalar boosted SPD extreme eigenvalues, the unique optimal boost, or the \(\pi/4\) cutoff. Helmberg (DOI 10.1007/s10107-023-01986-w, open full text Corollary 5 and Theorem 6 inspected) gives other low-rank Galerkin preconditioning bounds. The closest published result on stale-coordinate SOAP evaluates an *entrywise* adaptive normalization, not our inverse-projector multiplier. Successful database searches for principal-angle, spectral-boost, rank-one, and coarse-space aliases found no broader statement implying the claim. A 2014 paper on generic rank-one perturbation conditioning could not be read in full and remains a limitation of this originality conclusion.

## Value — PASS

Low-eigenmode boosting is natural for SPD iterative linear solvers, while approximate subspace angle is an accessible diagnostic. The theorem gives a complete, sharp, dimension-free finite-parameter answer, a switch at which boosting should cease, and an exact angle-versus-contrast accuracy requirement. It is not merely an isolated numerical example; it identifies the optimizer over an infinite family of noncommuting inverse preconditioners.

## Limitations and residual risk

The two-cluster spectrum is assumed *exactly*, the boost is scalar and noncontracting, and the resulting condition number is only a worst-case solver-performance proxy. The bibliographic coverage does not exclude unindexed or inaccessible equivalent statements; in particular, a potentially related 2014 rank-one-perturbation paper was not materially inspected. Scientific same-model acceptance is not independent validation.

Self-review: passed. Independent audit: not yet performed.
