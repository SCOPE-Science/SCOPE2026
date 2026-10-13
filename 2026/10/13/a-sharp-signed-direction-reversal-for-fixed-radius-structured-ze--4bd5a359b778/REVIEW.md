# Research review

## Correctness — PASS

The claimed formula follows from an exact quadratic forward-difference identity, followed by the algebraic frame identities \(R^2=(d/\ell)R\), \(Ru=(d/\ell)u\), \(\|u\|^2=d\), and \(\mathbb E R=I\). The resulting closed first- and second-moment recurrences have strictly subunit contraction factors throughout \(0<\alpha\lambda d/\ell<2\). Their limits yield the stated formula for arbitrary deterministic initial states. Cauchy--Schwarz plus isotropy gives the global \(0\le q\le\ell\) interval; signed, unsigned, and globally sign-biased coordinate frames attain all possible values. The algebra, scope and numerical examples were replayed with 1,305 exact-rational enumerative checks. Finite checks do not prove universality: the written algebra does.

## Originality — PASS with residual priority risk

The defining paper arXiv:2206.05124 specifies the update, frame assumptions and PL convergence bounds, but its inspected Algorithm 1, Theorem 2 and relevant appendices do not give an exact stationary mean-square functional for fixed \(\alpha,h\), much less its sign-orientation minimax reversal. The earlier arXiv:2107.03941 explicitly discusses signed-coordinate bias cancellation for a quadratic and leaves tailored analysis open (Remark 4.2); that does not imply the step-dependent change of optimal frame law. arXiv:2003.02684 instead concerns related gradient-free subspace descent. Indexed scientific summaries for exact Haar moments (published-finding corpus ID `2026/9/18/SCOPE-exact-haar-moments-sparse-ssd--d9ecf263b248`) and first-order coordinate sampling (`2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995`) were compared by implication; neither reported the finite-difference stationary law. A specialized 2022 estimator paper could be reviewed only at the abstract level; unindexed or inaccessible overlapping literature is a genuine residual risk, not a basis for an originality guarantee.

## Value — PASS

The question identifies a concrete, non-asymptotic tuning choice in a published finite-difference optimizer: does bias-free signed sampling always beat biased unsigned sampling? The complete answer is no. All admissible isotropic orthogonal-frame distributions are classified by one scalar statistic, with a sharp, achievable switch in optimal orientation at normalized step one. This is a structural parameter-selection boundary; it distinguishes estimator unbiasedness from actual stationary optimization risk and persists for every finite dimension and frame size. The finding makes no unsupported claim for noisy objectives, nonisotropic Hessians or almost-sure asymptotics.

Self-review: passed. Independent audit: not yet performed.
