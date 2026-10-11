# Sharp stationary variance defect in a reflection-symmetric quadratic flow

## Finding
For the real-parameter flow
\[
\dot x=x(1-y),\qquad \dot y=z,\qquad \dot z=x^2-y-a z,
\]
let \(\mu\) be any compactly supported invariant Borel probability measure with \(\mu(\{x=0\})=0\). Write \(\langle f\rangle=\int f\,d\mu\) and \(\operatorname{Var}_\mu(f)=\langle(f-\langle f\rangle)^2\rangle\). Then
\[
\boxed{\operatorname{Var}_\mu(x^2)-a^2\operatorname{Var}_\mu(y)
=\big\langle(x^2-1-a z)^2\big\rangle\ge0.}
\]
Equality holds if and only if \(\mu\) is a convex combination of the two equilibrium point masses at \((\pm1,1,0)\). In particular, the inequality is strict for every invariant probability not supported on those two equilibria.

On either invariant open half-space \(x>0\) or \(x<0\), the finite-time flow Jacobian has the exact expression
\[
\det D\phi_t(x_0,y_0,z_0)=e^{-at}\frac{|x(t)|}{|x_0|}.
\]
Thus every off-plane nonconstant period-\(T\) orbit has transverse Floquet-multiplier product \(e^{-aT}\), and every off-plane compactly supported ergodic invariant measure has total Lyapunov exponent \(-a\).

The variance defect is asymptotically *quadratically* small, with a determined leading coefficient, along the two reflection-related stable periodic-orbit branches born at the Hopf point \(a=2\):
\[
\operatorname{Var}(y)=(2-a)+o(2-a),\qquad
\operatorname{Var}(x^2)=4(2-a)+o(2-a),
\]
\[
\boxed{\big\langle(x^2-1-a z)^2\big\rangle=(2-a)^2+o\big((2-a)^2\big)}
\qquad(a\uparrow2).
\]
Consequently the coefficient \(a^2\) in the universal strict variance inequality cannot be uniformly increased on a parameter neighborhood that approaches \(2\) from below.

## Assumptions and scope
The parameter \(a\) is any real number for the exact identities and equality characterization. The flow need only be defined on the relevant compact invariant support; no global completeness is presumed for every initial condition of the polynomial field. The probability measure need not be ergodic and its support may accumulate on the invariant plane, provided it assigns that plane zero mass. The two stable Hopf branches exist only for \(a<2\) sufficiently close to \(2\); their measures are uniform time measures on one period. The Floquet statement concerns nonstationary orbits not contained in the plane \(x=0\). A fixed point has no canonical nontrivial period.

## Proof
**Stationary normalization without a support-gap assumption.** Since \(\dot x=x(1-y)\), the sign of a nonzero \(x\) is invariant and \(\frac{d}{dt}\log|x|=1-y\). For \(L>0\), choose a smooth bounded truncation \(h_L\) of the identity whose derivative is bounded by \(1\), equals \(1\) on \([-L,L]\), and vanishes outside \([-2L,2L]\). The composite \(h_L(\log|x|)\) extends smoothly to the plane \(x=0\), being constant sufficiently near it. Invariance gives \(\langle h_L'(\log|x|)(1-y)\rangle=0\). Dominated convergence as \(L\to\infty\) (the invariant support is compact and \(\mu(x=0)=0\)) gives \(\langle y\rangle=1\).

Write \(\mathcal L f\) for the derivative along the vector field. Stationarity of a smooth polynomial \(f\) means \(\langle\mathcal L f\rangle=0\). Successively using \(\mathcal L y=z\), \(\mathcal L z=x^2-y-a z\), \(\mathcal L x^2=2x^2(1-y)\), \(\mathcal L y^2=2yz\), \(\mathcal L(yz)=z^2+x^2y-y^2-a yz\), and \(\mathcal L z^2=2z(x^2-y-a z)\), obtain the exact moment relations
\[
\langle y\rangle=\langle x^2\rangle=1,\quad
\langle z\rangle=\langle yz\rangle=0,\quad
\langle x^2y\rangle=1,
\]
\[
\operatorname{Var}_\mu(y)=\langle z^2\rangle,
\qquad\langle x^2z\rangle=a\langle z^2\rangle.
\]
The squared defect expands as
\[
\begin{aligned}
\langle(x^2-1-a z)^2\rangle
&=\operatorname{Var}_\mu(x^2)-2a\langle(x^2-1)z\rangle+a^2\langle z^2\rangle\\
&=\operatorname{Var}_\mu(x^2)-a^2\operatorname{Var}_\mu(y).
\end{aligned}
\]
All quantities are finite because the support is compact.

**Equality rigidity.** Define \(g=x^2-1-a z\). If the squared defect vanishes, then \(g=0\) for \(\mu\)-almost every initial state. Flow invariance at every rational time and continuity make \(g\equiv0\) along \(\mu\)-almost every complete trajectory. Direct differentiation yields
\[
\dot g=(2x^2-a)(1-y)-a g.
\]
Thus along such a trajectory \((2x^2-a)(1-y)\equiv0\). Polynomial vector fields have real-analytic trajectories. The product of two real-analytic functions vanishing on a connected time interval implies that one factor vanishes identically. If \(y\equiv1\), then \(z=\dot y\equiv0\) and \(x^2-1=\dot z\equiv0\), leaving only equilibria \((\pm1,1,0)\). If \(2x^2\equiv a\), nonzero \(x\) is constant, so \(\dot x=x(1-y)=0\) again forces \(y\equiv1\), and the same conclusion follows. Conversely both equilibria satisfy \(g=0\), and all their mixtures give equality. This proves the stated if-and-only-if.

**Exact volume factor.** The Euclidean divergence is \(\nabla\cdot F=1-y-a\). Off the plane, \(\frac{d}{dt}\log|x|=1-y\). Liouville's formula therefore gives
\[
\log\det D\phi_t=\int_0^t(1-y(s)-a)\,ds
=-at+\log|x(t)/x_0|.
\]
Equivalently, the conjugate coordinate \(q=\log|x|\) makes the vector field
\[
\dot q=1-y,\qquad \dot y=z,\qquad \dot z=e^{2q}-y-a z,
\]
with constant divergence \(-a\). For a period-\(T\) orbit, \(x(T)=x_0\); the flow-direction Floquet multiplier is \(1\), leaving transverse product \(e^{-aT}\). On any compactly supported ergodic invariant probability off the plane, the preceding normalization implies \(\int\nabla\cdot F\,d\mu=-a\). Oseledets' and Liouville's identities give the total Lyapunov exponent \(-a\); this assertion assumes the standard ergodic Lyapunov spectrum of a compactly supported smooth-flow measure.

**Hopf sharpness.** In \(q=\log|x|\), eliminate \(y=1-\dot q\), \(z=-\ddot q\). The third-order scalar equation is
\[
\dddot q+a\ddot q+\dot q+e^{2q}-1=0.
\]
At \(q=0,a=2\), its characteristic polynomial is \((\lambda+2)(\lambda^2+1)\). The imaginary eigenvalue crosses transversely: \(\frac{d}{da}\operatorname{Re}\lambda\big|_{a=2}=-1/10\). Put \(a=2-\varepsilon^2\), \(\theta=\omega t\), and seek
\[
q(t)=\varepsilon A\cos\theta+\varepsilon^2Q_2(\theta)+O(\varepsilon^3),
\qquad\omega=1+\omega_2\varepsilon^2+O(\varepsilon^3).
\]
At second order, removal of constant and second-harmonic forcing gives
\[
Q_2=-\frac{A^2}{2}+\frac{A^2}{12}(\cos2\theta+\sin2\theta).
\]
At third order, the cosine and sine solvability conditions are
\[
-4A\omega_2+A-\frac56A^3=0,
\qquad2A\omega_2+\frac16A^3=0.
\]
The nonzero branch has \(A^2=2\), \(\omega_2=-1/6\). Their nonzero cubic coefficient, along with transversality, is the standard nondegenerate supercritical Hopf condition; hence the small stable periodic cycles exist for \(a<2\) close to \(2\). The reflection \(x\mapsto-x\) supplies the second branch. On either cycle,
\[
q=\varepsilon\sqrt2\cos\theta+\varepsilon^2\left[-1+\frac16(\cos2\theta+\sin2\theta)\right]+O(\varepsilon^3).
\]
Since \(y=1-\dot q\), \(z=-\ddot q\), \(x^2=e^{2q}\), the central defect observable has the sharper expansion
\[
g=x^2-1-a z=\varepsilon^2(\cos2\theta-\sin2\theta)+O(\varepsilon^3).
\]
Its mean square on the periodic orbit is \(\varepsilon^4+o(\varepsilon^4)\), as the trigonometric square has mean \(1\). Likewise \(\operatorname{Var}(y)=\varepsilon^2+o(\varepsilon^2)\) and \(\operatorname{Var}(x^2)=4\varepsilon^2+o(\varepsilon^2)\). Substitute \(\varepsilon^2=2-a\) to conclude.

## Verification
A standalone SymPy checker `verify_symbolic.py` verifies every polynomial generator identity, the divergence, the equality-manifold tangency formula, the exact Hopf characteristic factorization, second-order harmonic equation, third-order solvability coefficients, and the leading defect coefficient \(1\). Run `python verify_symbolic.py` with Python 3 and SymPy installed. The mathematical proof above, not finite numerical experimentation, establishes the invariant-measure statement and equality rigidity.

For numerical orientation only, direct ODE integrations near \(a=1.9\), \(1.95\), and \(1.98\) gave squared-defect-to-\((2-a)^2\) ratios about \(0.978\), \(0.989\), and \(0.993\); numerical trajectories are neither exhaustive nor a proof of Hopf existence.

## Relationship to prior work
The original full-text source, J. C. Sprott (2014), equation (8) and Section 4, introduces the five-term reflection-symmetric flow, identifies the two off-plane equilibria and the supercritical Hopf point \(a=2\), and discusses reflection-related periodic/chaotic attractors. It does not state in its inspected complete text the invariant-measure variance defect, exact Jacobian law, equality classification, or Hopf-limit defect coefficient. A later symmetry review (Li et al., 2023) reproduces the system and illustrates reflected attractors; the accessible indexed material concerns geometric symmetry rather than the defect identity. General stationary-moment and cohomological-divergence techniques for *other* chaotic flows do not logically imply this specific equation's strict equality classification or exact quadratic Hopf-limit coefficient. The possibility of an unindexed or inaccessible equivalent specialized treatment remains a literature-search risk.

## Limitations
The theorem does not establish global boundedness, existence of chaotic invariant measures at particular damping values, or attraction of all initial conditions. It does not apply to measures assigning positive mass to \(x=0\) without separately decomposing that mass. The exact Jacobian identity is off-plane; it does not imply individual Lyapunov exponents. The Hopf sharpness is an asymptotic statement along the small local periodic branch, not a universal fixed-parameter optimal constant. This analysis has not undergone independent audit.

## References
1. J. C. Sprott, “Simplest Chaotic Flows with Involutional Symmetries,” *International Journal of Bifurcation and Chaos* **24** (2014), 1450009. DOI: 10.1142/S0218127414500096. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper407.pdf (especially Section 4, Eq. (8)). The reproduced publisher-download stamp documents availability by 2014-02-19; its exact earliest release day has not been established.
2. “Symmetric Strange Attractors: A Review of Symmetry and Conditional Symmetry,” *Symmetry* **15** (2023), 1564. DOI: 10.3390/sym15081564 (Section 2.2, system (3); only indexed section excerpts accessible during comparison).
