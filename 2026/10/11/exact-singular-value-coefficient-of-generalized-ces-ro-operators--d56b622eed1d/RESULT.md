# Exact singular-value coefficient of generalized Cesàro operators on Hilbert space

## Finding
Let \(0\le t<1\) and consider the generalized discrete Cesàro operator on \(\ell_2(\mathbb N_0)\):
\[
(C_t x)_n=\frac{1}{n+1}\sum_{j=0}^{n}t^{n-j}x_j.
\]
Write \(s_1(C_t)\ge s_2(C_t)\ge\cdots\) for its singular values, counting multiplicities. Then
\[
\boxed{\lim_{n\to\infty}n\,s_n(C_t)
=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{|1-t e^{i\theta}|}
=\frac{2}{\pi(1+t)}K\!\left(\frac{2\sqrt t}{1+t}\right),}
\]
where \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\phi)^{-1/2}\,d\phi\) is the complete elliptic integral of the first kind. In particular,
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^{N}s_n(C_t)=c(t),
\qquad C_t\in\mathcal S_{1,\infty}\cap\bigcap_{q>1}\mathcal S_q,
\qquad C_t\notin\mathcal S_1.
\]
Here \(c(t)\) denotes the displayed positive coefficient and \(\mathcal S_{1,\infty}\) denotes the weak Schatten-one ideal, defined by \(\sup_{n\ge1}n s_n<\infty\). The formula also holds for the same real matrix acting on real \(\ell_2\).

## Assumptions and scope
The parameter range is \(0\le t<1\), with \(\mathbb N_0=\{0,1,2,\ldots\}\). Let \(S\) be the unilateral forward shift \(Se_n=e_{n+1}\) and \(De_n=(n+1)^{-1}e_n\). Then \(C_t=DA\), where \(A=(I-tS)^{-1}=\sum_{j\ge0}t^j S^j\) converges in operator norm. Thus \(C_t\) is compact. The proof first establishes an asymptotic counting lemma for \(DA\) when \(A\) is an absolutely summable one-sided Toeplitz series.

## Proof
**Step 1: finite-band counting lemma.** Fix an integer \(m\ge0\), coefficients \(a_0,\ldots,a_m\in\mathbb C\), and set \(A_m=\sum_{j=0}^m a_jS^j\), \(M=\sum_{j=0}^m|a_j|\). For any compact operator \(T\), put \(N(\varepsilon,T)=\#\{n:s_n(T)>\varepsilon\}\). We establish
\[
\lim_{\varepsilon\downarrow0}\varepsilon N(\varepsilon,DA_m)
=\frac{1}{2\pi}\int_0^{2\pi}\left|\sum_{j=0}^m a_j e^{ij\theta}\right|\,d\theta.\tag{1}
\]
Partition \(\mathbb N_0\) into consecutive blocks \(I_k=\{kB,\ldots,(k+1)B-1\}\) with an integer \(B>2m\). Let \(P_k\) be the corresponding coordinate projections and \(Q_B=P_0A_mP_0\), viewed as a \(B\)-square lower-triangular Toeplitz matrix. Decompose
\[
DA_m=H_{m,B}+R_{m,B}+E_{m,B}+F_B,
\qquad H_{m,B}=\bigoplus_{k\ge1}\frac{1}{kB}Q_B.
\]
Here \(F_B=P_0DA_m\) has finite rank. The operator \(E_{m,B}\) is the within-block discrepancy obtained by replacing each entry \((n+1)^{-1}\) in output block \(I_k\), \(k\ge1\), by \((kB)^{-1}\). It is trace class, since
\[
\|E_{m,B}\|_1\le M\sum_{k\ge1}\sum_{r=0}^{B-1}
\left|\frac{1}{kB+r+1}-\frac1{kB}\right|
\le \frac{M}{B^2}\sum_{k\ge1}\frac1{k^2}\sum_{r=0}^{B-1}(r+1)<\infty.\tag{2}
\]
The remaining \(R_{m,B}\) consists only of cross-boundary matrix entries. Because \(A_m\) shifts by at most \(m<B\) coordinates, its piece crossing into output block \(I_k\) has rank at most \(m\), norm at most \(M/(kB+1)\), and source and target coordinates disjoint from the pieces at other boundaries. Hence
\[
\limsup_{\varepsilon\downarrow0}\varepsilon N(\varepsilon,R_{m,B})
\le\frac{mM}{B}.\tag{3}
\]
A trace-class operator \(E\) satisfies \(\varepsilon N(\varepsilon,E)\to0\). The direct-sum formula for \(H_{m,B}\) gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon N(\varepsilon,H_{m,B})
=\frac1B\sum_{j=1}^{B}s_j(Q_B)=\frac1B\|Q_B\|_1.\tag{4}
\]
Indeed, for each singular value \(\sigma_j=s_j(Q_B)\), the corresponding contribution is \(\#\{k\ge1:\sigma_j/(kB)>\varepsilon\}\), whose product with \(\varepsilon\) tends to \(\sigma_j/B\). Let \(Z_B\) be the circulant matrix \(\sum_{j=0}^m a_j U_B^j\) with \(U_B\) the cyclic shift. The matrices \(Q_B\) and \(Z_B\) differ in rank by at most \(m\), so \(\bigl|\|Q_B\|_1-\|Z_B\|_1\bigr|\le2mM\). The Fourier basis diagonalizes \(Z_B\), yielding
\[
\lim_{B\to\infty}\frac1B\|Q_B\|_1
=\lim_{B\to\infty}\frac1B\sum_{j=0}^{B-1}
\left|\sum_{r=0}^m a_r e^{2\pi i rj/B}\right|
=\frac1{2\pi}\int_0^{2\pi}|a_m(e^{i\theta})|\,d\theta,\tag{5}
\]
where \(a_m(z)=\sum_{r=0}^m a_rz^r\). Finally, the singular-value counting inequalities
\[
N((\alpha+\beta)\varepsilon,X+Y)
\le N(\alpha\varepsilon,X)+N(\beta\varepsilon,Y)
\]
and the analogous inequality with \(X=(X+Y)-Y\), applied to (2)--(4), place the lower and upper limits in (1) within errors controlled by \(mM/(\eta B)\), for each fixed \(0<\eta<1\). First let \(B\to\infty\), using (5), and then let \(\eta\downarrow0\). This proves (1), including \(m=0\) (with trivial boundary part).

**Step 2: infinite one-sided Wiener series.** Suppose \(\sum_{j\ge0}|a_j|<\infty\), let \(A=\sum_{j\ge0}a_jS^j\), and let \(A_m\) denote its truncation. The discarded tail has operator norm at most \(\delta_m=\sum_{j>m}|a_j|\). For every \(n\ge1\), the singular-value ideal inequality gives
\[
s_n(D(A-A_m))\le\|A-A_m\|s_n(D)\le\frac{\delta_m}{n},
\]
so \(\limsup_{\varepsilon\downarrow0}\varepsilon N(\varepsilon,D(A-A_m))\le\delta_m\). Comparing \(DA\) with \(DA_m\) by the preceding counting inequalities, then taking \(m\to\infty\) at fixed comparison tolerance and finally taking that tolerance to zero, yields
\[
\lim_{\varepsilon\downarrow0}\varepsilon N(\varepsilon,DA)
=\frac1{2\pi}\int_0^{2\pi}\left|\sum_{j\ge0}a_je^{ij\theta}\right|\,d\theta.\tag{6}
\]
Absolute summability makes the symbol converge uniformly. If this integral is positive, monotonicity of the singular values converts (6) into
\[
\lim_{n\to\infty}n\,s_n(DA)
=\frac1{2\pi}\int_0^{2\pi}|a(e^{i\theta})|\,d\theta.\tag{7}
\]
For completeness, the conversion follows by sandwiching the \(n\)-th singular value between levels with counting functions asymptotic to a positive constant divided by the level; it requires no unverified interchange of a finite-section limit with the singular-index limit.

**Step 3: evaluate the coefficient.** In our case \(a_j=t^j\), so \(a(e^{i\theta})=(1-t e^{i\theta})^{-1}\). Formula (7) gives the asserted first integral. The identity
\[
|1-t e^{i\theta}|^2=(1+t)^2-4t\cos^2(\theta/2)
\]
and symmetry on the circle give the stated complete-elliptic-integral representation. Positivity of the coefficient is immediate. Since \(s_n(C_t)\sim c(t)/n\), logarithmic summation gives the claimed trace growth, finite weak Schatten-one quasi-norm, membership in every \(\mathcal S_q\) with \(q>1\), and failure of trace-class membership. The real and complex realizations have the same singular values because their matrices and their Hilbert Gram operators have real entries.

## Verification
At \(t=0\), the formula reduces to the diagonal operator \(D\), whose singular values are exactly \(1/n\), giving \(c(0)=1\). A finite-section numerical consistency test used the \(240\)-square northwest corner of the matrix, computed its full singular-value decomposition, and compared scaled singular values \(n s_n\) at indices \(20,40,75\) with the independently evaluated elliptic formula. At \(t=0.3\), the predicted coefficient is approximately \(1.0237155464\) and the computed values are \(1.02370,1.02371,1.02371\); at \(t=0.7\), the predicted coefficient is approximately \(1.1750052931\) and the computed values are \(1.17487,1.17497,1.17499\). These are finite consistency checks; the infinite asymptotic follows from the proof in Steps 1--3, not from numerical extrapolation.

## Relationship to prior work
Albanese, Bonet and Ricker (first public preprint 8 May 2023, 2020 primary MSC 47B37) investigate spectral and compactness properties for the same generalized Cesàro operators on Fréchet and related sequence spaces. Their results do not give the sharp Hilbert-space singular-number coefficient. Curbera and Ricker earlier established compactness, spectral classifications and norm estimates for Banach sequence lattices (journal article publicly available by 2021; an accessible arXiv copy appeared in 2023). Rhaly had previously established that the Hilbert-space operators are Hilbert–Schmidt for parameters below one in 1984. Neither Hilbert–Schmidt membership nor compactness determines the sharp first-order coefficient. Widom's 1989 singular-value theorems concern normalized distributions of finite Toeplitz sections, a component used here, rather than the singular-number asymptotic of the infinite compact product of a reciprocal diagonal with a one-sided Toeplitz operator. Bellavita, Dellepiane and Stylogiannis study Schatten membership for Rhaly matrices whose entries in each row are constant below the diagonal; for \(t\in(0,1)\), the present matrix has geometrically varying row entries, and the present statement gives a sharp first-order coefficient rather than a membership test. No general originality beyond these checked comparisons is claimed.

## Limitations
The theorem assumes a fixed \(t<1\); it is not a uniform limit as \(t\uparrow1\), and no assertion is made about the noncompact classical Cesàro operator at \(t=1\). The proof identifies first-order singular-value decay, not second-order corrections or individual singular vectors. Established finite Toeplitz distribution theorems provide background for the blocking method and pose a residual risk of broader existing coverage. Independent validation has not been performed.

## References
1. A. A. Albanese, J. Bonet and W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805v1 (first public 8 May 2023), https://arxiv.org/abs/2305.04805.
2. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices in* \(\mathbb C^{\mathbb N_0}\), J. Math. Anal. Appl. 507 (2022), 125824, DOI:10.1016/j.jmaa.2021.125824; accessible arXiv edition: https://arxiv.org/pdf/2302.08750.
3. H. C. Rhaly Jr., *Generalized Cesàro Matrices*, Canad. Math. Bull. 27 (1984), 417--422, DOI:10.4153/CMB-1984-064-5, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/967DB4D41F4A7EB149E5E3CBFC548BDE/S0008439500068879a.pdf/div-class-title-generalized-cesaro-matrices-div.pdf.
4. H. Widom, *On the Singular Values of Toeplitz Matrices*, Z. Anal. Anwend. 8 (1989), 221--229, DOI:10.4171/ZAA/350, https://ems.press/content/serial-article-files/34508?nt=1.
5. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930v3 (2025), https://arxiv.org/pdf/2503.21930.
