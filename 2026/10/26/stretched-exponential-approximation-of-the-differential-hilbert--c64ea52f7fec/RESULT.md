# Stretched-exponential approximation of the differential Hilbert operator

## Finding

For all real parameters \(-1<\alpha<0\) and \(\beta>\alpha+2\), the differential Hilbert operator
\[
(\mathcal H_2 f)(z)=\int_0^1\frac{f(t)}{(1-tz)^2}\,dt:\ A_\alpha^2\longrightarrow A_\beta^2
\]
admits explicit finite-rank approximants with rapidly decaying trace-norm errors. Put
\[
\theta=\frac14\min\{\beta-\alpha-2,-\alpha\}>0.
\]
For every pair of integers \(J,m\ge1\), there is a rank-at-most-\(Jm\) operator \(Q_{J,m}\), given below using the positive \(m\)-point Gauss–Legendre rule on \(J\) dyadic intervals, for which
\[
\|\mathcal H_2-Q_{J,m}\|_{\mathcal S_1}
\le C_{\alpha,\beta}\bigl(4^{-m}+2^{-J\theta}\bigr).
\tag{1}
\]
Consequently, after enlarging the parameter-dependent constant if needed, every singular value satisfies
\[
 s_n(\mathcal H_2)\le C_{\alpha,\beta}
 \exp\!\left[-\frac{\theta\log2}{2}\sqrt n\right],
 \qquad n\ge1.
\tag{2}
\]
In particular, \(\mathcal H_2\in\mathcal S_p(A_\alpha^2,A_\beta^2)\) for **every** \(p>0\), including \(0<p<1\). The rates in (1)–(2) are upper bounds, not asserted sharp.

## Assumptions and scope

The weighted Bergman Hilbert space \(A_\gamma^2\), \(\gamma>-1\), uses the normalized measure \((\gamma+1)(1-|z|^2)^\gamma dA(z)\) on the unit disk, with \(dA\) normalized to total area one. Its monomial squared norms are
\[
 w_k(\gamma)=\frac{\Gamma(\gamma+2)\Gamma(k+1)}{\Gamma(k+\gamma+2)},
 \qquad k=0,1,\ldots.
\]
Singular values are numbered in nonincreasing order starting at \(s_1\). All operators and Schatten ideals are between these two Hilbert spaces, including when \(p<1\). Constants may depend on the fixed parameters but not on \(J,m,n\). The endpoints \(\alpha=0\) and \(\beta=\alpha+2\) are excluded. The initial integral is defined on polynomials and extends as the operator given by the matrix below.

## Proof

**1. Exact analytic trace-class integrand.** In the normalized monomial bases, the matrix of \(\mathcal H_2\) is
\[
 B_{nk}=\frac{n+1}{n+k+1}
 \sqrt{\frac{w_n(\beta)}{w_k(\alpha)}}
 \qquad (n,k\ge0).
\tag{3}
\]
For complex \(|z|<1\) let \(T(z)\) be the rank-one operator whose matrix entries are
\[
 T(z)_{nk}=(n+1)\sqrt{\frac{w_n(\beta)}{w_k(\alpha)}}z^{n+k}.
\tag{4}
\]
This is a **holomorphic, trace-class-valued** map: writing \(u_n(z)=(n+1)\sqrt{w_n(\beta)}z^n\) and \(v_k(z)=z^k/\sqrt{w_k(\alpha)}\), it acts by \(T(z)x=u(z)\sum_k v_k(z)x_k\). The functional uses the coefficients \(v_k(z)\) without conjugating \(z\), so it is holomorphic. Its trace norm is \(\|u(z)\|_2\|v(z)\|_2\). A binomial-series identity gives
\[
 \|v(z)\|_2^2=(1-|z|^2)^{-\alpha-2},\qquad
 \|u(z)\|_2^2=F_\beta(|z|^2),
\quad F_\beta(r)=\sum_{n\ge0}(n+1)^2 w_n(\beta)r^n.
\tag{5}
\]
Stirling's ratio estimate implies \((n+1)^2w_n(\beta)\asymp(n+1)^{1-\beta}\). Summing this positive series gives, uniformly for \(0\le r<1\),
\[
 F_\beta(r)\le C_\beta
 \begin{cases}
 (1-r)^{\beta-2},&1<\beta<2,\\
 1+\log\frac1{1-r},&\beta=2,\\
 1,&\beta>2.
 \end{cases}
\tag{6}
\]
(Here \(\beta>\alpha+2>1\).) The definition of \(\theta\) leaves a strict positive margin in each case, including the logarithmic middle case; hence
\[
 \|T(z)\|_{\mathcal S_1}\le
 C_{\alpha,\beta}(1-|z|)^{-1+\theta}
 \qquad(|z|<1).
\tag{7}
\]
For real \(t\in[0,1)\), (7) is integrable. Entrywise integration of (4) yields (3), so the trace-class Bochner integral \(\int_0^1T(t)dt\) equals \(B\).

**2. Uniform dyadic Gaussian approximation.** Split \([0,1)\) into
\[
 I_j=[1-2^{-j},1-2^{-j-1}],\quad
 h_j=2^{-j-2},\quad c_j=1-3h_j,
 \qquad j=0,1,\ldots.
\tag{8}
\]
Thus \(t=c_j+h_jx\), \(-1\le x\le1\), parameterizes \(I_j\). For any \(|x|\le2\),
\[
 |c_j+h_jx|\le1-h_j,
\]
so \(G_j(x)=T(c_j+h_jx)\) is analytic in the disk \(|x|<3\) and, on \(|x|\le2\), satisfies
\[
 \|G_j(x)\|_{\mathcal S_1}\le C_{\alpha,\beta}h_j^{-1+\theta}.
\tag{9}
\]
By Banach-space-valued Cauchy estimates, the Taylor polynomial \(P_{j,2m-1}\) of \(G_j\) through degree \(2m-1\) obeys
\[
 \sup_{-1\le x\le1}
 \|G_j(x)-P_{j,2m-1}(x)\|_{\mathcal S_1}
 \le 2C_{\alpha,\beta}h_j^{-1+\theta}4^{-m}.
\tag{10}
\]
Let \((x_i,\omega_i)_{i=1}^m\) be the standard \(m\)-point Gauss–Legendre nodes and positive weights for \([-1,1]\). They obey \(\sum_i\omega_i=2\) and integrate polynomials of degree at most \(2m-1\) exactly. Consequently (10), positivity, and the triangle inequality imply
\[
 \left\|\int_{I_j}T(t)\,dt-
 h_j\sum_{i=1}^m\omega_iT(c_j+h_jx_i)
 \right\|_{\mathcal S_1}
 \le8C_{\alpha,\beta}h_j^\theta4^{-m}.
\tag{11}
\]
Set
\[
 Q_{J,m}=\sum_{j=0}^{J-1}h_j
 \sum_{i=1}^m\omega_iT(c_j+h_jx_i).
\tag{12}
\]
Each summand has rank one and real node argument in \((0,1)\), so \(\operatorname{rank}Q_{J,m}\le Jm\). Since \(\sum_{j\ge0}h_j^\theta<\infty\), summing (11) gives total quadrature error \(O_{\alpha,\beta}(4^{-m})\). The unapproximated tail satisfies by (7)
\[
 \left\|\int_{1-2^{-J}}^1T(t)\,dt\right\|_{\mathcal S_1}
 \le\frac{C_{\alpha,\beta}}\theta2^{-J\theta}.
\tag{13}
\]
Together (11)–(13) prove (1) without reliance on any finite-section experiment.

**3. Singular values.** Put \(J=m=k\). Equation (1) and the rank-approximation characterization of singular values on Hilbert space give
\[
 s_{k^2+1}(\mathcal H_2)
 \le C_{\alpha,\beta}\bigl(4^{-k}+2^{-k\theta}\bigr)
 \le C'_{\alpha,\beta}2^{-k\theta}.
\]
For \(n\ge4\) take \(k=\lfloor\sqrt{n-1}\rfloor\); then \(k\ge\sqrt n/2\). Monotonicity of singular values proves (2) for \(n\ge4\), and finitely many initial values are absorbed into the constant. Finally \(\sum_{n\ge1}\exp(-pc\sqrt n)<\infty\) for each \(p>0\), proving every asserted Schatten membership.

## Verification

The critical analytic steps are (3)–(7), the Banach-valued Cauchy remainder in (10), Gauss–Legendre exactness in (11), and the min–max/rank approximation step. Each follows under the stated parameter margins. The accompanying `check_operator.py` uses finite matrix sections, tests dyadic Gaussian approximation for three admissible parameter pairs, and reports singular values. These computations **illustrate** the quantitative construction but do not certify the infinite-dimensional bound; (1)–(2) follow from the preceding analytic proof.

Run the reproducible check with `python check_operator.py` (NumPy and SciPy required). Example: for \((\alpha,\beta)=(-1/2,7/4)\) and matrix size 100, the finite operator-norm errors at \(J=m=4,6,8,10\) are approximately \(2.26267,1.34558,0.502865,0.142445\), respectively. All entries in the checker's direct matrix are computed from (3).

## Relationship to prior work

Li and Zhou [1], Sections 2 and 4, identify exactly the weighted matrix (3) and the rank-one integral decomposition, and prove trace-class membership in the strict supercritical regime, equivalent to membership in all Schatten classes \(\mathcal S_p\) with \(p\ge1\) (Theorem 4.2). **Neither their theorem nor trace class alone gives (1), (2), or the quasi-Schatten range \(0<p<1\)**. The new step here is scale-uniform high-order quadrature of the analytic rank-one family, quantitatively balancing rank against its integrable boundary singularity. The one-space generalized Hilbert-operator results [2] treat a different mapping setup. Beckermann–Townsend [3] study finite structured matrices with dimension-dependent spectral decay; their stated finite-dimensional estimates do not imply the dimension-independent operator estimate (2). These comparisons do not rule out every unindexed general spectral approximation theorem.

## Limitations

The exponent \(\theta\log2/2\) is a deliberately conservative positive rate; no optimal exponent, converse lower bound, or singular-value asymptotic is established. Nothing is claimed at the noncompact equality case \(\beta=\alpha+2\), outside \(-1<\alpha<0\), or for non-Hilbert Bergman exponents. The numerical tests are finite truncations. A more general preexisting analytic-kernel approximation theorem could subsume this conclusion.

## References

1. S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672v1, first posted 2026-10-05. https://arxiv.org/html/2610.05672v1 . Especially Section 4, Lemma 4.1 and Theorem 4.2.
2. J. Á. Peláez and D. Seco, *Schatten classes of generalized Hilbert operators*, arXiv:1510.05455, first posted 2015. https://arxiv.org/abs/1510.05455 .
3. B. Beckermann and A. Townsend, *On the singular values of matrices with displacement structure*, arXiv:1609.09494v1, first posted 2016. https://arxiv.org/html/1609.09494v1 .
