# Sharp Fourier bandwidth and positivity for high-order projective-circle Fréchet degeneracy

## Finding
For each integer \(m\ge2\), the smallest Fourier degree of a strictly positive trigonometric-polynomial probability density on the projective circle capable of a unique population intrinsic Fréchet mean with a \(2m\)-fold loss minimum is **exactly \(m\)**. At that sharp degree there is, modulo rotation, one one-parameter family, with an explicit sharp positivity interval.

For \(c\in[-1,1]\), let
\[
R_m(c)=2m(1+c)^{m-1}(mc-m+1),\qquad
\epsilon_m=\frac{1}{2(2m-1)\bigl((2m-1)(m-1)/m^2\bigr)^{m-1}}.
\]
All sharp-degree densities are translates of
\[
\psi_{m,\epsilon}(t)=\frac{1+\epsilon R_m(\cos2t)}{\pi},
\qquad 0<\epsilon<\epsilon_m.
\]
Their Fréchet functions satisfy the **exact identity**
\[
F(t)-F(0)=\epsilon(1-\cos2t)^m,
\qquad F(0)=\frac{\pi^2}{12}-\epsilon\frac{\binom{2m}{m}}{2^m}.
\]
In particular, the Fréchet mean is unique, and its loss has exact order \(2m\). At the endpoint \(\epsilon=\epsilon_m\) the density has a zero; above it the putative density takes negative values. Consequently strict positivity has the precise stated range.

## Assumptions and scope
Write \(T=\mathbb R/\pi\mathbb Z\) for the projective circle, with geodesic metric \(d(t,u)=\min_{k\in\mathbb Z}|t-u+k\pi|\). The population Fréchet function of a law with density \(\psi\) with respect to angular Lebesgue measure is \(F(t)=\int_{-\pi/2}^{\pi/2}d(t,u)^2\psi(u)\,du\). Its Fourier degree is the largest \(j\) with nonzero coefficient at frequency \(2j\). The minimal-degree necessity applies to arbitrary real, normalized, strictly positive trigonometric-polynomial densities, including nonsymmetric ones. The equality-family formula permits arbitrary rotations; the displayed representative is centered at zero.

## Proof
**Exact kernel inversion.** The geodesic-square kernel on this circle has Fourier series, convergent uniformly,
\[
K(t)=\frac{\pi^2}{12}+\sum_{j\ge1}\frac{(-1)^j}{j^2}\cos(2jt).
\]
For a density \(\psi(t)=\pi^{-1}(1+\sum_{j=1}^d[a_j\cos(2jt)+b_j\sin(2jt)])\), convolution against \(K\) multiplies its \(j\)-th nonconstant harmonic by \((-1)^j/(2j^2)\). The binomial expansion is
\[
(1-\cos\theta)^m=\frac{\binom{2m}{m}}{2^m}+2^{1-m}\sum_{j=1}^m(-1)^j\binom{2m}{m-j}\cos(j\theta).
\]
Thus the *unique* centered density producing \(F(t)-F(0)=\epsilon(1-\cos2t)^m\) has coefficients
\[
a_j=2^{2-m}\epsilon j^2\binom{2m}{m-j},\quad b_j=0\quad(1\le j\le m).
\]
Twice differentiating the binomial trigonometric expansion gives the closed form \(\sum_{j=1}^m(a_j/\epsilon)\cos(2jt)=R_m(\cos2t)\). This also proves normalization because the perturbation has zero angular average. By the convolution identity, the Fréchet loss has the specified exact form, is nonnegative and is zero only at the origin modulo \(\pi\); \(F(0)\) follows by comparing constant Fourier terms.

**Sharp strict positivity.** Differentiate the polynomial:
\[
R_m'(c)=2m(1+c)^{m-2}[m^2c-m^2+3m-1].
\]
Its unique minimum on \([-1,1]\) is at \(c_m^*=1-3/m+1/m^2\), which lies in \((-1,1)\) for every integer \(m\ge2\). Direct substitution yields
\[
R_m(c_m^*)=-2(2m-1)\left(\frac{(2m-1)(m-1)}{m^2}\right)^{m-1}=-\epsilon_m^{-1}.
\]
The endpoint values are \(R_m(-1)=0\), \(R_m(1)>0\). Therefore \(1+\epsilon R_m(c)>0\) for every \(c\in[-1,1]\) exactly when \(0<\epsilon<\epsilon_m\), with nonnegative endpoint density at equality and sign violation beyond it.

**Necessity and uniqueness at minimum bandwidth.** Convolution preserves Fourier degree. Let \(G(t)=F(t)-F(t_0)\) be a nonconstant trigonometric polynomial of degree \(d\) having a zero of order at least \(2m\) at its minimum \(t_0\). With \(z=e^{2it}\), \(z^dG(t)\) is an ordinary polynomial of degree at most \(2d\). Since \(z\) is a local analytic coordinate on the circle, the zero has multiplicity at least \(2m\), forcing \(d\ge m\). If \(d=m\), the polynomial must be a positive real constant times \((z-z_0)^{2m}\) after accounting for the Laurent factor. Reality, nonnegativity and rotation then force \(G(t)=\epsilon(1-\cos(2(t-t_0)))^m\) with \(\epsilon>0\). Since the convolution multipliers \((-1)^j/(2j^2)\) never vanish, the density is uniquely reconstructed, yielding exactly the preceding family and positivity interval. No lower-bandwidth positive density can realize such a degenerate isolated minimum.

**Empirical limit, using existing circular theory.** For independent samples from a displayed density and any measurable intrinsic empirical Fréchet minimizer \(\hat t_N\) expressed near zero, the smooth population derivative has expansion
\[
F'(t)=m2^{m+1}\epsilon\,t^{2m-1}+O(t^{2m+1}).
\]
The centered empirical derivative at zero is \(-2N^{-1}\sum_{i=1}^N T_i\), where \(T_i\in(-\pi/2,\pi/2)\) is the principal signed sample angle. Its limiting square-root-sample-size variance is \(4F(0)\), since the density is symmetric about zero. Standard circular empirical Fréchet process stochastic equicontinuity (Hotz--Huckemann, Theorem 3, after doubling angles) then gives
\[
\sqrt N\,m2^{m+1}\epsilon\,\hat t_N^{2m-1}\ \xrightarrow{d}\ \mathcal N(0,4F(0)).
\]
Thus \(N^{1/(4m-2)}\hat t_N\) has a non-Gaussian signed-odd-root normal limit. This limiting-law mechanism is a known general theorem, not a separately claimed new central limit theorem.

## Verification
The standalone script `verify_harmonic_smeary.py` uses exact symbolic polynomial identities for every degree \(2\le m\le12\), including the Fourier inversion, critical point and sharp-minimum formula. It printed `Verified 121 symbolic identities through degree 12`. The calculation is a diagnostic only: the argument above proves all integer degrees. Run with Python 3 and SymPy using `python verify_harmonic_smeary.py`.

## Relationship to prior work
Banerjee, Banerjee and Das, *A Central Limit Theorem for Intrinsic Fréchet Means on Real Grassmannians* (arXiv:2610.24159v1, publicly submitted 2026-10-16), give an analytic quartically degenerate density on \(\operatorname{Gr}(1,2)\). Their choice corresponds to \(m=2\) and cosine amplitude \(a=4\epsilon\), with a sufficient parameter interval \(a<1/2\). The present sharp positivity threshold extends that particular parameter window to \(a<8/9\). Hotz and Huckemann, *Intrinsic means on the circle: uniqueness, locus and asymptotics* (2015), prove much broader arbitrary-order slow intrinsic-mean asymptotics for smooth circular laws. Accordingly, the new contribution assessed here is not the existence of slow rates or the generic limiting law: it is the minimal Fourier bandwidth, complete equality classification and explicit sharp positivity boundary across all orders.

## Limitations
This classification is for strictly positive real trigonometric-polynomial densities on the one-dimensional real projective circle. It does not claim a spectral minimality result among arbitrary smooth non-polynomial densities or on higher-dimensional Grassmannians. It neither extends nor re-proves the general nonstandard empirical Fréchet central limit theory. Independent scientific validation has not been performed. A hidden equivalent Fourier-bandlimited classification in earlier literature remains a possible originality risk.

## References
Banerjee, Banerjee and Das (2026), *A Central Limit Theorem for Intrinsic Fréchet Means on Real Grassmannians*, arXiv:2610.24159v1, https://arxiv.org/abs/2610.24159 (v1 published 2026-10-16).

Hotz and Huckemann (2015), *Intrinsic means on the circle: uniqueness, locus and asymptotics*, Annals of the Institute of Statistical Mathematics 67:177–193, https://doi.org/10.1007/s10463-013-0444-7 (first published online in 2014).
