# Exact two-query gain from orthogonal sampling in planar quadratic line minimization

## Finding

Let \(Q\in\mathbb R^{2\times2}\) be symmetric positive definite with spectral condition number \(\kappa\ge1\), and let \(f(x)=\tfrac12(x-x_*)^{\mathsf T}Q(x-x_*)\). Consider two exact one-dimensional minimizations in directions chosen independently and uniformly from the unit circle (scheme **I**), or chosen as the columns of a single Haar-uniform orthogonal matrix (scheme **O**). The second minimization starts from the output of the first, not from the original point. Both schemes use the same initial point \(x\).

For every deterministic \(x\), their expected objective gaps after these two minimizations obey the **exact identity**

\[
\mathbb E[f(x_{\mathrm O}^{(2)})-f(x_*)]
=\left(\frac{\kappa-1}{\kappa+1}\right)^2
\mathbb E[f(x_{\mathrm I}^{(2)})-f(x_*)].
\]

The identity is independent of the starting-error orientation. At \(\kappa=1\), an orthogonal pair solves the quadratic exactly in two minimizations, whereas independent directions leave one quarter of the initial objective gap in expectation. For finite \(\kappa>1\), the paired scheme has strictly smaller expected error for every nonoptimal start. At \(\kappa=4\), it has exactly \(9/25\) of the independent scheme's expected error; the relative improvement is \(4\kappa/(\kappa+1)^2\), vanishing in the ill-conditioned limit.

## Assumptions and scope

All variables, directions, and matrices are real and two-dimensional. The quadratic is unconstrained and strictly convex, and line minimization is exact. A uniform direction means the direction of a standard two-dimensional Gaussian vector or, equivalently, uniform normalized arc length on the circle. Scheme **I** uses two mutually independent such directions. Scheme **O** draws one uniform direction \(s\), then uses its Euclidean perpendicular \(s_\perp\); the sign of the perpendicular and the order of the orthogonal columns do not affect the stated expectation. Sampling is independent of the deterministic initial error. The claim covers the two-step outcome only, without extrapolating it to repeated epochs or nonquadratic objectives.

For any nonzero direction \(s\), one exact step is

\[
\mathcal L_s(x)=x-\frac{s^{\mathsf T}Q(x-x_*)}{s^{\mathsf T}Qs}\,s.
\]

## Proof

**1. Energy-space projection.** Orthogonal diagonalization and positive rescaling of \(Q\) do not alter either sampling law or the line minimizer. Work therefore with \(Q=\operatorname{diag}(r^2,1)\), where \(r=\sqrt\kappa\ge1\). Put \(z=Q^{1/2}(x-x_*)\). The transformed update is \(z\mapsto U_sz\), where

\[
U_s=I-\frac{Q^{1/2}ss^{\mathsf T}Q^{1/2}}{s^{\mathsf T}Qs}
\]

is a rank-one orthogonal projector. For \(s=(\cos\theta,\sin\theta)\) and \(t=\tan\theta\), a unit vector spanning its range is

\[
v=\frac{(-t,r)^{\mathsf T}}{\sqrt{r^2+t^2}},\qquad U_s=vv^{\mathsf T}.
\]

**2. Two independent directions.** By symmetry, the one-step mean projector is

\[
T=\mathbb E U_s=\operatorname{diag}\!\left(\frac1{r+1},\frac r{r+1}\right).
\]

The elementary angular moments are

\[
\mathbb E v_1^4=\frac{r+2}{2(r+1)^2},\qquad
\mathbb E v_1^2v_2^2=\frac r{2(r+1)^2},\qquad
\mathbb E v_2^4=\frac{r(2r+1)}{2(r+1)^2}.
\]

The second independent step gives the expected squared energy \(z^{\mathsf T}Dz\) with

\[
D=\mathbb E[U_sTU_s]
=\frac1{2(r+1)^3}
\begin{pmatrix}
r^2+r+2&0\\
0&r(2r^2+r+1)
\end{pmatrix}.
\]

The moments follow by \(t=\tan\theta\) and \(\mathbb E v_1^2=1/(r+1)\). Differentiating that last identity with respect to \(r\) yields \(\mathbb E v_1^2v_2^2=r/[2(r+1)^2]\), and the fourth moments follow from \(v_1^2+v_2^2=1\).

**3. Orthogonally paired directions.** Let \(s_\perp=(-\sin\theta,\cos\theta)\) and let \(w\) span the range of \(U_{s_\perp}\). Direct substitution gives

\[
(v^{\mathsf T}w)^2
=\frac{(r^2-1)^2t^2}{(r^2+t^2)(1+r^2t^2)},
\qquad U_sU_{s_\perp}U_s=(v^{\mathsf T}w)^2vv^{\mathsf T}.
\]

The expected two-step energy matrix \(C=\mathbb E[U_sU_{s_\perp}U_s]\) is diagonal, because its off-diagonal entry is odd under reflection of \(\theta\). For \(r>1\), its first diagonal entry is

\[
C_{11}=\frac2\pi\int_0^\infty
\frac{(r^2-1)^2t^4}{(1+t^2)(r^2+t^2)^2(1+r^2t^2)}\,dt
=\frac{(r-1)^2(r^2+r+2)}{2(r+1)(r^2+1)^2}.
\]

For transparency, this rational integral can be evaluated by decomposing its integrand into

\[
\frac{r^4}{(r^2+1)(r^2+t^2)^2}
+\frac{r^2(r^2+2)}{(r^2-1)(r^2+1)^2(r^2+t^2)}
+\frac{r^2}{(r^2-1)(r^2+1)^2(1+r^2t^2)}
-\frac1{(r^2-1)(1+t^2)}.
\]

Each term integrates using \(\int_0^\infty(t^2+a^2)^{-1}dt=\pi/(2a)\) or \(\int_0^\infty(t^2+a^2)^{-2}dt=\pi/(4a^3)\), with \(a>0\).

The trace is easier to find directly:

\[
\operatorname{tr}C=\mathbb E(v^{\mathsf T}w)^2
=1-\frac{2r}{r^2+1}=\frac{(r-1)^2}{r^2+1},
\]

by the standard trigonometric integral \(\frac2\pi\int_0^{\pi/2}(1+b\sin^2\varphi)^{-1}d\varphi=(1+b)^{-1/2}\), with \(b=(r^2-1)^2/(4r^2)\). Subtracting \(C_{11}\) gives

\[
C_{22}=\frac{(r-1)^2r(2r^2+r+1)}{2(r+1)(r^2+1)^2}.
\]

Consequently, **as complete matrices rather than merely after averaging the starting-error direction**,

\[
C=\left(\frac{r^2-1}{r^2+1}\right)^2D.
\]

When \(r=1\), the two energy projectors of a Euclidean orthogonal pair are complementary and their product is zero, giving the same identity by direct calculation. Returning to \(\kappa=r^2\) and using \(f(x)-f(x_*)=\|z\|_2^2/2\) proves the claim for every deterministic \(x\).

## Verification

The standalone `verify.py` checks the rational partial-fraction identity symbolically, verifies the two diagonal matrix identities in the indeterminate \(r\), and independently integrates both two-step sampling laws at 50-digit working precision. It includes the isotropic equality case and multiple nontrivial condition numbers. Execute `python verify.py` after installing the packages in `requirements.txt`. Successful local execution produced: `CHECK_OK symbolic-rational=4 high-precision-angular= 30`.

The numerical quadratures are independent cross-checks, not proofs of the identity for an infinite continuum of parameters. The analytical proof above supplies that justification.

## Relationship to prior work

The motivation comes from the use of random orthogonal direction sets in Kozak, Molinari, Rosasco, Tenorio and Villa (2021), where the update is a finite-difference projected-gradient step and the analysis establishes broader convergence guarantees, not the two-step exact line-search identity above. Berglund, Khirirat and Wang (2022) consider randomized subspace Newton steps and complexity bounds, again without this Haar-coupled versus independent two-query calculation.

Gürbüzbalaban, Ozdaglar, Vanli and Wright (2018/2020) analyze without-replacement versus independent sampling of a **fixed coordinate basis** in randomized coordinate descent. The present comparison changes the randomization law: its orthogonal pair is sampled from a fresh continuous Haar rotation, while its independent benchmark draws both directions afresh from the continuum. The explicit orientation-uniform proportionality is not an immediate statement of their fixed-coordinate results. Existing general sketch-and-project convergence analyses provide further context but do not supply this exact finite-two-query coefficient in the inspected material.

## Limitations

The identity is not asserted for dimensions greater than two, for approximate line minimization, finite-difference errors, noisy objectives, nonquadratic functions, or repeated correlated epochs. The benefit factor approaches one as \(\kappa\to\infty\), so a gain at fixed condition number does not guarantee a condition-independent acceleration. The probabilistic comparison treats expected objective gap rather than a samplewise ordering or a stochastic-dominance claim. Earlier specialized calculations not retrieved in the literature comparison could establish the same formula; independent originality review has not been performed.

## References

1. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio and S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941, first posted 2021-07-08. https://arxiv.org/abs/2107.03941
2. E. Berglund, S. Khirirat and X. Wang, *Zeroth-Order Randomized Subspace Newton Methods*, arXiv:2202.04612, first posted 2022-02-09. https://arxiv.org/abs/2202.04612
3. M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli and S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200, first posted 2018-03-22; *Mathematical Programming* **181** (2020), 349–376. https://arxiv.org/abs/1803.08200
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, *SIAM Journal on Matrix Analysis and Applications* **36** (2015), 1660–1690. https://arxiv.org/abs/1506.03296
