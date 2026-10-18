# Scientific review: exact nullspace-risk frontier

## Correctness

PASS. The residual is an exact product of independent random scalar factors, giving its second moment without approximation. Removing the component parallel to the rank-one forward direction produces a true martingale with explicitly computed conditional covariance. Orthogonality of its increments proves the finite-horizon and limiting covariance identities. Direct summability and the martingale second-moment bound justify almost-sure and mean-square convergence, respectively. Algebra yields the step-size threshold, unique residual-optimal step, and divergence at the residual-stability endpoint. A standard-library exact-rational verifier reproduces 5,579 tests across several nontrivial row and coordinate configurations, including full-path enumeration. Finite tests do not replace the proof.

## Originality

PASS, qualified by the stated bibliographic risk. The qualitative failure of minimum-norm selection by underdetermined randomized coordinate solvers is known from Ma--Needell--Ramdas and Jin--Liu, and is not the claimed novelty. Han--Xie gives broad residual and expected-iterate convergence guarantees. Xia--Zhou's new doubly sampled scheme and regularization conclusions are the direct source. The finding instead proves a joint exact finite-time residual/reconstruction law, full random-solution covariance, sharp mismatch frontier for positive-versus-negative reconstruction progress, and an exact two-row counterexample satisfying the original source's step-size condition. Primary full-text comparisons and searches did not reveal this complete stronger joint statement. An unindexed equivalent derivation remains possible; originality has not received independent confirmation.

## Mathematical value

PASS. Distinguishing data consistency from minimum-norm recovery is essential to iterative regularization. The exact risk-transition point is strictly inside the residual-stable interval, so an algorithm can improve the usual residual diagnostic while deteriorating the quantity of interest. The explicit conservative-step counterexample identifies the extra nullspace-control requirement in a current result, and the limiting covariance gives a reproducible benchmark against which future regularization mechanisms can be tested. The quantitative frontier is structurally motivated rather than a superficial parameter substitution.

## Closest sources, scope and residual risks

Compared directly: Xia--Zhou, arXiv:2610.15399v1 (Algorithm 1, Assumption 2.1 and Theorems 2.1/3.1); Ma--Needell--Ramdas, arXiv:1503.08235 (existing qualitative minimum-norm failure); Jin--Liu, arXiv:2405.13340 (random feasible limit and added selection assumptions); Han--Xie, arXiv:2208.05437 (general pseudoinverse-free randomized convergence). The scope is exact rank-one finite-dimensional dynamics with independent uniform row/column samples and constant step; no general-matrix or finite-precision theorem is claimed. The counterexample to a regularizing assertion holds for aligned vanishing noise, not arbitrary noisy data.

Self-review: passed. Independent audit: not yet performed.
