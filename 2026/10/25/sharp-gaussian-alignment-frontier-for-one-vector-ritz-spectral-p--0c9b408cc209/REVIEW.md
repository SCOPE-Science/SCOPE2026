# Self-review

## Correctness: PASS

The one-spike Hessian and rank-one inverse spectral correction are precisely specified for every integer \(d\ge2\), \(\kappa>1\), and \(\tau>0\). The preconditioned spectrum consists of two plane eigenvalues (and additional unit eigenvalues for \(d>2\)); its trace and determinant give \(W=\lambda(\kappa+2-\lambda)^2/\kappa\). Exact factorization provides the unique strict-improvement threshold. A chi-square ratio yields the full regularized-beta probability; expansion yields the critical covariance scale. The worst-case maximizer and generic Krylov-step statement follow from the same spectral calculation. The standalone checker reproducibly passes symbolic, rational, dense-matrix, and Gaussian finite checks. These finite checks support, rather than replace, the analytical proof.

## Originality: PASS, priority not independently established

Closest relevant primary work: Daužickaitė et al. (2026), arXiv:2605.23571, investigates ensemble-informed randomized sketches and LMP acceleration; accessible abstract and introduction do not give the present exact one-spike Gaussian condition-number distribution, though full text was unavailable and remains a priority risk. Daužickaitė et al. (2021), DOI 10.1002/qj.4151, supplies spectral-LMP and approximate Ritz constructions; Giraud and Gratton (2006), DOI 10.1137/040617546, treats local sensitivity to inaccurate eigenvectors. The deterministic ingredients may connect to established two-dimensional perturbation theory, but no inspected source or semantic research match yielded the precise improvement probability and critical \(\tau\kappa^{3/2}\) transition. Existing general sensitivity bounds do not alone calculate this distribution. Search failure is not a proof of priority.

## Mathematical value: PASS

A one-vector Hessian-product sketch is the smallest nontrivial instance of a practically motivated spectral limited-memory preconditioner. Rather than merely exhibiting a failed sketch, the result gives the exact chance of reducing a relevant condition number, a sharp covariance-design scale, the maximally harmful alignment, and an exact-arithmetic three-eigenvalue effect. In particular, variance scaling as \(\kappa^{-3/2}\) separates high- and low-probability improvement for the tested one-spike geometry, furnishing a quantitative diagnostic for sketch covariance design. It does not claim broad iteration-count, wall-clock, or multi-vector improvement.

## Residual scientific risks

A complete comparison with the inaccessible portions of the motivating 2026 article has not been performed. Earlier randomized approximate-eigenpair analysis might already imply the specific beta law after a special-case substitution; available sources were searched and actual inspected statements compared, but this possibility remains. The statement is restricted to the precise one-vector Rayleigh-LMP setup.

Self-review: passed. Independent audit: not yet performed.
