# An algebraic supercritical flip in a finite-rank population integrodifference equation

## Finding
On the circle, the exact growth–dispersal operator with positive cosine dispersal kernel and spatially variable inverse carrying capacity undergoes a *supercritical, locally attracting, genuinely spatially inhomogeneous period-doubling bifurcation* at an explicitly algebraic growth parameter. This is a bifurcation in the **full space of continuous population profiles**, rather than in a Galerkin approximation: the dispersal operator has finite rank and every image belongs to a three-dimensional Fourier subspace.

Let
\[
N(t)=1-5t^2+16t^3,\quad D(t)=1-4t-t^2+8t^3,
\]
and
\[
Q(t)=384t^6-44t^5-447t^4+122t^3+88t^2-34t+3.
\]
There is exactly one zero \(t_*\) of \(Q\) in the rational interval
\[
\frac{166763953195}{10^{12}}<t_*<\frac{166763953197}{10^{12}}.
\]
Set \(\lambda_*=N(t_*)/D(t_*)\), so \(\lambda_*=2.73248006589\ldots\). At this growth strength the positive, nonconstant fixed profile is
\[
u_*(\theta)=a_*+2b_*\cos\theta,\qquad
 a_* = \frac{5t_*}{N(t_*)},\quad b_*=t_*a_*.
\]
There exists \(\delta>0\) and a smooth positive nonconstant fixed-profile branch for \(|\lambda-\lambda_*|<\delta\). It is locally exponentially attracting for \(\lambda_* -\delta<\lambda<\lambda_*\), and has exactly one unstable multiplier for \(\lambda_*<\lambda<\lambda_*+\delta\). For \(\lambda_*<\lambda<\lambda_*+\delta\) a locally unique prime-period-two cycle of pointwise positive, nonconstant profiles bifurcates and is locally exponentially attracting in \(C(\mathbb T)\). This is a local assertion; no global attraction or bifurcation result for other dispersal kernels is claimed.

Normalize the critical even-mode right eigenvector as \(v=(1,v_2)\), with \(v_2=-0.24547412785\ldots\). The cycle's two even-mode coefficient vectors are
\[
(a_\pm,b_\pm)=(a(\lambda),b(\lambda))\pm
\sqrt{\frac{2\nu'(\lambda_*)}{c_*}}\;v\sqrt{\lambda-\lambda_*}
+O(\lambda-\lambda_*),
\]
where \(a(\lambda),b(\lambda)\) is the analytic fixed branch, \(\nu\) its critical multiplier, \(\nu'(\lambda_*)=-0.96973278\ldots\), and \(c_*=-19.18617852\ldots\) is the cubic coefficient of the second iterate in the specified center coordinate. The amplitude prefactor is approximately \(0.31794119\). The bifurcating profiles have no sine component.

## Assumptions and scope
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). On real \(C(\mathbb T)\) consider, for \(\lambda>0\),
\[
(\Phi_\lambda u)(y)=\frac{\lambda}{2\pi}\int_{-\pi}^{\pi}
(1+\cos(y-x))u(x)(1-\kappa(x)u(x))\,dx,
\quad \kappa(x)=\frac45-\frac25\cos x.
\]
The normalized kernel is nonnegative with integral one. The inverse carrying capacity satisfies \(2/5\le\kappa\le6/5\). Biologically admissible profiles near the bifurcation obey \(u>0\) and \(0<\kappa u<1\) pointwise, so their produced population is positive. The theorem covers this fixed kernel and capacity, not all kernels of the motivating growth–dispersal model.

## Proof
**Exact reduction.** The kernel's only nonzero Fourier multipliers are \(\widehat K_0=1\) and \(\widehat K_{\pm1}=1/2\). Consequently \(\Phi_\lambda(C(\mathbb T))\subset E=\operatorname{span}\{1,\cos,\sin\}\), and every fixed or periodic orbit lies in \(E\). Writing \(u(x)=a+2b\cos x+2c\sin x\), Fourier integration yields the **exact** polynomial map
\[
\begin{split}
 a'&=\frac\lambda5(5a-4a^2+4ab-8b^2-8c^2),\\
 b'&=\frac\lambda{10}(a^2+5b-8ab+3b^2+c^2),\\
 c'&=\frac\lambda{10}c(5-8a+2b).
\end{split}
\]
The even plane \(c=0\) is invariant, and the odd direction has scalar linear multiplier at every even fixed point.

**Exact fixed branch and critical polynomial.** With \(t=b/a\), direct substitution verifies the nonzero even fixed branch
\[
 a(t)=\frac{5t}{N(t)},\quad b(t)=\frac{5t^2}{N(t)},\quad
 \lambda(t)=\frac{N(t)}{D(t)}.
\]
Let \(A(t)\) be the two-by-two Jacobian on the even plane along this branch. Direct algebra gives
\[
A(t)=\frac1{D(t)}
\begin{pmatrix}
16t^3-t^2-8t+1 & -4t(4t-1)\\
-t(4t-1)&(16t^3+t^2-8t+1)/2
\end{pmatrix},
\qquad
\det(A(t)+I)=\frac{Q(t)}{D(t)^2}.
\]
Using the exact rational endpoints above, the checker establishes \(Q(t_\mathrm{lo})>0\), \(Q(t_\mathrm{hi})<0\), and \(Q'<0\) throughout their interval; therefore this interval contains exactly one simple root \(t_*\). It verifies positivity of denominators throughout, \(a_*-2b_*>0\), and the exact maximum
\[
\max_{x\in\mathbb T}\kappa(x)u_*(x)
=\frac{(4t_*+1)^2}{4N(t_*)}\in(0.74,0.75).
\]
Thus the profile is strictly inside the biologically admissible regime.

**Full spectrum.** At \(t_*\), the even eigenvalues are \(-1\) and \(\mu\in(-0.181,-0.178)\). The odd multiplier is
\[
\rho=\frac{16t_*^3-3t_*^2-8t_*+1}{2D(t_*)}
\in(-0.503,-0.500).
\]
As the derivative of \(\Phi\) maps the full Banach space into \(E\), its remaining spectrum consists only of zero. In particular, the center multiplier \(-1\) is simple and all others lie strictly inside the unit circle.

**Transversality and nonlinearity.** In even Fourier coordinates, let \(F\) denote the quadratic map, \(A=D_xF\) at the critical fixed point, and \(B=D_x^2F\). Choose a right eigenvector \(v\) and left eigenvector \(w\) of \(A\) at eigenvalue \(-1\) with \(v_1=1\) and \(w^Tv=1\). Because \(A-I\) is invertible, set
\[
h=-(A-I)^{-1}B(v,v),\qquad
x_\lambda'=-(A-I)^{-1}\partial_\lambda F,
\]
\[
\nu'(\lambda_*)=w^T\bigl(\partial_\lambda A+B(x_\lambda',\cdot)\bigr)v,
\quad c_*=-w^TB(v,h).
\]
These are the derivative of the critical multiplier along the fixed branch and the cubic coefficient of the second iterate after elimination of the nonresonant quadratic term, respectively. All entries are rational functions of \(t_*\). Certified rational interval arithmetic in the bundled program establishes
\[
-0.98<\nu'(\lambda_*)<-0.96<0,
\qquad -19.2<c_*<-19.1<0.
\]
In a local scalar center coordinate the second iterate has the expansion
\[
\xi_{n+2}=\xi_n-2\nu'(\lambda_*)(\lambda-\lambda_*)\xi_n+c_*\xi_n^3+
O\bigl(|\xi_n|^4+|\lambda-\lambda_*|\,|\xi_n|^2+(\lambda-\lambda_*)^2|\xi_n|\bigr).
\]
The one-dimensional nondegenerate flip theorem now produces a unique local prime-two cycle on the supercritical side, with the stated square-root amplitude. Its two-step center multiplier has modulus below one and transverse multipliers remain inside the unit circle by continuity. The symmetry-invariant even plane contains the local center manifold and cycle; the full-space derivative is finite rank, hence the positive two-cycle is locally attracting under arbitrary sufficiently small continuous perturbations.

## Verification
Run `python verify.py` with Python 3 and SymPy. The supplied self-contained script reconstructs the exact Fourier fixed-branch and Jacobian identities symbolically, proves rational root bracketing and derivative sign, and performs interval operations with exact `fractions.Fraction` endpoints. The script verifies the strict bounds for all needed eigenvalues, profile positivity, derivative of the critical multiplier, and cubic coefficient; its numerical prints are approximations of exact enclosures. An independent finite orbit simulation is not used as proof. The proof's only imported result is the standard smooth one-dimensional flip bifurcation theorem after the explicit center-manifold reduction.

## Relationship to prior work
Hénot and Lessard (2026) certify supercritical period doubling for a **ten-mode Galerkin approximation** of the Kot–Schaffer growth–dispersal model with a Poisson-type dispersal kernel. Their result does not itself establish the same bifurcation for the full non-finite-rank operator. Here a different, naturally nonnegative **rank-three** cosine dispersal kernel makes the reduction exact, with a wholly algebraic critical threshold and full-function-space attractivity, not a conclusion about their original all-mode kernel.

Day, Junge, and Mischaikow (2004) provide rigorous global analysis for infinite-dimensional integrodifference maps with richer kernels and parameters. Galias and Zgliczyński (2007) rigorously study periodic orbits via infinite-dimensional Krawczyk operators. Church, Constantineau, and Lessard (2025) consider spatially inhomogeneous two-cycles under different kernels and geometries. These are important antecedents for spatial population cycles; the precise finite-rank algebraic flip and local amplitude are not implied by the inspected statements. Material of the latter two relevant papers remained inaccessible in full, leaving historical-priority uncertainty.

## Limitations
This is a local bifurcation theorem for the specified nonnegative cosine kernel and spatial carrying capacity. It neither treats the source's infinite-rank Poisson kernel nor proves global population convergence, absence of other periodic orbits, or mathematical novelty against all non-digitized literature. The existence and stability assertions use ordinary real continuous profiles; extensions to stochastic kernels or higher-dimensional domains are unproved. Independent scientific audit has not been performed.

## References
1. O. Hénot and J.-P. Lessard, *Rigorous verification of period-doubling bifurcations in maps*, arXiv:2610.22986v1 (first public 2026-10-16), https://arxiv.org/abs/2610.22986.
2. S. Day, O. Junge, and K. Mischaikow, *A rigorous numerical method for the global analysis of infinite dimensional discrete dynamical systems*, SIAM J. Appl. Dyn. Syst. (2004).
3. Z. Galias and P. Zgliczyński, *Infinite dimensional Krawczyk operator for finding periodic orbits of discrete dynamical systems*, Int. J. Bifurcation and Chaos (2007), DOI:10.1142/S0218127407019937.
4. J. Church, M. Constantineau, and J.-P. Lessard, *Spatially inhomogeneous two-cycles in an integrodifference equation*, arXiv:2510.21134 (first public 2025-10-24).
