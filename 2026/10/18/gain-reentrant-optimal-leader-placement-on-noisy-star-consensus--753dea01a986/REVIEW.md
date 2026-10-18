# Review: Gain-reentrant optimal leader placement on noisy star consensus networks

## Correctness — PASS

The finite-gain OU covariance equals \(A_S^{-1}/2\), because the graph-plus-pinning quadratic form is positive definite for every nonempty leader set and the driving covariance is identity. The proof explicitly separates the hub and independent leaves, computes both orbit traces by a Schur complement, and proves that their difference has the stated rational numerator and strictly positive denominator. The symmetry argument covers **every** legal leader set. Maximizing \(\kappa/(1+\kappa)^2\) and solving its level sets gives the two reciprocal gains, the exact tie cases, and the first witness. Exact-rational Gauss–Jordan verification passes 1,455 regression cases, including all three-leader subsets on seven vertices. Finite tests do not prove the universal result; the algebra does.

## Originality — PASS, with residual risk

Lin–Fardad–Jovanović (arXiv:1302.0450) formulated the identical inverse-pinned-Laplacian variance **objective** for general networks; this background is fully acknowledged, and their algorithmic bounds do not state the proposed star classification. Fitch–Leonard (arXiv:1407.1569) explicitly treat one/two noisy leaders or arbitrarily many noise-free leaders, not three or more noisy star leaders. Patterson–Yi–Zhang (arXiv:1708.06873) analyze noisy-leader cycles and noise-free trees in the inspected specializations. Liu et al. (arXiv:1804.10818) provide a star result for the **smallest eigenvalue of a grounded Laplacian**, not a finite-gain trace inverse. Searches for the exact star/variance/gain formulation and close primary-literature comparisons found no dominating specialization. Historical priority cannot be certified; a latent equivalent star calculation remains a residual risk.

## Value — PASS

The theorem gives a closed-form global choice of leader orbit for **every** star order, finite homogeneous gain, and leader count. The strict reentrance is a substantive design distinction: in the seven-node, three-leader example, raising feedback gain first makes the center *worse* to pin, then makes it optimal again. Reciprocal algebraic switch thresholds and an exact smallest witness identify a natural boundary for finite-gain network control. The result does not purport to solve heterogeneous gains, nonstar graphs, or other objectives.

Self-review: passed. Independent audit: not yet performed.
