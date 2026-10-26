# Review of the sharp stale-batch safety frontier

## Correctness

PASS. The claim is explicitly for two independent normalized rows, independent with-replacement choices, and additive correction vectors all computed from a common snapshot. Conditioning on the current error gives the exact second-moment identity in RESULT.md. The only optimization is a two-by-two symmetric generalized Rayleigh quotient; its top eigenvector respects the maximal-residual ordering, including the tie and endpoint cases. This yields both a strict universal threshold and exact witnesses for failure at and above the threshold. The positive lower bound on weighted squared residuals proves uniform geometric mean-square convergence in the open safe interval. The full-greedy two-worker obstruction is exactly an orthogonal reflection off a union-of-lines exceptional set. The standalone verifier independently enumerates the finite draw distributions for rational systems.

## Originality

PASS, with acknowledged bibliographic uncertainty. Coleman's 2026 paper examines adaptive asynchronous Kaczmarz empirically, but does not give an exact shared-snapshot, two-row, mixture-dependent threshold. Moorman et al. (2020) provide parallel averaging and second-moment background, primarily for fixed distributions and probability-weight coupling; their stated bounds do not cover the optimized adaptive-mixture frontier and pure-greedy reflection trap. Gower et al. (2019) analyze one selected adaptive sketch per iteration, not several unaveraged commits from the same snapshot. Related published mathematical findings on cyclic two-row overrelaxation and greedy Kaczmarz residual spikes concern sequential iterations or different metrics. Searches checked aliases such as parallel randomized Kaczmarz, mini-batch stochastic projections, stale snapshots, max-distance sampling, collision, and coherent two-row relaxation. A more general unpublished theorem or an unnoticed implication in broader stochastic-gradient analyses remains a residual risk.

## Mathematical value

PASS. The motivating practical issue is the competition between aggressive residual selection and worker interference. This theorem supplies a sharp and interpretable robust relaxation rule and an exact design distinction: with two simultaneous full corrections, pure greed is generically a nonconvergent norm-preserving reflection, while every positive uniform-exploration component restores mean-square convergence. Its coherence- and worker-count dependence is mathematically motivated by the collision/interference geometry, rather than an arbitrary isolated constant. The claim concerns a clean controlled synchronization model, not arbitrary real-world asynchrony.

## Closest literature and limits

Primary comparisons: Coleman (2026), arXiv:2607.08313; Moorman, Tu, Molitor, and Needell (2020), arXiv:2002.04126; Gower, Molitor, Moorman, and Needell (2019), arXiv:1909.03604; Ferreira, Acebrón, and Monteiro (2024), DOI:10.1007/s11075-024-01945-2. Main mathematical limitations: two independent unit rows, identical pre-batch read, conditional with-replacement draws, and additive unaveraged corrections. Above-threshold one-step expected amplification does not imply eventual divergence. The theorem has not undergone independent audit.

Self-review: passed. Independent audit: not yet performed.
