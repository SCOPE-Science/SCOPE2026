# Scientific review: clique-cycle joins

## Correctness — PASS

The feasible invariant transition matrices have three edge-orbit probabilities, and convex averaging guarantees that an invariant global optimizer exists. The proof checks all three nonstationary spectral blocks: hub contrasts, class-constant contrast, and rim Fourier characters. It minimizes the two extreme rim modes exactly, proves that their balancing probability satisfies the stochastic constraints, and reduces optimization to the intersection of two one-variable spectral bounds. The complete interval of optimal hub-clique weights follows from the remaining eigenvalue inequality. The exact saturation threshold is proved using a parity-sensitive formula for the extreme cycle Laplacian eigenvalues and elementary trigonometric bounds. Numerical comparisons with independently assembled full matrices and linear programs support but do not replace the infinite-domain proof.

## Originality — PASS, qualified

The single-hub wheel is solved explicitly in Boyd, Diaconis, Parrilo and Xiao (2009), Section 5.4.3, and is explicitly excluded from the new domain. The 2004 foundational article gives general convex/SDP formulations, not the complete all-size formulas for a clique of at least two hubs joined to a cycle. The new hub-contrast eigenvalue, exact set of invariant optimizers, and two-regime integer saturation boundary are not supplied by the inspected closest primary work. Search comparisons with mathematical records and other graph descriptions found no dominating exact statement. Residual risk: less easily indexed generalized-wheel formulas or older unpublished technical treatments may overlap. Search failure alone is not a novelty certificate.

## Value — PASS

An all-parameter optimum with edge probabilities and convergence rate provides a natural quantitative comparison for networks with an interconnected set of hubs and a ring of peripheral states. Unlike the established one-hub wheel, the multi-hub optimum may leave the hub-to-rim transition budget unused, with a sharp \(2r+1\) versus \(2r+2\) activation threshold. The optimizer interval also identifies precisely when within-hub transitions are permitted or forced. This is a structural phase classification of a natural graph family rather than an arbitrary fixed-size numerical instance.

## Scope and residual risks

The theorem classifies global optimum value and all symmetry-invariant optimal matrices, not all nonsymmetric optimizers. The Markov chain may put probability zero on allowed edges. Other measures of mixing and nonuniform stationary laws are outside the claim. The technical-report version preceding the dated arXiv v1 is listed only to month-level precision; no invented day is assigned to it. An independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
