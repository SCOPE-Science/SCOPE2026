# A sharp phase-speed-minimum inverse theorem for finite-depth hydroelastic waves

## Finding
For gravity waves under a massless tensioned elastic sheet of strictly positive tension and bending rigidity on finite-depth water, measuring **only the wavenumber and the speed of the global phase-speed minimum** uniquely determines both elastic moduli. There is an exact necessary-and-sufficient open realizability interval for the measured speed at every positive wavenumber. Outside this interval no strictly positive moduli realize the measurements.

Let the measured wavenumber be \(k_*>0\), the measured minimum phase speed be \(c_*>0\), and write \(x=k_*h\), \(y=c_*^2/(gh)\), and \(S=\sinh(2x)/(2x)\). Then the exact admissibility criterion is
\[
\frac{4S\tanh x}{x(3S+1)}<y<\frac{2S\tanh x}{x(S+1)}.
\]
The unique positive in-plane tension \(T\) and bending rigidity \(D\) are
\[
T=\rho gh^2\frac{(3S+1)V-4S}{2Sx^2},\qquad
D=\rho gh^4\frac{2S-(S+1)V}{2Sx^4},\qquad
V=\frac{xy}{\tanh x}.
\]
In particular, the phase speed has an interior minimum precisely when \(0<T/(\rho gh^2)<1/3\), independently of the positive bending modulus, and that minimum is unique and strict.

## Assumptions and scope
Fix known gravitational acceleration \(g>0\), homogeneous fluid density \(\rho>0\), and uniform fluid depth \(h>0\). Consider an inviscid, incompressible, irrotational homogeneous fluid above a rigid impermeable horizontal bottom, capped by a negligible-inertia isotropic thin elastic sheet. The sheet has constant unknown tension \(T>0\) and bending modulus \(D>0\). We use infinitesimal-amplitude free waves on an infinite horizontal domain with no mean current. The linear dispersion law is
\[
\omega(k)^2=\left(gk+\frac{T}{\rho}k^3+\frac{D}{\rho}k^5\right)\tanh(kh),\quad k>0,
\]
with \(c(k)=\omega(k)/k\). The finite-depth factor is obtained by solving the fluid Laplace problem with the no-flux bottom condition and the linear sheet pressure balance. Distinct known constants \(g,\rho,h\) are required; the theorem does not infer depth or sheet inertia. All inequalities concern strict positivity; excluded boundary values correspond to one vanishing elastic coefficient.

## Proof
Introduce \(p=T/(\rho gh^2)>0\), \(q=D/(\rho gh^4)>0\), \(x=kh\). The dimensionless squared phase speed is
\[
f(x)=\frac{c(k)^2}{gh}=\left(\frac1x+px+qx^3\right)\tanh x,\quad x>0,
\]
and it extends continuously to \(f(0)=1\). Define
\[
S(x)=\frac{\sinh(2x)}{2x},\qquad
A(x)=\frac{S(x)-1}{x^2(S(x)+1)},\qquad
G(x)=x^2\frac{3S(x)+1}{S(x)+1}.
\]
Direct differentiation, with \(H(x)=(x\tanh x)'>0\), gives the exact factorization
\[
f'(x)=H(x)\bigl[p+qG(x)-A(x)\bigr].
\]
For \(x>0\), the function \(S\) increases strictly from \(1\) to infinity. Thus \(G\) is strictly increasing, \(G(0+)=0\), \(G(\infty)=\infty\). To prove the needed nontrivial global monotonicity of \(A\), observe that \(A'(x)<0\) is equivalent to
\[
xS'(x)<S(x)^2-1,
\]
or, on writing \(t=2x\), to
\[
\left(\frac{\sinh t}{t}\right)^2+\frac{\sinh t}{t}-\cosh t-1>0.
\]
The entire even power series on the left has zero constant and quadratic coefficients and, for every integer \(n\ge2\), coefficient
\[
\frac{2^{2n+1}-4n(n+1)}{(2n+2)!}>0
\]
at \(t^{2n}\): the numerator is \(32-24>0\) for \(n=2\), and increases positively thereafter (its exponential term outruns the quadratic term). Therefore \(A\) decreases strictly from \(1/3\) to zero.

It follows that \(p+qG(x)-A(x)\) increases strictly from \(p-1/3\) to infinity. If \(p\ge1/3\), then \(f\) is strictly increasing for positive \(x\), with no attained interior minimum. If \(0<p<1/3\), the factor has precisely one zero \(x_*>0\), so \(f\) decreases before \(x_*\), increases after it, and has one strict global minimum. No hidden local extrema are possible.

At a proposed observed minimum \(x>0\), let \(y=f(x)\) and \(V=xy/\tanh x\). The observation and stationarity equations become
\[
px^2+qx^4=V-1,\qquad
px^2+\frac{3S+1}{S+1}qx^4=\frac{S-1}{S+1}.
\]
Since \(S>1\), the determinant is \(2S/(S+1)>0\). Solving gives exactly the formulas in the Finding. The conditions \(p>0\) and \(q>0\) are respectively
\[
V>\frac{4S}{3S+1},\qquad V<\frac{2S}{S+1},
\]
which are exactly the stated strict inequalities in \(y\). These two bounds have positive width because \(S>1\). Conversely, an observation pair satisfying them generates positive \(p,q\) obeying both equations; stationarity with \(p>0,q>0\) forces \(p=A(x)-qG(x)<A(x)<1/3\), and the preceding monotonicity proves that the observed stationary point is the unique global minimum. This proves existence, global uniqueness, sharpness, and both converse directions.

For an additional critical law, the Taylor expansions are
\[
A(x)=\frac13-\frac{2x^2}{45}+O(x^4),\qquad G(x)=2x^2+O(x^4).
\]
Consequently, for every fixed \(q>0\), as \(p\uparrow1/3\), the minimizing wavenumber satisfies
\[
x_*^2\sim\frac{\frac13-p}{2q+2/45}.
\]
Implicit differentiation of \(p+qG(x_*)=A(x_*)\) shows that \(x_*\) decreases strictly as either elastic coefficient increases while the other is held fixed and the minimum exists.

## Verification
The standalone executable numerical cross-check in `checker.py` solves the stationary equation by a root finder, compares the reconstructed parameters with their generating values, tests strict admissibility boundaries and sampled global minima, and checks the critical asymptotics and the no-interior-minimum regime. Its reproducible seeded tests passed 800 forward/inverse parameter cases, nine monotonicity parameter configurations, four critical-limit cases, and 24 admissible synthetic inverse cases. These tests support but do not replace the analytic proof, and sampled grids are not proofs of global optimization. The proof above is exact for every positive parameter in the stated model.

## Relationship to prior work
Deike, Bacri and Falcon (2013), sections 1 and 2.1, establish the governing tension-and-flexure sheet equation and its deep-water dispersion (their equations (2.1) and (2.2)); they experimentally study wave fields, turbulence, and tension shifts. The finite-depth factor in the present forward model follows directly from their displayed fluid kinematic boundary condition before their deep-water approximation. Guyenne and Părău (2014) study finite-depth pure flexural–gravity solitary-wave dispersion and minimum-speed effects, with no simultaneous positive membrane-tension inverse theorem established in the accessible material. Milewski, Vanden-Broeck and Wang (2011) focus on near-minimum-speed nonlinear solitary waves in deep water. More recent ice-cover work uses the phase-speed minimum as a forcing threshold and compares physical parameters through full curves. These forward, pure-flexural, nonlinear, or multi-frequency analyses do not imply the stated strict two-modulus realizability wedge or the global inverse theorem in the inspected passages. We do not claim novelty for the dispersion law, the existence of minimum phase speeds, or the classical pure-capillary long-wave threshold.

## Limitations
The inversion presumes known depth, gravity, and fluid density and exact identification of the unique global phase-speed minimum. Sheet mass, nonlinear tension, finite geometry, damping, viscoelasticity, ambient currents and measurement uncertainty are excluded. Conditioning deteriorates as the minimum approaches the infinite-wavelength boundary or as one elastic coefficient approaches zero; no finite-noise stability bound is proved. Some older and specialized full texts were inaccessible; a historical equivalent phrased in terms of stationary or group/phase velocity data cannot be excluded, so priority remains a residual risk.

## References
- Deike, L., Bacri, J.-C., and Falcon, E. (2013). *Nonlinear waves on the surface of a fluid covered by an elastic sheet*. Journal of Fluid Mechanics **733**, 394–413. DOI: 10.1017/jfm.2013.379. First publicly dated online 2013-09-23. Author-hosted full text: https://labo.msc.u-paris.fr/~falcon/JFM13/JFM13.pdf ; preprint https://arxiv.org/abs/1309.6990 .
- Milewski, P., Vanden-Broeck, J.-M., and Wang, Z. (2011). *Hydroelastic solitary waves in deep water*. Journal of Fluid Mechanics **679**, 628–640. DOI: 10.1017/jfm.2011.163. Repository abstract: https://discovery.ucl.ac.uk/id/eprint/1324413/ .
- Guyenne, P., and Părău, E. I. (2014). *Finite-depth effects on solitary waves in a floating ice sheet*. Journal of Fluids and Structures. Public abstract and indexed text: https://research-portal.uea.ac.uk/ . Online availability date reported as 2014-05-28.
- *Observing Wind-Forced Flexural-Gravity Waves in the Beaufort Sea and Their Relationship to Sea Ice Mechanics* (2021). Journal of Marine Science and Engineering **9**, 471. https://www.mdpi.com/2077-1312/9/5/471 .
