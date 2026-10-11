# Half-line Hermite spectral gaps: arbitrary-mask Cauchy formula and a Barnes limit

## Finding
For every finite nonempty selection of one-dimensional harmonic-oscillator eigenfunctions, exact concentration on the positive half-line has a parity-rigid midpoint eigenspace and an explicit noncentral spectral-gap product. For the first \(2m\) oscillator levels, the product decays with exponent \(1/4\) and a sharp Barnes \(G\)-constant.

Use the normalized physicists' Hermite functions
\[\psi_n(x)=\frac{H_n(x)e^{-x^2/2}}{\sqrt{2^n n!\sqrt\pi}},\qquad n\in\mathbb N_0.\]
For any finite nonempty mask \(F\subset\mathbb N_0\), define \(V_F=\operatorname{span}\{\psi_n:n\in F\}\), the orthogonal projection \(P_F\) onto \(V_F\), and \(C_F=P_FM_{1_{(0,\infty)}}P_F\big|_{V_F}\). Write
\[E=\{a\in\mathbb N_0:2a\in F\},\quad O=\{b\in\mathbb N_0:2b+1\in F\},\quad e=|E|,\quad o=|O|,\quad r=\min(e,o).\]
With the boundary constants
\[u_a=\frac{(-1)^a\sqrt{(2a)!}}{2^a a!\pi^{1/4}},\qquad v_b=\frac{(-1)^b\sqrt{2(2b+1)!}}{2^b b!\pi^{1/4}},\]
the noncentral gap-product invariant (algebraic multiplicities included)
\[D_F=\prod_{\substack{\lambda\in\operatorname{spec}(C_F)\\\lambda\ne1/2}}|2\lambda-1|\]
has the exact finite formula
\[\boxed{D_F=\sum_{\substack{I\subseteq E,\;J\subseteq O\\|I|=|J|=r}}\frac{\displaystyle\prod_{a\in I}u_a^2\prod_{b\in J}v_b^2\prod_{a<a'\in I}(2a'-2a)^2\prod_{b<b'\in J}(2b'-2b)^2}{\displaystyle\prod_{a\in I,b\in J}(2b+1-2a)^2}.}\]
For \(r=0\) the one-term empty minor has value one. Furthermore,
\[\boxed{\operatorname{mult}_{C_F}(1/2)=|e-o|},\]
and all \(2r\) remaining eigenvalues occur in complementary pairs \(\lambda,1-\lambda\). No concentration eigenvalue equals zero or one.

For the canonical low-pass mask \(F_m=\{0,1,\ldots,2m-1\}\) with integer \(m\ge1\), the previous expression collapses to
\[\boxed{D_{F_m}=\prod_{j=0}^{m-1}\frac{\Gamma(j+1)^2}{\Gamma(j+1/2)\Gamma(j+3/2)}=\frac{G(m+1)^2G(1/2)G(3/2)}{G(m+1/2)G(m+3/2)}}\]
and in particular
\[\boxed{\lim_{m\to\infty}m^{1/4}D_{F_m}=\sqrt\pi\,G(1/2)^2\approx0.645002449}.\]

## Assumptions and scope
The Hilbert space is \(L^2(\mathbb R,dx)\) with ordinary Lebesgue measure; all finite spans are complex. The Hermite functions are normalized as displayed above and satisfy \((-d^2/dx^2+x^2)\psi_n=(2n+1)\psi_n\) and \(\psi_n(-x)=(-1)^n\psi_n(x)\). All finite masks, including gaps, unbalanced parity counts, and one-element masks, are allowed. The half-line is exactly \((0,\infty)\), not a shifted or finite interval. The indexed product counts each eigenvalue with its algebraic multiplicity. Barnes \(G\) obeys \(G(1)=1\) and \(G(z+1)=\Gamma(z)G(z)\).

## Proof
**1. Exact Hermite boundary data.** Rodrigues' formula gives \(H_{2a}(0)=(-1)^a(2a)!/a!\), \(H_{2b+1}(0)=0\), and \(H_{2b+1}'(0)=2(-1)^b(2b+1)!/b!\). In the stated normalization, \(\psi_{2a}(0)=u_a\), \(\psi'_{2b+1}(0)=v_b\), while \(\psi'_{2a}(0)=\psi_{2b+1}(0)=0\). All \(u_a,v_b\) are nonzero.

**2. Boundary-Wronskian Cauchy reduction.** Let \(f=\psi_{2a}\) and \(g=\psi_{2b+1}\). Their oscillator equations and integration by parts give
\[(2(2b+1-2a))\int_0^\infty f(x)g(x)\,dx=f(0)g'(0)-f'(0)g(0)=u_av_b.\]
The boundary term at infinity vanishes by Gaussian decay. Same-parity Hermite products are even, so their positive-half-line inner products are one half of their full-line orthogonality. In the parity-ordered orthonormal basis, the centered operator \(Q_F=2C_F-I\) therefore has block form
\[Q_F=\begin{pmatrix}0&B\\B^*&0\end{pmatrix},\qquad B_{ab}=\frac{u_av_b}{2b+1-2a},\quad a\in E,\ b\in O.\]
Distinct even integers \(2a\) and odd integers \(2b+1\) never coincide. The Cauchy determinant identity says any square minor indexed by equal-size \(I\subset E\), \(J\subset O\) is nonzero, with its squared modulus exactly
\[|\det B_{I,J}|^2=\frac{\prod_{a\in I}u_a^2\prod_{b\in J}v_b^2\prod_{a<a'\in I}(2a'-2a)^2\prod_{b<b'\in J}(2b'-2b)^2}{\prod_{a\in I,b\in J}(2b+1-2a)^2}.\]
Indeed this follows by pulling the row and column factors out and applying the usual Cauchy determinant identity to \(1/(y_b-x_a)\). Every maximal minor is nonzero, so \(\operatorname{rank}B=r\). The spectrum of \(Q_F\) consists of \(\pm\sigma_1(B),\ldots,\pm\sigma_r(B)\) and \(|e-o|\) zeros. Since \(C_F=(I+Q_F)/2\), the midpoint multiplicity and pair symmetry follow. A finite nonzero Hermite combination is real-analytic, so it cannot vanish identically on a half-line; strict positivity of \(\int_0^\infty |f|^2\) and \(\int_{-\infty}^0|f|^2\) implies all concentration eigenvalues lie in \((0,1)\).

**3. All-mask gap product.** The nonzero gap factors of \(Q_F\) are paired singular values \(\pm\sigma_j(B)\). Hence
\[D_F=\prod_{j=1}^r\sigma_j(B)^2.\]
The product of squared nonzero singular values is \(\det(B^*B)\) when \(o\le e\), or \(\det(BB^*)\) when \(e\le o\); the zero-dimensional convention is one. Cauchy–Binet expresses this as the sum of squares of maximal minors from Step 2, proving the displayed formula.

**4. Contiguous low-pass determinant.** For \(E=O=\{0,\ldots,m-1\}\), there is one maximal minor. Write \(D_m=D_{F_m}=|\det B_m|^2\) with \(D_0=1\). Extending \(B_m\) by its next row and column in the squared Cauchy determinant gives
\[\frac{D_{m+1}}{D_m}=u_m^2v_m^2\frac{16^m(m!)^4}{((2m-1)!!)^2((2m+1)!!)^2}=\frac{2\,16^m(m!)^4}{\pi(2m)!(2m+1)!}.\]
Here \((-1)!!=1\). Euler's gamma duplication formula simplifies this to
\[\frac{D_{m+1}}{D_m}=\frac{\Gamma(m+1)^2}{\Gamma(m+1/2)\Gamma(m+3/2)}.\]
Multiplication over \(m=0,\ldots,M-1\) proves the finite gamma product. Using \(G(z+1)=\Gamma(z)G(z)\) proves the Barnes quotient displayed in the finding.

**5. Sharp quarter-power limit.** From the standard large-positive-argument Barnes expansion
\[\log G(z+1)=\frac{z^2}{2}\log z-\frac{3z^2}{4}+\frac{z}{2}\log(2\pi)-\frac1{12}\log z+\zeta'(-1)+O(z^{-2}),\]
the centered second difference satisfies
\[\log G(m+1/2)+\log G(m+3/2)-2\log G(m+1)=\frac14\log m+o(1).\]
Applying this to the exact Barnes quotient and using \(G(3/2)=\sqrt\pi\,G(1/2)\) yields \(m^{1/4}D_m\to\sqrt\pi\,G(1/2)^2\). No numerical extrapolation is used in the proof.

## Verification
The accompanying standalone `verify.py` calculates oscillator half-line Gram entries by independent numerical quadrature and compares them against the Wronskian formula. It then checks every nonempty mask in initial ranges of oscillator levels, including midpoint multiplicity, complementary pairing, and noncentral products against independently computed minors. It also compares the low-pass determinant against the exact gamma product through ten matrix sizes and the limiting constant using a long finite product. Execution returned `VERIFY_OK masks=2036 max_gram_err=4.441e-16 max_gap_err=3.220e-15 exact_barnes_cases=10 asymptotic_ratio=0.645002448 target=0.645002449`. These are numerical diagnostics, not infinite proofs.

## Relationship to prior work
Hermite functions and parity-resolved expansions are classical. Lemvig's Hermite-series/Gabor article supplies a first-public 2015 harmonic-analysis starting point (primary MSC 42C15) but investigates Gabor frame obstructions, not positive-half-line concentration. Jaming–Karoui–Kerman–Spektor study approximation of almost time- and band-limited functions via Hermite series and do not derive an arbitrary-mask midpoint eigenspace or spectral-gap product.

A particularly close equivalent language is the Gaussian Hankel determinant with a sign jump at the origin, equivalently the parity characteristic function of the number of positive GUE eigenvalues. Its–Krasovsky's asymptotic theorem treats the Gaussian jump parameter in the strict strip \(|\Re\beta|<1/4\), not the sign case \(\beta=1/2\), and it does not calculate the exact arbitrary-mask matrix. Charlier's one-cut generalization retains the strict strip; Charlier–Deaño's related discontinuous-weight theory uses nonnegative jump weights. These stronger analytic frameworks are acknowledged, without claiming that the classical Wronskian and Cauchy identities are new.

## Limitations
The theorem is for the centered half-line and normalized one-dimensional Hermite oscillator only. It does not assert exact individual noncentral eigenvalues, a uniform spectral gap for growing masks, or equivalent formulas for shifted thresholds. The exact gamma/Barnes formula applies to even low-pass dimension \(2m\); no asymptotic is asserted for arbitrary irregular masks. The sign-jump Hankel literature is a serious source of potential equivalent formulations, and a future literature comparison may uncover the exact product under a different name. Numerical checks cannot resolve that bibliographic risk.

## References
- J. Lemvig, *On some Hermite series identities and their applications to Gabor analysis*, arXiv:1511.09470, first public 2015-11-30; primary MSC 42C15. https://arxiv.org/abs/1511.09470
- P. Jaming, A. Karoui, R. Kerman, S. Spektor, *Approximation of almost time and band limited functions I: Hermite expansions*, arXiv:1407.1293, 2014. https://arxiv.org/abs/1407.1293
- A. Its, I. Krasovsky, *Hankel determinant and orthogonal polynomials for the Gaussian weight with a jump*, arXiv:0706.3192, 2007. https://arxiv.org/abs/0706.3192
- C. Charlier, *Asymptotics of Hankel determinants with a one-cut regular potential and Fisher-Hartwig singularities*, arXiv:1706.03579, 2017. https://arxiv.org/abs/1706.03579
- C. Charlier, A. Deaño, *Asymptotics for Hankel Determinants Associated to a Hermite Weight with a Varying Discontinuity*, arXiv:1708.02519, 2017. https://arxiv.org/abs/1708.02519
