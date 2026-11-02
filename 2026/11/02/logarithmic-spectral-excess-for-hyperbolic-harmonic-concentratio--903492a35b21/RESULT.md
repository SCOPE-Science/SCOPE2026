# Logarithmic spectral excess for hyperbolic-harmonic concentration in the four-ball

## Finding

Consider the unit ball \(\mathbb B^4\subset\mathbb R^4\), and fix \(s>-1\) and \(0<R<1\). Write \(T=R^2\) and \(c=\log(1/T)\). For the radial concentration operator on weighted square-integrable hyperbolic-harmonic functions defined below, the eigenvalues are strictly decreasing across harmonic degrees and have the exact beta-integral formula
\[
\Lambda_m=\frac{B_T(m+2,s+1)+mB_T(m+2,s+2)+\tfrac14m^2B_T(m+2,s+3)}{B(m+2,s+1)+mB(m+2,s+2)+\tfrac14m^2B(m+2,s+3)},\qquad m\ge0,
\]
with multiplicity \((m+1)^2\). Their sharp large-degree asymptotic is
\[
\Lambda_m\sim \frac{T^2(1-T)^{s+2}}{\Gamma(s+1)(s+2)(s+5)}m^{s+2}T^m.
\]
For the corresponding *Euclidean*-harmonic concentration operator, the degree-\(m\) eigenvalue is
\[
E_m=\frac{B_T(m+2,s+1)}{B(m+2,s+1)}\sim\frac{T^2(1-T)^s}{\Gamma(s+1)}m^sT^m,
\]
so
\[
\frac{\Lambda_m}{E_m}\sim\frac{(1-T)^2}{(s+2)(s+5)}m^2.
\]
Write \(N_H(\varepsilon)\) and \(N_E(\varepsilon)\) for the numbers of eigenvalues greater than \(\varepsilon\), with multiplicities, of the hyperbolic- and Euclidean-harmonic operators. Setting \(L=\log(1/\varepsilon)\), one has
\[
N_H(\varepsilon)=\frac{L^3}{3c^3}+\frac{(s+2)L^2\log L}{c^3}+O_{s,T}(L^2),\qquad
N_E(\varepsilon)=\frac{L^3}{3c^3}+\frac{sL^2\log L}{c^3}+O_{s,T}(L^2),
\]
and in particular the **universal logarithmic spectral excess**
\[
\boxed{N_H(\varepsilon)-N_E(\varepsilon)=\frac{2L^2\log L}{c^3}+O_{s,T}(L^2).}
\]
These estimates hold with \(s,T\) fixed as \(\varepsilon\downarrow0\). All the operators lie in every positive Schatten class.

## Assumptions and scope

The measure is \(d\rho_s(x)=\Gamma(s+3)(\pi^2\Gamma(s+1))^{-1}(1-|x|^2)^s\,dx\), whose total mass is one. Define \(\mathcal H_s\) as the Hilbert space of complex \(L^2(d\rho_s)\) solutions of the hyperbolic-harmonic equation
\[
\Delta_hf=(1-|x|^2)\big[(1-|x|^2)\Delta f+4\langle x,\nabla f\rangle\big]=0.
\]
The concentration operator \(A_{s,R}:\mathcal H_s\to\mathcal H_s\) is uniquely specified by
\[
\langle A_{s,R}f,g\rangle_{\mathcal H_s}=\int_{|x|<R}f(x)\overline{g(x)}\,d\rho_s(x).
\]
The comparator \(A^{\mathrm{E}}_{s,R}\) is defined by the same form on the closed subspace of ordinary Euclidean-harmonic functions \(\Delta f=0\) in \(L^2(d\rho_s)\). Its eigenvalue counting function is \(N_E\); the hyperbolic one is \(N_H\). The incomplete beta and beta integrals mean \(B_T(a,b)=\int_0^T t^{a-1}(1-t)^{b-1}\,dt\) and \(B(a,b)=B_1(a,b)\). All degrees \(m\) are nonnegative integers.

## Proof

**1. Orthogonal hyperbolic-harmonic modes.** Let \(Y_m\) be a spherical harmonic of degree \(m\) on the unit three-sphere. The hyperbolic-harmonic radial solution normalized to \(S_m(1)=1\) is
\[
f_m(r\omega)=r^m S_m(r^2)Y_m(\omega),\qquad S_m(t)=1+\frac m2(1-t).
\]
Indeed the radial separation equation for \(r^mF(r^2)Y_m\), after cancellation of the positive interior scalar factor, reads
\[
(1-t)\big[4tF''(t)+4(m+2)F'(t)\big]+4\big[mF(t)+2tF'(t)\big]=0,
\]
and \(F(t)=1+\frac m2(1-t)\) solves it. (Equivalently, it is the dimension-four truncation of the standard hypergeometric mode formula.) The unique regular radial solution at the origin has this normalization. Different spherical degrees are orthogonal against every radial measure; each degree has dimension \((m+1)^2\) in \(\mathbb R^4\). Their completed direct sum gives \(\mathcal H_s\). The same decomposition with \(S_m\equiv1\) applies to ordinary harmonic functions.

**2. Exact spectral formula.** With \(t=r^2\), the common radial Jacobian gives the unnormalized degree-\(m\) density
\[
p_m(t)=t^{m+1}(1-t)^s\left(1+\frac m2(1-t)\right)^2,\qquad0<t<1.
\]
The normalized mass of \((0,T)\) is \(\Lambda_m\). Expanding the square proves the beta formula. The Euclidean-harmonic density is \(t^{m+1}(1-t)^s\), giving \(E_m\). Since angular irreducible subspaces diagonalize the radial form, these are the entire spectra, with the indicated multiplicities.

**3. Strict hyperbolic degree ordering.** Set \(S_m(t)=1+\frac m2(1-t)\). Direct differentiation shows
\[
\frac d{dt}\log\left(\frac{p_{m+1}(t)}{p_m(t)}\right)=\frac1t-\frac1{S_m(t)S_{m+1}(t)}>0\quad(0<t<1).
\]
Thus the normalized degree-\(m+1\) probability density strictly dominates the degree-\(m\) density in monotone-likelihood-ratio order, whence its cumulative mass at every interior cutoff is strictly lower: \(0<\Lambda_{m+1}<\Lambda_m<1\). Similarly, \(E_{m+1}<E_m\).

**4. Sharp individual eigenvalue tails.** The large-first-argument beta estimate gives
\[
B(m+2,s+j+1)\sim\Gamma(s+j+1)m^{-s-j-1},\qquad j=0,1,2.
\]
Therefore the denominator of \(\Lambda_m\) equals
\[
\Gamma(s+1)\frac{(s+2)(s+5)}4m^{-s-1}(1+o(1)).
\]
For fixed \(T<1\), one-sided endpoint Laplace integration yields
\[
\int_0^T p_m(t)\,dt\sim\frac m4T^{m+2}(1-T)^{s+2}.
\]
Their quotient proves the stated asymptotic; applying the same two estimates without \(S_m\) gives the Euclidean formula and their two-power ratio. Exponential decay proves membership in each \(\mathcal S_p\) for every finite \(p>0\), after accounting for the quadratic multiplicities.

**5. Counting the spectrum.** If \(\lambda_m\sim C m^a e^{-cm}\) for \(C,c>0\) and fixed real \(a\), with \(\lambda_m\) eventually decreasing, taking logarithms and solving the threshold inequality \(\lambda_m>\varepsilon\) shows the last admitted degree is
\[
M(L)=\frac Lc+\frac ac\log L+O(1),\qquad L=\log(1/\varepsilon).
\]
Indeed insertion of either expression plus or minus a sufficiently large constant bounds the true crossing because the residual logarithmic error is bounded. The exact multiplicity sum is
\[
\sum_{m=0}^{M}(m+1)^2=\frac{(M+1)(M+2)(2M+3)}6=\frac{M^3}{3}+O(M^2).
\]
Substituting \(a=s+2\) or \(a=s\) and expanding yields the two stated asymptotics with remainder \(O(L^2)\), and subtraction proves the excess. None of the finite checker runs below is used in this infinite-degree argument.

## Verification

The standalone standard-library script `checker.py` implements the radial beta integrals as exact rational polynomial integrals for integer weights and rational cutoff values. It checks the expanded formula, monotonicity and sample values of the tail constants and counting estimates, reporting 4,395 finite assertions passed. The radial differential equation is independently confirmed by direct substitution into the displayed PDE; the sharp asymptotics and the counting law are established by the preceding analytical arguments, not by finite enumeration. To reproduce: `python3 checker.py`.

## Relationship to prior work

Blaschke, Engliš and Youssfi (arXiv:2404.07384, first publicly posted April 10, 2024) establish spherical/hypergeometric decompositions of H-harmonic weighted Bergman spaces and their Möbius-invariant Dirichlet limit. The present dimension-four radial profile follows from that known general expansion; it is **not** presented as a new formula by itself. The result here instead concerns complete *inner-ball concentration spectra*, strict degree ordering and the logarithmic gap between H-harmonic and Euclidean-harmonic eigenvalue counts. Üreyen (arXiv:2303.12137) studies hyperbolic-harmonic Bergman atomic decomposition, interpolation and embeddings, not this localization spectrum. Choe, Koo and Lee (2008) analyze positive Schatten Toeplitz operators on an ordinary Euclidean-harmonic Bergman ball; their operator and differential equation are different. Bauer, Herrera Yañez and Vasilevski study holomorphic radial Toeplitz operators on complex balls, likewise a distinct function class. These distinctions do not establish exhaustive priority; equivalent-operator presentations may still exist.

## Limitations

The theorem is specific to the real four-ball, scalar radial cutoff \(0<R<1\), fixed \(s>-1\), and asymptotic \(\varepsilon\downarrow0\); uniformity as the cutoff approaches the boundary or the weight changes is not claimed. The dimensional simplification \(S_m(t)=1+\tfrac m2(1-t)\) fails verbatim in other dimensions. The exact eigenvalues and asymptotic coefficients are mathematical claims with an analytical derivation and finite diagnostic checks; they have not undergone independent validation. The novelty comparison is literature-limited and not a proof of historical uniqueness.

## References

1. P. Blaschke, M. Engliš and E.-H. Youssfi, *A Möbius invariant space of H-harmonic functions on the ball*, arXiv:2404.07384 (first posted April 10, 2024), https://arxiv.org/abs/2404.07384.
2. A. Ersin Üreyen, *Harmonic Bergman Spaces on the Real Hyperbolic Ball: Atomic Decomposition, Interpolation and Inclusion Relations*, arXiv:2303.12137 (first posted March 21, 2023), https://arxiv.org/abs/2303.12137.
3. B. R. Choe, H. Koo and Y. J. Lee, *Positive Schatten class Toeplitz operators on the ball*, *Studia Mathematica* 189 (2008), https://doi.org/10.4064/sm189-1-6.
4. W. Bauer, C. Herrera Yañez and N. Vasilevski, *Eigenvalue Characterization of Radial Operators on Weighted Bergman Spaces Over the Unit Ball*, 2013 (holomorphic, not hyperbolic-harmonic).
