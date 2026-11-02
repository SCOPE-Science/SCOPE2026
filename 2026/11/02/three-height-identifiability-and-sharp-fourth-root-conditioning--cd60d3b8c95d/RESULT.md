# Three-height identifiability and sharp fourth-root conditioning of a ground-reflected Gaussian plume

## Finding
For a perfectly reflecting-ground Gaussian vertical plume at one fixed horizontal station, three distinct nonnegative receptor heights determine the unknown positive amplitude, unknown positive vertical spread, and unknown nonnegative effective release height **globally and uniquely**, using exact positive concentration data. Every pair of receptor heights leaves a one-parameter family of physically admissible alternatives. A second divided difference of logarithmic concentrations supplies an exact compatibility test and a monotone one-dimensional reconstruction. When the release height tends to zero, that invariant vanishes to **fourth order** in the release height, and the inverse map is sharply fourth-root conditioned: no local Hölder exponent greater than \(1/4\) can uniformly recover source height from three log readings when amplitude and spread are also unknown.

Specifically, fix arbitrary \(0\le z_0<z_1<z_2\) and model
\[
 C(z)=A\left[e^{-(z-H)^2/(2\sigma^2)}+e^{-(z+H)^2/(2\sigma^2)}\right],\qquad A,\sigma>0,\quad H\ge0.
\]
Set \(u_i=z_i^2\), \(y_i=\log C(z_i)\), and define
\[
 \Delta=\frac1{u_2-u_0}\left(\frac{y_2-y_1}{u_2-u_1}-\frac{y_1-y_0}{u_1-u_0}\right),\qquad
 F(t)=\bigl[\log\cosh(t\sqrt u)\bigr]_{u_0,u_1,u_2}.
\]
(The bracket denotes the same ordinary second divided difference.) Then \(F(0)=0\), \(F\) is strictly decreasing for \(t>0\), and \(F(t)\to-\infty\) as \(t\to\infty\). Exact positive data are representable by a physical triple **if and only if** \(\Delta\le0\) and the uniquely defined \(t\ge0\) with \(F(t)=\Delta\) produces a positive \(s\) in the inversion in the next section.

## Assumptions and scope
The three sensors lie on the same vertical above one fixed positive-downwind and fixed crosswind coordinate. The horizontal geometry, mean wind, and the horizontal Gaussian factor are fixed; their combined effect, with emission strength, is represented by one unknown positive amplitude \(A\). The ground is perfectly reflecting (zero deposition), vertical spread \(\sigma\) is positive and common to the three heights, there is one steady point plume, additive background is zero or independently removed, and measurements are exact and simultaneous. Heights are arbitrary distinct real values in \([0,\infty)\). The effective source height \(H=0\) is included. The parameters being reconstructed are precisely \((A,\sigma,H)\), **not** separate source emission rate, wind speed, horizontal dispersion, or background concentration.

Let \(s=(2\sigma^2)^{-1}>0\), \(t=H/\sigma^2=2sH\ge0\), and \(a=\log(2A)-sH^2\). Then for every height
\[
 \log C(z)=a-sz^2+\log\cosh(tz).
\]
After obtaining \(t\) from \(F(t)=\Delta\), use the exact formulas
\[
 s=\frac{\log\cosh(tz_1)-\log\cosh(tz_0)-(y_1-y_0)}{u_1-u_0},\quad
 a=y_0+su_0-\log\cosh(tz_0),
\]
\[
 \sigma=(2s)^{-1/2},\qquad H=\frac{t}{2s},\qquad
 A=\frac12\exp\left(a+sH^2\right).
\]
Thus \(\Delta\le0\) together with \(s>0\) is also a necessary-and-sufficient model-compatibility criterion for arbitrary three positive readings.

## Proof
**1. Reduction.** Expanding both squares in the two Gaussian exponentials yields
\[
 C(z)=2A e^{-s(z^2+H^2)}\cosh(2sHz),
\]
so the logarithm is an affine function of \(u=z^2\) plus \(\log\cosh(t\sqrt u)\). Taking a second divided difference annihilates the affine part and gives exactly \(\Delta=F(t)\).

**2. Strict monotonicity of the invariant.** Fix \(t>0\) and put \(g_t(u)=\partial_t\log\cosh(t\sqrt u)=\sqrt u\tanh(t\sqrt u)\). For \(u>0\), writing \(x=t\sqrt u\), direct differentiation gives
\[
 g_t''(u)=\frac{x\operatorname{sech}^2x-\tanh x-2x^2\operatorname{sech}^2x\tanh x}{4u^{3/2}}<0.
\]
Indeed \(q(x)=\tanh x-x\operatorname{sech}^2x\) obeys \(q(0)=0\) and \(q'(x)=2x\operatorname{sech}^2x\tanh x>0\); thus the numerator is \(-q(x)-2x^2\operatorname{sech}^2x\tanh x<0\). The series \(g_t(u)=tu-t^3u^2/3+O(u^3)\) extends its strict concavity through \(u=0\). Every second divided difference of a strictly concave function on three strictly ordered knots is strictly negative. Hence
\[
 F'(t)=[g_t]_{u_0,u_1,u_2}<0 \qquad(t>0).
\]
Clearly \(F(0)=0\). Moreover \(\log\cosh(t\sqrt u)=t\sqrt u+O(1)\) uniformly at the three fixed knots as \(t\to\infty\), including \(u=0\), and \([\sqrt u]_{u_0,u_1,u_2}<0\); therefore \(F(t)\to-\infty\). This proves that \(F:[0,\infty)\to(-\infty,0]\) is a strictly decreasing bijection.

**3. Global inversion and exact admissibility.** For any modeled readings the only possible \(t\) solves \(F(t)=\Delta\), so it is unique. The first log difference determines \(s\); the first reading determines \(a\); the displayed transformation then uniquely determines \(\sigma,H,A\). Conversely, whenever the stated procedure gives \(t\ge0\) and \(s>0\), the reconstructed model agrees with the first two log readings by construction and the third by equality of divided differences; all three physical parameters satisfy their hypotheses. If \(\Delta>0\) no \(t\ge0\) exists, and if \(s\le0\) no positive finite vertical spread exists.

**4. Minimal number of vertical readings.** At any fixed physical parameter triple and any two distinct nonnegative heights, select any sufficiently nearby \(t'\ge0\) with \(t'\ne t\); solve the first log difference for \(s'\) and the first reading for \(a'\). Because \(s'>0\) by continuity and \(A'>0\), this generates infinitely many distinct admissible physical triples with exactly the same two measurements. At \(t=0\) select nearby \(t'>0\). Thus two measurements cannot identify all three unknowns, while any three can.

**5. Sharp weak identification at ground level.** For fixed heights, the Taylor series
\[
 \log\cosh(t\sqrt u)=\frac{t^2u}{2}-\frac{t^4u^2}{12}+\frac{t^6u^3}{45}+O(t^8)
\]
shows the universal expansion
\[
 F(t)=-\frac{t^4}{12}+\frac{u_0+u_1+u_2}{45}t^6+O(t^8),\qquad
 t\sim(-12\Delta)^{1/4}\quad(\Delta\uparrow0).
\]
Consequently, for fixed \(s\to s_0>0\), \(\Delta\sim-(2s_0H)^4/12\) as \(H\downarrow0\). To prove the exponent cannot be improved for **unknown amplitude and spread**, start from any physical ground source \(t=0\), \(s=s_0>0\), and keep the first two log measurements **exactly fixed** while varying \(t\downarrow0\). Their equations impose \(s(t)=s_0+t^2/2+O(t^4)>0\) and determine an admissible \(a(t)\). The third log reading differs from its initial value by
\[
 -\frac{(u_2-u_0)(u_2-u_1)}{12}t^4+O(t^6),
\]
whereas \(H(t)=t/(2s_0)+O(t^3)\). The full three-reading perturbation is therefore of order \(H^4\), disproving any local uniformly Hölder inverse estimate with exponent strictly larger than \(1/4\). The expansion gives a matching fourth-root upper estimate for \(H\) locally about the ground-source data because \(F\) is invertible and \(s\) remains bounded away from zero.

## Verification
The standalone `verify.py` evaluates the exact inversion for four parameter/height combinations with 70-decimal-digit arithmetic, checks monotonicity at a finite mesh, and checks the universal \(-1/12\) leading coefficient numerically. Run `python verify.py` after installing the publicly available `mpmath` package. The analytical monotonicity and weak-identification proofs above—not these finitely many checks—establish the all-parameter assertions.

## Relationship to prior work
The reflected two-Gaussian forward solution follows the classical method of images and appears explicitly as Eq. (3.8) of Stockie (2011). Lushi and Stockie (2009, first publicly posted August 11, 2009) invert Gaussian plume observations for **known** source locations and dispersion structure, using constrained linear least squares for emission rates; their discussion of Hogan et al. (2005) cites a distinct four-location source-localization result with prescribed transport structure. Kumar et al. (2021) discuss multilevel measurements in practical atmospheric inversion, and Newman et al. (2024) estimate several plume and source parameters with Bayesian methods while emphasizing geometry-dependent identifiability. These prior contributions motivate the problem but, in the inspected materials, do not provide this three-vertical-height universal uniqueness criterion together with its exact compatibility condition and fourth-root boundary conditioning. Full Gaussian-mixture identifiability results from continuously observed density functions do not alone prove uniqueness from just **three prescribed scalar point values**. Historical priority is provisional, particularly because the original Hogan et al. report and all possible specialized sensor-design literature were not fully accessible.

## Limitations
This is a theorem about exact static forward-model data, not a guarantee of stable estimation under realistic measurement error. The fourth-root singularity means the source-height estimate is **especially unstable near ground level** if amplitude and dispersion are unknown. Unknown background, incomplete reflection, dry deposition, inversion layers, wind shear, uncertain sensor altitudes or horizontal variation can invalidate the three-parameter model. The exponential sum is a reflected plume profile, not an arbitrary unequal Gaussian mixture. The combined amplitude \(A\) does not separately identify emission strength and meteorology. Only three readings on the same known vertical line are covered; the statement is not a result about all sensor configurations or arbitrary numbers of sources.

## References
1. E. Lushi and J. M. Stockie, *An inverse Gaussian plume approach for estimating atmospheric pollutant emissions from multiple point sources*, arXiv:0908.1589, first submitted 2009-08-11, https://arxiv.org/abs/0908.1589.  
2. J. M. Stockie, *The Mathematics of Atmospheric Dispersion Modelling*, SIAM Review 53 (2011), DOI:10.1137/10080991X; open full text https://www.sfu.ca/~jstockie/atmos/paper.pdf (especially Eq. (3.8), sections 3–4).  
3. P. Kumar et al., *Mobile atmospheric measurements and local-scale inverse estimation*, Atmospheric Measurement Techniques 14 (2021), DOI:10.5194/amt-14-5987-2021, https://amt.copernicus.org/articles/14/5987/2021/.  
4. T. Newman et al., *Probabilistic Inversion Modeling of Gas Emissions: A Gradient-Based MCMC Estimation of Gaussian Plume Parameters*, arXiv:2408.01298 (2024), https://arxiv.org/abs/2408.01298.  
5. W. R. Hogan et al. (2005), *An inverted Gaussian plume model for estimating the location and amount of release of airborne agents from downwind atmospheric concentrations*, referenced and discussed in [1]; original full text not established here.
