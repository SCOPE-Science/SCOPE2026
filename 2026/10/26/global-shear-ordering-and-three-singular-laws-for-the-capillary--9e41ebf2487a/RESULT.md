# Global shear ordering and three singular laws for the capillary–gravity phase-speed minimizer

## Finding

For every capillarity parameter \(B>0\) and every real signed shear \(\gamma\), define the positive phase speed \(c(x;B,\gamma)\) of linear finite-depth gravity–capillary surface waves by
\[
[x\coth(x)]c^2-\gamma c=1+Bx^2,\qquad x>0,\quad c>0.
\]
Here \(x=kh\), \(B=\sigma/(\rho gh^2)\), \(c\) is divided by \(\sqrt{gh}\), and \(\gamma\) is vorticity divided by \(\sqrt{g/h}\), in the sign convention of the displayed equation (the intrinsic surface velocity is set to zero). Define
\[
c_0(\gamma)=\frac{\gamma+\sqrt{\gamma^2+4}}2,\quad B_c(\gamma)=\frac{c_0(\gamma)^2}{3},\quad
\gamma_c(B)=\frac{3B-1}{\sqrt{3B}}.
\]
The existence threshold \(B<B_c(\gamma)\) of a positive-wavenumber phase-speed minimum is already known from the capillary–gravity shear literature; it is not claimed as a new result. The following joint quantitative classification is the finding.

**Global shear ordering:** When \(\gamma>\gamma_c(B)\), the unique minimizer \(x_*(B,\gamma)>0\) increases *strictly* with \(\gamma\) over the entire interval \((\gamma_c(B),\infty)\). There are no extra stationary points for any real \(\gamma\) and positive \(B\). For \(\gamma\le\gamma_c(B)\), the phase speed increases strictly on \((0,\infty)\) and no positive minimizer exists. Furthermore \(x_*(B,\gamma)\) increases continuously from zero to infinity as \(\gamma\) ranges from \(\gamma_c(B)\) to infinity. A one-dimensional strictly monotone equation below gives this minimizer exactly.

**Universal near-critical onset:** Let \(\eta=1-B/B_c(\gamma)\downarrow0\) with \(\gamma\) fixed. Then
\[
x_*(B,\gamma)=\sqrt{\frac{15}{2}}\,\eta^{1/2}[1+O_\gamma(\eta)],
\qquad c_{\min}=c_0-\frac{5c_0^2}{4\sqrt{\gamma^2+4}}\eta^2+O_\gamma(\eta^3).
\]
The dimensionless onset coefficient \(\sqrt{15/2}\) is independent of shear. At fixed \(B>0\), the equivalent shear-induced onset is
\[
x_*(B,\gamma)\sim \sqrt{\frac{15\sqrt{3B}}{1+3B}}\,\sqrt{\gamma-\gamma_c(B)}\qquad(\gamma\downarrow\gamma_c(B)).
\]

**Weak-capillarity and strong-shear laws:** For fixed \(\gamma\in\mathbb R\) as \(B\downarrow0\),
\[
x_*(B,\gamma)=B^{-1/2}+\frac{\gamma}{\sqrt2}B^{-1/4}
-\frac{\gamma^3}{16\sqrt2}B^{1/4}+O_\gamma(B^{1/2}).
\]
In particular, the constant-order term vanishes identically for every fixed shear. For fixed \(B>0\) as \(\gamma\to+\infty\),
\[
x_*(B,\gamma)\sim(2/B)^{1/3}\gamma^{2/3}.
\]
These formulas describe *linear dispersion only*; they do not assert existence or stability of nonlinear solitary waves.

## Assumptions and scope

Fix \(h,g,\rho,\sigma>0\) and a uniform real vorticity \(\Omega\) for a two-dimensional incompressible, inviscid fluid above a flat impermeable bed and below a free surface. Linearize about a uniform-vorticity current, measure phase speed relative to its surface speed, select the positive-propagating branch, and use \(x=kh>0\), \(B=\sigma/(\rho gh^2)>0\), \(\gamma=\Omega\sqrt{h/g}\). The convention is \(c\) solving \(A(x)c^2-\gamma c=1+Bx^2\), with \(A(x)=x\coth x\); reversing the physical vorticity sign merely reverses \(\gamma\). Quantifiers in the global theorem cover all \(B>0\), \(\gamma\in\mathbb R\), and \(x>0\). Singular expansions are for the indicated fixed parameter and their remainders need not be uniform as other parameters diverge.

## Proof

**1. Exact stationary selector.** Put
\[
A(x)=x\coth x,\quad R(x)=\frac{A'(x)}{2x},\quad P(x)=A(x)-x^2R(x).
\]
For each \(p>0\), \(\gamma\in\mathbb R\), let \(d(p,\gamma)>0\) denote the unique positive root of \(p d^2-\gamma d=1\):
\[
d(p,\gamma)=\frac{\gamma+\sqrt{\gamma^2+4p}}{2p}.
\]
Define the stationary selector \(F(x,\gamma)=R(x)d(P(x),\gamma)^2\). Differentiating the dispersion equation gives
\[
[2Ac-\gamma]c'=2x[B-Rc^2].
\]
At a stationary point \(B=Rc^2\) and \(P c^2-\gamma c=1\), hence \(c=d(P,\gamma)\) and \(B=F(x,\gamma)\). Conversely the latter equation supplies a genuine stationary point by substitution. Thus all stationary points are exactly the roots of \(B=F(x,\gamma)\).

**2. Strict monotonicity.** The classical product \(\sinh x/x=\prod_{n\ge1}(1+x^2/(\pi^2n^2))\) yields, by locally uniform logarithmic differentiation,
\[
R(x)=2\sum_{n=1}^{\infty}\frac{\pi^2n^2}{(x^2+\pi^2n^2)^2},\quad
R'(x)=-8x\sum_{n=1}^{\infty}\frac{\pi^2n^2}{(x^2+\pi^2n^2)^3}<0.
\]
Hence \(R(x)>0\), \(P'(x)=-x^2R'(x)>0\), \(P(0+)=1\), \(R(0+)=1/3\). Also \(P(x)\sim x/2\), \(R(x)\sim1/(2x)\) as \(x\to\infty\). From \(p d^2-\gamma d=1\), implicit differentiation gives \(d_p=-d^2/(2pd-\gamma)<0\) and \(d_\gamma=d/(2pd-\gamma)>0\) (the common denominator is \(\sqrt{\gamma^2+4p}>0\)). Consequently \(F\) is strictly decreasing in \(x\) and strictly increasing in \(\gamma\). Its range in \(x\) is precisely \((0,B_c(\gamma))\). For fixed \(x\), monotonicity of the positive dispersion root with respect to \(B\) and the identity \(x^2[B-Rc^2]=Pc^2-\gamma c-1\) show that \(\operatorname{sign}(c')=\operatorname{sign}(B-F(x,\gamma))\): at small \(x\) this is negative when \(B<B_c\), then positive after the unique crossing. Since \(c(x)\to\infty\) as \(x\to\infty\), the stationary point is a strict global minimum. If \(B\ge B_c\), \(c'>0\) for all \(x>0\). The identity \(B=B_c(\gamma_c)\) gives \(\gamma_c(B)=(3B-1)/\sqrt{3B}\). As \(\gamma\) increases above \(\gamma_c\), the strict increase of \(F\) in \(\gamma\) and strict decrease in \(x\) force \(x_*\) to increase strictly; continuity and the endpoint limits follow from the same root equation. No assertion about shear monotonicity is inferred merely from plots.

**3. Near-critical expansion.** Taylor expansion gives
\[
R(x)=\frac13-\frac{2x^2}{45}+O(x^4),\quad P(x)=1+\frac{x^4}{45}+O(x^6),
\]
so \(F(x,\gamma)=B_c-2c_0^2x^2/45+O_\gamma(x^4)\). Inverting the unique root as \(B\uparrow B_c\) proves \(x_*^2=45(B_c-B)/(2c_0^2)+O_\gamma((B_c-B)^2)\), equivalent to the displayed universal coefficient. Expand the dispersion equation at small \(x\) to order \(x^4\): at \(B=B_c-\delta\), the quadratic phase-speed coefficient is \(-\delta/\sqrt{\gamma^2+4}\) and the limiting quartic coefficient is \(c_0^2/[45\sqrt{\gamma^2+4}]\). Evaluating at the minimizing \(x_*\) gives the stated \(c_{\min}\) expansion. Differentiating \(B_c\) at \(\gamma_c\) yields \(B_c'(\gamma_c)/B_c(\gamma_c)=2/\sqrt{\gamma_c^2+4}\), proving the fixed-\(B\) shear onset.

**4. Weak capillarity.** As \(x\to\infty\),
\[
P(x)=x/2+O(x^2e^{-2x}),\quad R(x)=1/(2x)+O(e^{-2x}),
\]
so for fixed \(\gamma\),
\[
F(x,\gamma)=x^{-2}+\sqrt2\gamma x^{-5/2}
+\gamma^2x^{-3}+\frac{\gamma^3}{2\sqrt2}x^{-7/2}+O_\gamma(x^{-4}).
\]
Set \(\varepsilon=B^{1/4}\), \(x=\varepsilon^{-2}(1+a\varepsilon+b\varepsilon^2+d\varepsilon^3+O(\varepsilon^4))\). Expanding \(B=F(x,\gamma)\) sequentially gives \(a=\gamma/\sqrt2\), \(b=0\), \(d=-\gamma^3/(16\sqrt2)\). This is the claimed three-term expansion; the exponentially small finite-depth correction cannot alter an algebraic coefficient.

**5. Strong positive shear.** At fixed \(B\), monotonicity forces \(x_*\to\infty\) as \(\gamma\to\infty\), since \(F(x,\gamma)\to\infty\) for every fixed \(x>0\). At any test point \(x=t(2/B)^{1/3}\gamma^{2/3}\), \(t>0\) fixed, \(P\sim x/2\), \(R\sim1/(2x)\), \(d(P,\gamma)\sim2\gamma/x\), so \(F(x,\gamma)/B\to t^{-3}\). Bracketing the unique root between the choices \(t=1\pm\epsilon\) proves the \(2/3\) law.

## Verification

The bundled standalone Python program `verify.py` independently evaluates the positive dispersion root and the monotone selector. It checks exact stationary equations, uniqueness against nearby comparison points, shear ordering, both near-critical scaling laws, weak-capillarity asymptotics, and strong-shear convergence at parameter grids. It also checks analytic coefficient identities from the displayed expansions. Run `python3 verify.py` in an environment with Python 3; the program uses only the standard library. Numerical sampling corroborates but does not replace the preceding infinite-domain proof. No result about nonlinear wave existence, modulation, or finite-amplitude stability is proved.

## Relationship to prior work

Ellingsen and Brevik (initial arXiv release 2013-11-05, equations (33)–(35), section 5.1) derived the underlying dispersion and already described a qualitative shear-induced movement of the minimum wavenumber in their deep-water plot. This work does **not** claim that qualitative observation as novel. Guo, Tao and Zeng (2014) reported numerically monotone solitary-wave bifurcation behavior with shear, which is different from the full exact minimizing-wavenumber law here. Hur and Johnson (2015) studied capillarity-only and vorticity-only dispersive mechanisms in their Whitham stability analysis. Gao, Milewski and Wang (2021, equations (10)–(13) and figures 5–6) explicitly derived the finite-depth shear-dependent Bond threshold and marked the minimum-wavenumber curves; the threshold and the mere existence of a minimum are therefore **established prior results**, not the contribution. The contribution is the strict global all-shear ordering of its location at fixed independent \(B\), a shear-independent normalized onset coefficient, the cancellation and next nonzero weak-capillarity correction, and the strong-shear \(2/3\)-power asymptotic. The inspected primary text and accessible comparison records did not explicitly supply this combined quantitative theorem or stronger implication; that is a limited literature comparison, not a proof of historical priority.

## Limitations

The parameter \(\gamma\) is signed, so increasing it means increasing vorticity *in the sign convention of the displayed dispersion equation*, not necessarily increasing upstream current speed in an arbitrary frame. The positive-frequency branch is used, and the opposite-propagating branch follows only after reversing the sign. The theory assumes ideal two-dimensional linear inviscid flow, constant vorticity, finite positive depth, positive gravity and capillarity, and an undisturbed flat interface. The results do not infer experimental observability, nonlinear solitary-wave existence, or modulation stability. Asymptotic remainders are parameterwise rather than uniform across simultaneous extreme limits. Historical equivalence in less accessible primary works remains an originality risk; the exact forward dispersion, shear effect and threshold predate this result.

## References

1. S. Å. Ellingsen and I. Brevik, *How linear surface waves are affected by a current with constant vorticity*, arXiv:1311.1073 (first version 2013-11-05); European Journal of Physics 35, 025005 (2014), doi:10.1088/0143-0807/35/2/025005. See equations (33)–(35), section 5 and figure 4.
2. D. Guo, B. Tao and X. Zeng, *On the Dynamics of Two-Dimensional Capillary-Gravity Solitary Waves with a Linear Shear Current*, Advances in Mathematical Physics (first published 2014-04-14), doi:10.1155/2014/480670.
3. V. Hur and M. A. Johnson, *Modulational instability in the Whitham equation with surface tension and vorticity*, arXiv:1506.07560 (2015).
4. T. Gao, P. A. Milewski and Z. Wang, *Capillary-gravity solitary waves on water of finite depth interacting with a linear shear current*, Studies in Applied Mathematics 147 (2021), 1036–1057, doi:10.1111/sapm.12422; author manuscript: https://gala.gre.ac.uk/id/eprint/32313/ .
