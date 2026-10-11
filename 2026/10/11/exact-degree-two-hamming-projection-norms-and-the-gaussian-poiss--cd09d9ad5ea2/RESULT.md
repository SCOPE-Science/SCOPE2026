# Exact degree-two Hamming projection norms and the Gaussian–Poisson crossover

## Finding
For every alphabet size \(q\ge3\) (not necessarily a prime power) and integer \(n\ge2\), equip \(X=\{0,\ldots,q-1\}^n\) with uniform measure. Let \(P_2\) be the orthogonal projection onto the degree-two Hamming harmonic space: tensors that are mean-zero in exactly two coordinates and constant in all others. Its dimension is \(\binom n2(q-1)^2\).

Put \(p=(q-1)/q\), define
\[
 K_{n,q}(d)=\frac12\left(\big((q-1)n-qd\big)^2-(q-2)\big((q-1)n-qd\big)-n(q-1)\right),\quad 0\le d\le n,
\]
and let \(L\) and \(U\) be the first and last integers in \(\{0,\ldots,n\}\) for which \(K_{n,q}(d)<0\). The negative set is nonempty and is precisely \(\{L,\ldots,U\}\). Explicitly, with
\[
 \alpha_{\pm}=\frac{q-2\pm\sqrt{(q-2)^2+4n(q-1)}}2,
 \qquad d_{\pm}=\frac{(q-1)n-\alpha_{\mp}}q,
\]
one has \(L=\max\{0,\lfloor d_-\rfloor+1\}\) and \(U=\min\{n,\lceil d_+\rceil-1\}\). For integers \(t\), set
\[
 b(t)=\begin{cases}\binom{n-2}{t}p^t(1-p)^{n-2-t},&0\le t\le n-2,\\0,&\text{otherwise}.\end{cases}
\]
Then the **exact sharp endpoint norm**, with either normalized or unnormalized counting \(\ell^1\) and \(\ell^\infty\) conventions, is
\[
 \boxed{\|P_2\|_{\ell^1\to\ell^1}=\|P_2\|_{\ell^\infty\to\ell^\infty}
 =2\binom n2p^2\big[b(L-1)-b(L-2)-b(U)+b(U-1)\big].}
\]
Thus a potentially \((n+1)\)-term absolute Krawtchouk sum collapses to four binomial boundary masses.

This family has a precise change of asymptotic behavior when the alphabet grows with dimension. For any sequence of admissible integers with \(n/q\to\infty\),
\[
 \boxed{\frac{\|P_2\|}{n(q-1)}\longrightarrow \sqrt{\frac{2}{\pi e}}.}
\]
In contrast, when \(q\to\infty\) and \(n/q\to\lambda\in(0,\infty)\),
\[
 \boxed{\frac{\|P_2\|}{n(q-1)}\longrightarrow
 \Phi(\lambda):=\frac1{2\lambda}\sum_{k=0}^{\infty}\frac{e^{-\lambda}\lambda^k}{k!}
 \left|k(k-1)-2\lambda k+\lambda^2\right|.}
\]
The limit is the normalized absolute second Charlier moment, not the Gaussian constant. In particular,
\[
 \Phi(\lambda)=\lambda e^{-\lambda}(2-\lambda),\qquad
 0<\lambda<2-\sqrt2,
\]
and \(\Phi\) has a genuine first-derivative jump of size
\[
 \boxed{\Phi'_+(2-\sqrt2)-\Phi'_-(2-\sqrt2)
 =\sqrt2(2-\sqrt2)e^{-(2-\sqrt2)}>0.}
\]
Moreover \(\Phi(\lambda)\sim2\lambda\) as \(\lambda\downarrow0\), while \(\Phi(\lambda)\to\sqrt{2/(\pi e)}\) as \(\lambda\to\infty\).

## Assumptions and scope
The alphabet is simply a set of \(q\) symbols; no field or additive character structure is needed. Write \(\mathcal H_0\) for the one-coordinate constants and \(\mathcal H_1\) for their orthogonal complement (dimension \(q-1\)). Then \(\operatorname{ran}P_2\) is the orthogonal direct sum, over all two-element coordinate sets, of \(\mathcal H_1\) in those coordinates tensored with \(\mathcal H_0\) elsewhere. The integral kernel for normalized measure is \(K_{n,q}(d_H(x,y))\); the matrix with respect to point masses has entries \(q^{-n}K_{n,q}(d_H(x,y))\). Norms are for the full complex function spaces; absolute row and column sums give the exact endpoint operator norms.

The endpoints \(L,U\) exclude zeros of the quadratic exactly (strict negativity). Out-of-range values of \(b\) are zero. The sequence conditions are essential: the Gaussian conclusion requires \(n/q\to\infty\); the nonconstant Poisson profile requires \(q\to\infty\) and \(n/q\to\lambda>0\). No convergence rate or claim of originality for the underlying classical Krawtchouk/Charlier polynomials is asserted.

## Proof
**1. Kernel and normalization.** The one-coordinate orthogonal projection onto mean-zero functions has integral kernel \(u(a,b)=q\mathbf1_{a=b}-1\). Thus the degree-two integral kernel equals \(\sum_{i<j}u(x_i,y_i)u(x_j,y_j)\). With \(d=d_H(x,y)\), the \(n\) factors are \(q-1\) at matching positions and \(-1\) at mismatches, so their sum is \(S=(q-1)n-qd\). Since each factor satisfies \(u^2=(q-2)u+(q-1)\), we have
\[
 \sum_{i<j}u_i u_j=\tfrac12\left(S^2-(q-2)S-n(q-1)\right)=K_{n,q}(d).
\]
Each row has \(\binom nd(q-1)^d\) entries at Hamming distance \(d\), and all rows and columns have the same absolute sum. If \(D\sim\mathrm{Bin}(n,p)\), the common absolute row sum is \(\mathbb E|K_{n,q}(D)|\). Independence and \(\mathbb Eu_i=0\) give \(\mathbb EK_{n,q}(D)=0\). The value at \(d=0\) is \(\binom n2(q-1)^2>0\), so there is a negative value. Because the quadratic is upward-opening, its negative integers form one nonempty interval \([L,U]\), and solving its roots gives the stated explicit endpoints.

**2. Four-mass identity.** Let \(Z\sim\mathrm{Bin}(n-2,p)\) be independent of the first two mismatch indicators. In the signed expectation with \(u_1u_2\), each of the four choices of the first two mismatch bits has absolute probability weight \(p^2\) and signs \(+,-,-,+\), because \((1-p)(q-1)=p\). Consequently, for every integer \(t\),
\[
 \mathbb E[u_1u_2\mathbf1_{D\le t}]
 =p^2\big[\Pr(Z\le t)-2\Pr(Z\le t-1)+\Pr(Z\le t-2)\big]
 =p^2\big[b(t)-b(t-1)\big].
\]
Summing over the \(\binom n2\) coordinate pairs gives
\[
 \mathbb E[K_{n,q}(D)\mathbf1_{D\le t}]
 =\binom n2p^2[b(t)-b(t-1)].
\]
By the mean-zero property, \(\mathbb E|K_{n,q}(D)|=-2\mathbb E[K_{n,q}(D)\mathbf1_{L\le D\le U}]\). Subtract the last identity at \(t=U\) and \(t=L-1\) to obtain the displayed sharp finite formula. No estimate or numerical diagonalization is involved.

**3. Gaussian regime.** Let \(J=n-D\) count the matching coordinates, and \(Z_n=(qJ-n)/\sqrt{n(q-1)}\). The summands have mean zero and variance \(q-1\). Under \(n/q\to\infty\), their standardized third absolute moments satisfy a Lyapunov bound \(O(\sqrt{q/n})\to0\), so \(Z_n\) tends to a standard normal random variable \(Z\). The exact polynomial identity is
\[
 \frac{K_{n,q}(D)}{n(q-1)}
 =\frac12\left[Z_n^2-1-\frac{q-2}{\sqrt{n(q-1)}}Z_n\right].
\]
The linear coefficient tends to zero. The fourth moments of \(Z_n\) are uniformly bounded (from independent centered summands, with fourth-moment correction \(O(q/n)\)), so the absolute quadratic expressions are uniformly integrable. Their expectations therefore converge to \(\frac12\mathbb E|Z^2-1|=2e^{-1/2}/\sqrt{2\pi}=\sqrt{2/(\pi e)}\).

**4. Poisson regime and threshold.** Put \(\mu=n/q\) and let \(J\sim\mathrm{Bin}(n,1/q)\). When \(q\to\infty\) and \(\mu\to\lambda\in(0,\infty)\), one has \(J\Rightarrow T_\lambda\sim\mathrm{Poisson}(\lambda)\), and the exact identity
\[
 \frac{K_{n,q}(n-J)}{n(q-1)}
 =\frac{(J-\mu)^2-(1-2/q)(J-\mu)-\mu(1-1/q)}{2\mu(1-1/q)}
\]
converges in distribution to \(\frac{T_\lambda(T_\lambda-1)-2\lambda T_\lambda+\lambda^2}{2\lambda}\). Uniform integrability follows from bounded fourth moments of \(J\), which in turn follow from \(\mathbb E(J)_r=(n)_rq^{-r}\le\mu^r\) for each \(r\le4\). This proves the expression for \(\Phi\). For \(0<\lambda<2-\sqrt2\), the Charlier quadratic is negative exactly at the integer \(1\). Since its expectation is zero, twice the negative mass divided by \(2\lambda\) yields \(\Phi(\lambda)=\lambda e^{-\lambda}(2-\lambda)\). At \(\lambda_*=2-\sqrt2\), the term \(k=2\) changes sign with derivative \(-2\sqrt2\), whereas all other terms are smooth there (local uniform convergence of the factorially damped series and its differentiated terms applies). Its absolute value gives the displayed positive jump in \(\Phi'\). The small-parameter asymptotic follows from the first regime; the large-parameter limit follows from the Poisson central limit theorem and bounded normalized fourth moments, exactly as in Step 3.

## Verification
The standalone `verify.py` uses exact rational arithmetic for \(1152\) finite parameter pairs \((n,q)\) (including the boundary cases), compares the four-mass formula against the full absolute Hamming-distance sum, and independently constructs all relevant row entries for \(20\) small complete product spaces. It additionally compares the Gaussian approximation at \((n,q)=(10000,4)\) with the predicted constant, tests the first Poisson branch at four parameters, and compares four binomial sparse-alphabet cases against the predicted Poisson crossover. Replaying the packaged script gave:

`VERIFY_OK exact_parameters=1152 direct_rows=20 gaussian_n=10000 gaussian_q=4 ratio=0.483931970541 target=0.483941449038 poisson_first_regime=4 sparse_crossover=4`

The infinite-dimensional statements and threshold are proved analytically above. Finite computational checks do not certify them.

## Relationship to prior work
Scarabotti and Tolli's *Harmonic analysis on a finite homogeneous space* (arXiv:math/0701533v1, publicly posted 2007-01-19, primary MSC 43A95) develops the classical Hamming scheme and general wreath-product decomposition. Its sections 5.1–5.4 concern representation decompositions, not the absolute endpoint norm of the degree-two primitive idempotent or a varying-alphabet asymptotic.

Polyanskiy's *Hypercontractivity of spherical averages in Hamming space* (arXiv:1309.3014) studies the binary Hamming cube and \(L^p\to L^2\) bounds for spherical averages and Fourier projections; it gives Krawtchouk formulas and asymptotics but not the sharp \(\ell^1\) or \(\ell^\infty\) degree-two projection norm for general \(q\). Kirshner and Samorodnitsky's *A moment ratio bound for polynomials and some extremal properties of Krawchouk polynomials and Hamming spheres* (arXiv:1909.11929) studies binary-cube \(p\ge2\) moment ratios and spectral concentrations, not this growing-alphabet Gaussian–Poisson norm crossover. The one-alphabet binary case is not claimed as a new result. The new contribution is the exact general-alphabet endpoint formula together with the sharp nonconstant crossover profile and its first cusp.

## Limitations
This is a degree-two statement for homogeneous Hamming harmonics; it does not give norms for higher idempotents or arbitrary combinations of degrees. The asymptotic regimes do not claim a uniform rate or a limit at all possible joint sequences. The threshold is a nonsmoothness of the limiting normalized norm, not a thermodynamic singularity or a statement about finite-parameter analyticity. The endpoint formula is a consequence of a classical orthogonal-polynomial representation and may have an equivalent unpublished or differently named expression in historical Krawtchouk/Charlier literature; this originality risk remains despite the comparisons described above. No independent validation has been performed.

## References
1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1 (19 January 2007), https://arxiv.org/abs/math/0701533, particularly Sections 5.1–5.4.
2. Y. Polyanskiy, *Hypercontractivity of spherical averages in Hamming space*, arXiv:1309.3014, https://arxiv.org/abs/1309.3014, especially Section 2.
3. N. Kirshner and A. Samorodnitsky, *A moment ratio bound for polynomials and some extremal properties of Krawchouk polynomials and Hamming spheres*, arXiv:1909.11929, https://arxiv.org/abs/1909.11929, Sections 1–3.
