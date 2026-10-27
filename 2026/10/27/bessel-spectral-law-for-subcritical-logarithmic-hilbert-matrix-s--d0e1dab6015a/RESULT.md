# Bessel spectral law for subcritical logarithmic Hilbert-matrix sections

## Finding
Let \(1<\alpha<2\) and let \(A^2_{\log^\alpha}\) be the analytic Hilbert space on the unit disk with norm
\[
\|f\|_{\alpha}^{2}=\int_{\mathbb D}|f(z)|^2\left(\log\frac{e}{1-|z|^2}\right)^\alpha\frac{dx\,dy}{\pi}.
\]
Let \(A^2\) carry normalized unweighted area norm. For an integer \(N\ge0\), let \(P_N\) be orthogonal projection onto analytic polynomials of degree at most \(N\), understood in the appropriate source or target space. On polynomials define the Hilbert-matrix transform
\[
(\mathcal H f)(z)=\sum_{m\ge0}\left(\sum_{n=0}^N\frac{a_n}{m+n+1}\right)z^m,\qquad f(z)=\sum_{n=0}^Na_nz^n.
\]
Write \(s_j(T)\) for singular values in nonincreasing order, including multiplicity, and \(j_{\nu,j}\) for the \(j\)-th strictly positive zero of the classical Bessel function \(J_\nu\). Set
\[
\nu=\frac{\alpha-1}{2-\alpha},\qquad L_N=\log(N+2).
\]
Then, **for each fixed positive integer \(j\)**,
\[
\boxed{\lim_{N\to\infty}\frac{s_j(\mathcal H P_N:A^2_{\log^\alpha}\to A^2)}{L_N^{\,1-\alpha/2}}=\frac{2}{(2-\alpha)j_{\nu,j}}.}
\]
The identical limit holds if the target is simultaneously compressed, replacing \(\mathcal H P_N\) by \(P_N\mathcal H P_N\). More strongly, after natural logarithmic coordinate identifications, the normalized finite matrices converge in **Hilbert–Schmidt norm** to the compact weighted Volterra operator
\[
(V_\alpha g)(x)=\int_x^1y^{-\alpha/2}g(y)\,dy\quad(0<x<1).
\]
In particular, the **entire normalized squared singular-value mass** converges:
\[
\boxed{\lim_{N\to\infty}\frac{\|\mathcal H P_N\|_{\mathcal S_2}^2}{L_N^{\,2-\alpha}}=\frac1{2-\alpha}.}
\]
These are asymptotic statements for the *bounded polynomial-section maps*; no bounded global map \(A^2_{\log^\alpha}\to A^2\) is asserted.

## Assumptions and scope
The exponent is real and satisfies \(1<\alpha<2\); the source Hilbert space is complex, and the boundary measure is the normalized area \(dx\,dy/\pi\). The parameter \(j\) is held fixed as \(N\to\infty\), not allowed to increase with \(N\). The singular values refer to operators between their stated, generally different, Hilbert norms. All logarithms are natural. If an operator has finite-dimensional source, its Hilbert–Schmidt norm is the square root of the sum of the squared singular values. The positive Bessel zeros are enumerated strictly increasingly. The Bessel characterization of the continuous weighted Volterra operator is established prior literature, and is used here as a known exact spectral formula; the new transfer is to logarithmically weighted Hilbert-matrix polynomial sections.

## Proof
**1. Reduction to a concrete finite matrix.** Monomial orthogonality yields
\[
\|\textstyle\sum a_nz^n\|_\alpha^2=\sum_{n\ge0}v_n|a_n|^2,\quad v_n=\int_0^1t^n\left(1-\log(1-t)\right)^\alpha dt,
\]
while \(\|\sum b_mz^m\|_{A^2}^2=\sum_{m\ge0}|b_m|^2/(m+1)\). The elementary logarithmic beta-moment asymptotic is
\[
v_n=\frac{(\log(n+2))^\alpha}{n+1}(1+o(1))\qquad(n\to\infty).
\]
It follows, for example, by substituting \(u=(n+1)(1-t)\), splitting at \(u\) of moderate size, and applying dominated convergence after division by \((\log(n+1))^\alpha/(n+1)\). This is also an established lemma in the motivating paper [1].

Initially replace \(v_n\) by the model moments \(\widehat v_n=(\log(n+2))^\alpha/(n+1)\). The normalized square section becomes
\[
M^{(N)}_{mn}=\frac{\sqrt{(n+1)/(m+1)}}{(m+n+1)(\log(n+2))^{\alpha/2}},\qquad0\le m,n\le N.
\]
The actual matrix \(B^{(N)}\) has \(B^{(N)}_{mn}=M^{(N)}_{mn}\sqrt{\widehat v_n/v_n}\). The same formula with all \(m\ge0\) describes the polynomial-source, unrestricted-output map.

**2. Tightness near the first logarithmic coordinate.** For each \(n\ge0\), splitting the sum over \(m\le n\) and \(m>n\) gives
\[
\sum_{m=0}^\infty |M_{mn}|^2
=\frac{n+1}{(\log(n+2))^\alpha}
\sum_{m=0}^\infty\frac1{(m+1)(m+n+1)^2}
\le\frac{C_\alpha(\log(n+2))^{1-\alpha}}{n+1}.
\]
The first piece uses \(m+n+1\ge n+1\), and the second uses \(m+n+1\ge m+1\). Because \(1<\alpha<2\), integral comparison implies, uniformly for \(N\) large and \(0<\varepsilon<1\),
\[
L_N^{\alpha-2}\sum_{n+2\le\exp(\varepsilon L_N)}\sum_{m=0}^N|M_{mn}|^2
\le C_\alpha\varepsilon^{\,2-\alpha}+o_N(1).
\]
The limit weighted Volterra kernel has the corresponding small-column mass
\[
\int_0^\varepsilon\int_0^y y^{-\alpha}\,dx\,dy
=\frac{\varepsilon^{\,2-\alpha}}{2-\alpha}.
\]
This tail estimate is what permits an infinite-dimensional limit, rather than extrapolation from finite singular values.

**3. Hilbert–Schmidt convergence.** Put \(T=L_N\), \(\Delta_n=\log((n+2)/(n+1))\), and
\[
I_{n,T}=\left[\frac{\log(n+1)}T,\frac{\log(n+2)}T\right),\quad 0\le n\le N.
\]
These intervals partition \([0,1)\). Identify the \(n\)-th coordinate vector with the normalized indicator \(e_{n,T}=\sqrt{T/\Delta_n}\,\mathbf1_{I_{n,T}}\) in \(L^2(0,1)\). Extend the rescaled finite matrix \(T^{\alpha/2-1}M^{(N)}\) by zero on the orthogonal complement of this step subspace. Its integral kernel is, for \(x\in I_{m,T}\) and \(y\in I_{n,T}\),
\[
K_T(x,y)=\frac{n+1}{m+n+1}\,
\frac{1}{\sqrt{(m+1)\Delta_m}\sqrt{(n+1)\Delta_n}}
\left(\frac T{\log(n+2)}\right)^{\alpha/2}.
\]
For almost all \((x,y)\in(0,1)^2\) with \(x\ne y\), one has
\[
K_T(x,y)\longrightarrow\mathbf1_{\{x<y\}}y^{-\alpha/2}.
\]
Indeed, \((n+1)\Delta_n\to1\), \(\log(n+2)/T\to y\), and \((n+1)/(m+n+1)\to\mathbf1_{\{x<y\}}\), whenever \(x,y>0\) are fixed and distinct. On \(y\ge\varepsilon>0\) the kernels are uniformly bounded for all sufficiently large \(T\): the two square-root factors are bounded independently of indices, and \(T/\log(n+2)\le 2/\varepsilon\). Dominated convergence on that region, combined with the two small-column estimates in Step 2, gives
\[
\boxed{\|K_T-\mathbf1_{\{x<y\}}y^{-\alpha/2}\|_{L^2((0,1)^2)}\longrightarrow0.}
\]
Thus the zero-extended matrix converges in Hilbert–Schmidt norm to \(V_\alpha\), which is compact because \(\|V_\alpha\|_{\mathcal S_2}^2=\int_0^1y^{1-\alpha}dy=(2-\alpha)^{-1}\).

**4. Replacement by the exact analytic-space norm.** The moment asymptotic implies \(d_n:=\sqrt{\widehat v_n/v_n}\to1\). For any fixed \(n_0\), the contribution to \(\|T^{\alpha/2-1}(B^{(N)}-M^{(N)})\|_{\mathcal S_2}\) from \(n<n_0\) is \(O_{n_0}(T^{\alpha/2-1})=o(1)\), by the column bound in Step 2. For \(n\ge n_0\), its norm is at most \(\sup_{n\ge n_0}|d_n-1|\) times the uniformly bounded Hilbert–Schmidt norm of \(T^{\alpha/2-1}M^{(N)}\). First let \(N\to\infty\), then \(n_0\to\infty\). The perturbation therefore tends to zero in Hilbert–Schmidt norm.

**5. The unrestricted output tail does not alter the limit.** For all \(n\le N\), direct estimation of the coefficient matrix gives
\[
\sum_{m>N}|B_{mn}|^2
=\frac1{v_n}\sum_{m>N}\frac1{(m+1)(m+n+1)^2}
\le\frac C{N^2v_n}.
\]
As \(v_n\asymp(\log(n+2))^\alpha/(n+1)\), the elementary sum estimate \(\sum_{n\le N}v_n^{-1}\le C_\alpha N^2/(\log(N+2))^\alpha\) shows
\[
\sum_{m>N}\sum_{n=0}^N|B_{mn}|^2=O_\alpha(L_N^{-\alpha})=o(L_N^{2-\alpha}).
\]
Thus the normalized full-output operator and its compressed section have vanishing Hilbert–Schmidt difference. Their fixed-index singular values have the same limits.

**6. Exact spectrum of the Volterra limit.** Set \(\sigma=1-\alpha/2>0\). The nonzero singular spectrum of \(V_\alpha\) is the previously known Bessel spectrum [2]. For completeness, if \(V_\alpha^*V_\alpha f=s^2f\), write \(u=V_\alpha f\); then \(u'=-x^{-\alpha/2}f\) and differentiation of the adjoint equation gives
\[
(x^\alpha u')'+s^{-2}u=0,\qquad u(1)=0,\quad\lim_{x\downarrow0}x^\alpha u'(x)=0.
\]
The admissible solution is proportional to
\[
x^{(1-\alpha)/2}J_{\nu}\left(\frac{x^\sigma}{\sigma s}\right),\qquad \nu=\frac{\alpha-1}{2-\alpha}.
\]
(The linearly independent branch fails the flux condition at zero.) The condition \(u(1)=0\) is exactly \(J_\nu(1/(\sigma s))=0\). Therefore
\[
s_j(V_\alpha)=\frac1{\sigma j_{\nu,j}}=\frac{2}{(2-\alpha)j_{\nu,j}}.
\]
This spectrum is simple and consists of positive eigenvalues decreasing to zero. Hilbert–Schmidt convergence implies convergence in operator norm; the standard singular-value perturbation inequality \(|s_j(A)-s_j(B)|\le\|A-B\|\) proves the asserted fixed-index laws. Norm convergence in \(\mathcal S_2\) also yields the squared-mass formula.

## Verification
The complete proof depends on the exact coefficient normalization, the summable column bound, and the logarithmic-step kernel identity; these provide analytical Hilbert–Schmidt convergence without assuming any rate from numerics. The Sturm–Liouville reduction reproduces the pre-existing Bessel singular-value formula. The accompanying standalone Python checker verifies selected finite matrix entries, their kernel-representation identities, the limiting Bessel constants, and monotone numerical trends on finite examples. Its finite examples are illustrative, not proofs of the asymptotic limits.

## Relationship to prior work
Norrbo [1] proved the critical boundedness threshold for the Hilbert matrix into \(A^2\): logarithmic exponent \(\alpha=2\) is bounded, and the untruncated mapping fails for \(\alpha<2\). That mapping-property dichotomy neither gives a sharp growth rate for the finite polynomial sections below the threshold nor determines their fixed-index singular values. Böttcher and Dörfler [2], notably their Theorem 5.1, previously computed the exact Bessel singular spectrum for the relevant family of weighted Volterra operators; the present argument uses this established fact and proves that the rescaled *Hilbert matrices* converge to that model.

Published analyses of this logarithmic Hilbert matrix establish compactness for \(\alpha>2\), essential norm \(2\) at \(\alpha=2\), and a critical Copson/Fredholm model. These concern a different exponent regime and do not imply the subcritical Bessel constants, which require the new logarithmic-step Hilbert–Schmidt limit. Standard finite Cesàro singular-value asymptotics concern a different matrix and a bounded spectral-edge regime. Targeted searches did not identify a mathematical statement equivalent to the asserted all-fixed-index subcritical law, although historical priority remains subject to independent confirmation.

## Limitations
Only real \(1<\alpha<2\) and each fixed \(j\) are covered. The theorem does not give uniform asymptotics for \(j\) growing with \(N\), nor the critical \(\alpha=2\) or supercritical \(\alpha>2\) cases. It characterizes the singular values of finite polynomial input sections, not the unbounded full operator. The rate of convergence to the Bessel profile is not quantified. Search-based originality assessment cannot exclude unindexed earlier equivalent findings; independent validation remains outstanding.

## References
1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1, first public version 2026-09-23, especially logarithmic moment asymptotics and the critical threshold. https://arxiv.org/abs/2610.00252
2. A. Böttcher and P. Dörfler, *Weighted Markov-type inequalities, norms of Volterra operators, and zeros of Bessel functions*, author-hosted preprint, 2009, Theorem 5.1 (known weighted-Volterra singular spectra). https://www.tu-chemnitz.de/mathematik/preprint/2009/PREPRINT_01.pdf
3. B. Karapetrović, *Libera and Hilbert matrix operator on logarithmically weighted Bergman, Bloch and Hardy-Bloch spaces*, Czechoslovak Mathematical Journal 68 (2018), 559–576, DOI:10.21136/CMJ.2018.0555-16 (earlier boundedness setting).
