# Two physical-time clocks and one transverse multiplier at a four-oval chemical bifurcation
## Finding
For the shifted quartic chemical oscillator of Craciun and Erban, all four attracting cycles have the same nontrivial Floquet multiplier, even though their physical-time periods separate into two unequal pairs. At the parameter where the four real ovals meet at ordinary double points, the two period coefficients have exact ratio \(13/7\), while the common multiplier tends to a finite number strictly between zero and one.

Specifically, set \(\mu_c=337/9\), let \(\varepsilon>0\), and put
\[
q_\mu(u,v)=16(u^4+v^4)-25(u^2+v^2)+\mu u^2v^2+9,\qquad h(x,y)=q_\mu(x-2,y-2).
\]
Consider original-time dynamics
\[
\dot x=xy(-h h_x-\varepsilon h_y),\qquad
\dot y=xy(-h h_y+\varepsilon h_x).
\]
For every \(\mu>\mu_c\) the system has **exactly four nonconstant periodic orbits in the positive quadrant**, the four ovals of \(h=0\), denoted right, top, left, and bottom according to the unshifted coordinate direction. They are attracting and hyperbolic, and their minimal physical-time periods satisfy
\[
T_R=T_T<T_L=T_B.
\]
For a right oval \(\Gamma_R(\mu)\) in unshifted coordinates, define the positive geometric integral
\[
I(\mu)=\int_{\Gamma_R(\mu)}|\nabla q_\mu|\,ds.
\]
The nontrivial Floquet multiplier of **each** of the four cycles is exactly
\[
\rho_R=\rho_T=\rho_L=\rho_B=\exp\!\left(-\frac{I(\mu)}{\varepsilon}\right)\in(0,1).
\]
Writing \(\delta=\mu-\mu_c\), the two original-time periods have sharp asymptotics
\[
T_R=T_T=\frac{125}{8281\varepsilon}\log\frac1\delta+O_\varepsilon(1),\qquad
T_L=T_B=\frac{125}{4459\varepsilon}\log\frac1\delta+O_\varepsilon(1),
\qquad \delta\downarrow0.
\]
In particular, \(\lim_{\delta\downarrow0}T_L/T_R=13/7\). The geometric exponent has an **explicit nonzero critical limit**
\[
\lim_{\mu\downarrow\mu_c}I(\mu)=I_c
=\frac{8407}{400}+\frac{1225}{384}\arctan\frac7{24}
=21.92283277026094\ldots.
\]
Consequently all four transverse multipliers converge to \(\exp(-I_c/\varepsilon)\) even as their physical-time periods diverge, and their transverse exponents per unit physical time approach zero from below with
\[
\chi_R=\chi_T\sim-\frac{8281I_c}{125\log(1/\delta)},\qquad
\chi_L=\chi_B\sim-\frac{4459I_c}{125\log(1/\delta)}.
\]
Here \(\chi_j=\log(\rho_j)/T_j\). The exponents are exactly independent of \(\varepsilon\) at fixed \(\mu\), whereas the multipliers depend on \(\varepsilon\).

## Assumptions and scope
All assertions concern real \(\mu>337/9\), \(\varepsilon>0\), and original physical time in the displayed mass-action differential equations, without reparametrizing time. The four cycles lie in \([1,3]^2\), hence strictly inside the positive quadrant. The labels are with respect to \((u,v)=(x-2,y-2)\); the right oval has \(u>0\), top \(v>0\), left \(u<0\), and bottom \(v<0\). The explicit limit and the logarithmic laws are one-sided as \(\mu\downarrow337/9\) with \(\varepsilon\) fixed. No claim is made about periodic orbits at or below the critical parameter or about uniformity in \(\varepsilon\).

## Proof
**1. The invariant curve and exhaustive periodic-orbit count.** Direct differentiation gives the exact, globally valid cofactor identity
\[
\dot h=-xy|\nabla h|^2h,\qquad
\frac{d}{dt}(h^2)=-2xy|\nabla h|^2h^2.
\]
Thus, on any nonstationary periodic orbit in the strictly positive quadrant, \(h=0\), because otherwise the nonnegative quantity \(h^2\) is strictly decreasing wherever \(\nabla h\ne0\), and if \(\nabla h=0\) the full vector field vanishes. Craciun and Erban's Lemma 13 gives precisely four smooth ovals of \(q_\mu=0\) when \(\mu>\mu_c\). The direct polar description below also confirms that there are no other curve components. On a regular oval the vector field equals \(\varepsilon xy(-h_y,h_x)\), which never vanishes; hence each oval is a periodic orbit. Since all its points satisfy \(|u|,|v|\le1\), the translated curve is strictly positive and has \(xy>0\). Linearizing the scalar cofactor along an oval gives negative normal exponent; hence all four cycles are hyperbolically attracting. (The source already proves their existence and stability.)

**2. Exact polar quadrature and period splitting.** Put \(u=r\cos\theta\), \(v=r\sin\theta\), and define
\[
A_\mu(\theta)=16+\frac{\mu-32}{4}\sin^2(2\theta),\quad
\Delta_\mu(\theta)=49-9(\mu-32)\sin^2(2\theta),\quad
k=\frac7{3\sqrt{\mu-32}}\in(0,1).
\]
Since \(q_\mu=A_\mu r^4-25r^2+9\), the two squared radii on the right oval, indexed by \(+\) and \(-\), are
\[
r_\pm^2(\theta)=\frac{25\pm\sqrt{\Delta_\mu(\theta)}}{2A_\mu(\theta)},
\quad -\theta_*\le\theta\le\theta_*,\quad
\theta_*=\tfrac12\arcsin k.
\]
The two arcs meet smoothly where \(\Delta_\mu=0\). On the zero level, the polar angular speed is
\[
\dot\theta=\varepsilon(2+u)(2+v)\frac{\partial_r q_\mu}{r}
=\pm 2\varepsilon(2+u)(2+v)\sqrt{\Delta_\mu(\theta)}.
\]
Write \(u_\pm=r_\pm\cos\theta\), \(v_\pm=r_\pm\sin\theta\), and \(w_\pm=(2+u_\pm)(2+v_\pm)\). Addition of the travel times on the two radial branches yields the exact convergent quadrature
\[
T_R=\frac1{2\varepsilon}\int_{-\theta_*}^{\theta_*}
\frac{w_+^{-1}+w_-^{-1}}{\sqrt{\Delta_\mu(\theta)}}\,d\theta.
\]
Reflection \((u,v)\mapsto(-u,v)\) sends the right oval to the left and replaces the two factors \(2+u_\pm\) by \(2-u_\pm\); the other factor remains \(2+v_\pm>0\). As \(u_\pm>0\) in the angular interior, the integrand becomes strictly larger at every interior angle, proving \(T_R<T_L\). Reflection across the diagonal exchanges the right and top ovals without changing the symmetric time factor \((2+u)(2+v)\); similarly for left and bottom. Thus \(T_R=T_T<T_L=T_B\) for **every** admissible parameter.

**3. Floquet multiplier.** Along any regular zero-level oval \(\Gamma\), the physical tangential speed has magnitude \(\varepsilon xy|\nabla h|\). The variation of \(h\) normal to the orbit satisfies
\[
\frac{d}{dt}(\delta h)=-xy|\nabla h|^2\delta h,
\]
so the nontrivial eigenvalue of the Poincaré map equals
\[
\rho(\Gamma)=\exp\!\left(-\int_0^{T_\Gamma}xy|\nabla h|^2\,dt\right)
=\exp\!\left(-\frac1\varepsilon\oint_\Gamma|\nabla h|\,ds\right).
\]
All four unshifted ovals are related by quarter-turns and reflections, which preserve \(|\nabla q_\mu|\) and arclength. Their geometric integrals and hence their multipliers coincide. The derivative \(\nabla h\ne0\) on the smooth ovals, giving strict contraction. This uses the known cofactor, but the comparison and the exact geometric multiplier specialization are distinct from the source's existence theorem.

**4. Sharp logarithmic clock split.** Make the monotone angular substitution \(\sin(2\theta)=k\sin\phi\), \(-\pi/2\le\phi\le\pi/2\). Then \(\Delta_\mu=49\cos^2\phi\) and
\[
T_R=\frac{k}{28\varepsilon}\int_{-\pi/2}^{\pi/2}
\frac{w_+^{-1}(\phi)+w_-^{-1}(\phi)}{\sqrt{1-k^2\sin^2\phi}}\,d\phi.
\]
The left formula is identical with \(2+u_\pm\) replaced by \(2-u_\pm\). As \(\delta\downarrow0\),
\[
1-k^2=\frac{9\delta}{49+9\delta}.
\]
The two endpoint pairs of radial branches converge to the critical nodes \((u,v)=(3/5,\pm3/5)\) for the right oval and \((-3/5,\pm3/5)\) for the left. At these nodes the positive chemical weights are
\[
w_{++}=\frac{169}{25},\qquad w_{+-}=w_{-+}=\frac{91}{25},\qquad w_{--}=\frac{49}{25}.
\]
The standard elementary endpoint estimate
\[
\int_0^{c}\frac{d\psi}{\sqrt{\psi^2+1-k^2}}
=\tfrac12\log(1/\delta)+O(1),\qquad c>0\text{ fixed},
\]
combined with \(w_+^{-1}+w_-^{-1}=2/w_s+O(|\cos\phi|+\sqrt\delta)\) in each endpoint collar, gives a bounded integrated remainder. Each endpoint with node weight \(w_s\) therefore contributes \(\log(1/\delta)/(28\varepsilon w_s)+O_\varepsilon(1)\). Summing the two nodes gives exactly
\[
\frac{1}{28\varepsilon}\left(\frac{25}{169}+\frac{25}{91}\right)
=\frac{125}{8281\varepsilon},\qquad
\frac{1}{28\varepsilon}\left(\frac{25}{91}+\frac{25}{49}\right)
=\frac{125}{4459\varepsilon}.
\]
The ratio of these coefficients simplifies to \(13/7\).

**5. Explicit limiting multiplier.** Denote by \(\Omega_R(\mu)\) the right lobe where \(q_\mu<0\). Its outward unit normal is \(\nabla q_\mu/|\nabla q_\mu|\). The divergence theorem therefore gives the exact identity
\[
I(\mu)=\iint_{\Omega_R(\mu)}\Delta_{u,v}q_\mu\,du\,dv
=\iint_{\Omega_R(\mu)}\big[(192+2\mu)(u^2+v^2)-100\big]\,du\,dv.
\]
At \(\mu=\mu_c\), the radial discriminant becomes \(49\cos^2(2\theta)\) on \([-\pi/4,\pi/4]\). The lobes converge in area and the integrand is uniformly bounded, so this identity has a finite limit. Performing the radial integral and setting \(t=\sin(2\theta)\) gives
\[
I_c=12600\int_0^1\frac{625-49t^2}{(576+49t^2)^2}\,dt
=\frac{8407}{400}+\frac{1225}{384}\arctan\frac7{24}.
\]
This is strictly positive. The common-multiplier limit and the stated physical-time exponent asymptotics follow by dividing \(-I(\mu)/\varepsilon\) by the two period asymptotics.

## Verification
The accompanying standard-library program `verify.py` computes both period quadratures and the independent divergence-area integral by deterministic Simpson integration for several parameters; checks strict period splitting, exact critical coefficients as rational numbers, and the critical integral against its closed form; and confirms a sample original-time return by direct Runge–Kutta integration. It prints `CHECK_OK` when these finite tests pass. The proof above, rather than the finite numerical checks, establishes the theorem for the entire parameter range. In particular, the convergence of the multiplier follows from the divergence theorem and bounded-domain convergence, not from numerical extrapolation.

## Relationship to prior work
Craciun and Erban (2024 preprint; 2025 journal revision) derive this exact mass-action vector field, its polynomial cofactor and the four-oval geometry, prove existence of at least four stable algebraic cycles, and identify the ordinary double-point parameter \(337/9\). These inputs are **not** new. General cofactor and invariant-curve cycle-count methods occur in Gasull and Giacomini, and logarithmic slowdowns near saddles are classical. The present theorem is the specific **pairwise unequal original physical periods together with exactly equal transverse multipliers**, the sharp, unequal logarithmic coefficients with rational ratio \(13/7\), and the explicit nonzero critical multiplier limit. These particular quantitative statements are not extracted from the prior existence and cofactor formulas without the geometric and singular-period calculations given here.

## Limitations
The assertions apply only to the displayed ninth-degree family for \(\mu>337/9\), not to arbitrary chemical realizations of quartic curves. At the critical parameter the degenerate curve does not consist of four periodic orbits; all asymptotic quantities refer to the one-sided limit. No uniform error bounds in \(\varepsilon\) are established. The named sources were inspected, but exhaustive priority across unindexed publications is not asserted; related general separatrix and cofactor results may imply components of the proof. Independent mathematical audit has not been performed.

## References
1. G. Craciun and R. Erban, *Planar chemical reaction systems with algebraic and non-algebraic limit cycles*, arXiv:2406.05057, first posted 2024-06-07; Journal of Mathematical Biology (2025). Source: https://arxiv.org/abs/2406.05057 . See Theorem 3, Lemma 13 and equations (5.13)–(5.19).
2. A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803 (2022); see general invariant-curve cycle methods. Source: https://arxiv.org/abs/2210.15803 .
