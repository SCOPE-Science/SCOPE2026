# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

PASS.

The cancellation follows directly by coefficient matching between the three explicit triplet Fourier modes in the source's second-order emergent contribution and the corresponding first-order physical nonpairwise contribution. With eta = epsilon^2/(4a), the asymmetric coefficients require motif weights w_1232=w_12 w_23 and w_1323=w_13 w_32, while the symmetric coefficient requires w_1213=2 w_12 w_13. The three Fourier modes are distinct, so these are the coefficient-wise cancellation conditions for the prescribed global scale.

For the unweighted triangle, direct trigonometric simplification leaves a common pairwise-additive phase interaction H(phi). Linearization at synchrony gives lambda_sync=-3 H'(0). Circulant linearization at the three-oscillator splay state gives Re(lambda_splay)=-(3/2)[H'(2pi/3)+H'(-2pi/3)]. Substitution yields the same factor F(c)=4 a c+3 epsilon-2 epsilon c^2 with opposite signs and the exact relation lambda_sync=-2 Re(lambda_splay). The stated root and its location for 0<epsilon<4a follow from solving the quadratic in c=cos(rho).

A standalone symbolic verification reconstructs the retained phase field from the source expressions and checks both the pairwise residual identity and the stability relation exactly.

## Originality

PASS, to the best of our knowledge.

The primary source arXiv:2609.20632v1 was inspected in full-text HTML. It explicitly identifies the three triplet harmonics, their unequal motif coefficients, the engineered physical nonpairwise terms, and the scaling eta=epsilon^2/(4a). For its unweighted numerical design it sets all nonzero weights to one, which cancels the asymmetric contribution and one half of the symmetric contribution. The source then studies the movement of stability boundaries numerically. It does not state the 1:1:2 motif-weight choice, the pairwise-additive residual identity, or the exact sync–splay stability relation derived here.

Related literature was checked for equivalent coverage. Bick, Böhle and Kuehn (2024) derive higher-order phase reductions and analytic stability information for synchronized and splay states, including the uncanceled Stuart–Landau setting; those general and uncanceled formulas are excluded from the novelty claim. Namura, Muolo and Nakao (2026) design interaction functions that realize prescribed pairwise and higher-order Kuramoto harmonics for general limit-cycle oscillators; that general harmonic-realization principle is likewise excluded from the novelty claim.

Searches using the primary paper title and identifier together with cancellation, motif weights, triplet harmonics, synchrony, splay, and bistability did not locate a source-specific statement equivalent to the result here. The main residual risk is the recency of arXiv:2609.20632v1: immediate author revisions or discussions may not yet be indexed. No inaccessible paper was identified that specifically appears likely to contain this exact source-specific cancellation and stability-collapse statement.

## Value

PASS.

The result upgrades partial numerical coupling compensation to an exact second-order design criterion using no additional global coupling scale. More importantly, it shows that the exact coefficient choice has a qualitative dynamical consequence: the synchronized and splay states have opposite transverse stability signs controlled by one common factor, eliminating their local linear-stability overlap at the retained order. The remaining transition shift also isolates what the explicit triplet harmonics do not explain: pairwise-looking second-order corrections still move the threshold away from the first-order Kuramoto value.

## Sources checked

- R. Muolo, H. Nakao, C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1: https://arxiv.org/abs/2609.20632
- C. Bick, T. Böhle, C. Kuehn, *Higher-Order Network Interactions Through Phase Reduction for Oscillators with Phase-Dependent Amplitude*, Journal of Nonlinear Science 34, 77 (2024): https://doi.org/10.1007/s00332-024-10053-3
- N. Namura, R. Muolo, H. Nakao, *Optimal interaction functions realizing higher-order Kuramoto dynamics with arbitrary limit-cycle oscillators*, Chaos 36, 023120 (2026): https://doi.org/10.1063/5.0307452

## Limitations retained

The exact cancellation is a statement about the retained mixed-order phase reduction, not an all-orders identity for the physical Stuart–Landau system. The analytic stability-collapse theorem is for the unweighted three-oscillator triangle, straight isochrones, and local linear stability of synchrony and splay. Other attractors are not excluded. Path-dependent second-order terms can retain emergent nonpairwise provenance despite pairwise-additive phase dependence after explicit triplet cancellation. The common transition remains shifted from rho=pi/2.
