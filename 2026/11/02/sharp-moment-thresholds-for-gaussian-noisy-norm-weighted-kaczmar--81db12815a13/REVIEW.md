# Scientific review

## Correctness — PASS

For refreshed nondegenerate Gaussian candidate rows, the normalized importance-sampling rule makes the exact \(q\)-moment of the affine projection innovation the integral of \(\sum_i |b_i|^q r_i^{\beta-q}/\sum_j r_j^\beta\). The proof separately checks the singular selected-row face and simultaneous all-row collapse; together they give the strict cutoff \(q<\min\{md,d+\beta\}\), with endpoint divergence. A uniform expected-contraction argument supplies the invariant law and its same sharp cutoff, including the one-dimensional exact-reset case. Gamma/Dirichlet factorization and pathwise projection orthogonality give the centered exact second-moment law. The standalone verifier passed its independent computations. Simulations are corroboration only, not infinite-dimensional proof.

## Originality — PASS (qualified)

The sampled projection and importance weighting are established in Needell–Srebro–Ward (arXiv:1310.5715); noisy-matrix Kaczmarz is established in Bergou et al. (arXiv:2308.16904). The latter's Theorem 5 conditions on a fixed perturbed matrix, whereas the new claim classifies **unconditional** every-order moments for a fresh Gaussian coefficient matrix per iteration. Anderson et al. (arXiv:2511.20877) concern higher moments of homogeneous error maps on fixed consistent systems, not singular affine innovations. Results for subspace-constrained Kaczmarz (arXiv:2309.04889) are also distinguished. Related records and precise implication variants were searched; none identified coverage. Prior inverse-Gamma, Dirichlet and random contraction principles are credited. Equivalent earlier affine-random-projection analyses may exist and independent priority checking remains outstanding.

## Value — PASS

The theorem provides an exact, reproducible diagnostic for finite variance, higher-order concentration moments and stationary error of a noisy row-action algorithm. Changing selection from uniform to the classical squared-norm weighting changes the variance requirement from \(d>2\) to \(md>2\), but cannot remove the all-row collapse obstruction or the next higher-moment threshold. The exact equilibrium mean-square floor is new method-specific quantitative information with direct interpretation, not just a numerical experiment.

## Scope and residual risks

This is an online, independently re-observed Gaussian coefficient model; one frozen noisy matrix is not covered. No optimization accuracy guarantee for a fixed true system is asserted. No invariant tail constant is derived. Scientific review was performed on the stated argument, not by an independent authority.

Self-review: passed. Independent audit: not yet performed.
