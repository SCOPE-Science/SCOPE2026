# Scientific review

## Correctness — PASS

The graph-Laplacian spectrum has one zero eigenvalue and two nonzero eigenvalues with sum twice the total conductance and product three times the sum of pairwise conductance products. This exact identity reduces the [2/2] rational matrix to an edgewise quadratic with a strictly positive denominator. The numerator has exactly one positive root precisely for a dominant edge. Strict positivity of each diagonal follows from positivity of the scalar [2/2] Padé function on the negative real axis. The two-state exception is explicit. The exact rational verification program corroborates the derivation on 30,485 checks. Risk: no independent external audit; the calculations do not purport to prove claims for arbitrary higher-dimensional networks.

## Originality — PASS, with residual risk

The closest accessible primary full text is the eight-page 2010 Zappavigna–Colaneri–Kirkland–Shorten article on Padé discretization of positive systems, together with its expanded 2012 study of general Metzler systems. Its Theorem 2 provides a sufficient step condition and its two-dimensional section gives a different classification. Those results do not supply the sharp conductance-dominance condition or the complete time interval for all connected weighted three-site symmetric Laplacians. Published studies of unweighted diffusion graphs address other graph families, while the dimension-eight minimality result concerns small-step positivity for arbitrary generators rather than large-step loss for symmetric ones. Search and implication comparisons appear in AUDIT.json. Risk: an equivalent criterion might appear in unindexed matrix-function or graph-Laplacian literature.

## Value — PASS

The network is the smallest reversible diffusion system in which a fourth-order Gauss endpoint can become nonpositive at large timesteps. The result completely separates unconditionally safe weighted three-site systems from those with an exact finite positivity horizon, identifies the unique negative edge, and quantifies the strong-edge scaling. It is a sharp design and timestep-selection rule—not an arbitrary numerical instance or mere recomputation of a known table. Scope is deliberately three vertices and completed-step positivity only.

Self-review: passed. Independent audit: not yet performed.
