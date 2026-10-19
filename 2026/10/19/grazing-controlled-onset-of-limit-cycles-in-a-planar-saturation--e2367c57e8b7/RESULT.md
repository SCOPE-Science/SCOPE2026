# Grazing-controlled onset of limit cycles in a planar saturation oscillator

## Finding

Let \(S(t)=\max(-1,\min(1,t))\), applied componentwise, and consider the continuously differentiable-in-time, piecewise-affine planar flow
\[
\dot x=(1+a)S(x)+bS(y)-x,\qquad
\dot y=-bS(x)+(1+a)S(y)-y.
\]
For each **fixed** \(b>0\), put
\[
C_* = \left(\frac{3\pi}{8\sqrt 2}\right)^{2/3},
\qquad K_b=\frac{8\sqrt{2C_*}}{b}.
\]
There is an \(a_0(b)>0\) such that for every \(0<a<a_0(b)\) the flow has a hyperbolically attracting periodic orbit \(\Gamma_a\), unique among periodic orbits meeting the positive \(x\)-axis in the annulus
\[
1+\frac{C_*}{2}a^{2/3}<\sqrt{x^2+y^2}<1+2C_*a^{2/3}.
\]
Its radius is uniformly, over every point of the orbit,
\[
\sqrt{x^2+y^2}=1+C_*a^{2/3}+O_b(a).
\]
If \(T_a\) is its **physical-time** least period and \(\mu_a\) its nontrivial Floquet multiplier, then
\[
T_a=\frac{2\pi}{b}(1+a)+O_b(a^{4/3}),
\qquad
\mu_a=1-K_ba^{1/3}+O_b(a^{2/3}).
\]
In particular, \(0<\mu_a<1\) for all sufficiently small positive \(a\). The leading amplitude constant \(C_*\) does not depend on \(b\). At \(a=0\), every circle of radius at most one is periodic, and \(\Gamma_a\) approaches the *outer boundary* of this period annulus, not the equilibrium at the origin.

## Assumptions and scope

The parameter \(b\) is an arbitrary fixed positive real number. All asymptotics are for \(a\downarrow0\), and all constants implicit in \(O_b(\cdot)\) may depend on \(b\). The vector field is globally Lipschitz and piecewise affine. The result constructs and identifies one locally unique attracting orbit near the unit circle; it does not assert global uniqueness of limit cycles or provide parameter-uniform estimates as \(b\downarrow0\). The natural classification is MSC2020 34C25 (periodic solutions of ordinary differential equations).

## Proof

**1. Critical period annulus and polar equations.** Introduce \(z=(x,y)^\mathsf T\), \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), and \(d(z)=z-(S(x),S(y))^\mathsf T\). The vector field is exactly
\[
\dot z=(aI+bJ)z-((1+a)I+bJ)d(z).
\]
Use clockwise polar coordinates \(x=r\cos\phi\), \(y=-r\sin\phi\), and the cross product \(u\times v=u_1v_2-u_2v_1\). Direct differentiation gives
\[
\dot r=ar-\frac{(1+a)z\cdot d+bz\cdot Jd}{r},
\qquad
\dot\phi=b-\frac{bz\cdot d}{r^2}+\frac{(1+a)z\times d}{r^2}.
\]
For \(r\le1\), the clipping defect vanishes. At \(a=0\) the entire closed unit disk is filled by the unperturbed rotations \(\dot z=bJz\), with period \(2\pi/b\). For \(a>0\), radial growth in this disk is \(\dot r=ar\).

**2. Uniform first-return expansion.** Fix arbitrary constants \(0<c<C\), and initially take \(r(0)=1+\eta\) with \(ca^{2/3}\le\eta\le Ca^{2/3}\). For sufficiently small \(a\), the angular speed stays above \(b/2\), so increasing \(\phi\) defines a full return to the positive \(x\)-axis. The clipping defects are supported in four short angular caps around the coordinate axes. Each cap has width \(2\sqrt{2\eta}+O(\eta^{3/2})\); on a cap, with \(u\) the angular displacement from its axis, its leading radial defect is
\[
(\eta-u^2/2)_+.
\]
Hence the total first-order clipping area is
\[
4\int_{-\sqrt{2\eta}}^{\sqrt{2\eta}}(\eta-u^2/2)\,du
=\frac{16\sqrt2}{3}\eta^{3/2}.
\]
Here is the uniform remainder control. On any one revolution, \(|d|=O(\eta)\) on caps of total length \(O(\sqrt\eta)\), while the terms involving \(z\cdot Jd\) are at most \(O(\eta^{3/2})\) on those caps. Thus integration of the exact polar equation yields \(r(\phi)-r(0)=O_b(a+\eta^{3/2}+\eta^2)=O_b(a)\). Replacing this moving radius in the clipped area by the initial radius contributes at most \(O_b(a\sqrt\eta)\): the radial clipping function is Lipschitz, and the union of the original and displaced caps still has angular width \(O(\sqrt\eta)\). Replacing the angular speed by \(b\) and the exact cosine profile by its parabolic approximation contributes \(O_b(\eta^2+a\eta)\). These estimates hold uniformly for the stated \(\eta\)-range. Consequently the positive-axis first-return map \(P_a\) satisfies
\[
P_a(1+\eta)-(1+\eta)
=\frac{2\pi}{b}a-\frac{16\sqrt2}{3b}\eta^{3/2}
+O_b(a^{4/3}),
\qquad ca^{2/3}\le\eta\le Ca^{2/3}.
\]

**3. Existence, selection, and uniqueness.** Take \(c=C_*/2\) and \(C=2C_*\). By the identity \((16\sqrt2/3)C_*^{3/2}=2\pi\), the leading term of the return displacement is strictly positive at the smaller endpoint and strictly negative at the larger endpoint. The return map is continuous, so it has a fixed point \(1+\eta_a\) in between. The fixed-point equation and the uniform remainder imply
\[
\eta_a^{3/2}=\frac{3\pi}{8\sqrt2}a+O_b(a^{4/3}),
\qquad \eta_a=C_*a^{2/3}+O_b(a).
\]
The radius varies by only \(O_b(a)\) during the revolution, proving the uniform orbit profile.

For uniqueness and stability, note that for \(r<\sqrt2\) at most one coordinate can be saturated. Away from switching lines the divergence is \(2a\) where neither coordinate is saturated and \(a-1\) where one is saturated. The transverse switches for our annulus have nonzero normal velocity, and the vector field is continuous, so their saltation matrices are the identity. Along a return, the total saturated *physical* time is
\[
\tau_{\mathrm{sat}}=\frac{8\sqrt2}{b}\sqrt\eta+O_b(a^{2/3}),
\]
uniformly for \(\eta\asymp a^{2/3}\). The planar variational determinant is therefore
\[
\exp\left(2aT-(1+a)\tau_{\mathrm{sat}}\right)<1.
\]
On the positive \(x\)-axis both the start and return points have \(x>1\) and section-normal velocity \(\dot y=-b\); therefore the derivative of the one-dimensional return map equals this determinant. In particular \(0<P_a'(r)<1\) throughout the annulus, so \(P_a(r)-r\) decreases strictly and its fixed point is unique there. At that fixed point its derivative is the nontrivial Floquet multiplier; hence the cycle is hyperbolically attracting.

**4. Physical period and transverse rate.** In the reciprocal angular-speed integral for time, the first clipping correction is \(b^{-1}\int z\cdot d/r^2\,d\phi\). Terms involving \(z\times d\) have integral size \(O_b(\eta^2)\). The same four-cap computation gives
\[
T=\frac{2\pi}{b}+\frac{16\sqrt2}{3b}\eta^{3/2}
+O_b(a^{4/3}).
\]
At \(\eta=\eta_a\), use the fixed-point relation to obtain \(T_a=\frac{2\pi}{b}(1+a)+O_b(a^{4/3})\). Finally, Liouville's formula and the saturated-time estimate give
\[
\log\mu_a=2aT_a-(1+a)\tau_{\mathrm{sat}}
=-\frac{8\sqrt{2C_*}}{b}a^{1/3}+O_b(a^{2/3}).
\]
Expanding the exponential yields the asserted multiplier law.

## Verification

The included standalone program `verify.py` numerically constructs the angular return map, finds its fixed point, integrates the physical-time and divergence equations, and checks the three predicted normalized limits for \(b=1.5,2\) and \(a=0.004,0.0006\). It also checks the exact cap-area normalization algebraically using floating-point identities. A replay produced `VERIFY_OK`. These numerical tests are finite consistency checks only; the all-small-parameter theorem is proved by the uniform return-map argument above.

## Relationship to prior work

The vector field and its saturation model are equation (2) and the symmetric matrix specialization in Ma, Yuan, Li, Ao, and Yuan (2013). That article studies continuous Lyapunov functions and qualitatively identifies the transition to a limit cycle as its diagonal feedback crosses one; its section V also describes a critical region filled with periodic orbits. The contribution here is the *quantitative near-critical selection* at the boundary of that period annulus: the **two-channel four-cap** amplitude constant, coupling dependence of the Floquet coefficient, and physical-time period coefficient. The fractional exponents themselves are not new. Freire, Ponce and Ros (1999, and explicitly in their 2005 SISO saturation treatment, Theorem 1) already establish a \(2/3\)-power amplitude onset, a \(1/3\)-power characteristic-multiplier logarithm, and period expansions for a planar **single-input scalar saturation** system. Their dynamics have a single clipped scalar output and **three linear zones separated by two parallel frontiers**, not the two independent clipped coordinates, four switching lines and four angular caps here. A theorem for one scalar saturation does not, under its stated hypotheses, apply to the present two-channel system or determine its four-cap coefficient. The formulas here must therefore be read as a particular quantitatively established multi-saturation instance, not as discovery of these exponents in piecewise-linear systems. Simpson (2019) additionally describes \(2/3\)-power scaling for a different hysteretic invisible two-fold with a vanishing-period cycle. None of these inspected results directly gives the combined *model-specific* amplitude, period and Floquet coefficients.

## Limitations

The orbit is asserted to be the unique periodic orbit only within the displayed shrinking annulus, not globally. This is a singular, finite-radius onset rather than the ordinary smooth Hopf scaling near a point equilibrium. The estimates are not uniform as the prescribed coupling \(b\) approaches zero. The 1999 Freire–Ponce–Ros origin article was located at the bibliographic/abstract level but not inspected in full; an unrecognized theorem therein or other earlier work may already imply part of the model-specific calculation. The fractional powers are known in related saturation systems, and historical priority is not certified. Numerical checks are not independent verification or proof of the asymptotic theorem.

## References

1. Y. Ma, R. Yuan, Y. Li, P. Ao, B. Yuan, *Lyapunov Functions in Piecewise Linear Systems: From Fixed Point to Limit Cycle*, arXiv:1306.6880v1 (first posted 2013-06-28), especially equation (2) and sections III–V. https://arxiv.org/html/1306.6880v1
2. E. Freire, E. Ponce and J. Ros, *Limit cycle bifurcation from center in symmetric piecewise-linear systems*, *International Journal of Bifurcation and Chaos* **9** (1999), 895–907, DOI:10.1142/S0218127499000638. The bibliographic record and abstract were checked; the complete original text was not available for inspection.
3. E. Freire, E. Ponce and J. Ros, *Limit cycle bifurcation in SISO control systems with saturation*, IFAC Proceedings Volumes (2005), DOI:10.3182/20050703-6-CZ-1902.00763, especially §2 (one-input three-zone hypotheses) and Theorem 1 (explicit fractional exponents and period). Author-provided full text: https://www.researchgate.net/publication/228894493_Limit_cycle_bifurcation_in_SISO_control_systems_with_saturation
4. D. J. W. Simpson, *Twenty Hopf-like bifurcations in piecewise-smooth dynamical systems*, arXiv:1905.01329 (first posted 2019-05-03), especially the introductory scaling table and section 10.2. https://arxiv.org/abs/1905.01329
