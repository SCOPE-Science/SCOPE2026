# An Airy edge correction for Legendre compression of the Volterra operator

## Finding

Let \(J:L^2(0,1)\to L^2(0,1)\) be the integration operator \((Jf)(x)=\int_0^x f(t)\,dt\), over either real or complex scalars. Let \(P_n\) be the orthogonal projection onto polynomials of degree at most \(n\), using Lebesgue measure on \([0,1]\). Let \(a_1<0\) be the largest negative zero of the classical Airy function \(\operatorname{Ai}\). Then

\[
\boxed{\displaystyle\lim_{n\to\infty}n^{5/3}\left(\frac{1}{2n}-\|J-P_nJP_n\|_{L^2\to L^2}\right)=\frac{|a_1|}{2^{4/3}}.}
\]

Thus the sharp asymptotic includes an Airy boundary correction:
\[
\|J-P_nJP_n\|=\frac1{2n}-\frac{|a_1|}{2^{4/3}n^{5/3}}+o(n^{-5/3}).
\]

This quantifies the Galerkin error **in operator norm over all unit-norm inputs**, rather than for selected smooth solutions. By comparison, the best rank-\((n+1)\) approximation error is \(s_{n+2}(J)=1/(\pi(n+3/2))\), so the polynomial compression has an asymptotic optimality ratio \(\pi/2\).

## Assumptions and scope

The underlying Hilbert space is \(L^2((0,1),dx)\). Degree refers to ordinary polynomials, and \(P_n\) is the Hilbert orthogonal projector. The operator norm is the unrestricted induced Hilbert norm. The limit is over positive integers \(n\); the Airy zero is characterized by \(\operatorname{Ai}(a_1)=0\), \(a_1\approx-2.33810741046\). No assertion is made about other bases, weighted spaces, or pointwise regularity of inputs.

## Proof

**Step 1: an exact Jacobi tail.** Put \(p_k(x)=\sqrt{2k+1}\,L_k(2x-1)\), where \(L_k\) is the ordinary Legendre polynomial, so \((p_k)_{k\geq0}\) is orthonormal. The integrated Legendre recurrence yields, for \(k\geq1\),
\[
Jp_k=c_k p_{k+1}-c_{k-1}p_{k-1},\qquad c_k=\frac{1}{2\sqrt{(2k+1)(2k+3)}}.
\]
For \(k=0\), \(Jp_0=\tfrac12p_0+c_0p_1\). Consequently, \(E_n=J-P_nJP_n\) vanishes on the first \(n\) basis coordinates, and on indices \(k=n,n+1,\ldots\) its only nonzero entries are \((E_n)_{k+1,k}=c_k\) and \((E_n)_{k,k+1}=-c_k\). After multiplication by coordinatewise unit phases, \(E_n\) becomes \(i\) times a positive off-diagonal, self-adjoint compact Jacobi matrix. Hence
\[
4n\|E_n\|=\lambda_{\max}(B_n),\qquad
(B_n u)_m=b_{n,m-1}u_{m-1}+b_{n,m}u_{m+1},
\]
where \(m\geq0\), \(u_{-1}=0\), \(b_{n,-1}=0\), and
\[
b_{n,m}=4nc_{n+m}=\frac{2n}{\sqrt{(2n+2m+1)(2n+2m+3)}}\quad(m\geq0).
\]
Compactness follows from \(b_{n,m}\to0\) as \(m\to\infty\). Positivity and bipartite spectral symmetry imply that its norm equals its largest eigenvalue.

**Step 2: exact positive quadratic form.** For a finitely supported real or complex vector \(u\), direct expansion gives
\[
2\|u\|_2^2-\langle u,B_nu\rangle
=\sum_{m=0}^{\infty}b_{n,m}|u_{m+1}-u_m|^2
+\sum_{m=0}^{\infty}v_{n,m}|u_m|^2,
\]
where \(v_{n,m}=2-b_{n,m-1}-b_{n,m}\). Each term is nonnegative because \(0<b_{n,m}<1\). In particular \(v_{n,0}>1\). For fixed \(R<\infty\), uniformly for \(1\leq m\leq Rn^{1/3}\),
\[
b_{n,m}=1-\frac{m+1}{n}+O_R(n^{-4/3}),\qquad
v_{n,m}=\frac{2m+1}{n}+O_R(n^{-4/3}).
\]
Globally, elementary comparison with \(n/(n+m+1)\) gives an absolute \(c>0\) such that
\[
v_{n,m}\geq c\min\{m/n,1\}\quad (m\geq1,n\geq2).
\]

**Step 3: Airy limit of the lowest form value.** Set \(h=n^{-1/3}\) and
\[
q_n(u)=h^{-2}\bigl(2\|u\|_2^2-\langle u,B_nu\rangle\bigr),\qquad \|u\|_2=1.
\]
We show that \(\inf q_n\) tends to the lowest Dirichlet eigenvalue \(\mu\) of
\[
H=-\frac{d^2}{dx^2}+2x\quad\text{on }L^2(0,\infty),\qquad f(0)=0.
\]
For the upper bound, take any smooth compactly supported \(f\) with \(f(0)=0\), sample \(u_m=\sqrt h\,f(mh)\), and normalize. The exact form and the local expansions above give
\[
q_n(u)\longrightarrow\frac{\int_0^\infty(|f'|^2+2x|f|^2)dx}{\int_0^\infty|f|^2dx}.
\]
Density of such functions in the form domain proves \(\limsup\inf q_n\leq\mu\).

For the lower bound, take normalized almost-minimizers with bounded \(q_n\). The boundary term gives \(|u_0|^2\leq Ch^2\). Interpolate linearly the samples \(u_m/\sqrt h\) at the nodes \(mh\). On each fixed \([0,R]\), the first term of the form bounds the interpolants in \(H^1\), since \(b_{n,m}\to1\) locally. The boundary estimate forces their limiting trace at zero to vanish. The global potential bound implies
\[
\limsup_{n\to\infty}\sum_{m>R/h}|u_m|^2\leq C/R,
\]
so mass cannot escape to infinity. Local Rellich compactness and this tail bound give a strongly convergent subsequence in \(L^2(0,\infty)\) with a unit-norm limit \(f\in H^1_0(0,\infty)\). Local weak lower semicontinuity of the derivative energy, the expansion \(h^{-2}v_{n,m}\to2mh\), and monotone passage \(R\to\infty\) give
\[
\liminf q_n(u)\geq\int_0^\infty(|f'|^2+2x|f|^2)dx\geq\mu.
\]
Thus \(h^{-2}(2-\lambda_{\max}(B_n))\to\mu\).

**Step 4: Airy normalization.** The eigenvalue equation \(-f''+2xf=\mu f\) has its unique decaying solution proportional to \(\operatorname{Ai}(2^{1/3}x-2^{-2/3}\mu)\). The Dirichlet condition makes \(-2^{-2/3}\mu\) a negative Airy zero. The ground eigenvalue is \(\mu=2^{2/3}|a_1|\). Inserting \(\|E_n\|=\lambda_{\max}(B_n)/(4n)\) and \(h^2=n^{-2/3}\) gives precisely \(\lim n^{5/3}(1/(2n)-\|E_n\|)=\mu/4=|a_1|/2^{4/3}\).

For the final comparison, \(J^*J\) is unitarily equivalent to the Brownian covariance integral operator with kernel \(\min(x,y)\). Solving its elementary mixed-boundary Sturm–Liouville eigenproblem yields singular values \(s_j(J)=1/(\pi(j-\tfrac12))\), so the optimal rank-\((n+1)\) approximation error equals \(s_{n+2}(J)\). The ratio follows.

## Verification

The standalone file `check_legendre_airy.py` computes finite Jacobi eigenvalues directly from the stated coefficients and compares the scaled correction against \(|a_1|/2^{4/3}\). It also checks integrated Legendre recurrences numerically. The variational convergence argument above, not the finite tests, establishes the infinite-dimensional limit.

## Relationship to prior work

Classical singular-value theory of Volterra integration determines the best rank-\((n+1)\) approximation benchmark, but not the norm of the prescribed Legendre compression. Legendre spectral-Galerkin literature studies convergence of approximate solutions under smoothness hypotheses, rather than the unrestricted operator-norm error of the bare integration operator. General Airy-edge methods for Jacobi matrices motivate the boundary scaling, but the precise rational off-diagonal sequence and the constant for this Galerkin truncation require the specialized tail identification and quadratic-form limit above. This work does not claim the Airy variational method itself is new.

## Limitations

The result is asymptotic, with an \(o(n^{-5/3})\) remainder and no explicit all-dimensional bound on the remainder. It does not imply convergence at this rate for solutions with prescribed smoothness, nor does it provide higher Airy eigenvalue corrections. A relevant 1996 article on Volterra singular values was available only through its abstract and bibliographic record, so exhaustive historical priority has not been established. The existing spectrum of geometric weighted shifts exhibits a related but distinct Airy-edge phenomenon.

## References

1. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization **17** (1996), 453–461, DOI: 10.1080/01630569608816704. Bibliographic public-date evidence: 1996-12-04, https://portal.mardi4nfdi.de/wiki/Asymptottcs_of_singular_values_of_volterra_integral_operators.
2. Z. Wan, Y. Chen, Y. Huang, *Legendre spectral Galerkin method for second-kind Volterra integral equations*, Frontiers of Mathematics in China **4** (2009), 181–193, DOI: 10.1007/s11464-009-0002-z. Public full text: https://www.researchgate.net/publication/225528128_Legendre_spectral_Galerkin_method_for_second-kind_Volterra_integral_equations.
3. J. Shen and L.-L. Wang, *Error analysis for mapped Legendre spectral and pseudospectral methods*, SIAM J. Numer. Anal. **42** (2004), 326–349, DOI: 10.1137/S0036142903422065.
4. NIST DLMF, Airy functions, https://dlmf.nist.gov/9.
