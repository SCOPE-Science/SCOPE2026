# Exact local conditioning and optimal weighting for two-tap cyclic spectrograms

## Finding
For each integer \(N\ge3\), let \(a,b\in\mathbb C\) be two window coefficients satisfying \(|a|^2+|b|^2=1\). For \(x=(x_j)_{j\in\mathbb Z_N}\), define the two-tap intensity measurement
\[
Y_{a,b}(x)_{j,k}=\left|a x_j+b\,e^{2\pi i k/N}x_{j+1}\right|^2,
\qquad j,k\in\mathbb Z_N.
\]
The map is the squared-magnitude cyclic short-time Fourier measurement for a two-point window, up to harmless Fourier-modulation and normalization conventions. Let \(J=D Y_{a,b}(\mathbf1)\) be its real derivative at the constant signal \(\mathbf1=(1,\ldots,1)\), and put \(t=|a b|^2\). The complete multiset of squared real singular values is
\[
\boxed{\{4-4t+12t\cos(2\pi k/N):0\le k<N\}
\ \cup\ \{4t(1-\cos(2\pi k/N)):0\le k<N\}.}
\]
Here the first and second branches correspond to real-amplitude and imaginary-phase perturbations, respectively; multiplicities are retained.

For \(c_N=1\) when \(N\) is even and \(c_N=\cos(\pi/N)\) when \(N\) is odd, and \(s_N=\sin^2(\pi/N)\), the exact squared minimum gain on perturbations orthogonal to global phase is
\[
\lambda_N(t)=\min\{4-4t(1+3c_N),\ 8t s_N\}.
\]
The globally optimal choice among normalized two-tap windows is uniquely determined, up to interchange and coefficient phases, by
\[
\boxed{t_N^*=\frac{1}{1+3c_N+2s_N},\qquad
\lambda_N^*=\frac{8s_N}{1+3c_N+2s_N}.}
\]
In particular, the optimal powers are
\[
\{|a|^2,|b|^2\}=\left\{\frac{1+\sqrt{1-4t_N^*}}{2},
\frac{1-\sqrt{1-4t_N^*}}{2}\right\}.
\]
The balanced choice is optimal only when \(N=3\); for every even \(N\), it introduces an extra local amplitude null direction, whereas the optimal unbalanced choice does not. As \(N\to\infty\), the sharp gain satisfies \(\lambda_N^*\sim 2\pi^2/N^2\).

## Assumptions and scope
The integer \(N\) is at least three; \(a,b\) are arbitrary complex coefficients with total squared magnitude one. The real input norm is \(\|h\|_{\mathrm{sig}}^2=\sum_j|h_j|^2\). The real data norm is \(\|z\|_{\mathrm{dat}}^2=N^{-1}\sum_{j,k}|z_{j,k}|^2\). The signal \(\mathbf1\) is fixed with all coordinates one. A phase-equivalent perturbation is \(i\mathbf1\); its real orthogonal complement is exactly the collection of \(h=u+iv\) with \(\sum_jv_j=0\). The claimed \(\lambda_N\) is the infimum of \(\|Jh\|_{\mathrm{dat}}^2\) over that complement subject to \(\|h\|_{\mathrm{sig}}=1\). Zero coefficients may be included as endpoint windows, for which the minimum gain is zero; the optimizer has both coefficients nonzero.

## Proof
Write \(\alpha=|a|^2\), \(\beta=|b|^2\), \(\alpha+\beta=1\), and \(t=\alpha\beta\). For each cyclic position \(j\), expand
\[
Y_{a,b}(x)_{j,k}=D_j(x)+2\operatorname{Re}\left(e^{-2\pi i k/N}Z_j(x)\right),
\quad D_j(x)=\alpha|x_j|^2+\beta|x_{j+1}|^2,
\quad Z_j(x)=a\overline b\,x_j\overline{x_{j+1}}.
\]
For a real perturbation \(h=u+iv\), differentiation at \(\mathbf1\) yields
\[
D'_j=2(\alpha u_j+\beta u_{j+1}),\qquad
Z'_j=a\overline b\big((u_j+u_{j+1})+i(v_j-v_{j+1})\big).
\]
Since the three frequency characters of orders \(0,+1,-1\) are distinct for every \(N\ge3\), their discrete orthogonality gives the **exact identity**
\[
\|Jh\|_{\mathrm{dat}}^2
=4\sum_j(\alpha u_j+\beta u_{j+1})^2
+2t\sum_j(u_j+u_{j+1})^2
+2t\sum_j(v_j-v_{j+1})^2.
\tag{1}
\]
No amplitude–phase cross terms remain. The cyclic shift has Fourier multipliers \(e^{2\pi i k/N}\). The first two sums in (1) therefore have multiplier
\[
4(\alpha^2+\beta^2+2t\cos\theta_k)+2t(2+2\cos\theta_k)
=4-4t+12t\cos\theta_k,
\]
where \(\theta_k=2\pi k/N\). The last sum has multiplier \(2t(2-2\cos\theta_k)=4t(1-\cos\theta_k)\). Because each cyclic real symmetric form is diagonalized by its cosine/sine Fourier eigenvectors, each branch accounts for exactly \(N\) real eigenvalues including multiplicities. This proves the full \(2N\)-dimensional spectrum. The unique obligatory zero direction for \(0<t\le1/4\) in the phase branch is the constant imaginary vector.

The smallest amplitude eigenvalue occurs at \(\min_k\cos\theta_k=-c_N\); the smallest **nonzero** phase eigenvalue occurs at \(\max_{k\ne0}\cos\theta_k=\cos(2\pi/N)\). This gives
\[
\lambda_N(t)=\min\{4-4t(1+3c_N),\ 4t(1-\cos(2\pi/N))\}=
\min\{4-4t(1+3c_N),\ 8t s_N\}.
\tag{2}
\]
The first affine term in (2) strictly decreases with \(t\), while the second strictly increases. They intersect at \(t_N^*=1/(1+3c_N+2s_N)\). This lies in \((0,1/4]\): when \(N\) is even the denominator is \(4+2s_N>4\); when \(N\) is odd, writing \(c=\cos(\pi/N)\), the excess of the denominator over four equals \((1-c)(2c-1)\ge0\), with equality exactly at \(N=3\). Thus (2) is maximized **uniquely** at \(t_N^*\), and its value is \(8t_N^*s_N\). The elementary equation \(\alpha+\beta=1\) and \(\alpha\beta=t_N^*\) classifies all windows attaining it, with unrestricted individual coefficient phases.

For even \(N\) and \(t=1/4\), the amplitude eigenvalue at \(k=N/2\) vanishes; its eigenvector alternates sign. For every odd \(N\), \(c_N<1\) and this additional zero does not occur. Equality of the optimal weights \(\alpha=\beta\) requires \(t_N^*=1/4\), hence \(N=3\). Finally, \(s_N\sim\pi^2/N^2\) and \(c_N\to1\), giving the stated asymptotic. All comparisons are exact for every permitted integer \(N\).

## Verification
A standalone Python/NumPy checker named `verify_local_two_tap.py` builds the real Jacobian from the original intensity measurement, diagonalizes the Gram matrix with the specified data normalization, and matches all \(2N\) eigenvalues and the claimed minimal transverse gain for every integer \(3\le N\le24\), using multiple coefficient products including the optimum and the balanced boundary. It also checks seven centered finite-difference Jacobian actions directly against nonlinear intensities. These tests are numerical corroboration, not a proof for all \(N\); equation (1) and the Fourier diagonalization supply the unrestricted proof. To reproduce, run `python verify_local_two_tap.py` with Python 3 and NumPy installed.

## Relationship to prior work
Alaifari and Wellershoff [1], first public version January 12, 2019, study stability of discrete Gabor phase retrieval using ambiguity-function and autocorrelation estimates. Their Sections 3–4 provide stability estimates, but do not provide the exact two-tap **intensity derivative spectrum** at the constant signal or solve its normalized amplitude-design maximin problem. Cheng, Daubechies, Dym and Lu [2] link local phase-retrieval stability to graph connectivity and establish dimension-dependent bounds for cyclic local measurements; neither their abstract graph bounds nor their Example 3.1 computes the stated complete two-branch Jacobian spectrum or the sharp optimally weighted window. Earlier support-graph approaches to short-time Fourier phase retrieval [3] address connectivity, uniqueness and reconstruction error, not the exact maximin singular value in the stated normalization. Thus prior qualitative injectivity and bounds are respected, while the exact local spectral optimization is the present claim. An equivalent formulation in unindexed finite-dimensional ptychographic conditioning literature is not excluded.

## Limitations
The statement is **only local at the constant nonvanishing signal** with the explicitly stated data and input norms; it does not establish globally uniform injectivity, global nonlinear stability, or optimality for a Poisson or heteroscedastic noise model. Different measurement scalings change the numerical gains. Some two-tap windows fail global phase retrieval for sparse signals despite having a positive Jacobian gain at this flat signal. The finite numerical checks do not certify all dimensions. Independent mathematical audit has not been performed.

## References
[1] R. Alaifari and M. Wellershoff, *Stability estimates for phase retrieval from discrete Gabor measurements*, arXiv:1901.05296v1 (first public January 12, 2019), https://arxiv.org/abs/1901.05296 ; inspected lawful full text https://arxiv.org/html/1901.05296v4 .

[2] C. Cheng, I. Daubechies, N. Dym, J. Lu, *Stable Phase Retrieval from Locally Stable and Conditionally Connected Measurements*, arXiv:2006.11709v1 (first public June 21, 2020), https://arxiv.org/html/2006.11709v1 .

[3] L. Li, C. Cheng, D. Han, Q. Sun, G. Shi, *Phase Retrieval from Multiple-Window Short-Time Fourier Measurements*, arXiv:1605.07046v1 (2016), https://arxiv.org/html/1605.07046v1 .
