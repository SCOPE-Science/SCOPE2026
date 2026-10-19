# A unique thermal-mode transition and universal peak splitting for a harmonically confined run-and-tumble particle

## Finding

For a one-dimensional, harmonically confined run-and-tumble particle with additive thermal Brownian motion, the familiar Gaussian-convolved beta stationary law admits a *strictly ordered, globally unique* bimodal-to-unimodal transition. The Gaussian convolution and the center-curvature equation themselves are known; the refinements established here are uniqueness and strict monotonicity of the critical thermal curve, a proof excluding additional peak branches, and an exact universal onset coefficient.

Let \(a>0\) be the dimensionless reversal-to-confinement ratio and \(t>0\) the dimensionless thermal variance. For \(0<a<1\) there is exactly one critical variance \(t_c(a)\in(0,1)\), strictly decreasing in \(a\), continuous and real analytic on \((0,1)\), with
\[
\lim_{a\downarrow0}t_c(a)=1,\qquad \lim_{a\uparrow1}t_c(a)=0.
\]
For \(t<t_c(a)\), the stationary position density has exactly two strict global maxima at \(\pm m(a,t)\) and a strict central minimum. For \(t\ge t_c(a)\), it has one global maximum, at zero; the maximum is quartically flat at equality and strictly quadratic for \(t>t_c(a)\). The critical curve does not admit disconnected branches or hidden additional modes. When \(a\ge1\), the stationary law is strictly unimodal for every \(t>0\).

At the transition the two nonzero modes coalesce with the **parameter-independent coefficient**
\[
\boxed{m(a,t)^2=3\,[t_c(a)-t]+O_a\bigl([t_c(a)-t]^2\bigr)\quad(t\uparrow t_c(a)).}
\]
In particular, \(m(a,t)/\sqrt{t_c(a)-t}\to\sqrt3\) for every fixed \(0<a<1\). This is a statement about stationary density peaks, not about dynamical critical exponents or relaxation times.

## Assumptions and scope

The particle's position satisfies
\[
 dX_s=(-\lambda X_s+v\sigma_s)\,ds+\sqrt{2D}\,dW_s,
\]
where \(\lambda,v,D>0\), \(W\) is standard Brownian motion independent of the two-state orientation process \(\sigma_s\in\{-1,+1\}\), and each orientation flips at rate \(\gamma>0\). Let \(R=v/\lambda\), \(a=\gamma/\lambda\), and \(t=D/(\lambda R^2)=D\lambda/v^2\). We work with the dimensionless stationary position \(Y=X/R\). A stationary version exists and is unique. The known stationary law is the convolution
\[
 P_{a,t}(x)=\int_{-1}^{1}\frac{e^{-(x-u)^2/(2t)}}{\sqrt{2\pi t}}\,f_a(u)\,du,\qquad
 f_a(u)=\frac{\Gamma(a+1/2)}{\sqrt\pi\,\Gamma(a)}(1-u^2)^{a-1}\mathbf1_{(-1,1)}(u).
\]
Here \(x\) denotes a dimensionless position, \(\pm m(a,t)\) are the dimensionaless modes, and physical modes equal \(\pm Rm(a,t)\). These formulas assume the orientation **flip** rate is \(\gamma\), not the total rate of attempted redraws; for a convention using flip rate \(\alpha/2\), substitute \(a=\alpha/(2\lambda)\).

For numerical evaluation, let \(S=U^2\), with \(U\) distributed according to \(f_a\); thus \(S\sim\mathrm{Beta}(1/2,a)\). Define
\[
 F_a(z)=\mathbb E[e^{-zS}]={}_1F_1\bigl(\tfrac12; a+\tfrac12;-z\bigr),\qquad q_a(z)=-z\frac{F_a'(z)}{F_a(z)}.
\]
The **known** center-curvature condition defining the transition is \(q_a(z_c)=1/2\), with \(t_c(a)=1/(2z_c)\). We prove here that this equation has exactly one positive root for each \(0<a<1\), and derive the additional assertions above.

## Proof

**1. The stationary law and the center curvature.** In the stationary stochastic-integral representation, the thermal contribution is an independent centered Gaussian with variance \(D/\lambda\). The active contribution, after division by \(R\), has the symmetric beta density \(f_a\), as established in the references. Consequently \(P_{a,t}\) is the stated Gaussian convolution and is positive, symmetric, and real analytic in \(x\) for every \(t>0\). Its center value and second derivative obey
\[
 P_{a,t}(0)=\frac{F_a(1/(2t))}{\sqrt{2\pi t}},\qquad
 P_{a,t}''(0)=\frac{P_{a,t}(0)}{t}\bigl(2q_a(1/(2t))-1\bigr).
\]
This identity also follows by differentiating the Gaussian inside the convolution.

**2. Exactly one crossing, with strict parameter ordering.** Write \(z>0\) for the argument of \(F_a\). Kummer's differential equation gives
\[
 zF_a''(z)+(a+\tfrac12+z)F_a'(z)+\tfrac12F_a(z)=0.
\]
Substitution yields the Riccati equation
\[
 q_a'(z)=\tfrac12-q_a(z)+\frac{q_a(z)^2+(\tfrac12-a)q_a(z)}{z}.
\]
At *every* positive solution of \(q_a(z)=1/2\), therefore,
\[
 q_a'(z)=\frac{1-a}{2z}.
\]
For \(0<a<1\), every crossing of the level \(1/2\) is transverse and upward. At small \(z\), \(q_a(z)=z/(2a+1)+O(z^2)\); Laplace's expansion at the beta-law endpoint \(S=0\) gives
\[
 q_a(z)=\frac12+\frac{1-a}{2z}+O_a(z^{-2})\qquad(z\to\infty).
\]
There must be a crossing and, since every crossing is upward, there can be only one. This proves that the center changes from a local minimum at small thermal variance to a local maximum at large variance. At \(t=1\), directly \(P_{a,1}''(0)<0\) because \(U^2<1\) almost surely; thus \(0<t_c(a)<1\).

For fixed \(z>0\), the density of \(S\) under exponential tilting is proportional to \(S^{-1/2}(1-S)^{a-1}e^{-zS}\). Increasing \(a\) strictly multiplies this density by a decreasing function of \(S\), hence strictly decreases its mean and therefore strictly decreases \(q_a(z)\). Since \(q_a\) crosses \(1/2\) upward, the root \(z_c(a)\) strictly increases with \(a\), so \(t_c(a)\) strictly decreases. The implicit-function theorem and the positive crossing derivative give real analyticity. As \(a\downarrow0\), \(S\) converges in law to one, so \(q_a(z)\to z\) locally uniformly, implying \(z_c(a)\to1/2\) and \(t_c(a)\to1\). As \(a\uparrow1\), \(f_a\) tends to the uniform density; the Gaussian smoothing of that uniform law has negative second derivative at zero at all finite positive \(t\). Therefore \(q_1(z)<1/2\) for every finite \(z>0\), and \(z_c(a)\to\infty\), giving \(t_c(a)\to0\).

**3. No additional peaks (sign-variation argument).** We include the elementary variation lemma required for a global, rather than only local, assertion. Let \(g\) be an integrable compactly supported real function with at most \(n\) changes of sign (in the ordered support). Its bilateral Laplace transform \(H(s)=\int e^{su}g(u)\,du\) has at most \(n\) distinct real zeros. To prove this, induct on \(n\). When \(n=0\) the transform has one constant sign. Otherwise choose a sign-change point \(c\); \((u-c)g(u)\) has at most \(n-1\) changes. By induction the derivative of \(e^{-cs}H(s)\), which is \(e^{-cs}\int e^{su}(u-c)g(u)\,du\), has at most \(n-1\) distinct real zeros. If \(H\) had \(n+1\) distinct real zeros, Rolle's theorem would contradict this bound. A Gaussian convolution of \(g\) is a strictly positive Gaussian factor times \(H(x/t)\) after replacing \(g(u)\) by \(e^{-u^2/(2t)}g(u)\); the latter has the same sign changes.

For \(0<a<1\), choose \(0<\epsilon<1-a\) and the smooth, compactly supported approximant
\[
 f_{a,\epsilon}(u)=C_{a,\epsilon}(1-u^2)^{a-1}\exp\bigl[-\epsilon/(1-u^2)\bigr]\mathbf1_{(-1,1)}(u).
\]
Its derivative has exactly three sign changes: one at zero, and one at each of \(\pm\sqrt{1-\epsilon/(1-a)}\). By the variation lemma the derivative of \(f_{a,\epsilon}*\phi_t\) has at most three distinct zeros (and three sign changes). As \(\epsilon\downarrow0\), the approximants converge to \(f_a\) in \(L^1\), and their Gaussian-convolution derivatives converge locally uniformly. Therefore \(P_{a,t}'\) has at most three *sign changes*, since any four strict changes would persist in the approximants. By symmetry \(P_{a,t}'\) is odd. It is negative for every \(x\ge1\), since \(P_{a,t}'(x)=\int (u-x)\phi_t(x-u)f_a(u)\,du/t<0\) there.

When \(t<t_c\), center curvature is positive, so the derivative is positive for small positive \(x\), while negative for \(x\ge1\). An extra positive-side sign change would, by symmetry, force at least five sign changes including the central one, impossible. Thus there is exactly one positive-side transition from increasing to decreasing, giving precisely the two strict modes \(\pm m(a,t)\). When \(t>t_c\), the derivative is negative immediately to the right of zero and beyond one; any intervening positive region would force at least five changes across the whole line, impossible. Hence the density is strictly decreasing on the positive half-line and has its sole mode at zero. The critical case follows from the strict negative quartic derivative proved in Step 4. For \(a>1\), the original density \(f_a\) is already strictly unimodal and has a derivative with just one sign change. The same lemma (or direct symmetric-Gaussian pairing) makes its Gaussian convolution strictly unimodal. At \(a=1\), it is the convolution of a uniform law, whose derivative is explicitly negative for all \(x>0\).

**4. The quartic critical point and universal bifurcation law.** A Gaussian convolution satisfies the heat equation \(\partial_tP_{a,t}=\tfrac12\partial_x^2P_{a,t}\). Differentiating the center-curvature identity from Step 1 with respect to \(t\) at \(t=t_c\), using \(q_a'(z_c)=(1-a)/(2z_c)>0\) and \(dz/dt=-1/(2t^2)<0\), gives
\[
 \partial_tP_{a,t}''(0)\big|_{t_c}<0,
 \qquad P_{a,t_c}^{(4)}(0)=2\partial_tP_{a,t}''(0)\big|_{t_c}<0.
\]
Thus at criticality zero is a strict, quartically flat maximum, with no additional maxima by Step 3. For \(t\) close to \(t_c\), the quotient \(P_{a,t}'(x)/x\) extends to a jointly analytic function \(G(y,t)\) of \(y=x^2\) near \((0,t_c)\), and
\[
 G(y,t)=P_{a,t}''(0)+\frac16 P_{a,t}^{(4)}(0)y+O(y^2).
\]
At criticality \(G(0,t_c)=0\) and \(\partial_yG(0,t_c)=P_{a,t_c}^{(4)}(0)/6\ne0\). By the implicit-function theorem its unique nearby zero has \(y(t_c)=0\), with derivative
\[
 y'(t_c)=-\frac{\partial_t P_{a,t}''(0)|_{t_c}}{P_{a,t_c}^{(4)}(0)/6}=-3.
\]
For \(t<t_c\), Step 3 identifies this positive root \(y=m(a,t)^2\) with the square of the **unique** positive mode. Analyticity of \(y\) in \(t\) implies \(m(a,t)^2=3(t_c-t)+O_a((t_c-t)^2)\). The cancellation responsible for the exact coefficient \(3\) is the heat equation; no fitted number or assumption about a particular persistence ratio is involved.

## Verification

The accompanying standalone Python program `verify.py` uses SciPy Gauss–Jacobi quadrature to evaluate the convolution and its first, second and fourth spatial derivatives; it independently solves the hypergeometric curvature equation and locates off-center peaks. Run `python verify.py` with NumPy and SciPy installed. It checks five persistence ratios \(a\in\{0.1,0.25,0.5,0.75,0.9\}\), both sides of the phase curve, the signs of the quartic derivatives, numerical sign patterns, and four near-critical peak locations. At \(a=0.5\), the computed ratios \(m(a,t)^2/(t_c-t)\) tend toward \(3\), approximately \(2.95452, 2.98627, 2.99542, 2.99862\) for decreasing gaps \(0.01,0.003,0.001,0.0003\). These are finite checks, *not* a proof of global uniqueness or the limiting formula; those follow from the Riccati, variation, and heat-equation arguments above.

## Relationship to prior work

The symmetric-beta stationary distribution for an athermal one-dimensional trapped RTP, its Gaussian smoothing by thermal diffusion, the possibility of a bimodal-to-unimodal change, and a hypergeometric center-curvature equation are **not new here**. Closest earlier work includes Sabhapandit and Majumdar (2024), Sec. IV and Eq. (95)–(96), which analyzes an exactly equivalent stochastic-trap-center formulation and plots the thermal phase boundary. Guéneau, Majumdar and Schehr (2026), Sec. V.1.1, also give the convolved law and phase-boundary analysis; Sevilla and Meléndez Mora (2026), Secs. II–IV, present the same convolution framework and physical regimes. These cover a substantial part of the setup and known phase picture. The claim here is limited to the global uniqueness and strict ordering proof, exclusion of extra modal branches via sign variation, the exact quartic criticality, and the universal \(\sqrt3\) peak-splitting constant. These strengthened statements were not located in the specific inspected sources; broader uninspected Gaussian scale-space theory might imply some of them.

## Limitations

The result concerns the ideal one-dimensional, symmetric, constant-speed, constant-flip-rate, harmonic model with independent *additive* Brownian thermal noise and strictly positive thermal variance. It does not cover position-dependent tumbling, asymmetry, nonharmonic confinement, interactions, higher-dimensional radial modes, or critical relaxation. The limiting onset formula fixes \(a\) strictly inside \((0,1)\); it does not assert uniformity as \(a\) approaches an endpoint. The universal coefficient is a local-onset property, not an independent claim that arbitrary heat-smoothed mixtures have exactly two modes. A full external novelty audit has not been performed, and other scale-space literature may contain equivalent general lemmas.

## References

1. F. J. Sevilla and J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781v1 (first posted 2026-08-22). https://arxiv.org/abs/2608.21781
2. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (first posted 2026-02-09). https://arxiv.org/abs/2602.08436
3. S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480v1 (first posted 2024-04-03). https://arxiv.org/abs/2404.02480
4. R. Garcia-Millan and G. Pruessner, *Run-and-tumble motion in a harmonic potential: field theory and entropy production*, Journal of Statistical Mechanics (2021) 063203. https://doi.org/10.1088/1742-5468/ac014d
