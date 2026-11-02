# Scientific review

## Correctness — PASS
The two-step expectation matrices follow by exhaustive expansion of the four with-replacement and two without-replacement products. The difference factors through \(P+Q\), with two explicit orthogonal eigenvectors and eigenvalues. Strict signs, the equality line, and the phase transition follow directly. Two separate contraction arguments establish convergence of both schemes over repeated uses, without conflating finite-step expectation with infinite-time performance. A standard-library verifier reproduces the rational identities and a strict reversal example exactly. The proof, not the finite test set, establishes all real-parameter quantifiers.

## Originality — PASS (qualified)
Han–Xie (arXiv:2410.01140) analyzes standard unrelaxed random reshuffling; Recht–Ré and Lai–Lim address general positive-semidefinite matrix-product comparisons, whereas overrelaxed row-update matrices have a negative eigenvalue for \(\alpha>1\). Ying et al. study stationary constant-stepsize stochastic-gradient behavior, while Safran–Shamir use commuting quadratic components and finite-epoch rate estimates. The closely related public two-row Kaczmarz result concerns **deterministic cyclic** worst-case norms, not the sampled two-update expected-error difference. No inspected claim supplies the sign-changing, angle-dependent eigenvalue classification. Older matrix inequalities may still contain an equivalent specialization, and independent priority review is pending.

## Value — PASS
An exact, sharp robustness frontier answers when a practically important sampling preference survives Kaczmarz overrelaxation. The result exhibits a reversal for two **individually convergent** methods and identifies precisely which initial-error directions experience it. This corrects the overbroad inference that eliminating repeated rows must improve every expected finite-horizon error and quantifies how row coherence moves the boundary. The scope is intentionally two rows and one epoch, not a purported universal many-row or long-horizon ranking.

## Scientific limits
No claim is made for higher row counts, inconsistent systems, noisy measurements, objective residual norms, or all future epochs. The lower-relaxation positive-comparison regime is not asserted as a new general principle. The priority judgment remains qualified by possible historical two-factor matrix-product formulations.

Self-review: passed. Independent audit: not yet performed.
