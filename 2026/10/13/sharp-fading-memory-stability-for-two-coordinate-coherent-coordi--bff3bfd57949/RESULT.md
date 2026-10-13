# Sharp fading-memory stability for two-coordinate Coherent Coordinate Descent

## Finding

For Coherent Coordinate Descent (CoCD) with one refreshed coordinate per update, a two-entry fading gradient buffer, and cyclic coordinate order, consider the positive-definite quadratic
\[
f_\rho(x_1,x_2)=\tfrac12(x_1^2+x_2^2)+\rho x_1x_2,
\qquad -1<\rho<1.
\]
Write \(\alpha>0\) for its constant learning rate and \(0\le\gamma\le1\) for its buffer-decay factor. The update converges geometrically to the unique minimizer \(0\), with its gradient buffer converging to zero, from every initial iterate and buffer **if and only if**
\[
\boxed{\quad 0<\alpha<\alpha_*(\gamma,\rho)
:=\frac{4}{1+\gamma+\sqrt{(1+\gamma)^2-8\gamma(1-\gamma)\rho^2}}.\quad}
\]
At equality there is a nondecaying trajectory; for larger \(\alpha\) the iteration admits exponentially growing trajectories. The same necessity is witnessed by suitable nonzero initial iterates with an initially zero buffer. This is an exact global linear stability classification for the specified quadratic, not merely a sufficient bound.

The threshold has a nonmonotone geometric feature. For every fixed \(0<\gamma<1\), increasing \(|\rho|\) strictly *enlarges* the admissible learning-rate interval, even though the objective's condition number increases. Moreover, \(\alpha_*(\gamma,\rho)>2\) holds precisely when
\[
0<\gamma<\tfrac12
\quad\text{and}\quad
\rho^2>\frac{1}{2(1-\gamma)}.
\]
For example, at \(\gamma=1/4\) and \(\rho=99/100\), the stepsize \(\alpha=5/2\) is stable (the exact threshold is approximately \(2.574182422\)). In contrast, the memory-free case \(\gamma=0\) is stable only for \(\alpha<2\), independently of coupling.

## Assumptions and scope

The dimension is exactly two; all real couplings \(-1<\rho<1\) are admitted, including zero, and the starting iterate and gradient buffer are arbitrary finite real vectors. The objective is the displayed centered positive-definite quadratic; its Hessian eigenvalues are \(1-|\rho|\) and \(1+|\rho|\). The finite-difference perturbation \(\varepsilon>0\) is arbitrary and fixed; central differences equal partial derivatives exactly for every such \(\varepsilon\) because the objective is quadratic. The compute budget refreshes exactly one coordinate per step, with order \(1,2,1,2,\ldots\). Both buffer entries exist and the shared multiplicative decay \(\gamma\) is applied **before** refreshing the active entry.

For a current iterate \(x\) and stored gradient estimate \(g\), each elementary update acts by first setting \(g\leftarrow\gamma g\), then overwriting the active entry with \(\partial_i f_\rho(x)\), and finally setting \(x\leftarrow x-\alpha g\). Thus both components of the *iterate* change, even though only one buffer entry is refreshed. The sampling order is deterministic and no stochastic noise or line search is present.

## Proof

**1. Exact sweep dynamics.** At the start of a sweep (just before refreshing coordinate \(1\)), let \(h\) be the stored entry for coordinate \(2\). The old coordinate-\(1\) buffer entry plays no role, since it is immediately overwritten. One refresh of coordinate \(1\) yields
\[
\begin{aligned}
 x'_1&=x_1-\alpha(x_1+\rho x_2),\\
 x'_2&=x_2-\alpha\gamma h,\\
 g'_1&=x_1+\rho x_2,\qquad g'_2=\gamma h.
\end{aligned}
\]
After decay, coordinate \(2\) is refreshed using \(x'\): \(g''_1=\gamma(x_1+\rho x_2)\) and \(g''_2=x'_2+\rho x'_1\). The second full-vector update and retention of \(h''=g''_2\) give the exact three-dimensional sweep map \(z''=Tz\), where \(z=(x_1,x_2,h)^{\mathsf T}\) and
\[
T=\begin{pmatrix}
1-\alpha(1+\gamma)&-\alpha\rho(1+\gamma)&0\\
-\alpha\rho(1-\alpha)&1-\alpha+\alpha^2\rho^2&-\alpha\gamma(1-\alpha)\\
\rho(1-\alpha)&1-\alpha\rho^2&-\alpha\gamma
\end{pmatrix}.
\]
The removed fourth buffer coordinate is refreshed once each sweep and is a linear function of \(z\) after this first update. Hence the full stepwise algorithm converges for all initial data exactly when every eigenvalue of \(T\) lies strictly inside the unit disk. The same equivalence holds for geometric decay because intermediate steps are fixed linear maps of the sweep state.

**2. Characteristic polynomial and Schur test.** Direct determinant expansion gives \(\det(zI-T)=p(z)=z^3+bz^2+cz+d\), with
\[
\begin{aligned}
 b&=-2+2\alpha(1+\gamma)-\alpha^2\rho^2,\\
 c&=[1-\alpha(1+\gamma)]^2-2\alpha^2\gamma\rho^2,\\
 d&=-\alpha^2\gamma^2\rho^2.
\end{aligned}
\]
For a real monic cubic, the strict Schur conditions are
\[
|d|<1,\quad p(1)>0,\quad -p(-1)>0,\quad 1-c+bd-d^2>0.
\]
For completeness, when \(|d|<1\), the Schur transform \(\{p(z)-dz^3p(1/z)\}/z\) equals
\[
(1-d^2)z^2+(b-cd)z+(c-bd).
\]
The quadratic strict Schur conditions are a positive value at each of \(z=\pm1\) and its constant coefficient strictly below its positive leading coefficient. The former are equivalent to \(p(1)>0\) and \(-p(-1)>0\), respectively, after multiplying by \(1-d\) and \(1+d\); the latter is \(1-c+bd-d^2>0\).

Direct algebra factors these three critical quantities:
\[
\begin{aligned}
 p(1)&=\alpha^2(1+\gamma)^2(1-\rho^2)>0,\\
 -p(-1)&=[2-\alpha(1+\gamma)]^2+\alpha^2\rho^2(1-\gamma)^2,\\
 1-c+bd-d^2
 &=\alpha(1+\gamma)(1+\alpha\gamma\rho^2)Q(\alpha),\\
 Q(\alpha)&:=2-(1+\gamma)\alpha+\gamma(1-\gamma)\rho^2\alpha^2.
\end{aligned}
\]

**3. Resolution of all parameters, not just local sign tests.** First suppose \(0<\gamma<1\) and \(0<|\rho|<1\). The discriminant
\[
\Delta=(1+\gamma)^2-8\gamma(1-\gamma)\rho^2
\]
is strictly positive: its value is greater than or equal to \((1-3\gamma)^2\), and equality at zero would require the excluded singular coupling \(|\rho|=1\). Thus \(Q\) has two distinct positive roots. Its smaller root, by rationalizing the quadratic formula, is precisely \(\alpha_*(\gamma,\rho)\). The determinant bound \(|d|<1\) demands \(\alpha<1/(\gamma|\rho|)\); at that determinant boundary,
\[
Q\left(\frac{1}{\gamma|\rho|}\right)
=-\frac{(1+\gamma)(1-|\rho|)}{\gamma|\rho|}<0.
\]
Therefore the determinant boundary lies strictly between the two positive roots of \(Q\). Below the smaller root, all four Schur conditions hold; from that root onward, either \(Q\le0\) before the determinant boundary or \(|d|\ge1\) thereafter. The \(-p(-1)\) condition is strictly positive in the entire generic case. This proves the claimed exact criterion.

If \(\gamma=0\) or \(\rho=0\), the polynomial respectively has a zero root or the form \(p(z)=z[z-1+\alpha(1+\gamma)]^2\); in either case its strict Schur interval is \(0<\alpha<2/(1+\gamma)\) whenever \(\rho=0\), and \(0<\alpha<2\) when \(\gamma=0\) (even for \(\rho\ne0\)). If \(\gamma=1\), then \(Q(\alpha)=2(1-\alpha)\), giving \(0<\alpha<1\); at the boundary \(p(z)=(z+1)^2(z-\rho^2)\). These agree with the universal formula, including every endpoint.

At \(\alpha=\alpha_*\), at least one characteristic root has modulus one; the corresponding invariant mode yields a bounded but nondecaying (or, in degenerate cases, polynomially growing) state. For \(\alpha>\alpha_*\), the preceding strict inequalities fail with an unstable root outside the unit disk, yielding exponential growth for suitable real initial data. The nonconvergent modes genuinely affect the iterates: when \(\gamma>0\), a pure buffer-only sweep eigenvector can occur only at \(\alpha=1\), in which case its eigenvalue has modulus \(\gamma\); for \(\gamma=0\) any pure buffer-only mode has eigenvalue zero. At \(\gamma=1\), the buffer-only unit mode at \(\alpha=1\) nevertheless produces a nonzero intermediate iterate in the first half-sweep. Furthermore, if all zero-buffer initial iterates converged, the two-dimensional plane \(h=0\) would be contained in the stable invariant subspace and hence invariant whenever that subspace had dimension two. This is impossible because the displayed third row maps \(h=0\) to \(\rho(1-\alpha)x_1+(1-\alpha\rho^2)x_2\), whose two coefficients cannot simultaneously vanish when \(|\rho|<1\). If the stable subspace has smaller dimension, the conclusion is immediate. Thus arbitrary zero initialization of the buffer does not rescue the critical or unstable regime.

**4. Strict enlargement and the beyond-two frontier.** For \(0<\gamma<1\), the formula's denominator strictly decreases with increasing \(\rho^2\); hence the critical step strictly increases. The smaller root exceeds \(2\) exactly when \(Q(2)>0\) and \(2\) lies before the determinant ceiling. The former condition is \(2\gamma[2(1-\gamma)\rho^2-1]>0\); its feasibility forces \(\gamma<1/2\). In that range \(2<1/(\gamma|\rho|)\), establishing the asserted necessary and sufficient condition. Substituting \(\alpha=5/2\), \(\gamma=1/4\), and \(\rho=99/100\) gives \(Q(\alpha)=603/25600>0\) and \(\alpha^2\gamma^2\rho^2=9801/25600<1\), with the remaining Schur margins strictly positive.

## Verification

The standalone `verify.py` reproduces the two elementary update matrices, their exact three-variable sweep reduction, the cubic coefficients, the displayed Schur factorizations, special-case polynomials, and exactness of central differences. Symbolic identities are checked by `sympy`; representative interior, boundary, and exterior spectra are compared by `numpy` as supplemental diagnostics. Execute `python verify.py` from a directory containing the file with Python 3.10+, SymPy, and NumPy installed. A successful run prints `VERIFY_OK symbolic identities; 576 matrix-root checks; 6 boundary checks; central differences`. The inequalities and all infinite-iteration assertions rest on the foregoing analytic proof, not on the finite numerical tests.

## Relationship to prior work

Liang, Sun, Wang, and Rakita [1] introduce the exact fading/refresh/full-vector CoCD rule studied here and give general sufficient convergence/stability bounds (§§4–5, Appendix C), not an exact necessary-and-sufficient two-coordinate quadratic threshold. At zero decay their update becomes ordinary block cyclic coordinate descent; that classical limit is acknowledged, not presented as a new algorithm. The positive-decay, coupling-dependent stability surface and strict over-two region are the substantive new classification.

Gürbüzbalaban, Ozdaglar, and Parrilo [2] prove convergence for incremental aggregated gradients of *component functions* and give conservative stepsize controls. Here the coordinate vector fields \((x_1+\rho x_2,0)\) and \((0,x_2+\rho x_1)\) are not individually gradients of scalar component potentials for \(\rho\ne0\), as their mixed partial matrices are nonsymmetric. Moreover, the buffer's explicit multiplicative decay is different from the iterate-momentum mechanism in [2]. Accordingly [2] does not directly imply the sharp stated CoCD criterion. The underlying cubic Schur test itself is classical; the contribution is identifying its exact factorization for this algorithm and the resulting complete sharp transition.

## Limitations

The analysis is exact only for the specified two-coordinate quadratic with equal positive diagonal Hessian entries and cyclic one-coordinate updates. It is not a theorem for arbitrary dimensions, unequal diagonal curvature, stochastic refreshes, nonlinear losses, arbitrary variable rates, or an arbitrary stochastic zeroth-order oracle. It asserts **asymptotic linear stability**, not monotone objective decrease at each substep or an optimal convergence rate. No numerical sampling establishes originality; older analyses of periodically switched buffered systems could conceivably contain an equivalent spectral classification under different terminology, and independent checking has not been performed.

## References

[1] C. Liang, X. Sun, Q. Wang, and D. Rakita, *Turning Stale Gradients into Stable Gradients: Coherent Coordinate Descent with Implicit Landscape Smoothing for Lightweight Zeroth-Order Optimization*, arXiv:2605.14373, first posted 2026-05-14, especially equations (3), (5)–(7), §5.3, and Appendix D. https://arxiv.org/abs/2605.14373 .

[2] M. Gürbüzbalaban, A. Ozdaglar, and P. A. Parrilo, *On the Convergence Rate of Incremental Aggregated Gradient Algorithms*, arXiv:1506.02081 (2015); SIAM Journal on Optimization 27 (2017), 1035–1048. https://arxiv.org/abs/1506.02081 .

[3] S. J. Wright, *Coordinate Descent Algorithms*, Mathematical Programming 151 (2015), 3–34, DOI:10.1007/s10107-015-0892-3. Classical coordinate-descent background.
