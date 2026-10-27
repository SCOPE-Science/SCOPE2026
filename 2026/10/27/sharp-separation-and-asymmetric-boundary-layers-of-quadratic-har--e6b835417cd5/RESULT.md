# Sharp separation and asymmetric boundary layers of quadratic harmonic-Bergman Toeplitz spectral islands

## Finding
Let \(T_p=P_hM_p\) act on the complex harmonic Bergman space \(L_h^2(\mathbb D,dA)\), with normalized area measure. For every quadratic analytic polynomial \(p(z)=c_2z^2+c_1z+c_0\), \(c_2\ne0\), put \(a=c_1/c_2\), \(t=|a|\), and
\[
\lambda_*=c_0-\frac{12c_1^2}{49c_2},\qquad t_-=\frac74,\qquad t_+=\frac73.
\]
The essential spectrum is \(p(\partial\mathbb D)\). The entire spectrum is exactly \(p(\partial\mathbb D)\) unless \(t_-<t<t_+\), in which case it is exactly
\[
\sigma(T_p)=p(\partial\mathbb D)\cup\{\lambda_*\}.
\]
Here \(\lambda_*\) is a simple **geometric** eigenvalue, and no assertion about its algebraic multiplicity is needed. For \(t_-<t<t_+\), its exact distance from the essential spectrum is
\[
\Delta(p)=\operatorname{dist}(\lambda_*,p(\partial\mathbb D))
=|c_2|\left(1-\frac{3t}{7}\right)\left(\frac{4t}{7}-1\right)
=|c_2|\left(\frac1{48}-\frac{12}{49}\left(t-\frac{49}{24}\right)^2\right).
\]
Consequently, among all such quadratics with fixed \(|c_2|\), the sharp possible normalized isolation gap is \(\Delta(p)/|c_2|\le1/48\), attained exactly when \(|c_1/c_2|=49/24\).

The unique eigenfunction normalized by the natural point-evaluation condition \(u_*(0)=1\) (equivalently, constant anti-analytic coefficient one) is
\[
u_*(z)=\frac{1}{(1-\alpha\bar z)^2}+\frac{z}{\beta-z},
\qquad\alpha=-\frac{3a}{7},\quad\beta=-\frac{4a}{7}.
\]
Its exact norm, depending only on \(t\), is
\[
\|u_*\|_{L_h^2}^2=\frac{1}{(1-(3t/7)^2)^2}
+\frac{-\log(1-v)-v}{v},\quad v=\left(\frac{7}{4t}\right)^2.
\]
Put \(\delta_-=t-t_-\) and \(\delta_+=t_+-t\). The two ends of the same spectral-island window have *different* sharp norm growth:
\[
\|u_*\|_{L_h^2}^2=\log(1/\delta_-)+\frac{256}{49}-1-\log(8/7)+o(1)
\quad(t\downarrow t_-),
\]
\[
\|u_*\|_{L_h^2}^2\sim\frac{49}{36\delta_+^2}
\quad(t\uparrow t_+),
\]
while the normalized spectral distance vanishes linearly with the *same slope* at either end:
\(\Delta(p)/|c_2|\sim\delta_-/7\) and \(\Delta(p)/|c_2|\sim\delta_+/7\), respectively. The discrepancy reflects analytic versus anti-analytic norm concentration.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(dA=dx\,dy/\pi\). The harmonic Bergman space consists of complex-valued harmonic functions square-integrable for \(dA\), decomposed orthogonally as \(zA^2(\mathbb D)\oplus\overline{A^2(\mathbb D)}\). The Toeplitz operator is compression of multiplication by the bounded analytic polynomial \(p\). All coefficients are complex. The phase of \(a\) does not affect the magnitude of the isolation gap or the displayed normalized eigenfunction norm. If \(a=0\), the spectrum is simply \(p(\partial\mathbb D)\). The boundary values \(t=t_-\) and \(t=t_+\) are excluded from the island: the candidate spectral point lies on the essential curve there and the displayed canonical eigenfunction is not in the harmonic Bergman space. The normalization is intrinsic to the eigenline: \(u(0)=g(0)\), and the squared norm \(\|u\|^2/|u(0)|^2\) is invariant under eigenvector rescaling. In particular, the canonical vector satisfies \(u_*(0)=1\).

## Proof
Affine normalization gives \(T_p=c_2T_q+c_0I\) with \(q(z)=z^2+az\), so it suffices to treat \(q\). For any \(\lambda\notin q(\partial\mathbb D)\), the continuous-symbol Fredholm theorem of Guo and Zheng (recalled as Theorem 2.1 of Huang–Wang–Zhao) gives Fredholm index zero; hence \(\lambda\in\sigma(T_q)\) precisely when \(T_q-\lambda I\) has a nonzero kernel. The same theorem gives \(\sigma_{\mathrm e}(T_q)=q(\partial\mathbb D)\).

Write \(\psi(z)=q(z)-\lambda\) and \(u=f+g(\bar z)\), where \(f\in zA^2\), \(g\in A^2\). The standard harmonic-Bergman block representation yields
\[
\psi f+P[\psi\,g(\bar z)]-\langle g,\psi^*\rangle=0,
\qquad T_{\widehat\psi}g=0.
\]
If \(\psi\) has no roots in \(\mathbb D\), invertibility of \(\psi\) in \(H^\infty\) gives invertibility of the harmonic Toeplitz operator. For a simple root \(w\in\mathbb D\), the second block's kernel contains \((1-wz)^{-2}\). For degree two, the Bergman-projection identity in equation (3.4) of Huang–Wang–Zhao specializes exactly to
\[
P\left[\frac{q(z)-q(w)}{(1-w\bar z)^2}\right]=zh(z,w),
\qquad h(z,w)=z+a+\frac43w.
\]
When \(\psi\) has exactly one simple root \(\alpha\) in \(\mathbb D\), the other root \(\beta\) is exterior and \(g(z)=C(1-\alpha z)^{-2}\). Here \(\langle g,\psi^*\rangle=0\) because \(\psi(\alpha)=0\), so the first block equation gives
\[
f(z)=-C\frac{zh(z,\alpha)}{(z-\alpha)(z-\beta)}.
\]
Analyticity at \(\alpha\) requires \(h(\alpha,\alpha)=a+7\alpha/3=0\), hence \(\alpha=-3a/7\) and, by Vieta, \(\beta=-4a/7\). Both root-location conditions hold precisely when \(7/4<|a|<7/3\). Conversely, in this range \(h(z,\alpha)=z-\alpha\) and the displayed \(u_*\) solves the block equations. The one-dimensional Bergman-kernel space gives geometric multiplicity one.

No other off-curve eigenvalues exist. With two distinct roots \(\alpha_1,\alpha_2\in\mathbb D\), the second block kernel consists of \(g=\sum_{j=1}^{2}C_j(1-\alpha_jz)^{-2}\). Analyticity forces the linear polynomial \(C_1h(z,\alpha_1)+C_2h(z,\alpha_2)\) to vanish at both roots, hence identically. Comparing coefficients gives \(C_1+C_2=C_1\alpha_1+C_2\alpha_2=0\), so both constants vanish. For a repeated root \(\gamma\in\mathbb D\), the second block's kernel is spanned by \((1-\gamma z)^{-2}\) and its parameter derivative \(2z(1-\gamma z)^{-3}\). Because \(q'(\gamma)=0\), differentiating the preceding projection identity in \(w\) at \(\gamma\) gives the analytic numerator \(z[C_0h(z,\gamma)+(4/3)C_1]\). Divisibility by \((z-\gamma)^2\) forces the linear bracket identically zero, and therefore \(C_0=C_1=0\). Roots on the unit circle occur only for \(\lambda\in q(\partial\mathbb D)\), already accounted for. This exhausts the spectrum.

For an island root pair, \(q(z)-\lambda_*=(z-\alpha)(z-\beta)\), so
\[
\operatorname{dist}(\lambda_*,q(\partial\mathbb D))=
\min_{|z|=1}|z-\alpha|\,|z-\beta|.
\]
The roots are collinear and have the same argument. The minimizer on the unit circle is their common radial direction, attaining each of the two separate distance lower bounds simultaneously. Thus the exact product is \((1-|\alpha|)(|\beta|-1)\). Completing its quadratic square gives the unique peak \(1/48\) at \(t=49/24\), and differentiating at the endpoints gives both gap slopes \(1/7\).

Finally, the orthogonal analytic/anti-analytic decomposition and the convergent expansions
\[
(1-\alpha\bar z)^{-2}=\sum_{k\ge0}(k+1)\alpha^k\bar z^k,
\qquad \frac{z}{\beta-z}=\sum_{k\ge1}\beta^{-k}z^k
\]
give
\[
\|u_*\|^2=\sum_{k\ge0}(k+1)|\alpha|^{2k}
+\sum_{k\ge1}\frac{|\beta|^{-2k}}{k+1}.
\]
Summing the two power series yields the exact norm formula. At the lower endpoint, \(1-v\sim(8/7)\delta_-\) while \(|\alpha|\to3/4\), yielding the logarithmic expansion and its explicit constant. At the upper endpoint, \(1-|\alpha|^2\sim(6/7)\delta_+\) while \(|\beta|\to4/3\), yielding \(49/(36\delta_+^2)\). These arguments prove all quantifiers for arbitrary complex coefficients.

## Verification
The standalone standard-library Python program `verify_quadratic.py` checks 1,548 concrete assertions: 12 exact rational projection identities, 1,452 exact rational eigenvector mode equations on the normalized harmonic Fourier basis, 59 exact rational isolation-gap and sharp-peak identities, 18 finite complex-phase unit-circle distance comparisons, and 7 asymptotic-normalization checks. Its output is `PASS ALL CHECKS 1548`. These computations are finite cross-checks, not substitutes for the analytic proof that there are no other eigenvalues or for the endpoint limits. The coefficient identity for \(P(z^k\bar z^\ell)\), the complete case distinction of root configurations, and the summation of exact Bergman norms provide the infinite-dimensional argument.

## Relationship to prior work
Huang, Wang and Zhao (arXiv:2610.09638v1, October 7, 2026), Theorem 3.1, prove that for a polynomial of any degree \(n\), the harmonic-Bergman Toeplitz spectrum consists of the essential curve plus at most \((n-1)2^{n-1}\) isolated eigenvalues. Their proof supplies a general determinant/kernel criterion (equations (3.2)–(3.6)), which already implies the **qualitative quadratic eigenvalue characterization after specializing to \(n=2\)**. The quadratic specialization is credited to that criterion rather than presented as independently novel. The quantitative findings here are the universal sharp normalized spectral-island separation \(1/48\), the exact canonical eigenvector norm, and the distinct logarithmic versus inverse-square norm concentration as the same spectral island meets the essential curve at its two endpoints. Those exact spectral-distance and eigenfunction-norm asymptotics do not appear in the inspected 2026 paper. Wang and Zhao (2021) already exhibited a quadratic analytic harmonic-Bergman Toeplitz operator with disconnected spectrum; that existence phenomenon is likewise not claimed as new. The original full 2021 text was not accessible in this review, so there remains a nontrivial risk of priority overlap with quantitative conclusions there.

## Limitations
The classification concerns analytic **quadratic** symbols on the normalized unweighted complex harmonic Bergman disk. It is not a result for general harmonic, nonanalytic, or higher-degree symbols, other weights, or other domains. The spectral island is geometrically simple; no proof of an algebraic-multiplicity statement or spectral-projection condition number is asserted. The boundary asymptotics describe the intrinsic squared eigenline-to-origin-evaluation ratio \(\|u\|^2/|u(0)|^2\), rather than the norm of an arbitrarily rescaled eigenvector. The earlier general determinant criterion covers the elementary qualitative root classification; the quantitative isolation and norm rates are the candidate additions. Absence of a matching result in searched records does not establish publication priority, especially because one plausible 2021 full text was unavailable. No independent scientific validation has been performed.

## References
1. M. Huang, J. Wang and X. Zhao, "The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space," arXiv:2610.09638v1 (first public October 7, 2026). https://arxiv.org/html/2610.09638v1 ; see Theorem 2.1, Lemma 2.2 and equations (3.2)–(3.6).
2. C. Wang and X. Zhao, "Weyl's theorem for Toeplitz operators with polynomial symbols on the harmonic Bergman space," Journal of Mathematical Analysis and Applications 495 (2021), 124770, https://doi.org/10.1016/j.jmaa.2020.124770 . The abstract and its existence claim were consulted; its full text was unavailable.
3. K. Guo and D. Zheng, essential-spectrum and index theorem for harmonic-Bergman Toeplitz operators with continuous symbols, as quoted in reference 1, Theorem 2.1 (secondary full-text inspection of the statement rather than direct inspection of the original).
