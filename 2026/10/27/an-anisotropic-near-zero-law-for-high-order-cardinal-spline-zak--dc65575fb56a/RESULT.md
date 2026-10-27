# An anisotropic near-zero law for high-order cardinal-spline Zak transforms

## Finding
Let \(b=\mathbf 1_{[-1/2,1/2]}\), let \(g_m=b^{*m}\) for integers \(m\geq3\), and use the Zak convention
\[
Z_m(x,\omega)=\sum_{k\in\mathbb Z}g_m(x-k)e^{2\pi i k\omega},\qquad (x,\omega)\in\mathbb R^2.
\]
Put \(h_m=(2/\pi)^m\). For every compact \(S\subset\mathbb R\), uniformly in \((x,s)\in[0,1]\times S\),
\[
 h_m^{-1}Z_m\left(x,\tfrac12+\tfrac{s}{m}\right)
 \longrightarrow F(x,s):=e^{-2s+i\pi x}+e^{2s-i\pi x}.
\]
The convergence also holds for first derivatives in \(x,s\). In particular,
\[
 |F(x,s)|^2=4\left(\cos^2(\pi x)+\sinh^2(2s)\right).
\]
For every fixed \(\tau>0\), the **entire** Zak fundamental square has the exact small-modulus area law
\[
\boxed{\lim_{m\to\infty}m\,\operatorname{Leb}\{(x,\omega)\in[0,1)^2:|Z_m(x,\omega)|\leq\tau h_m\}=A(\tau),}
\]
where the explicit, positive and finite limit is
\[
 A(\tau)=\int_0^1\operatorname{arsinh}\!\left(\sqrt{\bigl(\tau^2/4-\cos^2(\pi x)\bigr)_+}\right)\,dx,
 \qquad A(\tau)=\tau^2/8+O(\tau^4)\quad(\tau\downarrow0).
\]
The unique Zak zero at \((1/2,1/2)\), whose uniqueness is known from the earlier spline-Zak literature, is nondegenerate for every \(m\ge3\). Its real two-dimensional Jacobian has the sharp law
\[
\boxed{\det D(\Re Z_m,\Im Z_m)(1/2,1/2)
 =8\pi m(2/\pi)^{2m}\bigl(1+O(3^{1-m})\bigr)>0.}
\]
Thus near-critical small-modulus values occupy a frequency layer of width \(1/m\), while the transverse determinant is exponentially small in spline order.

## Assumptions and scope
Here \(b\) has unit mass and support \([-1/2,1/2]\); convolution is on \(\mathbb R\). The order \(m\) varies through integers at least three. Fourier transforms use \(\widehat f(\xi)=\int_\mathbb R f(t)e^{-2\pi i t\xi}\,dt\), while the Zak exponent has the positive sign shown above. Lebesgue area is the ordinary planar measure on the fundamental square; the boundary has measure zero. All limits hold at fixed \(\tau>0\). This is a large-order law, **not** a claim about changing the critical Gabor lattice density. In the profile, \(s=m(\omega-1/2)\) is a rescaled frequency coordinate, not an additional Fourier variable.

## Proof
**1. Exact Poisson representation.** The Fourier transform of the centered box is the sinc function. Hence
\[
\widehat g_m(\xi)=\left(\frac{\sin\pi\xi}{\pi\xi}\right)^m,
\quad
Z_m(x,\omega)=\sum_{n\in\mathbb Z}
\widehat g_m(n+\omega)e^{2\pi i(n+\omega)x}.
\]
For \(m\ge3\) the series and its first \(x\)- and \(\omega\)-derivatives converge absolutely locally (in fact uniformly for the displayed real variables). The second equality follows by periodizing the Fourier inversion formula; it is also immediate from Poisson summation applied to the compactly supported spline.

**2. Two-alias boundary layer.** For \(\omega=1/2+s/m\), the terms \(n=0,-1\) are the only terms whose absolute Fourier frequencies approach \(1/2\). For \(s\) in any fixed bounded interval, their normalized coefficients satisfy
\[
 h_m^{-1}\widehat g_m(\tfrac12+\tfrac{s}{m})=e^{-2s}\bigl(1+O_S(m^{-1})\bigr),\qquad
 h_m^{-1}\widehat g_m(-\tfrac12+\tfrac{s}{m})=e^{2s}\bigl(1+O_S(m^{-1})\bigr).
\]
Indeed, their common sine numerator is \(\cos(\pi s/m)\), while their denominators are respectively \(1\pm2s/m\) times \(\pi/2\). The combined remainder of the remaining Fourier aliases is \(O_S(3^{-m})\) after division by \(h_m\). Differentiating the same expressions in \(x,s\), with \(\partial_s=m^{-1}\partial_\omega\), preserves these bounds (with harmless order-polynomial factors absorbed in the exponentially small remainder). Thus the complex profile and its first derivatives converge uniformly on compact strips.

**3. No missing low-modulus mass outside the layer.** By periodicity and conjugate reflection it suffices to take \(0\le\omega\le1/2\). Write \(r=\omega\), \(u=m(1/2-r)\ge0\), and let
\[
 a=\left(\frac{\sin\pi r}{\pi r}\right)^m,\qquad
 d=\left(\frac{\sin\pi r}{\pi(1-r)}\right)^m.
\]
The first two Fourier aliases have moduli \(a,d\). The combined modulus of all other aliases is at most
\[
 a\,2\sum_{j\ge1}(2j+1)^{-m}\le5a\,3^{-m}.
\]
The ratio \(d/a=(r/(1-r))^m\) is at most \(e^{-4u}\). Also, \(a/h_m\ge e^{cu}\) for some absolute \(c>0\): this follows from the positivity, on \([0,1/2)\), of \(\log(\sin\pi r/(2r))\), whose ratio to \(1/2-r\) has a positive infimum and extends continuously at the endpoints. Therefore
\[
 \frac{|Z_m(x,r)|}{h_m}\ge e^{cu}\bigl(1-e^{-4u}-5\cdot3^{-m}\bigr).
\]
For every fixed \(\tau>0\), this exceeds \(\tau\) whenever \(u\ge S_\tau\) and \(m\) is sufficiently large, for some finite \(S_\tau\). By symmetry the entire sublevel set is therefore confined to \(|\omega-1/2|\le S_\tau/m\).

**4. Exact area law.** Substitute \(s=m(\omega-1/2)\), giving a Jacobian factor \(m^{-1}\). The compact-strip uniform convergence from step 2 and the confinement from step 3 permit dominated convergence of sublevel indicators. Every level set \(\{|F|=\tau\}\), \(\tau>0\), has planar measure zero, as follows directly from the displayed sum of a squared cosine and squared hyperbolic sine. For each \(x\), the allowable \(s\)-interval has length
\[
\operatorname{arsinh}\left(\sqrt{(\tau^2/4-\cos^2\pi x)_+}\right).
\]
Integration in \(x\) proves the formula for \(A(\tau)\). Taylor expansion around \((x,s)=(1/2,0)\) gives
\[
|F(x,s)|^2=4\pi^2(x-1/2)^2+16s^2+O((x-1/2)^4+s^4),
\]
so the corresponding ellipse has area \(\tau^2/8\) and the stated next-order bound follows.

**5. Nondegenerate zero and its exact Jacobian.** Symmetry makes \(Z_m(1/2,1/2)=0\), \(\partial_xZ_m\) real and \(\partial_\omega Z_m\) purely imaginary there. Pairing the positive and negative half-integer Fourier aliases gives the absolutely convergent identities
\[
\begin{aligned}
\partial_x Z_m(1/2,1/2)&=-2\pi h_m\sum_{j=0}^{\infty}\frac{(-1)^{j(m+1)}}{(2j+1)^{m-1}},\\
\partial_\omega Z_m(1/2,1/2)&=-4im h_m\sum_{j=0}^{\infty}\frac{(-1)^{j(m+1)}}{(2j+1)^{m+1}}.
\end{aligned}
\]
Both real sums are strictly positive: they have only positive terms for odd \(m\), and are positive alternating series with decreasing terms for even \(m\). Their respective values are \(1+O(3^{1-m})\) and \(1+O(3^{-m-1})\). The determinant is the product of the real \(x\)-derivative and the imaginary \(\omega\)-derivative, giving the announced positive sharp asymptotic. This nondegeneracy is proved here without relying on the earlier uniqueness theorem.

## Verification
The self-contained `CHECKER.py` computes the Zak transform independently from the exact truncated-power cardinal-spline identity and from its Fourier alias series. It checks eighteen cross-representation values, four time-domain finite-difference derivative comparisons, the two-alias profile for orders 60, 120 and 240, positivity and asymptotics of the derivative sums, and the scaled sublevel area at threshold one for orders 40, 80 and 160. `CHECKER_OUTPUT.txt` records the actual output. The finite checks validate normalization and numerics, while steps 1–5 prove the universal statements. The area quadrature is diagnostic, not an interval-arithmetic certificate.

## Relationship to prior work
Kloos and Stöckler (first arXiv version, 2013) proved the one-zero property for Zak transforms of exponential B-splines and related it to Gabor frame construction. Kloos (2014) extended unique-zero results to further totally positive functions. The location and uniqueness of the cardinal-spline zero are consequently **not claimed as new**. The present assertion is instead the sharp joint large-order and near-Nyquist frequency asymptotic, its *global* small-modulus-area distribution, and the exact transverse Jacobian asymptotic. Janssen (2003) studies few-zero Zak transforms and critical-density frame construction for other windows. Earlier Schoenberg-type Euler-spline work remains a priority risk, especially Jetter, Riemenschneider and Sivakumar (1991), for which full-text inspection was not possible. The stated theorem does not follow from uniqueness alone; the global area law requires a uniform two-alias limit and an exclusion of distant sublevel components.

## Limitations
There is no assertion of optimal Gabor frame bounds at noncritical densities, no claim of uniqueness beyond the already known theorem, and no extension to nonuniform knot spacing, shifted nonsymmetric windows or noninteger order. The small-modulus law is at fixed \(\tau\), not uniformly over thresholds that depend on \(m\). Exact prior-publication priority has not been independently certified; the 1991 Euler-spline article was only accessible by its abstract, and its potential relevance is retained as a residual risk.

## References
- T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (28 November 2013), https://arxiv.org/abs/1311.7359.
- T. Kloos, *Zeros of the Zak transform of totally positive functions*, arXiv:1411.1539v1 (6 November 2014), https://arxiv.org/abs/1411.1539.
- A. J. E. M. Janssen, *On Generating Tight Gabor Frames at Critical Density*, J. Fourier Anal. Appl. **9** (2003), 175–214, https://doi.org/10.1007/s00041-003-0011-3.
- K. Jetter, S. D. Riemenschneider and N. Sivakumar, *Schoenberg's exponential Euler spline curves*, Proc. R. Soc. Edinburgh Sect. A **118** (1991), 21–33, https://doi.org/10.1017/S0308210500028869 (abstract inspected; full text unavailable).
