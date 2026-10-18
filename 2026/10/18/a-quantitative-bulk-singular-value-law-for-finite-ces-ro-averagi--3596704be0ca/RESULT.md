# A quantitative bulk singular-value law for finite Cesàro averaging

## Finding
Let \(C_n\) denote the real \(n\)-by-\(n\) Cesàro averaging matrix with \((C_n)_{ij}=1/i\) for \(1\leq j\leq i\leq n\), and zero otherwise. Write its singular values in nonincreasing order as \(s_1(C_n)\geq\cdots\geq s_n(C_n)>0\). Put
\[
\mu_n=\frac1n\sum_{j=1}^n\delta_{1/(n s_j(C_n))}.
\]
Let \(X\) and \(\Theta\) be independent and uniform on \([0,1]\) and \([0,\pi/2]\), respectively, and let \(\mu\) be the law of \(U=2X\sin\Theta\). Then, **for every integer \(n\geq1\)**,
\[
W_1(\mu_n,\mu)\leq\frac{12}{\sqrt n}.
\]
Here \(W_1\) is the ordinary \(1\)-Wasserstein distance on the real line. The limiting distribution function is explicit:
\[
F(t)=\mu(( -\infty,t])=
\begin{cases}
0,&t\leq0,\\
\dfrac{2}{\pi}\arcsin\dfrac t2+\dfrac t\pi\log\dfrac{2+\sqrt{4-t^2}}t,&0<t<2,\\
1,&t\geq2.
\end{cases}
\]
Its density on \((0,2)\) is \(f(t)=\pi^{-1}\log((2+\sqrt{4-t^2})/t)\). Thus every proportional singular-value rank has an exact limit: for any \(0<\alpha<1\),
\[
\lim_{n\to\infty}n\,s_{\lceil\alpha n\rceil}(C_n)=\frac1{F^{-1}(\alpha)}.
\]
The result includes the following finite-size bound for singular-value observables. Given \(M\geq1\) and any real \(1\)-Lipschitz function \(g\) on \([1/2,M]\),
\[
\left|\frac1n\sum_{j=1}^n g(\min\{M,n s_j(C_n)\})-\mathbb E\,g(\min\{M,U^{-1}\})\right|\leq\frac{12M^2}{\sqrt n}.
\]
(The event \(U=0\) has probability zero.)

## Assumptions and scope
All matrices and Hilbert-space norms are over the real field; singular-value results are identical over the complex field. The matrix \(C_n\) acts on Euclidean \(\mathbb R^n\) with indexing beginning at one, and \(W_1\) uses cost \(|u-v|\). The assertion concerns the full empirical *bulk* spectrum after reciprocal-and-dimension scaling; it does not assert an unscaled operator-norm limit, a pointwise rate for every individual singular value, or a rate near the singular endpoint \(\alpha=0\). The rate \(12n^{-1/2}\) is explicit but is not claimed optimal.

## Proof
**1. Exact inverse and uniform support.** Let \(D_n=n^{-1}C_n^{-1}\). Taking first differences of \(y_i=i^{-1}\sum_{j\leq i}x_j\) gives \(x_i=iy_i-(i-1)y_{i-1}\), with \(y_0=0\). Hence
\[
(D_n)_{ii}=\frac in,\qquad(D_n)_{i,i-1}=-\frac{i-1}{n}\quad(2\leq i\leq n),
\]
with all other entries zero. Its singular multiset is precisely \(\{(n s_j(C_n))^{-1}\}_{j=1}^n\). Since each diagonal and subdiagonal has magnitude at most one, \(\|D_n\|_2\leq2\); therefore \(\mu_n\) is supported on \([0,2]\).

**2. Freezing local coefficients.** Fix an integer \(1\leq m\leq n\) and partition \(\{1,\ldots,n\}\) into \(L=\lceil n/m\rceil\) consecutive intervals, each of length \(\ell_b\leq m\), starting at \(a_b\). Delete from \(D_n\) the \(L-1\) subdiagonal entries joining distinct intervals and call the resulting block-diagonal matrix \(E_n\). Its difference from \(D_n\) has rank at most \(L-1\), so singular-value rank interlacing implies
\[
\sup_{t\geq0}\left|\mu_{D_n}([0,t])-\mu_{E_n}([0,t])\right|\leq\frac{L-1}{n}.
\]
Both measures are supported in \([0,2]\); integrating their distribution-function difference gives
\[
W_1(\mu_{D_n},\mu_{E_n})\leq\frac{2(L-1)}n.
\]
On block \(b\), replace both the diagonal coefficient \(i/n\) and the magnitude of the subdiagonal coefficient \((i-1)/n\) by \(c_b=a_b/n\), yielding the bidiagonal block \(T_b=c_b(I-S_{\ell_b})\) with \(S_{\ell_b}\) the backward unit shift. The diagonal and subdiagonal errors have magnitudes at most \(m/n\). Because a diagonal or shifted-diagonal matrix has operator norm equal to its maximum entry magnitude,
\[
\|E_n-\bigoplus_bT_b\|_2\leq\frac{2m}{n}.
\]
The singular-value Weyl inequality, pairing the ordered singular values, therefore gives
\[
W_1\left(\mu_{E_n},\mu_{\oplus_bT_b}\right)\leq\frac{2m}{n}.
\]

**3. Exact constant-block spectrum.** The matrix \((I-S_\ell)^*(I-S_\ell)\) has diagonal \(2\) except for final diagonal \(1\), with both neighboring diagonals equal to \(-1\). Its eigenvector recurrence admits \(v_j=\sin(j\varphi)\), with the fictitious boundaries \(v_0=0\) and \(v_{\ell+1}=v_\ell\). Thus \(\varphi=(2k-1)\pi/(2\ell+1)\), the eigenvalue is \(4\sin^2(\varphi/2)\), and its singular values, in ascending order, are
\[
2\sin\left(\frac{(2k-1)\pi}{4\ell+2}\right),\qquad k=1,\ldots,\ell.
\]
For each \(k\), the sampling angle \(\phi_k=(2k-1)\pi/(4\ell+2)\) lies in the \(k\)-th cell \([(k-1)\pi/(2\ell),k\pi/(2\ell)]\) of the equispaced partition of \([0,\pi/2]\). Coupling the discrete angle to a uniform angle chosen from its corresponding cell and using that \(\sin\) is \(1\)-Lipschitz gives an expected error at most \(\pi/(2\ell)\) in angle, hence at most \(\pi c_b/\ell\) in the singular value. With block mass \(\ell_b/n\) this sums to at most \(\pi L/n\).

**4. Restoring the continuum position.** The coupled block distribution is the law of \(2c_b\sin\Theta\), where the label \(b\) is chosen with probability \(\ell_b/n\) and \(\Theta\) is uniform on \([0,\pi/2]\). Couple the label to uniform \(X\in[0,1]\) by assigning block \(b\) the interval \([(a_b-1)/n,(a_b+\ell_b-1)/n]\). Then \(|X-c_b|\leq m/n\). Since \(2\sin\Theta\leq2\), this last coupling incurs cost at most \(2m/n\). Combining steps 2–4 yields
\[
W_1(\mu_n,\mu)\leq\frac{2(L-1)+\pi L+4m}{n}.\tag{1}
\]
For \(n\geq16\), choosing \(m=\lceil\sqrt n\rceil\) gives \(L\leq\sqrt n+1\) and \(m\leq\sqrt n+1\), hence the right side of (1) is at most \((\pi+6)(n^{-1/2}+n^{-1})<12n^{-1/2}\). For \(1\leq n<16\), both laws lie in \([0,2]\), so \(W_1\leq2<12n^{-1/2}\). This proves the uniform bound.

**5. Distribution and singular-value consequences.** Conditioning on \(\Theta\) gives for \(0<t<2\)
\[
F(t)=\frac2\pi\int_0^{\pi/2}\min\left\{1,\frac{t}{2\sin\theta}\right\}\,d\theta.
\]
Split the integral at \(\arcsin(t/2)\) and use \(\int(\sin\theta)^{-1}\,d\theta=\log\tan(\theta/2)\) to obtain the displayed formula and derivative. The density is positive on \((0,2)\), so weak convergence from the proved \(W_1\) estimate forces convergence of each fixed interior order statistic. Finally the scalar map \(h_M(u)=\min\{M,1/u\}\) for \(u>0\), with \(h_M(0)=M\), is \(M^2\)-Lipschitz on \([0,2]\) and maps into \([1/2,M]\). Wasserstein duality applied to \(g\circ h_M\) proves the observable bound.

## Verification
The proof is independent of numerical experiments. A standalone deterministic checker `checker.py` constructs the exact bidiagonal inverse, checks its singular eigenvalues through tridiagonal Sturm bisection, compares the constant-block spectrum with its explicit sine formula, and tests the finite-dimensional Wasserstein inequality against numerical integration of the exact distribution function. Reproduce with `python3 checker.py`. These finite checks are diagnostic only; the infinite family and the universal error constant follow from the rank, operator-norm, and coupling estimates above.

## Relationship to prior work
Generalized locally Toeplitz (GLT) spectral-distribution theory describes limiting singular distributions for variable-coefficient finite-band matrices. Applied to \(D_n\), it supplies the qualitative limiting symbol \(x|1-e^{i\theta}|\), which is **not claimed as new** here. The contribution is the elementary **all-dimension quantitative** bound in \(W_1\), its explicit numerical constant, the closed CDF, and the reciprocal-clipped singular-observable estimate. Work on fixed top ranks of finite Cesàro matrices concerns the logarithmic spectral edge, whereas the present statement controls the entire empirical distribution at positive-proportion ranks. Work on generalized compact Cesàro operators with geometric parameter less than one concerns a different asymptotic regime.

## Limitations
No optimality of the \(n^{-1/2}\) rate or of the numerical constant is claimed. The estimate does not give a useful direct estimate of the largest singular value of \(C_n\) because reciprocal inversion magnifies errors near the zero endpoint of the limiting law. The comparison with GLT theory establishes that the *unquantified* limit already follows from general results; independent examination of potentially stronger quantitative results remains advisable. The date of the archival Toeplitz spectral-distribution source identifies the research foundation; it is not a date of publication of this theorem.

## References
1. E. Ngondiep, S. Serra-Capizzano and D. Sesana, *Spectral features and asymptotic properties for alpha-circulants and alpha-Toeplitz sequences*, arXiv:0906.2104, first public version 2009-06-11. (Qualitative Toeplitz spectral-distribution framework.) https://arxiv.org/abs/0906.2104
2. A. Kamińska and D. Kubiak, *On the dual of Cesàro function space*, arXiv:1109.5400, first public version 2011-09-25. (Context on the Cesàro operator family.) https://arxiv.org/abs/1109.5400
3. C. Garoni and S. Serra-Capizzano, *Spectral Distribution Results Beyond the Algebra Generated by Variable-Coefficient Toeplitz Sequences: The GLT Approach*, preprint 2017, J. Fourier Anal. Appl. 24 (2018), 506–524. (General qualitative GLT singular-distribution theorem.) https://doi.org/10.1007/s00041-017-9525-y
