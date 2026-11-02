# A double radial shell and a Dawson boundary layer in three-dimensional Boltzmann breathers

## Finding

Consider the exact, centered, nonrotating, three-dimensional Boltzmann breather in an isotropic harmonic trap, with strictly positive periodic spatial Gaussian variance. If the position of a particle is sampled at a uniformly random physical time in one full breather period, then its **radial** distribution is a phase mixture of Maxwell laws. Although each instantaneous radial law has one mode and the full spatial phase-mixed density decreases strictly away from the origin, the phase-mixed radial law has **at least two separated local maxima** for every sufficiently large breather amplitude. The inner shell is governed by a universal Dawson-function boundary layer.

More precisely, let \(q\in[0,1)\) be the relative variance oscillation amplitude and choose length units in which the Cartesian variance at phase \(\theta\) is \(1+q\cos\theta\). Let \(R_q\) denote the radius of a phase-mixed position and \(p_q\) its probability density. Then
\[
p_q(r)=\sqrt{\frac2\pi}\,\frac{r^2}{2\pi}\int_0^{2\pi}\frac{\exp[-r^2/(2(1+q\cos\theta))]}{(1+q\cos\theta)^{3/2}}\,d\theta,\qquad r>0.
\]
For \(q=0\), its unique mode is \(r=\sqrt2\). Write \(\varepsilon=1-q\). As \(\varepsilon\downarrow0\), uniformly with two derivatives for \(y\) on each compact subset of \((0,\infty)\),
\[
p_{1-\varepsilon}(\sqrt\varepsilon\,y)\longrightarrow \frac{2}{\pi^{3/2}}\,F(y),\quad
F(y)=\sqrt2\,y\operatorname{Dawson}(y/\sqrt2)
=y^2\int_0^1e^{-y^2(1-u^2)/2}\,du.
\]
The function \(F\) has exactly one positive maximizer \(y_*\), characterized by
\[
y_*>1,\quad F(y_*)=\frac{y_*^2}{y_*^2-1},\qquad
 y_*=2.1241137947344\ldots,\quad F(y_*)=1.2847494396568\ldots.
\]
For all sufficiently small \(\varepsilon>0\), one radial mode satisfies
\[
\frac{r_{\mathrm{inner}}(1-\varepsilon)}{\sqrt\varepsilon}\longrightarrow y_*,\qquad
p_{1-\varepsilon}(r_{\mathrm{inner}}(1-\varepsilon))\longrightarrow\frac2{\pi^{3/2}}F(y_*),
\]
and a distinct radial local maximum lies in a **fixed compact subinterval of \((0,\infty)\)**. In particular, the two radial shells are separated in scale. This is an existence claim for *at least two* local maxima, not a complete count of modes or a determination of a critical amplitude.

The fixed-radius limit of the density also has the exact special-function form
\[
p_q(r)\longrightarrow p_1(r)=\frac{r^2}{4\pi^{3/2}}e^{-z}[K_0(z)+K_1(z)],\qquad z=r^2/8,\quad r>0,
\]
with \(p_1(0+)=2/\pi^{3/2}\). Here \(K_\nu\) denotes the modified Bessel function of the second kind and \(\operatorname{Dawson}(z)=e^{-z^2}\int_0^z e^{t^2}\,dt\).

## Assumptions and scope

The mathematical statement concerns the exactly Gaussian breather solution of the low-density Boltzmann equation, not finite-density corrections, damping, or a finite collection of interacting hard spheres. In the source notation, \(\beta(t)=\beta_s+\Delta_\beta\cos(2\omega t-\varphi)\), \(a=4\omega^2(\beta_s^2-\Delta_\beta^2)>0\), and the normalized instantaneous spatial density is \(n_B(\mathbf x,t)/N=[a/(4\pi\beta(t))]^{3/2}\exp[-a|\mathbf x|^2/(4\beta(t))]\). Thus a Cartesian spatial coordinate has variance \(2\beta(t)/a\). Set \(L=\sqrt{2\beta_s/a}\), \(q=\Delta_\beta/\beta_s\), and sample a particle's \(\mathbf x/L\) at independent uniformly random physical phase \(\theta=2\omega t-\varphi\). Its conditional distribution is \(N_3(0,(1+q\cos\theta)I_3)\). The measured \(R_q\) is the *dimensionless distance*, not a coordinate projection or a position-space density. The parameter restriction \(q<1\) ensures strictly positive variance in every phase. The singular endpoint \(q=1\) is used only as a density limit; it need not be a physically admissible finite-size breather.

## Proof

**1. Phase-mixture identity.** A centered isotropic three-dimensional Gaussian of coordinate variance \(v>0\) has radius density \(\sqrt{2/\pi}\,r^2v^{-3/2}\exp(-r^2/(2v))\). Averaging over the uniform phase proves the displayed identity for \(p_q\), including normalization by Tonelli's theorem. At \(q=0\), differentiation gives the unique positive critical point \(r=\sqrt2\), a strict global maximum.

**2. Fixed positive radii and the Bessel formula.** At any fixed \(r>0\), dominated convergence in phase gives the limiting density with variance \(1+\cos\theta\). Using the arcsine phase law and setting \(u=\cot(\theta/2)\), the integral becomes
\[
p_1(r)=\frac{r^2}{\pi^{3/2}}\int_0^\infty\sqrt{1+u^2}\,\exp[-r^2(1+u^2)/4]\,du.
\]
The substitution \(u=\sinh t\), followed by \(\cosh^2 t=(1+\cosh2t)/2\), gives the quoted expression through the standard integral representation of \(K_0\) and \(K_1\). Standard small-argument expansions give, with \(z=r^2/8\),
\[
\frac{p_1(r)}{2/\pi^{3/2}}=z e^{-z}(K_0(z)+K_1(z))
=1+z[-\log(z/2)-\gamma-1]+O(z^2|\log z|),
\]
where \(\gamma\) is Euler's constant. Consequently \(p_1(r)>p_1(0+)\) for all sufficiently small positive \(r\), whereas \(p_1(r)\to0\) as \(r\to\infty\). Choose fixed \(0<a<b<c\) with \(p_1(b)>\max(p_1(a),p_1(c))\). Convergence at these three fixed radii implies that, for all sufficiently large \(q<1\), \(p_q\) achieves a local maximum in the interior \((a,c)\). This maximum remains uniformly separated from the origin. No numerical inequality is used in this existence argument.

**3. Inner boundary layer.** By symmetry, replace the phase integral with an integral over \(\phi\in[0,\pi]\) of variance \(v=1-q\cos\phi\). Put \(q=1-\varepsilon\), \(r=\sqrt\varepsilon\,y\), and scale \(\phi=\sqrt{2\varepsilon/q}\,s\) near \(\phi=0\). Since \(v/\varepsilon\to1+s^2\), dominated convergence after separating the small-angle region from its complement gives
\[
\lim_{\varepsilon\downarrow0}p_{1-\varepsilon}(\sqrt\varepsilon\,y)
=\frac2{\pi^{3/2}}y^2\int_0^\infty\frac{\exp[-y^2/(2(1+s^2))]}{(1+s^2)^{3/2}}\,ds.
\]
For rigorous domination, use \(1-\cos\phi\asymp\phi^2\) on \([0,\pi]\), obtaining an integrable multiple of \((1+s^2)^{-3/2}\) in the rescaled domain. On each compact positive \(y\)-interval the first two \(y\)-derivatives of the integrand have additional bounded polynomial factors in \((1+s^2)^{-1}\), so the convergence is locally \(C^2\). With \(u=s/\sqrt{1+s^2}\), the integral becomes \(\int_0^1e^{-y^2(1-u^2)/2}\,du\), which equals the stated Dawson expression.

**4. Unique, nondegenerate inner maximum.** Dawson's differential identity gives
\[
F'(y)=y+(y^{-1}-y)F(y).
\]
It follows that \(F'(y)>0\) on \((0,1]\). For \(y>1\), \(F'\) has the opposite sign to \(F(y)-H(y)\), where \(H(y)=y^2/(y^2-1)\). Near \(y=1+\), \(F-H<0\). From the large-argument expansion of Dawson's integral,
\[
F(y)=1+y^{-2}+3y^{-4}+O(y^{-6}),\qquad H(y)=1+y^{-2}+y^{-4}+O(y^{-6}),
\]
so \(F-H>0\) eventually. At every zero of \(F-H\), the differential identity implies \((F-H)'=-H'=2y/(y^2-1)^2>0\). Hence there is precisely one zero \(y_*>1\), and \(F\) strictly increases before and strictly decreases after it. At that zero, \(F''(y_*)=-2/(y_*^2-1)<0\). Local \(C^2\) convergence and the sign change of the derivative give an inner local maximum with \(r_{\rm inner}/\sqrt\varepsilon\to y_*\) and the specified limiting height.

**5. Two distinct modes and spatial-versus-radial distinction.** The inner maximum tends to zero, whereas the other maximum belongs to the fixed interval \((a,c)\) with \(a>0\); they are distinct for all sufficiently small \(\varepsilon\). Finally, the three-dimensional *volume density* at radius \(r\) is \(g_q(r)=\mathbb E[(2\pi V)^{-3/2}e^{-r^2/(2V)}]\), with \(V=1+q\cos\Theta\). For every fixed \(q<1\), differentiation under the integral gives \(g_q'(r)=-r\mathbb E[V^{-1}(2\pi V)^{-3/2}e^{-r^2/(2V)}]<0\) for \(r>0\). The two maxima arise from the radial Jacobian \(4\pi r^2\), not from multiple maxima of \(g_q\).

## Verification

The accompanying `verify.py` computes the radial phase integral by adaptive quadrature, evaluates the Bessel fixed-radius limit and Dawson inner-scale profile independently, locates the defining positive root, and checks representative high-amplitude inner and outer peaks. Run `python verify.py` with Python 3, NumPy and SciPy installed. Its successful numerical output is **supporting diagnostics only**; the infinite-parameter and asymptotic statements follow from the analytic proof above. In a representative check with \(q=0.9999\), the computed maxima lie near \(r=0.021248535\) and \(r=0.883317123\). The inner scaled location approaches \(y_*=2.1241137947344\ldots\).

## Relationship to prior work

Maynar, García de Soria, Guéry-Odelin, and Trizac derive the exact periodic Gaussian breather and instantaneous spatial density, including the physical amplitude \(q\). Their instantaneous radial diagnostic in numerical simulations concerns \(d=2\) at selected phases, not the uniformly phase-averaged \(d=3\) radial density or the Dawson boundary-layer/multimodal result proved here. García de Soria and collaborators' earlier hydrodynamic analysis likewise gives an instantaneous Gaussian profile and breather damping but no phase-mixed radial-shell classification. The Maxwell distribution, Gaussian scale-mixture representation, Bessel integral, and Dawson integral are standard ingredients, not claimed as new. The claim is specifically their strong-breathing three-dimensional radial-shell consequence and sharp inner scaling.

## Limitations

This theorem proves *at least* two local radial maxima for all sufficiently near-unit amplitudes; it does not prove the exact number of modes at every amplitude or any critical amplitude. It addresses the exact low-density breather and uniform physical-phase averaging only. It does not extend its conclusions to finite-density damping, anisotropy, noisy phase sampling, finite-duration measurements, or arbitrary Gaussian variance mixtures. It does not imply multiple local maxima of the full spatial density. The proof does not provide a universal explicit numerical threshold on \(q\). Its originality is a best-knowledge literature comparison, not an exhaustive priority certification; independent scientific review has not been performed.

## References

1. P. Maynar, M. I. García de Soria, D. Guéry-Odelin, E. Trizac, *Fate of Boltzmann's breathers: kinetic theory perspective*, arXiv:2409.07831v1 (first public 2024-09-12), https://arxiv.org/html/2409.07831v1 ; especially equations (29)--(35) and instantaneous radial diagnostics in Section III.2.
2. M. I. García de Soria, P. Maynar, D. Guéry-Odelin, E. Trizac, *Fate of Boltzmann's breathers: Stokes hypothesis and anomalous thermalization*, arXiv:2312.09726 (first public 2023-12-15), https://arxiv.org/abs/2312.09726 ; especially the time-dependent Gaussian density, equation (9), and damping analysis.
3. NIST Digital Library of Mathematical Functions, standard modified Bessel function integral representations and asymptotics, https://dlmf.nist.gov/10 and Dawson integral, https://dlmf.nist.gov/7 ; classical special-function identities used in the proof.
