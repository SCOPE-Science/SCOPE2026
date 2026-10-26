# Endpoint-driven quarter-power amplification in Chebyshev affine restriction

## Finding

For every fixed interval \([a,b]\) with \(-1\le a<b\le1\) and \([a,b]\ne[-1,1]\), let \(C_{[a,b]}p(x)=p(\alpha x+\beta)\), where \(\alpha=(b-a)/2\in(0,1)\) and \(\beta=(a+b)/2\). Let \(R_N(a,b)\) be its exact \((N+1)\)-dimensional representation in the *orthonormal* first-kind Chebyshev basis \(\phi_0=1/\sqrt\pi\), \(\phi_j=\sqrt{2/\pi}\,T_j\) for \(1\le j\le N\). Then there exist finite positive \(c_{a,b},C_{a,b}\) and an integer \(N_{a,b}\) such that for every integer \(N\ge N_{a,b}\),

\[
c_{a,b} N^{1/4}\le \|R_N(a,b)\|_{2\to2}\le C_{a,b} N^{1/4}.
\]

The exponent is sharp for every fixed nondegenerate *proper* interval. Moreover \(R_N\) is upper triangular and has eigenvalues \(1,\alpha,\ldots,\alpha^N\), so its spectral radius is exactly \(1\), independent of \(N\). Under iterated restriction one has the separate **exact** limit

\[
\lim_{k\to\infty}\|R_N(a,b)^k\|_{2\to2}
=\left(1+2\sum_{j=1}^{N}T_j(t_*)^2\right)^{1/2},
\qquad t_*=\frac{\beta}{1-\alpha}.
\]

The latter is of order \(N^{1/2}\) for fixed \([a,b]\): it equals \(\sqrt{2N+1}\) when \(a=-1\) or \(b=1\), and is \(\sqrt{N+O_{a,b}(1)}\) otherwise. For the full interval \([a,b]=[-1,1]\), the operator is the identity at every degree and all powers have norm \(1\).

The same two **growth orders**, but not necessarily the exact power-limit constant, hold for the usual unnormalized Chebyshev coefficient Euclidean norm, since that normalization differs by a fixed diagonal similarity whose condition number is \(\sqrt2\).

## Assumptions and scope

All polynomials may have real or complex coefficients; \(N\) is their maximum degree. The input and output norms are both the fixed full-interval Chebyshev Hilbert norm

\[
\|p\|_\mu^2=\int_{-1}^{1}\frac{|p(y)|^2}{\sqrt{1-y^2}}\,dy.
\]

The matrix norm is precisely the induced norm on this polynomial space in the orthonormal basis above. The constants in the quarter-power estimate depend on the fixed endpoints, and **are not uniform** as the interval degenerates or approaches the full interval. The theorem makes no claim that rounding errors necessarily grow at the same rate or that the complete Volterra solver is unstable. The iteration limit is first in the number of repetitions \(k\) at a fixed degree \(N\), not a simultaneous limit.

## Proof

**1. Exact change of measure.** The affine substitution \(y=\alpha x+\beta\) gives

\[
\|C_{[a,b]}p\|_\mu^2
=\int_a^b \frac{|p(y)|^2}{\sqrt{(y-a)(b-y)}}\,dy
=:\|p\|_\nu^2.
\]

Thus \(\|R_N\|^2\) is the largest ratio \(\|p\|_\nu^2/\|p\|_\mu^2\) over nonzero polynomials of degree at most \(N\). The output arcsine measure has square-root singularities at both subinterval endpoints. An endpoint equal to \(-1\) or \(1\) shares the input singularity; a strictly interior endpoint yields a new singularity in the density ratio.

**2. Upper bound.** Fix the proper interval. At least one of its endpoints lies in \((-1,1)\). Let \(E\) denote the nonempty set of strictly interior endpoints, and set \(\delta=1/N\). By Chebyshev orthonormality and \(|T_j(y)|\le1\), Cauchy--Schwarz yields the uniform Christoffel bound

\[
|p(y)|^2\le K_N(y,y)\,\|p\|_\mu^2
\le\frac{2N+1}{\pi}\,\|p\|_\mu^2
\quad(-1\le y\le1),
\]

where \(K_N(y,z)=1/\pi+(2/\pi)\sum_{j=1}^{N}T_j(y)T_j(z)\). For sufficiently large \(N\), the \(\nu\)-measure of the union of the one-sided \(\delta\)-neighborhoods of \(E\) is at most \(C_{a,b}\sqrt\delta\). Consequently, the integral over those neighborhoods is at most \(C_{a,b}(N+1)\sqrt\delta\,\|p\|_\mu^2=O_{a,b}(\sqrt N)\|p\|_\mu^2\).

On the complement, the density ratio relative to the input measure is

\[
\frac{d\nu}{d\mu}(y)
=\sqrt{\frac{1-y^2}{(y-a)(b-y)}}\,\mathbf1_{[a,b]}(y)
\le C_{a,b}\sqrt N.
\]

Indeed, each nonshared endpoint factor is at least \(\delta\); at a shared endpoint, its matching factor in \(1-y^2\) cancels the apparent singularity. Thus the complementary integral is also at most \(C_{a,b}\sqrt N\|p\|_\mu^2\). Together these show \(\|R_N\|^2\le C_{a,b}\sqrt N\).

**3. Matching lower bound.** Choose an interior endpoint \(e\in E\), and write \(e=\cos\theta_e\) with \(0<\theta_e<\pi\). The normalized reproducing-kernel polynomial

\[
q_N(y)=\frac{K_N(y,e)}{\sqrt{K_N(e,e)}}
\]

has \(\|q_N\|_\mu=1\) and

\[
K_N(e,e)=\frac{N+1}{\pi}+\frac1\pi\sum_{j=1}^N\cos(2j\theta_e)
=\frac N\pi+O_e(1).
\]

Using \(|\cos(j\theta)-\cos(j\theta_e)|\le j|\theta-\theta_e|\), one gets

\[
|K_N(\cos\theta,e)-K_N(e,e)|
\le\frac{N(N+1)}\pi|\theta-\theta_e|.
\]

It follows that, for all large \(N\), \(|q_N(y)|^2\ge c_e N\) throughout a one-sided interval of length \(c'_e/N\) abutting \(e\) *from within* \([a,b]\). On that interval, the output measure is bounded below by \(c_{a,b}|y-e|^{-1/2}dy\). Therefore

\[
\|q_N\|_\nu^2\ge c_{a,b}N\int_0^{c'_e/N}s^{-1/2}\,ds
\ge c''_{a,b}\sqrt N.
\]

Since \(\|q_N\|_\mu=1\), this proves \(\|R_N\|^2\ge c''_{a,b}\sqrt N\), completing the sharp quarter-power claim. This is an infinite-degree result proved analytically; numerical extrapolation is not used to establish the exponent.

**4. Triangular spectrum.** The polynomial \(T_j(\alpha x+\beta)\) has degree \(j\); comparison of its leading coefficient with that of \(T_j(x)\) gives diagonal Chebyshev coefficient \(\alpha^j\) (including \(j=0\)). The basis normalization is diagonal, so it does not alter diagonal entries. The matrix is therefore upper triangular with the asserted eigenvalues. Since \(\alpha\in(0,1)\), its spectral radius is \(1\), even though its singular norm diverges with degree.

**5. Exact power limit.** The affine map iterates as \(\ell^k(x)=t_*+\alpha^k(x-t_*)\), with \(t_*\in[-1,1]\). On each fixed degree space, \(R_N^k\) therefore converges in operator norm to the rank-one map \(p\mapsto p(t_*)\cdot1\). Because the norm of the constant function is \(\sqrt\pi\), and the norm of evaluation at \(t_*\) is \(\sqrt{K_N(t_*,t_*)}\), the limiting norm is exactly \(\sqrt{\pi K_N(t_*,t_*)}\), yielding the stated formula. If \(t_*=\pm1\), every \(T_j(t_*)^2=1\). Otherwise, \(T_j(t_*)=\cos(j\theta_*)\) with fixed \(0<\theta_*<\pi\), and a finite trigonometric geometric sum gives \(\sum_{j=1}^N\cos^2(j\theta_*)=N/2+O_{t_*}(1)\). This proves the square-root power-limit growth.

## Verification

The standalone `check.py` computes the exact polynomial-space norms through Gauss--Chebyshev quadrature: \(N+1\) nodes integrate the squared image of every degree-\(N\) polynomial exactly (algebraically, before floating-point rounding). It independently compares one-step norms across multiple intervals and degrees with the quarter-power scaling, checks the exact spectral diagonal of the restriction matrix, and tests numerical convergence of high powers against the closed-form reproducing-kernel evaluation norm. The code requires NumPy. Numerical checks exercise finite cases only; all uniform degree and limit statements follow from the argument above.

## Relationship to prior work

Chen and Xu [1, Section 2, Theorems 2.1--2.2] define this exact affine Chebyshev restriction matrix, prove its upper-triangular recurrence and give endpoint-entry formulas. They do **not** state the quarter-power growth of its induced orthonormal-coefficient norm or the exact limiting norm of its powers. Their numerical stability results concern assembled Volterra approximation methods, not uniform Euclidean bounds on a standalone restriction block. Standard Chebyshev orthogonality and reproducing kernels [3] are used as tools, not claimed as discoveries. Olver and Townsend [2] study conditioning of spectral differential-equation formulations; their abstract does not provide bounds for this affine restriction family. The result can equivalently be viewed as a comparison of full-interval and rescaled-subinterval arcsine \(L^2\) norms on polynomial subspaces; classical Jacobi-weight comparison theory is an important remaining possible source of stronger preexisting coverage.

In contrast, if both input and output use *unweighted Lebesgue* \(L^2\), affine substitution gives \(\|p\circ\ell\|_{L^2[-1,1]}\le\alpha^{-1/2}\|p\|_{L^2[-1,1]}\), uniformly in degree. The quarter-power blowup is therefore specifically driven by the mismatch of Chebyshev endpoint weights, rather than by restricting polynomials per se.

## Limitations

The result proves sharp growth *order*, not a leading constant for the one-step norm. It does not imply growth in a particular well-conditioned transformed basis or prove instability of the full spectral Volterra schemes in [1]. The constants need not be uniform across varying intervals, and the zero-length interval is excluded. The infinite-degree restriction map is unbounded on the full Chebyshev \(L^2\) space, but finite matrices are well defined. No statement about finite-precision algorithm performance or random coefficient distributions is made. Historical priority against all possible general weighted-polynomial comparison theorems has not been independently certified.

## References

[1] Xi Chen and Kuan Xu, *Fast spectral methods for Volterra integral equations*, arXiv:2610.20206v1 (first posted 2026-10-14), especially Section 2, equations (5)--(13), Section 7, and Appendix A. https://arxiv.org/html/2610.20206v1

[2] Sheehan Olver and Alex Townsend, *A fast and well-conditioned spectral method*, arXiv:1202.1347 (2012). https://arxiv.org/abs/1202.1347

[3] Gábor Szegő, *Orthogonal Polynomials*, American Mathematical Society Colloquium Publications 23 (1939), standard Chebyshev orthogonality and trigonometric identities.
