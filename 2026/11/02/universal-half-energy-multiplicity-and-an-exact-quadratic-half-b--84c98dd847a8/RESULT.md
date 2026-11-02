# Universal half-energy multiplicity and an exact quadratic half-ball Slepian spectrum

## Finding

Let \(d\ge2\) and \(L\ge0\). For a bounded, reflection-symmetric open set \(\Omega\subset\mathbb R^d\), equipped with a finite, strictly positive, reflection-invariant density, let \(\Pi_L\) denote all complex polynomials of total degree at most \(L\), and let \(C_L=P_L\mathbf1_{\{x_1>0\}}\vert_{\Pi_L}\) be the half-domain energy-concentration operator. Every eigenvalue lies strictly between zero and one. Its spectrum is symmetric under \(\lambda\mapsto1-\lambda\), and the multiplicity of exactly \(\lambda=1/2\) is

\[
h_{d,L}=\sum_{j=0}^{\lfloor L/2\rfloor}\binom{d+L-2j-2}{L-2j}.
\]

For the uniformly weighted unit ball \(\Omega=B^d\) and \(L=2\), this general law can be strengthened to a complete closed spectrum. Put

\[
\mu_d=\frac{\Gamma((d+2)/2)}{\sqrt\pi\,\Gamma((d+3)/2)},\quad
s_0=\mu_d\frac{d+2}{d+3}\sqrt{\frac{3d+11}{2}},\quad
s_1=\mu_d\frac{d+2}{d+3}\sqrt{d+4}.
\]

Then \(0<s_1<s_0<1\), and the eigenvalues, including multiplicities, are

\[
\frac{1\pm s_0}{2}\quad(\text{each once}),\qquad
\frac{1\pm s_1}{2}\quad(\text{each with multiplicity }d-1),\qquad
\frac12\quad\left(\text{multiplicity }\frac{d^2-d+2}{2}\right).
\]

In particular, the sharp quadratic-polynomial concentration fraction is \((1+s_0)/2\), with a unique maximizing complex line. As \(d\to\infty\), the two squared singular values converge to \(3/\pi\) and \(2/\pi\), respectively.

## Assumptions and scope

Write \(x=(t,y)\), where \(t=x_1\in\mathbb R\) and \(y\in\mathbb R^{d-1}\). Reflection is \((t,y)\mapsto(-t,y)\). Assume \(\Omega\) is bounded, nonempty, open, invariant under reflection, and has nonempty intersections with both open halfspaces. Assume \(w\in L^1(\Omega)\), \(w>0\) almost everywhere, and \(w(t,y)=w(-t,y)\) almost everywhere. The Hilbert norm is \(\|p\|^2=\int_\Omega|p|^2w\,dx\); multiplication by \(\mathbf1_{\{t>0\}}\) is compressed by the orthogonal projection onto \(\Pi_L\). The statement holds for all integers \(L\ge0\) and all \(d\ge2\). For the explicit spectrum and maximizers only, take \(\Omega=B^d\), \(w=1/\operatorname{vol}(B^d)\), and \(L=2\).

## Proof

**General half-energy rigidity.** Let \(R\) be reflection on \(\Pi_L\), and decompose \(\Pi_L=E\oplus O\) into polynomials even and odd in \(t\). Both spaces are orthogonal because the measure is invariant under reflection. Let \(J=P_L\operatorname{sgn}(t)\vert_{\Pi_L}\). Reflection gives \(RJR=-J\), so relative to \(E\oplus O\),

\[
J=\begin{pmatrix}0&B\\ B^*&0\end{pmatrix},\qquad C_L=\frac{I+J}{2}.
\]

The map \(B:O\to E\) is injective. Indeed, any \(f\in O\) has the polynomial factorization \(f=t h\) with \(h\in E\) and \(\deg h\le L-1\). If \(Bf=0\), taking its inner product with \(h\) gives

\[
0=\langle Bf,h\rangle=\int_\Omega |t|\,|h(t,y)|^2w(t,y)\,dx,
\]

forcing \(h=0\) and \(f=0\). Thus \(J\) has exactly \(\dim O\) strictly positive and the same number of strictly negative eigenvalues, and exactly \(\dim E-\dim O\) zeros. For each monomial \(y^\alpha\) of degree \(r\), the allowable powers of \(t\) are \(0,\ldots,L-r\), and the number of even ones exceeds the number of odd ones by one exactly when \(L-r\) is even. Summing the number \(\binom{d+r-2}{r}\) of such monomials proves the displayed formula for \(h_{d,L}\). Since no nonzero polynomial \(f\) can have \(\operatorname{sgn}(t)f\) equal almost everywhere to a polynomial on both open halves, the finite-dimensional compression \(J\) has norm strictly less than one. This proves the spectral pairing, exact central multiplicity, and strict interior location.

**Quadratic spectrum on the ball.** Use probability-normalized ball moments. Set \(\mu_d=\mathbb E|t|\). Rotational invariance and beta integration give

\[
\mathbb Et^2=\frac1{d+2},\quad \mathbb Et^4=\frac3{(d+2)(d+4)},\quad
\mathbb E|t|^3=\frac{2\mu_d}{d+3},\quad
\mathbb Ey_j^2=\frac1{d+2},\quad
\mathbb Et^2y_j^2=\frac1{(d+2)(d+4)},\quad
\mathbb E|t|y_j^2=\frac{\mu_d}{d+3}.
\]

The odd quadratic polynomials have orthonormal basis

\[
u_0=\sqrt{d+2}\,t,\qquad
u_j=\sqrt{(d+2)(d+4)}\,t y_j\quad(1\le j\le d-1).
\]

The images under \(B\) are mutually orthogonal by \(O(d-1)\)-symmetry. For the first, \(Bu_0=\sqrt{d+2}\,P_E|t|\). Conditional rotation symmetry gives \(\mathbb E(|y|^2\mid t)=\frac{d-1}{d+1}(1-t^2)\), so the projection of \(|t|\) onto even quadratics uses only \(1,t^2\). The displayed moments yield

\[
P_E|t|=\mu_d\frac{d+2}{2(d+3)}\,[1+(d+4)t^2].
\]

Its normalized even companion is

\[
v_0=\sqrt{\frac{d+2}{2(3d+11)}}\,[1+(d+4)t^2].
\]

Thus \(Bu_0=s_0v_0\). For each transverse direction the companion is \(v_j=\sqrt{d+2}\,y_j\), and the moment \(\mathbb E|t|y_j^2\) gives \(Bu_j=s_1v_j\). The two squared singular values are

\[
s_0^2=\mu_d^2\frac{(d+2)^2(3d+11)}{2(d+3)^2},\qquad
s_1^2=\mu_d^2\frac{(d+2)^2(d+4)}{(d+3)^2}.
\]

Their ratio is \((3d+11)/(2d+8)>1\). All remaining even quadratics are in the kernel of \(J\), with multiplicity \(\binom{d+2}{2}-2d=(d^2-d+2)/2\). Therefore \((u_0\pm v_0)/\sqrt2\) are normalized eigenfunctions with eigenvalues \((1\pm s_0)/2\); the analogous \((u_j\pm v_j)/\sqrt2\) yield the transverse pairs. This gives the full spectrum and proves that the maximizers are exactly the nonzero scalar multiples of \(u_0+v_0\). Finally \(\Gamma(z)/\Gamma(z+1/2)\sim z^{-1/2}\) proves the two dimension limits.

## Verification

The standalone `halfball_slepian_checker.py` independently constructs the Gram matrix of all monomials through degree \(L\), computes the compressed sign multiplier from closed beta/gamma moments, and diagonalizes the resulting matrix. It checks the displayed quadratic eigenvalues in dimensions \(2\) through \(9\), and checks exact central multiplicities, complementary eigenvalue pairs, and strict \((0,1)\) spectrum for dimensions \(2\) through \(5\) and bandwidths \(0\) through \(3\). It reports 24 passing dimension-band tests. This is supplementary numerical evidence, not a substitute for the general algebraic proof.

## Relationship to prior work

Gerhards and Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth* (arXiv:2308.03543, first public 7 August 2023), provide the polynomial-bandlimit framework, prove asymptotic eigenvalue clustering and a Shannon-number law, and illustrate three-dimensional subdomains numerically. Their Theorem 2.1 and Appendix B do not state the all-bandwidth half-energy multiplicity or the explicit all-dimensional quadratic spectrum above. Earlier ball-Slepian work of Khalid, Kennedy and McEwen uses Fourier-Bessel and Fourier-Laguerre bandwidths rather than degree-bounded polynomials. Analogous central-eigenvalue laws for hemispherical spherical harmonics, half-line Hermite functions, and discrete Walsh frequency bands rely on different ambient spaces and do not give the ball-polynomial formulas. General parity block decompositions are standard ingredients; the positive-weight polynomial injectivity and the explicit gamma-function spectral values are the asserted contribution.

## Limitations

The closed list of all noncentral eigenvalues is proved only for polynomial bandwidth \(L=2\), although the central multiplicity and pairing law holds at every finite polynomial degree. The general-domain theorem requires reflection symmetry and positive density on an open domain. No assertion is made about radial/angular Fourier-Jacobi bandwidths, arbitrary nonsymmetric subdomains, higher-degree sharp outer eigenvalues, or noise-robust reconstruction. Historical priority is provisional; a specialized earlier calculation or a stronger abstract result may imply some of these formulas. No independent mathematical validation is represented.

## References

1. C. Gerhards and X. Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543, first version 7 August 2023, https://arxiv.org/abs/2308.03543 .
2. Z. Khalid, R. A. Kennedy and J. D. McEwen, *Slepian spatial-spectral concentration on the ball*, Applied and Computational Harmonic Analysis 40 (2016), 470–504, https://doi.org/10.1016/j.acha.2015.03.008 .
3. C. Gerhards and X. Huang, *Spatiospectral localization within the ball — studies on the influence of the spectral shape*, Applied and Computational Harmonic Analysis 84 (2026), 101882, https://doi.org/10.1016/j.acha.2026.101882 .
