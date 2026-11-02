# Scientific review

## Correctness — PASS

The exact symmetric preconditioned matrix has a positive definite coupled \(2\times2\) block for \(0<d<\sqrt b\) and an untouched eigenvalue \(c\). Its eigenvalues are obtained by a quadratic identity. The ratio of the two coupled eigenvalues is strictly minimized at \(\theta=b\) by AM–GM. The lower eigenvalue increases monotonically and crosses the untouched value at precisely \(\theta=c(b-c)/(b-c-d^2)\), when that crossing exists. Comparing its location against \(\theta=b\) proves both global branches and uniqueness for positive perturbations. The analytic argument establishes the continuum theorem; 255 exact-fraction identities and 4,032 numerical comparisons independently check the algebra and representative cases.

## Originality — PASS, subject to historical-priority limitations

The closest motivating study [1] considers recycled scaled spectral preconditioning for perturbed SPD systems, but its Section 3.3 works in a fixed-separated-scaling regime and proves eigenpair sensitivity estimates and energy-error comparisons; it does not provide the explicit all-positive-scaling condition-number optimum for this three-mode off-diagonal perturbation. The predecessor studies [2,3] address choice of cluster placement for finite-iteration CG; [4] studies approximate-eigenpair sensitivity to first order; [5] gives general algorithmic procedures for diagonal-preconditioning optimization but not the explicit collision threshold. The claim does not assert that diagonal scaling, the quadratic eigenvalue formula or general condition-number optimization is new. A specialized older matrix-scaling result could imply it, so the source comparison is qualified rather than a proof of absolute priority.

## Value — PASS

The object is the smallest SPD example with one recycled direction and two competing untouched eigenvalues: fewer than three modes cannot exhibit an optimizer changing its collision target from one untouched mode to another. The theorem replaces a heuristic scaling choice with an exact global parameter rule. In particular, the optimal scale escapes the fixed-eigenvalue-gap regime of the motivating perturbation theory at quadratic order and reaches exact coincidence with another untouched eigenvalue at a finite, explicit threshold. This supplies a concrete calibration and limitation for spectral recycling; it does not claim a general CG iteration-count improvement.

## Closest literature and limitations

[1] Diouane, Gürol, Mouhtal, Orban, *Deflation-Based Spectral Preconditioning for the Conjugate Gradient Method on Perturbed Systems* (2026), arXiv:2610.28808v1, Sections 3.3 and 4, https://arxiv.org/html/2610.28808v1 .

[2] Same authors, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget* (2026), arXiv:2603.28969, https://arxiv.org/abs/2603.28969 .

[3] Same authors, *An Efficient Scaled Spectral Preconditioner for Sequences of Symmetric Positive Definite Linear Systems* (2024), arXiv:2410.02204, https://arxiv.org/abs/2410.02204 .

[4] Giraud and Gratton, *On the Sensitivity of Some Spectral Preconditioners* (2006), doi:10.1137/040617546 .

[5] Qu et al., *Optimal Diagonal Preconditioning* (2022), arXiv:2209.00809 .

Only the special three-dimensional SPD family with one coupling and one adjustable recycled scale is proved. Historical-priority searches are not exhaustive. No independent verification has been undertaken.

Self-review: passed. Independent audit: not yet performed.
