# The ninefold scale-gap transition in two-octave Cauchy-wavelet localization

## Finding
For each integer \(k\ge2\), the positive Cauchy-wavelet localization operator with scale mask \([1,2]\cup[k,2k]\) has a spectral multiplier with exactly one critical point if \(2\le k\le8\), but exactly three simple critical points if \(k\ge9\). In the latter case there are two distinct local maxima and a single intervening local minimum, and the lower-frequency local maximum is globally strict. Consequently the absolutely continuous spectral multiplicity is two almost everywhere for \(2\le k\le8\), whereas for \(k\ge9\) a nonempty spectral-energy interval has multiplicity four (multiplicity two elsewhere). This is a sharp transition between the consecutive integer scale ratios eight and nine.

For \(k\ge9\), let \(0<r_{1,k}<r_{2,k}<r_{3,k}<1\) be the three roots of
\[
1-2t+kt^{k-1}-2kt^{2k-1}=0,
\]
and let \(p_k(t)=t-t^2+t^k-t^{2k}\). Then the fourfold multiplicity interval is exactly
\[
\bigl(p_k(r_{2,k}),\,p_k(r_{1,k})\bigr).
\]
The top eigenvalue is absent: the norm \(M_k=p_k(r_{3,k})\) is not attained by a nonzero Hardy signal. Moreover, as \(k\to\infty\),
\[
-k\log r_{3,k}=\log2+\frac2k+O(k^{-2}),\qquad
M_k=\frac14+\frac{\log2}{k}
+\frac{1-\frac32(\log2)^2}{k^2}+O(k^{-3}).
\]

## Assumptions and scope
Use the unitary Fourier transform \(\widehat f(\omega)=(2\pi)^{-1/2}\int_{\mathbb R}f(t)e^{-it\omega}\,dt\) and the Hardy space \(H^2_+=\{f\in L^2(\mathbb R):\widehat f(\omega)=0\text{ for almost all }\omega<0\}\). Let \(\widehat\psi(\omega)=\sqrt{\omega/\pi}\,e^{-\omega}\mathbf1_{\omega>0}\). For \(x\in\mathbb R\) and \(y>0\) define \(\psi_{x,y}(t)=y^{-1/2}\psi((t-x)/y)\) and \(W_\psi f(x,y)=\langle f,\psi_{x,y}\rangle_{L^2}\). This wavelet transform is isometric from \(H^2_+\) to \(L^2(\mathbb R\times\mathbb R_+,dx\,dy/y^2)\).

For integer \(k\ge2\), set \(E_k=[1,2]\cup[k,2k]\); the touching endpoint for \(k=2\) has measure zero. The positive localization operator is \(L_k=W_\psi^*M_{\mathbf1_{\mathbb R\times E_k}}W_\psi\) on \(H^2_+\). All spectral multiplicities refer to the standard Lebesgue absolutely continuous spectral representation; endpoint multiplicities are not asserted.

## Proof
**1. Exact wavelet normalization and diagonalization.** The Fourier transform in the translation variable of \(W_\psi f(\cdot,y)\) equals \(\sqrt{2\pi y}\,\widehat f(\omega)\overline{\widehat\psi(y\omega)}\), up to an immaterial unit-modulus convention in the inner product. Consequently Plancherel gives
\[
\int_{\mathbb R}|W_\psi f(x,y)|^2dx
=\int_0^\infty 2\pi y\,|\widehat\psi(y\omega)|^2|\widehat f(\omega)|^2d\omega.
\]
Since \(2\pi\int_0^\infty|\widehat\psi(y\omega)|^2dy/y=\int_0^\infty2\omega e^{-2y\omega}dy=1\), integration against \(dy/y^2\) proves the isometry. Restriction to the two scale bands yields the exact multiplier
\[
m_k(\omega)=\int_{E_k}2\omega e^{-2y\omega}\,dy
=e^{-2\omega}-e^{-4\omega}+e^{-2k\omega}-e^{-4k\omega}
=p_k(e^{-2\omega}).
\]

**2. Exact finite root counts for ratios two through eight.** Differentiation gives
\[
p'_k(t)=1-2t+kt^{k-1}-2kt^{2k-1}.
\]
For \(2\le k\le8\), the exact rational Sturm algorithm for \(p'_k\) gives the following variations at \(t=0\) and \(t=1\) (zero terms omitted):

| \(k\) | \(V(0)\) | \(V(1)\) | \(V(0)-V(1)\) |
|---|---:|---:|---:|
| 2 | 1 | 0 | 1 |
| 3 | 2 | 1 | 1 |
| 4 | 3 | 2 | 1 |
| 5 | 3 | 2 | 1 |
| 6 | 4 | 3 | 1 |
| 7 | 4 | 3 | 1 |
| 8 | 4 | 3 | 1 |

The reproducibility program `check.py` constructs each integer polynomial, forms its exact Euclidean Sturm chain, and checks these signs and square-free roots. With \(p'_k(0)>0\), \(p'_k(1)=-k-1<0\), and one root, the multiplier has exactly one simple maximum.

**3. Exactly three stationary points for every ratio at least nine.** Set \(s=13/20\). For any integer \(k\ge9\), four exact sign tests are
\[
p'_k(1/2)>0,\quad p'_k(s)<0,\quad
p'_k(1-1/k)>0,\quad p'_k(1)=-k-1<0.
\]
For the second, \(p'_k(s)<-3/10+ks^{k-1}<0\), because \(9(13/20)^8<3/10\) and \(ks^{k-1}\) decreases for \(k\ge9\). For the third put \(u=1-1/k\). The elementary bounds \(u^{k-1}\ge e^{-1}\) and \(u^k\le e^{-1}\) imply
\[
p'_k(u)\ge-1+\frac2k+k\frac{e-2}{e^2}
>-1+\frac2k+\frac{3k}{32}>0.
\]
Here \((e-2)/e^2>3/32\), and the last expression is positive and increasing for \(k\ge9\). Hence the three mutually disjoint intervals \((1/2,s)\), \((s,1-1/k)\), and \((1-1/k,1)\) each contain a critical point. Descartes's rule gives **at most three positive roots counted with multiplicity** for the four-term sign pattern \(+,-,+,-\). The roots are therefore exactly three and simple, with alternating maximum–minimum–maximum structure.

**4. Which peak is global.** The first peak occurs at \(r_{1,k}<s\), so \(p_k(r_{1,k})\le1/4+s^k\). Put \(t_*=2^{-1/k}\), which lies to the right of \(1-1/k\) because \(\log2<1\). Then
\[
p_k(t_*)=\frac14+t_*(1-t_*),\qquad
t_*(1-t_*)\ge\frac{\log2}{k}e^{-2\log2/k}
>\frac{14}{27k}>\frac1{2k}>s^k.
\]
The strict middle estimate uses \(\log2>2/3\) and \(e^{-2\log2/k}>1-2/9=7/9\); the last estimate follows from \(18s^9<1\) and monotonic decrease of \(2ks^k\) for \(k\ge9\). The right peak dominates this trial point, so \(p_k(r_{3,k})\ge p_k(t_*)>p_k(r_{1,k})\). Thus the top peak is unique and strict.

**5. Spectrum, multiplicity, and asymptotics.** As \(p_k\) is positive on \((0,1)\), vanishes at both endpoints, and has one or three simple stationary points, it has image \([0,M_k]\) after closure. The spectral theorem for a multiplication operator yields \(\sigma(L_k)=[0,M_k]\). The level sets of a nonconstant polynomial are finite, hence no eigenvalue occurs. On each monotonic interval, change of variables \(\lambda=p_k(t)\) gives absolutely continuous spectral measures. The number of such inverse branches is two except that, for \(k\ge9\), energies strictly between the local minimum and lower local maximum have four inverse branches. Hence the asserted multiplicities.

For asymptotics write \(t=e^{-x/k}\):
\[
G_k(x)=e^{-x}-e^{-2x}+e^{-x/k}-e^{-2x/k}.
\]
The maximizing right peak is confined to \(0<x<-k\log(1-1/k)\), a fixed compact interval for large \(k\). On that interval \(G_k\) converges in \(C^2\) to \(F(x)=e^{-x}-e^{-2x}\), whose unique maximum is at \(x_0=\log2\), with \(F''(x_0)=-1/2\). A uniform Taylor expansion yields \(G_k(x)=F(x)+x/k-3x^2/(2k^2)+O(k^{-3})\) in \(C^2\), so the critical equation gives \(x_k=x_0+2/k+O(k^{-2})\). Substituting into the uniform expansion gives the displayed two-term correction for \(M_k\).

## Verification
Run `python check.py` (requires Python and SymPy). It checks the rational Sturm variations for each \(k=2,\ldots,8\), polynomial identities, and exact sign inequalities for \(k=9,\ldots,39\), together with representative numerical profiles for several larger ratios; at preparation time all 205 assertions passed. The unbounded range \(k\ge9\), spectrum multiplicities, and asymptotics are justified by the proofs above, **not** by a finite test. Rational Sturm arithmetic is deterministic and reproducible.

## Relationship to prior work
Hutník (2011), *Wavelets from Laguerre Polynomials and Toeplitz-type Operators*, Theorem 3.2, already gives the general spectral-function representation for scale-only Calderón–Toeplitz symbols, including vertical interval symbols; this diagonalization is used here and is **not** claimed as new. Hutník–Maximenko–Mišková (2016), *Toeplitz Localization Operators: Spectral Functions Density*, gives the general convolution spectral-function representation and a density theorem for vertical symbols, rather than a sharp stationary-point classification for the explicit two-octave filters. Nicola–Tilli (2022, arXiv:2207.08624), Section 5, provides sharp norm inequalities for integrable Cauchy-wavelet localization weights, but these entire-horizontal-strip masks have infinite Haar measure and are outside those finite-\(L^p\) hypotheses. The claim here is only the newly derived **sharp ninefold bifurcation, full multiplicity pattern, peak comparison and large-gap asymptotic for this natural two-band family**. A search of accessible literature and mathematical result records found no such classification; it does not establish historical uniqueness.

## Limitations
The integer-ratio classification does not identify a critical transition for noninteger ratios. The symbol is restricted to two equally wide octave bands and to the displayed Cauchy wavelet. The two local peaks are not eigenvalues because the domain is translation invariant. No independent mathematical audit is claimed. A genuinely earlier equivalent result might be present in literature not accessible or not found by the searches reported in `AUDIT.json`.

## References
1. O. Hutník, *Wavelets from Laguerre Polynomials and Toeplitz-type Operators*, Integral Equations and Operator Theory (2011), author-hosted complete text: https://umv.science.upjs.sk/hutnik/papers/propertiesI.pdf.
2. O. Hutník, E. A. Maximenko and A. Mišková, *Toeplitz Localization Operators: Spectral Functions Density*, Complex Analysis and Operator Theory **10** (2016), 1757–1774, DOI:10.1007/s11785-016-0564-1; author-provided complete text at https://www.researchgate.net/publication/303411897_Toeplitz_Localization_Operators_Spectral_Functions_Density.
3. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624, first public 2022-07-18; https://arxiv.org/abs/2207.08624.
4. J.-P. Serre, *A Course in Arithmetic*, Chapter II (classical Descartes rule); standard Sturm theorem of real algebra, alternatively derivable by the Euclidean sign-change algorithm in `check.py`.
