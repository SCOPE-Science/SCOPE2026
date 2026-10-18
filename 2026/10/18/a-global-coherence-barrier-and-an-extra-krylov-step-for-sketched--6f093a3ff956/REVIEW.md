# Self-review

## Correctness — PASS

The stated result is limited to positive equicorrelation kernels, the precise surrogate block matrices in the motivating source, and exact arithmetic. The normal matrix is \(h_0I+\eta\mathbf1\mathbf1^{\mathsf T}\). A direct decomposition into within-block contrasts, between-block contrasts, and the global constant vector gives the complete spectrum with multiplicities. A displayed positive-polynomial identity proves the nontrivial eigenvalue ordering for every allowed dimension and regularization. The unit-phase-block Rayleigh witness establishes the structural lower bound for arbitrary local SPD scaling, and the minimal-polynomial argument proves the exact-CG counts. The bundled checker passed 1,393 parameter/certificate checks and an exact-rational two-versus-three-step CG test. Numerical evidence supplements rather than substitutes for the analytic proof.

## Originality — PASS, qualified

The paper introducing the sketched block construction was inspected at its method definition and in the available block-PCG comparison/appendix excerpts, and its stated contributions are empirical and algorithmic rather than this exact compound-symmetry spectral theorem. Older work on optimally conditioned block matrices may already imply the abstract no-improvement lower bound; that broad lemma is not presented as an independently new result. Southworth and Olivier supply general two-block eigenvalue machinery and illustrate preconditioner iteration penalties but do not state this all-parameter BLOKS-specific spectral profile. The result assessed as new is the precise 2026 sketched-preconditioner three-eigenvalue identity, the equality of its condition number to the unpreconditioned normal matrix, and the sharp extra-exact-CG-step consequence for normalized kernel data. Database and literature searches did not identify this conjunction. This does not prove global novelty, and unavailable older full texts leave a nonzero bibliography risk.

## Mathematical value — PASS

Sketched block preconditioning is motivated by a memory-versus-iteration tradeoff. A normalized, Gaussian-kernel-realizable family for which *every* nontrivial partition loses all condition-number advantage is a structural stress test, not an arbitrary rescaling or numerical curiosity. The result quantifies how shared cross-block coherence defeats purely local approximations and isolates an exact-iteration penalty. It motivates comparing local preconditioning with low-rank global/coarse corrections. The theorem does not predict empirical performance on non-equicorrelated datasets.

The closest sources are Vitale et al. (arXiv:2610.13382v1), Kolotilina (2002), Shapiro (1985), Demmel (2023), and Southworth–Olivier (arXiv:2001.00711). The strongest residual risk is a general older spectral preconditioning identity whose specialization might subsume part of this calculation. Independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
