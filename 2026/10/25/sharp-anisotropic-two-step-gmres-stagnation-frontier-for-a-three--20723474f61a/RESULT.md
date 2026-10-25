# Sharp anisotropic two-step GMRES stagnation frontier for a three-site bidiagonal system

## Finding

For positive real numbers \(u,v\), let
\[
M_{u,v}=\begin{pmatrix}1&u&0\\0&1&v\\0&0&1\end{pmatrix},\qquad
\rho=\frac vu,\qquad
G_\rho(t)=\frac{(t^2+1)(t+\rho)^2}{t(t^2+\rho t+\rho^2)}\quad(t>0),
\]
and define the positive attained minimum \(g_*(\rho)=\min_{t>0}G_\rho(t)\).

There exists a nonzero real initial residual for which **the entire two-step GMRES minimization makes no progress** on \(M_{u,v}x=b\) if and only if
\[
\boxed{uv\ge g_*(v/u).}
\]
Equivalently, every nonzero residual enjoys strict two-step norm reduction precisely when \(uv<g_*(v/u)\). In the latter regime, a uniform strict contraction bound exists over all unit residuals, though no general closed formula for that contraction factor is asserted. For the equal-coupling Jordan case \(u=v\), the sharp threshold is \(g_*(1)=8/3\). For arbitrary positive unequal weights,
\[
2<g_*(\rho)\le 2+\frac{2\rho}{\rho^2+\rho+1}\le\frac83.
\]
The upper endpoint \(8/3\) is achieved only for \(\rho=1\), and the lower endpoint \(2\) is the unattained infimum over all weight ratios, approached as \(\rho\to0\) or \(\rho\to\infty\). Thus \(uv\le2\) guarantees two-step progress for all ratios; \(uv\ge8/3\) guarantees the *existence* of a stagnating initial residual for every ratio; the intervening region depends genuinely on anisotropy.

The source two-grid accelerator TGA(1;1,0), with identity fixed-point preconditioner and its specified \(M^\top M\)-orthogonal residual correction, minimizes over precisely the same two-dimensional correction space on its first cycle. It therefore inherits this exact frontier. By contrast, the underlying undamped Richardson fixed-point map \(I-M_{u,v}\) is nilpotent of index three, so the unaccelerated method solves every such system in at most three steps.

For an exact fixed-product contrast let \(uv=5/2\). The balanced pair \(u=v=\sqrt{5/2}\) has no stagnating GMRES(2) residual. The anisotropic pair
\[
u=\frac{5+\sqrt5}{2\sqrt2},\qquad v=\frac{5-\sqrt5}{2\sqrt2}
\]
produces complete stagnation for \(r=(1,-1/\sqrt2,1)^\top\): \(r^\top M_{u,v}r=r^\top M_{u,v}^2r=0\), while \(r,M_{u,v}r,M_{u,v}^2r\) are linearly independent. The two matrices have the same eigenvalues \(1,1,1\) and the same positive coupling product.

## Assumptions and scope

All vectors and matrices are real and computed in exact arithmetic. The matrix is the specified \(3\times3\) upper-bidiagonal unipotent matrix with **strictly positive** upper off-diagonal entries. We consider unrestarted two-step Euclidean residual-minimizing GMRES, or the first residual minimization of TGA(1;1,0) with \(B=I\), one presmoothing step, no postsmoothing, and the residual inner product arising from \(M^\top M\). We call complete two-step stagnation \(r_2=r_0\ne0\), not merely equal norms with a different residual. Since the starting iterate is arbitrary, the initial residual may be any nonzero vector.

The criterion is existential in the residual and necessary-and-sufficient for fixed \(u,v\). The displayed universal bounds concern the *critical coupling product* as the ratio varies; they do not claim that every initial residual stagnates above threshold. For \(uv<g_*(v/u)\), every nonzero residual strictly improves after two steps.

## Proof

**1. Two-step stationarity.** Put \(N=M-I\), so \(N^3=0\). The two-step GMRES search space is \(\operatorname{span}\{r,Mr\}\), and its residuals are \(r-M(c_1r+c_2Mr)\). The zero correction is optimal if and only if
\[
r^\top Mr=0,\qquad r^\top M^2r=0.
\]
The Euclidean least-squares objective is convex; these two normal equations are therefore necessary and sufficient for the residual to remain *exactly* \(r\). No conditioning or minimizer uniqueness assumption is required.

**2. Elimination.** Write \(r=(x,y,z)^\top\), \(Q=x^2+y^2+z^2\), and \(P=y(ux+vz)\). Since \(M=I+N\) and \(N^2r=(uvz,0,0)^\top\), the stationarity equations reduce to
\[
Q+P=0,\qquad Q+2P+uvxz=0.
\]
Consequently \(Q=uvxz>0\), so \(xz>0\) and neither \(x\) nor \(z\) vanishes. By rescaling and simultaneous sign reversal we may set \(xz=1\) with \(x,z>0\). Put \(t=x^2>0\); then \(x=\sqrt t\), \(z=1/\sqrt t\). With \(\rho=v/u\), the first equation gives
\[
y=-\frac{uv}{u\sqrt t+v/\sqrt t}.
\]
Substitution into \(Q=uv\) gives precisely
\[
uv=\frac{(t^2+1)(t+\rho)^2}{t(t^2+\rho t+\rho^2)}=G_\rho(t).
\]
Conversely, any positive \(t\) satisfying this identity defines \(r\) by the displayed formulas and satisfies both normal equations. These implications do not rely on sampling or numerical approximation.

**3. Exact frontier.** For fixed \(\rho>0\), \(G_\rho\) is continuous and positive, diverging to \(+\infty\) as \(t\to0\) and as \(t\to\infty\). It therefore attains a finite minimum and its image is \([g_*(\rho),\infty)\). The existence statement follows. If no stationary residual exists, the function taking a unit residual to the optimal two-step relative residual is upper semicontinuous (an infimum of continuous polynomial residual norms), is strictly below one at every unit vector, and hence has a maximum strictly below one on the compact unit sphere. This establishes the uniform strict reduction assertion.

**4. Sharp coupling-product corridor.** Every stationary residual obeys \(uvxz=Q>x^2+z^2\ge2xz\); hence \(uv>2\). Since the minimum is attained, \(g_*(\rho)>2\). Testing \(t=1\) yields
\[
g_*(\rho)\le G_\rho(1)=\frac{2(1+\rho)^2}{1+\rho+\rho^2}
=2+\frac{2\rho}{1+\rho+\rho^2}\le\frac83,
\]
with the last equality only if \(\rho=1\). In that balanced case an exact factorization proves global sharpness:
\[
G_1(t)-\frac83=\frac{(t-1)^2(3t^2+4t+3)}{3t(t^2+t+1)}\ge0.
\]
The upper bound tends to \(2\) when \(\rho\to0\) or \(\infty\), establishing the global infimum and both universal cutoffs.

**5. Exact witnesses and the two-grid interpretation.** For the anisotropic pair stated in the finding, \(uv=5/2\), \(u+v=5/\sqrt2\), and \(r=(1,-1/\sqrt2,1)^\top\) has \(Q=5/2\), \(P=-5/2\), and \(uvxz=5/2\). It satisfies both stationarity equations. Its third coordinate is nonzero and \(uv\ne0\), so \(r,Mr,M^2r\) are independent: replacing later columns by their successive differences gives independent vectors \(r,Nr,N^2r\), with determinant \(u v^2 z^3\) up to sign, nonzero. For the balanced pair \(uv=5/2<8/3\), the earlier equivalence excludes stationarity.

For the specified TGA first cycle, presmoothing sends \(x\) to \(x+r\), with new residual \((I-M)r\). Equation (4.1) of the motivating paper gives prolongation columns \(-r\) and \(-(I-M)r\). Their span is \(\operatorname{span}\{r,Mr\}\). Its \(M^\top M\)-orthogonal coarse correction consequently minimizes the Euclidean residual over the same affine space as GMRES(2). If the latter stagnates, TGA returns exactly to its original iterate, and repeats this behavior. Finally \((I-M)^3=(-N)^3=0\), so three ordinary Richardson steps solve the same linear system exactly for every right-hand side.

## Verification

The companion `verify_weighted_tga.py` independently checks the exact algebraic witness, the balanced-frontier factorization, the ratio-reversal identity, and 4,000 numerical zero-correction constructions. It also checks the threshold numerically for eleven ratios. Run with `python verify_weighted_tga.py` using Python 3.10+, NumPy, SciPy, and SymPy. The numerical tests are finite spot checks only: the universal claims and strict boundaries follow from the preceding analytic proof.

## Relationship to prior work

Adler, He, Hu and Lefebvre (2026, arXiv:2609.13091v1) propose the two-grid acceleration framework and the prolongation columns analyzed here; neither those columns nor general GMRES equivalences are claimed as new. Tichý and Liesen (2006) analyze worst-case GMRES and polynomial numerical hulls for a *standard Jordan block* with equal superdiagonal coefficients; their published balanced-weight stagnation criterion is acknowledged and agrees with the \(\rho=1\) specialization. The theorem here concerns the ratio-dependent **Euclidean** frontier for *unequal* edge weights, including a same-product reversal not implied by standard-Jordan conclusions: nonunitary diagonal similarity does not preserve Euclidean GMRES residual norms. Soodhalter (2026) establishes broad realizability of prescribed GMRES stagnation behavior for constructed matrices, but does not constrain the matrix to these prescribed three-site bidiagonal weights or provide the resulting sharp weight-parameter frontier. Related work on numerical ranges of weighted shifts treats a distinct scalar extremal problem. The proof is self-contained and does not claim uniqueness of this characterization in all unpublished or unindexed literature.

## Limitations

This is a three-dimensional exact-arithmetic Euclidean-residual statement. It does not establish rates for larger bidiagonal matrices, arbitrary nonnormal matrices, floating-point orthogonality, nonlinear two-grid methods, or all values of the TGA memory parameter. It does not give a closed radical formula for \(g_*(\rho)\) at every ratio; the displayed smooth one-dimensional minimization is exact and its minimum is attained. The first-cycle equivalence is specific to identity presmoothing and the stated inner product. Prior-work search cannot exclude unindexed earlier analyses of this exact weighted family; independent audit has not been performed.

## References

1. J. H. Adler, Y. He, X. Hu and S. Lefebvre, *A Unified Two-Grid Framework for Anderson Acceleration and Nonlinear GMRES*, arXiv:2609.13091v1 (first posted 11 September 2026), especially Algorithm 4.1 and equation (4.1). https://arxiv.org/pdf/2609.13091
2. P. Tichý and J. Liesen, *GMRES Convergence and the Polynomial Numerical Hull for a Jordan Block*, TU Berlin Preprint 34-2006, especially Sections 1–3. https://www3.math.tu-berlin.de/preprints/files/TiLi2006.pdf
3. K. M. Soodhalter, *Admissible and Attainable Convergence Behavior with Stagnation Mirroring in Restarted (Block) GMRES*, *Numerical Algorithms* (2026), doi:10.1007/s11075-026-02368-x. https://link.springer.com/article/10.1007/s11075-026-02368-x
