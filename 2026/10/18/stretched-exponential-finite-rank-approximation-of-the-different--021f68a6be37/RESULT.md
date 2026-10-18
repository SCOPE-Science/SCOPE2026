# Stretched-exponential finite-rank approximation of the differential Hilbert operator

## Finding
Let \(\mathcal H_2:A^2_\alpha\to A^2_\beta\) be the differential Hilbert operator. Whenever \(-1<\alpha<0\) and \(\beta>\alpha+2\), define
\[
\delta=\beta-\alpha-2>0,\qquad h=\frac14\min\{\delta,-\alpha\}>0.
\]
There is a constant \(C_{\alpha,\beta}\) such that for every pair of integers \(J,m\ge1\) an explicit operator \(Q_{J,m}\) with rank at most \(Jm\) satisfies
\[
\|\mathcal H_2-Q_{J,m}\|_{A^2_\alpha\to A^2_\beta}
\le C_{\alpha,\beta}(2^{-m}+2^{-hJ}). \tag{1}
\]
In particular, writing singular values in decreasing order, the choice \(J=m\) gives
\[
s_{m^2+1}(\mathcal H_2)\le 2C_{\alpha,\beta}2^{-hm},\qquad m\ge1. \tag{2}
\]
Consequently, for suitable positive constants \(C'_{\alpha,\beta},c_{\alpha,\beta}\),
\[
s_n(\mathcal H_2)\le C'_{\alpha,\beta}e^{-c_{\alpha,\beta}\sqrt n}\quad(n\ge1),\qquad
\mathcal H_2\in\mathcal S_p(A^2_\alpha,A^2_\beta)\quad\text{for every }p>0. \tag{3}
\]
The quasi-Schatten range \(0<p<1\) and the quantitative finite-rank construction are included. No matching singular-value lower bound is asserted.

## Assumptions and scope
For every \(\gamma>-1\), let \(A_\gamma^2\) consist of analytic functions on the open unit disk, with
\[
\|f\|^2_{A^2_\gamma}=\frac{\gamma+1}{\pi}\int_{|z|<1}|f(z)|^2(1-|z|^2)^\gamma\,dx\,dy.
\]
The monomials are orthogonal, with squared norms
\[
w_n(\gamma)=\frac{\Gamma(\gamma+2)\Gamma(n+1)}{\Gamma(n+\gamma+2)}\quad(n\ge0).
\]
Define \(\mathcal H_2f(z)=\int_0^1 f(t)/(1-tz)^2\,dt\), initially on polynomials and then by its bounded extension in the stated region. The singular values \(s_n\) and operator norms are those of the indicated Hilbert-space map. The result concerns strict compactness parameters \(-1<\alpha<0\) and \(\beta>\alpha+2\), with no uniformity of constants as parameters approach the boundary.

## Proof
**Step 1: An analytic rank-one kernel.** Express the operator in the normalized monomial orthonormal bases. Its matrix is
\[
B_{nk}=(n+1)\sqrt{\frac{w_n(\beta)}{w_k(\alpha)}}\int_0^1t^{n+k}\,dt
=\frac{n+1}{n+k+1}\sqrt{\frac{w_n(\beta)}{w_k(\alpha)}}.
\]
For \(|z|<1\) define an operator-valued holomorphic function \(K(z):\ell^2\to\ell^2\) by
\[
(K(z)x)_n=(n+1)\sqrt{w_n(\beta)}z^n\sum_{k\ge0}\frac{z^kx_k}{\sqrt{w_k(\alpha)}}.
\]
The series converge in the appropriate vector and dual-functional norms uniformly on compact subsets of \(|z|<1\). Each \(K(z)\) has rank one, and at real \(0\le t<1\), \(B=\int_0^1K(t)\,dt\) entrywise. The operator norm has the exact product expression
\[
\|K(z)\|=\left[F_\beta(|z|^2)(1-|z|^2)^{-\alpha-2}\right]^{1/2},\quad
F_\beta(s)=\sum_{n\ge0}(n+1)^2w_n(\beta)s^n.
\]
Here \(\sum_{k\ge0}s^k/w_k(\alpha)=(1-s)^{-\alpha-2}\) is the binomial series. In the Hilbert space with complex scalars, the functional in the definition of \(K(z)\) is complex-linear in \(x\), so \(K\) is genuinely holomorphic despite the usual conjugate notation for an adjoint.

**Step 2: The integrable holomorphic majorant.** Gamma-ratio asymptotics give \((n+1)^2w_n(\beta)=O((n+1)^{1-\beta})\). Since \(\beta>\alpha+2>1\), comparison with geometric power sums yields as \(s\uparrow1\)
\[
F_\beta(s)=\begin{cases}
O((1-s)^{\beta-2}),&1<\beta<2,\\
O(1+\log(1/(1-s))),&\beta=2,\\
O(1),&\beta>2.
\end{cases}
\]
When \(1<\beta<2\), the resulting kernel norm is \(O((1-|z|)^{-1+\delta/2})\); for \(\beta>2\) it is \(O((1-|z|)^{-1+(-\alpha)/2})\). For \(\beta=2\), it is this latter power times \(\sqrt{1+\log(1/(1-|z|))}\). In every case the choice \(h=\frac14\min\{\delta,-\alpha\}\) leaves a strictly positive power margin (including the logarithmic case), so there exists \(M=M_{\alpha,\beta}<\infty\) such that
\[
\|K(z)\|\le M(1-|z|)^{h-1}\qquad(|z|<1). \tag{4}
\]
Because \(h>0\), \(K(t)\) is Bochner-integrable in the trace-class norm on \([0,1)\); the entrywise integral therefore equals the bounded operator \(B\).

**Step 3: An explicit multiscale quadrature approximant.** Partition \([0,1)\) into the dyadic intervals
\[
I_j=[1-2^{-j},\,1-2^{-j-1}],\qquad j=0,1,2,\ldots .
\]
Their centers, half-lengths and Cauchy-circle radii are
\[
c_j=1-3\cdot2^{-j-2},\qquad \ell_j=2^{-j-2},\qquad R_j=2\ell_j=2^{-j-1}.
\]
The disk \(\{|z-c_j|\le R_j\}\) lies in \(|z|\le1-2^{-j-2}\). By (4), on this disk \(\|K(z)\|\le M2^{(j+2)(1-h)}\). Cauchy's operator-valued coefficient estimate shows that the Taylor polynomial \(P_{j,m-1}\) of degree \(m-1\) about \(c_j\) satisfies, for all \(t\in I_j\),
\[
\|K(t)-P_{j,m-1}(t)\|\le2M2^{(j+2)(1-h)}2^{-m}. \tag{5}
\]
Let \(t_{j,\nu},\omega_{j,\nu}\), \(1\le\nu\le m\), be the standard \(m\)-point Gauss–Legendre nodes and positive weights on \(I_j\); in particular \(\sum_\nu\omega_{j,\nu}=|I_j|=2^{-j-1}\), and the rule integrates \(P_{j,m-1}\) exactly. Define
\[
Q_{J,m}=\sum_{j=0}^{J-1}\sum_{\nu=1}^{m}\omega_{j,\nu}K(t_{j,\nu}). \tag{6}
\]
Every summand has rank one, so \(\operatorname{rank}Q_{J,m}\le Jm\). Subtracting the polynomial before comparing each quadrature integral, using positivity of weights and (5), gives
\[
\left\|\int_{I_j}K(t)\,dt-\sum_{\nu=1}^{m}\omega_{j,\nu}K(t_{j,\nu})\right\|
\le 4M |I_j|2^{(j+2)(1-h)}2^{-m}
\le C_1 2^{-hj}2^{-m}.
\]
The error over the first \(J\) intervals is at most \(C_2 2^{-m}\), since \(\sum_{j\ge0}2^{-hj}<\infty\). The uncovered tail is bounded by
\[
\left\|\int_{1-2^{-J}}^1K(t)\,dt\right\|
\le M\int_{1-2^{-J}}^1(1-t)^{h-1}\,dt=\frac{M}{h}2^{-hJ}.
\]
Combining the two bounds proves (1).

**Step 4: Spectral consequences.** Approximation numbers equal singular values for operators between Hilbert spaces, so an operator of rank at most \(Jm\) whose distance to \(B\) is bounded by the right-hand side of (1) implies
\[
s_{Jm+1}(B)\le C_{\alpha,\beta}(2^{-m}+2^{-hJ}).
\]
As \(0<h<1\), taking \(J=m\) yields (2). Monotonicity of singular values, with \(m=\lfloor\sqrt{n-1}\rfloor\) and adjustment of finitely many indices, implies the stated stretched-exponential estimate (3). Finally \(\sum_{n\ge1}e^{-pc\sqrt n}<\infty\) for every real \(p>0\), proving all Schatten and quasi-Schatten memberships. \(\square\)

## Verification
The standalone standard-library program `verify.py` reconstructs the monomial weights in two independent ways, checks positivity and polynomial moments of the dyadic Gauss–Legendre quadrature, and compares its finite matrix against the integral formula for four parameter pairs spanning the three regimes \(1<\beta<2\), \(\beta=2\) and \(\beta>2\). It makes 512 assertions and prints `CHECKS_OK` when successful. These floating-point finite truncation checks are diagnostic only; the infinite-dimensional estimates are proved by the analytic steps above.

## Relationship to prior work
Li and Zhou [1] prove exactly which weighted Hilbert-space parameters give boundedness and compactness of the differential Hilbert operator and establish \(\mathcal S_p\) membership for \(1\le p<\infty\). Their Section 4 supplies the rank-one integral but not the dyadic quadrature singular-value estimate, nor the quasi-Schatten range \(0<p<1\). The present assertion is not a corollary of trace-class membership alone: \(\mathcal S_1\not\subset\mathcal S_p\) for \(0<p<1\). Ye and Feng [2] classify boundedness and compactness for related measure-defined Hilbert operators, without a corresponding singular-number theorem. Kindermann [3] gives bounds for symmetric generalized Hilbert matrices, not this two-weight nonsymmetric matrix; his generic upper estimates do not give (1). Finite-dimensional structured matrix estimates [4] have an explicit dimension-dependent rate and cannot directly imply the stated uniform infinite-operator bound.

## Limitations
The theorem gives an upper estimate on singular values, not an exact asymptotic or a matching lower bound. The positive constants depend on the fixed weights \(\alpha,\beta\) and may diverge at the compactness boundary. The quadrature formula is a constructive approximation, not an optimal-rank algorithm. The finite numerical checks do not certify the infinite proof. Complete originality against all unindexed literature is not guaranteed; the comparison with related structured-matrix results is necessarily limited by access to some full texts. No independent audit has been performed.

## References
[1] S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672v1 (first posted 2026-10-05), especially Sections 2–4. https://arxiv.org/html/2610.05672v1

[2] S. Ye and G. Feng, *Generalized Hilbert Operator Acting on Weighted Bergman Spaces and on Dirichlet Spaces*, arXiv:2207.11176v1 (2022), Sections 4–5. https://arxiv.org/html/2207.11176v1

[3] S. Kindermann, *On the type of ill-posedness of generalized Hilbert matrices and related operators*, arXiv:2402.05503v1 (2024), Theorems 1 and 5. https://arxiv.org/html/2402.05503v1

[4] B. Beckermann and A. Townsend, *On the Singular Values of Matrices with Displacement Structure*, SIAM Journal on Matrix Analysis and Applications (2017), DOI:10.1137/16M1096426; abstract and bibliographic information consulted. https://doi.org/10.1137/16M1096426
