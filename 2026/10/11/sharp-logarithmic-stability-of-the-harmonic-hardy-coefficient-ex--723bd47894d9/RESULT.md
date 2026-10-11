# Sharp logarithmic stability of the harmonic Hardy coefficient extremizers

## Finding
Let \(f=h+\overline g\) be a complex-valued bounded harmonic function on the unit disk, normalized by \(\|f\|_\infty\le1\), with \(h(z)=\sum_{j\ge0}a_jz^j\) and \(g(z)=\sum_{j\ge1}b_jz^j\). For each integer \(n\ge1\) set
\[
\Delta_n(f)=\frac4\pi-|a_n|-|b_n|.
\]
Let \(F(e^{it})\) be the almost-everywhere radial boundary trace, and let
\[
\mathcal E_n=\big\{e^{i\phi}\operatorname{sgn}(\cos(nt-\tau)):\phi,\tau\in\mathbb R\big\},
\qquad d_n(F)=\inf_{G\in\mathcal E_n}\int_0^{2\pi}|F(e^{it})-G(t)|\,\frac{dt}{2\pi}.
\]
Then \(0\le\Delta_n(f)\le4/\pi\), with \(d_n(F)=0\) when \(\Delta_n(f)=0\), and universally
\[
\boxed{d_n(F)\le5\sqrt{\Delta_n(f)\log\frac{e}{\Delta_n(f)}}}\qquad(\Delta_n(f)>0).
\]
The square-root logarithmic rate is optimal **for every fixed integer** \(n\ge1\): there are bounded harmonic functions \(f_{n,\eta}\), \(0<\eta\downarrow0\), with \(\|f_{n,\eta}\|_\infty=1\), such that
\[
\Delta_n(f_{n,\eta})=\frac2\pi\eta^2\log\frac1\eta+O(\eta^2),\qquad
 d_n(F_{n,\eta})\asymp\eta\log\frac1\eta.
\]
In particular, no uniform estimate \(d_n(F)=o(\sqrt{\Delta_n\log(e/\Delta_n)})\) as \(\Delta_n\downarrow0\) is valid, even at a fixed coefficient index.

## Assumptions and scope
The norm \(\|f\|_\infty\) is the supremum over the open disk. Every bounded complex harmonic function is the Poisson extension of its unique \(L^\infty\) boundary function \(F\). The normalized circular measure is \(d\sigma(t)=dt/(2\pi)\). Equality functions are regarded as boundary traces, not as two-valued interior harmonic functions. The sign at a cosine zero is irrelevant because those points have zero measure. The modulus \(d_n\) is an \(L^1(d\sigma)\) distance, with the two phases optimized separately. No univalence, quasiregularity, or orientation condition is imposed.

## Proof
**1. Exact coefficient deficit.** Fourier inversion of the Poisson integral gives
\[
a_n=\int F(e^{it})e^{-int}\,d\sigma(t),\qquad
\overline{b_n}=\int F(e^{it})e^{int}\,d\sigma(t).
\]
Choose unit complex numbers \(u,v\) making \(ua_n\) and \(v\overline{b_n}\) nonnegative real. There are phases \(\gamma,\tau\) for which
\[
u e^{-int}+v e^{int}=2e^{-i\gamma}\cos(nt-\tau).
\]
Write \(w(t)=|\cos(nt-\tau)|\), \(G(t)=e^{i\gamma}\operatorname{sgn}(\cos(nt-\tau))\). Then
\[
|a_n|+|b_n|=2\int w\operatorname{Re}(F\overline G)\,d\sigma,\qquad
\Delta_n=2\int w(1-\operatorname{Re}(F\overline G))\,d\sigma.
\]
As \(|F|\le1\) almost everywhere, \(|F-G|^2\le2(1-\operatorname{Re}(F\overline G))\). Thus
\[
\int w|F-G|^2\,d\sigma\le\Delta_n.
\tag{1}
\]
This also proves nonnegativity and the exact equality characterization, since \(w>0\) almost everywhere.

**2. Uniform quantitative estimate.** Under normalized circular measure, the random variable \(w=|\cos(nt-\tau)|\) has density \(2/(\pi\sqrt{1-w^2})\) for \(0<w<1\), independently of \(n\) and \(\tau\). Consequently,
\[
\sigma\{w<s\}=\frac2\pi\arcsin s\le s,\qquad
\int_{\{w\ge s\}}\frac{d\sigma}{w}
=\frac2\pi\log\frac{1+\sqrt{1-s^2}}s\le\frac2\pi\log\frac2s.
\tag{2}
\]
For \(0<\Delta_n\le1/16\), split \(\int|F-G|\) at \(s=\sqrt{\Delta_n}\). The part \(w<s\) is at most \(2s\). Cauchy--Schwarz, (1), and (2) bound the other part by
\[
\sqrt{\Delta_n}\left(\frac2\pi\log\frac2{\sqrt{\Delta_n}}\right)^{1/2}.
\]
Since \(\log(2/\sqrt\Delta)\le\log(e/\Delta)\) for \(0<\Delta\le1\), the sum is smaller than \(5\sqrt{\Delta_n\log(e/\Delta_n)}\). For \(1/16\le\Delta_n\le4/\pi\), use \(d_n\le2\) and the elementary bound \(5\sqrt{\Delta_n\log(e/\Delta_n)}>2\) on that interval. When \(\Delta_n=0\), (1) forces \(F=G\) almost everywhere.

**3. A sharpness family.** For \(0<\eta<1/16\) define
\[
F_{n,\eta}(e^{it})=
\operatorname{sgn}(\cos nt)\exp\left(i\operatorname{sgn}(\sin nt)\rho_\eta(|\cos nt|)\right),
\quad \rho_\eta(w)=\min\{1,\eta/w\}.
\tag{3}
\]
Let \(f_{n,\eta}\) be its Poisson extension. This trace is unimodular almost everywhere, so its harmonic extension has supremum norm one. By the even/odd symmetries under \(t\mapsto-t\) and \(t\mapsto\pi/n-t\), the Fourier coefficients at frequencies \(\pm n\) are both the real number \(\int w\cos\rho_\eta(w)\,d\sigma\), which is positive. Therefore
\[
\Delta_n(f_{n,\eta})=2\int w(1-\cos\rho_\eta(w))\,d\sigma.
\tag{4}
\]
The contribution of \(0<w<\eta\) is \(O(\eta^2)\). On \(w\ge\eta\), Taylor's formula \(1-\cos(\eta/w)=\eta^2/(2w^2)+O(\eta^4/w^4)\) has integrated error \(O(\eta^2)\). Using (2) for the main term yields
\[
\Delta_n(f_{n,\eta})=\frac2\pi\eta^2\log\frac{1+\sqrt{1-\eta^2}}\eta+O(\eta^2)
=\frac2\pi\eta^2\log\frac1\eta+O(\eta^2).
\tag{5}
\]
Also, comparison to the unshifted trace \(G_0(t)=\operatorname{sgn}(\cos nt)\) gives
\[
d_n(F_{n,\eta})\le\int|F_{n,\eta}-G_0|\,d\sigma\le\int\rho_\eta(w)\,d\sigma
=O(\eta\log(1/\eta)).
\tag{6}
\]

For the matching lower bound, by substituting \(x=nt\pmod{2\pi}\) it suffices to treat \(n=1\). Any comparison trace can be written as \(G_{\phi,\tau}(t)=e^{i\phi}\operatorname{sgn}(\cos(t-\tau))\), with \(|\tau|\le\pi/2\) after absorbing a sign into \(\phi\). If \(|\tau|>\sqrt\eta\), the sign-disagreement set between \(G_0\) and the shifted sign function has normalized measure \(|\tau|/\pi\). The elementary inequality \(|1-e^{i\phi}|+|1+e^{i\phi}|\ge2\) implies
\[
\|G_0-G_{\phi,\tau}\|_1\ge2|\tau|/\pi.
\]
The triangle inequality and (6) therefore give a lower bound of order \(\sqrt\eta\), stronger than required for small \(\eta\).

If \(|\tau|\le\sqrt\eta\), then on \(w=|\cos t|>2\sqrt\eta\) the signs of \(\cos(t-\tau)\), \(\cos(-t-\tau)\), and \(\cos t\) agree. At the paired points \(t,-t\), the two values of (3), after dividing by the common sign, are \(e^{i\eta/w}\) and \(e^{-i\eta/w}\), whereas the comparison trace has the same constant phase at both points. Hence the triangle inequality gives
\[
\|F_{1,\eta}-G_{\phi,\tau}\|_1
\ge\int_{\{w>2\sqrt\eta\}}\sin(\eta/w)\,d\sigma
\ge\frac\eta2\int_{\{w>2\sqrt\eta\}}\frac{d\sigma}{w}
\ge c\eta\log(1/\eta)
\]
for an absolute \(c>0\) and all sufficiently small \(\eta\), by (2) and \(\sin x\ge x/2\) for \(0\le x\le1\). This proves the lower estimate uniformly over both free phases. Together with (5)--(6), it proves optimality of the square-root logarithmic modulus.

## Verification
The entire argument uses only Poisson Fourier inversion, Cauchy--Schwarz, the explicit cosine pushforward density, Taylor's formula with an integrable remainder, and a two-point reflection comparison. The standalone `check_stability.py` re-computes representative Fourier coefficients, the exact deficit identity (4), and the claimed upper inequality by numerical midpoint quadrature for three indices and three positive parameters. Run `python3 check_stability.py` in the directory containing this file. The nine finite tests are consistency checks and are not evidence for the all-index, all-function bounds or the asymptotic assertions, which are proved above.

## Relationship to prior work
Chen, Ponnusamy and Wang established the sharp coefficient constant \(4/\pi\) and classified its exact equality functions in 2012. Chen, Huang, Jin and Li (first publicly available September 27, 2026) revisited the harmonic Hardy coefficient problem and determined sharp constants for finite \(p\ge1\), recalling the \(p=\infty\) case. Those results establish exact sharpness, not an \(L^1\) distance-to-extremizers modulus in terms of the coefficient deficit. The present finding concerns the quantitative endpoint stability and determines its optimal logarithmic order. It is not an improvement of the already sharp coefficient constant.

## Limitations
The distance is measured on boundary traces in \(L^1\), not in stronger norms, nor inside the disk. The result makes no claim about geometric subclasses of harmonic maps such as univalent or quasiconformal maps. Optimality concerns the **order** of the modulus; no best numerical leading stability constant is asserted. No assertion of an independent audit or exhaustive global literature coverage is made.

## References
1. S. Chen, S. Ponnusamy and X. Wang, *Integral means and coefficient estimates on planar harmonic mappings*, Annales Academiae Scientiarum Fennicae Mathematica **37** (2012), 69--79, DOI: 10.5186/aasfm.2012.3707. In particular Theorem 3(c) and its proof.
2. S. Chen, M. Huang, L. Jin and Q. Li, *Sharp constant problems for harmonic mappings*, arXiv:2609.33159v1 (first public submission 2026-09-27), Section 1.2 and Theorem 1.3.
