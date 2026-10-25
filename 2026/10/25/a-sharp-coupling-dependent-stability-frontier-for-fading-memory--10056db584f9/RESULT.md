# A sharp coupling-dependent stability frontier for fading-memory cyclic coordinate gradients

## Finding
For the two-coordinate, one-query-per-update coherent coordinate descent (CoCD) scheme with full two-entry memory and decay \(0\le\gamma\le1\), the exact convergence boundary on a coupled strongly convex quadratic is
\[
0<\alpha\lambda<\tau_*(\gamma,c):=
\frac{4}{1+\gamma+\sqrt{(1+\gamma)^2-8c^2\gamma(1-\gamma)}}.
\]
Here the quadratic has Hessian \(\lambda\begin{psmallmatrix}1&c\\c&1\end{psmallmatrix}\), with \(\lambda>0\) and \(|c|<1\). This is necessary and sufficient for convergence to the minimizer from every initial point when the gradient buffer is initialized to zero, and equivalently for convergence of every augmented state. At equality or above, not every initial point converges.

The ordinary cyclic block-coordinate limit \(\gamma=0\) has the exact threshold \(\alpha\lambda<2\), whereas the perfect-memory limit \(\gamma=1\) has threshold \(\alpha\lambda<1\), independently of coupling. For \(0<\gamma<1\), the admissible threshold exceeds that of ordinary cyclic coordinate descent precisely when
\[
0<\gamma<\frac12,\qquad c^2>\frac{1}{2(1-\gamma)}.
\]
Across all admissible \(\gamma,c\), \(\tau_*<3\), and \(3\) is the sharp unattained supremum, approached as \(\gamma=1/3\) and \(|c|\uparrow1\). Thus moderate fading memory can permit a stepsize larger than the cyclic coordinate-descent limit, despite memory reducing the permissible stepsize for uncoupled coordinates.

## Assumptions and scope
The objective is \(f(x,y)=\frac\lambda2(x^2+2cxy+y^2)\) on \(\mathbb R^2\), with \(\lambda>0\), \(-1<c<1\). Fix \(\alpha>0\), \(0\le\gamma\le1\), and any positive centered finite-difference radius \(\varepsilon\). The buffer has exactly two entries, initially zero. At each step multiply the entire buffer by \(\gamma\), replace the active component by its centered finite-difference derivative at the current position, and update both coordinates simultaneously by subtracting \(\alpha\) times the resulting buffer. Active coordinates alternate first, second, first, second, and so on. Central differences equal exact partial derivatives for this quadratic, independently of \(\varepsilon\). There is no randomness or projection.

Global convergence means \((x_k,y_k)\to(0,0)\) for every starting \((x_0,y_0)\) with the stated zero buffer, not monotonic descent at every update. The same boundary holds for convergence from every admissible augmented state with arbitrary initial buffer.

## Proof
Write \(t=\alpha\lambda\) and rescale the gradient buffer by \(\lambda\). At the beginning of a two-update cycle, let \(p\) be the previously stored second-component gradient in rescaled units, and let \((x,y)\) be the position. The first refresh gives \(q=x+cy\) and
\[
x'=x-tq,\qquad y'=y-t\gamma p.
\]
At the second update, the retained first component has decayed to \(\gamma q\), and the freshly evaluated second component is \(p'=cx'+y'\). Hence
\[
x''=x'-t\gamma q,\qquad y''=y'-tp',
\]
so that the cycle map on \((x,y,p)\) is the exact matrix
\[
T=\begin{pmatrix}
1-(1+\gamma)t&-(1+\gamma)ct&0\\
-ct(1-t)&1-t+c^2t^2&-\gamma t(1-t)\\
c(1-t)&1-c^2t&-\gamma t
\end{pmatrix}.
\]
Its monic characteristic polynomial is \(P(z)=z^3+a_1z^2+a_2z+a_3\), where
\[
\begin{aligned}
a_1&=-c^2t^2+2(1+\gamma)t-2,\\
a_2&=1-2(1+\gamma)t+\big((1+\gamma)^2-2c^2\gamma\big)t^2,\\
a_3&=-c^2\gamma^2t^2.
\end{aligned}
\]
For a real monic cubic, all roots lie strictly inside the unit circle if and only if \(|a_3|<1\), \(1+a_1+a_2+a_3>0\), \(1-a_1+a_2-a_3>0\), and \(1-a_2+a_1a_3-a_3^2>0\). These are the cubic Schur–Jury inequalities, obtainable from one Schur reduction to a quadratic.

The three nontrivial expressions factor exactly as
\[
\begin{aligned}
1+a_1+a_2+a_3&=t^2(1-c^2)(1+\gamma)^2,\\
1-a_1+a_2-a_3&=[2-(1+\gamma)t]^2+c^2(1-\gamma)^2t^2,\\
1-a_2+a_1a_3-a_3^2&=t(1+\gamma)(1+c^2\gamma t)F(t),
\end{aligned}
\]
with \(F(t)=2-(1+\gamma)t+c^2\gamma(1-\gamma)t^2\), while \(|a_3|<1\) is \(|c|\gamma t<1\).

For \(0<|c|<1\) and \(0<\gamma<1\), the discriminant of \(F\) is strictly positive:
\[
(1+\gamma)^2-8c^2\gamma(1-\gamma)>(1-3\gamma)^2\ge0.
\]
Also \(F(0)=2>0\), whereas \(F(1/(|c|\gamma))=(1+\gamma)(1-1/|c|)/\gamma<0\). Thus the smaller positive root of \(F\) lies below \(1/(|c|\gamma)\), and its larger positive root lies above it. The Schur–Jury inequalities are therefore simultaneously satisfied exactly when \(0<t<\tau_*\), where the rationalized smaller root equals the displayed \(\tau_*\). The nonnegative-square second expression is strictly positive throughout that range. The degenerate cases \(c=0\), \(\gamma=0\), or \(\gamma=1\) follow directly from the same identities by continuity and direct substitution, yielding respectively \(2/(1+\gamma)\), \(2\), and \(1\).

Strict Schur stability makes every augmented state decay geometrically. Conversely, suppose all positions started with zero buffer converged despite \(\rho(T)\ge1\). The initial-position plane \(E=\{(x,y,0)\}\) would satisfy \(T^nE\to0\). But \(E+TE=\mathbb R^3\): the third row of \(T\) has at least one nonzero entry in its first two columns (otherwise both \(c(1-t)=0\) and \(1-c^2t=0\), impossible for \(|c|<1\)). Consequently \(T^n\) would converge to zero on all of \(\mathbb R^3\), contradicting \(\rho(T)\ge1\). This proves necessity even for the zero-buffer initialization, including equality.

For the comparison with ordinary cyclic updates, \(\tau_*>2\) is equivalent to \(1+\gamma+\sqrt{(1+\gamma)^2-8c^2\gamma(1-\gamma)}<2\). After imposing \(\gamma>0\) and squaring the nonnegative sides, this is precisely \(\gamma<1/2\) and \(c^2>1/[2(1-\gamma)]\). Finally, since \(c^2<1\), the square root in \(\tau_*\) strictly exceeds \(|1-3\gamma|\) for \(0<\gamma<1\). For \(\gamma\le1/3\), this gives \(\tau_*<2/(1-\gamma)\le3\); for \(\gamma\ge1/3\), it gives \(\tau_*<1/\gamma\le3\). The endpoints \(\gamma=0,1\) are smaller. Taking \(\gamma=1/3\) and \(|c|\uparrow1\) approaches \(3\), proving sharpness.

## Verification
The included `verify.py` reconstructs the cycle matrix directly from the two refresh/update operations and establishes five symbolic characteristic-polynomial, Schur–Jury and determinant identities. It then checks 500 independently sampled exact-rational iteration identities, 3,000 finite matrix-eigenvalue classifications on both sides of the proposed frontier, and endpoint/enlargement/limiting cases. All checks passed when run with Python, SymPy and NumPy. The universal theorem and strict boundary follow from the analytical argument; finite tests are not proofs.

## Relationship to prior work
Liang, Sun, Wang and Rakita (2026, arXiv:2605.14373, Sections 4, 5.3, Appendix C and Algorithm 1 in Appendix D) introduce the cyclic buffer method and derive conservative sufficient smoothness bounds, with qualitative treatment of fading memory; they do not state the exact two-coordinate coupled-quadratic stability frontier or coupling-induced expansion beyond the no-memory baseline. The displayed iteration is exactly their full-memory two-coordinate, one-query scheme on this objective. Beck and Tetruashvili (2013) establish convergence rates for cyclic block coordinate methods, but their non-buffered updates are the \(\gamma=0\) comparator. Mokhtari, Gürbüzbalaban and Ribeiro (2018) aggregate delayed component-function gradients and iterate averages in DIAG; their update (18) is structurally different from the cyclic coordinate buffer whose nonactive entry is decayed and reused. The Schur–Jury criterion and stability computations are standard tools, not claimed as original.

## Limitations
The sharp frontier is for two equal-curvature coordinates, a symmetric coupling, one coordinate refreshed each step, constant step and decay, and a full two-entry buffer. It does not imply general convergence for arbitrary dimensions, losses, nonuniform diagonal entries, memory budgets or stochastic gradient noise, nor does it prove per-step objective descent. The original paper's higher-dimensional empirical conclusions are not assessed. Prior specialized delayed-gradient stability analyses may contain mathematically equivalent specializations; the literature comparisons do not constitute an exhaustive uniqueness proof. Independent validation has not been performed.

## References
1. C. Liang, X. Sun, Q. Wang and D. Rakita, *Turning Stale Gradients into Stable Gradients: Coherent Coordinate Descent with Implicit Landscape Smoothing for Lightweight Zeroth-Order Optimization*, arXiv:2605.14373, first posted 2026-05-14, https://arxiv.org/pdf/2605.14373.
2. A. Beck and L. Tetruashvili, *On the Convergence of Block Coordinate Descent Type Methods*, SIAM Journal on Optimization 23(4), 2037–2060 (2013), DOI:10.1137/120887679.
3. A. Mokhtari, M. Gürbüzbalaban and A. Ribeiro, *Surpassing Gradient Descent Provably: A Cyclic Incremental Method with Linear Convergence Rate*, SIAM Journal on Optimization 28(2), 1420–1447 (2018), arXiv:1611.00347, https://arxiv.org/pdf/1611.00347.
