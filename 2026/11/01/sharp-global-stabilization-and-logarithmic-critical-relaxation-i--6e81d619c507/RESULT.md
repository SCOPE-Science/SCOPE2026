# Sharp global stabilization and logarithmic critical relaxation in a quadratic Lorenz-like flow

## Finding

For the polynomial flow
\[
\dot x=-ax+yz,\qquad \dot y=x(b-z),\qquad \dot z=-z+xy+c,
\]
with real initial conditions and parameters \(a,b,c>0\), the equilibrium \(E_c=(0,0,c)\) attracts **every** initial condition exactly when \(c\ge b\). All forward solutions exist globally. If \(c<b\), the additional equilibria are precisely
\[
\left(\pm\sqrt{\frac{b(b-c)}a},\;\pm\sqrt{\frac{a(b-c)}b},\;b\right),
\]
with matching signs, and \(E_c\) has one positive real eigenvalue. For \(c>b\), convergence to \(E_c\) is exponentially fast for every initial condition (with a rate and prefactor potentially dependent on its initial condition).

At the critical surface \(c=b\), set \(w=z-b\), \(k=b^2/a^2\), and \(L=2(a^2+ab^2+b^2)/a^3\). There is a two-dimensional global strong-stable manifold \(W^{ss}(E_b)\) consisting precisely of trajectories converging exponentially to \(E_b\). For every initial condition outside it, \(y(t)\) eventually has a constant nonzero sign and
\[
\boxed{\quad y(t)^{-2}=2kt+L\log t+C+o(1)\quad(t\to\infty),\quad}
\]
where \(C\in\mathbb R\) depends on the trajectory. Equivalently,
\[
\lim_{t\to\infty}\sqrt t\,y(t)=\pm\frac{a}{b\sqrt2},\quad
\lim_{t\to\infty}\frac{x(t)}{y(t)}=\frac ba,\quad
\lim_{t\to\infty}\frac{z(t)-b}{y(t)^2}=\frac ba.
\]
The exceptional strong-stable manifold has three-dimensional Lebesgue measure zero. The logarithmic coefficient is exact for all \(a,b>0\), not fitted from numerical trajectories.

## Assumptions and scope

The vector field is exactly the first, unswitched system of Yan, Liu, Jie and Hong (2024), not the nonlinear-term variants subsequently defined in that article. Parameters are fixed positive real numbers. Global attraction means convergence of every trajectory in \(\mathbb R^3\) to the **specified** equilibrium, not the existence of an absorbing ball or of some other attracting set. The statement on \(W^{ss}\) concerns the global set of initial conditions eventually entering the local strong-stable manifold; it is not a claim that this manifold is an embedded closed plane. The constant \(C\) is a trajectory-dependent finite limit, not a universal constant.

## Proof

**1. Global forward completeness and equilibrium count.** Put \(w=z-b\), so
\[
\dot x=-ax+by+yw,\qquad \dot y=-xw,\qquad \dot w=-w+xy+(c-b).
\]
For \(H=(y^2+w^2)/2\), exact cancellation gives
\[
\dot H=-w^2+(c-b)w\le(c-b)^2/4.
\]
Thus \(y,w\) are bounded on each finite forward interval; \(x\) solves a stable linear equation with bounded finite-interval forcing \((b+w)y\), so it is likewise bounded. Polynomial local existence and the continuation criterion imply global forward existence. An equilibrium with \(x=0\) has \(z=c>0\) and \(y=0\), hence is \(E_c\). If \(x\ne0\), \(\dot y=0\) forces \(z=b\), then \(y=ax/b\), and \(\dot z=0\) gives \(x^2=b(b-c)/a\). This proves the complete equilibrium list.

**2. The strict stabilization half-space.** If \(c>b\), let \(q=b/(c-b)>0\) and
\[
V_q=\tfrac12\bigl[x^2+(1+q)y^2+q(z-c)^2\bigr].
\]
Direct differentiation (without inequalities or averaging) yields
\[
\dot V_q=-ax^2-q(z-c)^2.
\]
This positive-definite, proper function makes trajectories bounded. On the zero-derivative set \(x=0,z=c\), invariance requires \(\dot x=cy=0\), hence \(y=0\). LaSalle's principle gives global convergence to \(E_c\). The linearization at \(E_c\) is a \(2\times2\) block with characteristic polynomial \(\lambda^2+a\lambda+c(c-b)\), together with \(-1\); all eigenvalues have negative real part. Once a trajectory enters a sufficiently small neighborhood, ordinary hyperbolic stability gives exponential convergence, completing the stronger rate assertion.

**3. Critical global convergence.** When \(c=b\), the same \(H\) obeys \(\dot H=-w^2\). In particular \(y,w\) are bounded for all future time, and variation of constants again bounds \(x\), so every trajectory is precompact. The omega-limit set is nonempty, compact and invariant and lies in \(w=0\) by LaSalle. On any *complete bounded trajectory* contained in \(w=0\), the equations imply \(xy=0\), \(\dot y=0\), and \(\dot x=-ax+by\). If the constant \(y\ne0\), then \(xy=0\) forces \(x=0\), contradicted by \(\dot x=by\ne0\). Thus \(y=0\) and \(x(t)=x(0)e^{-at}\); boundedness for negative as well as positive times forces \(x(0)=0\). Consequently the only compact full invariant subset of \(w=0\) is \(E_b\), so every forward trajectory tends to \(E_b\). (The noncompact invariant \(x\)-axis does not contradict this compact omega-limit argument.)

**4. Local center manifold and five-jet.** At \(E_b\), the eigenvalues are \(0,-a,-1\). Use the center coordinate \(u=y\) and express a smooth local center manifold as \(x=h(u)\), \(w=g(u)\). The symmetry \((x,u,w)\mapsto(-x,-u,w)\) permits odd \(h\) and even \(g\). Write
\[
A=\frac ba,\qquad B=\frac{b(a^2+b^2)}{a^4},\qquad
D=\frac{b(a^2+ab^2+b^2)}{a^4}+\frac{b^3}{a^3}
=\frac{b(a^2+2ab^2+b^2)}{a^4}.
\]
The invariance equations are
\[
h'(u)(-h(u)g(u))=-ah(u)+bu+ug(u),\qquad
g'(u)(-h(u)g(u))=-g(u)+h(u)u.
\]
Matching coefficients through degree four gives
\[
h(u)=Au+Bu^3+O(u^5),\qquad
g(u)=Au^2+Du^4+O(u^6).
\]
(The second displayed expression for \(D\) is purely algebraic; the last equality is the defining simplest form.) The center equation is therefore
\[
\dot u=-h(u)g(u)=-k u^3-\ell u^5+O(u^7),
\qquad k=\frac{b^2}{a^2},\quad
\ell=\frac{2b^2(a^2+ab^2+b^2)}{a^5}>0.
\]
For each sufficiently small nonzero center solution, \(u(t)\) retains its sign and decreases to zero in modulus. Put \(R=u^{-2}\), obtaining
\[
\dot R=2k+\frac{2\ell}{R}+O(R^{-2}).
\]
First \(R/(2kt)\to1\). Substitution back into this equation gives \(R=2kt+O(\log t)\). Since
\[
\frac{2\ell}{R}-\frac{\ell}{kt}=O\!\left(\frac{\log t}{t^2}\right),
\]
the derivative of \(R-2kt-(\ell/k)\log t\) is integrable. Thus its limit \(C\) exists and
\[
\frac{\ell}{k}=\frac{2(a^2+ab^2+b^2)}{a^3}=L.
\]

**5. From center trajectories to all initial conditions.** The smooth center-manifold theorem with its local exponentially tracking stable foliation applies because the two transverse eigenvalues are strictly negative. Every sufficiently small forward trajectory is exponentially close to a center-manifold trajectory; the points whose associated center trajectory is stationary form precisely the local two-dimensional strong-stable manifold. Every global trajectory eventually enters this neighborhood by Step 3. For nonexceptional trajectories the tracked center solution is nonzero and decays as \(t^{-1/2}\); exponential tracking changes its inverse square by \(o(1)\), so the same full expansion and limits hold for the physical coordinate \(y(t)\). Exceptional trajectories converge exponentially by the strong-stable manifold theorem. The global exceptional set is a countable union of inverse images (where defined) of a local smooth two-dimensional manifold under smooth finite-time flow maps, so it has three-dimensional Lebesgue measure zero.

**6. Necessity of the boundary.** If \(c<b\), Step 1 supplies two equilibria other than \(E_c\), already disproving global attraction to \(E_c\). More strongly, at \(E_c\) the characteristic polynomial of the planar linearization is \(\lambda^2+a\lambda-c(b-c)\), which has one positive root. Thus \(E_c\) is unstable and cannot attract all initial conditions. Together with Steps 2–3 this proves the claimed if-and-only-if boundary.

## Verification

Run `python verify.py` with SymPy, NumPy and SciPy available. This checks the exact weighted Lyapunov derivative, the critical cancellation, five-jet invariance residuals, the logarithmic coefficient, equilibrium coordinates and several independent finite numerical trajectories. The symbolic computations verify polynomial identities; global LaSalle arguments, infinite-time asymptotics and manifold statements are established in the proof and **not** by finite samples. At three positive parameter pairs the numerical remainder after subtracting the exact linear and logarithmic clocks changes only by \(0.01\)–\(0.05\) between times \(3000\) and \(4000\), consistent with a finite limit. The executable has no dependence on any external research record.

## Relationship to prior work

Yan, Liu, Jie and Hong introduced the displayed three-dimensional ODE, computed equilibria and local stability, and studied chaotic trajectories, switching variants and implementations. Their open-access article does not state the sharp global attraction criterion, its closed critical endpoint, the complete strong-stable exception, or the five-jet logarithmic relaxation coefficient. Standard LaSalle and center-manifold theorems are necessary tools, but do not supply these parameter-specific identities or the exact global result. Nearby results for the classical Lorenz and other modified Lorenz-type flows have distinct vector fields and cannot be substituted merely by matching a pitchfork or an inverse-square decay mechanism. A literature search is not a proof of absolute publication priority.

## Limitations

No assertion about global attractors, chaos or periodic orbits is made for \(c<b\), except the explicit existence of the two noncentral equilibria and local instability of \(E_c\). The exceptional global stable manifold is asserted to be immersed and measure zero, not globally a single graph. The asymptotic expansion is for each fixed \(a,b>0\) at \(c=b\); no uniformity as parameters tend to zero or infinity is claimed. Independent mathematical validation and a complete exhaustive literature priority examination have not been performed.

## References

1. M. Yan, X. Liu, J. Jie, Y. Hong, “Construction and implementation of wide range parameter switchable chaotic system,” *Scientific Reports* **14**, 4059 (2024), first online 2024-02-19, DOI: 10.1038/s41598-024-54458-2. https://www.nature.com/articles/s41598-024-54458-2
2. J. Carr, “Center Manifold,” *Scholarpedia* **1**(12), 1826 (2006), DOI: 10.4249/scholarpedia.1826. https://www.scholarpedia.org/article/Center_manifold_theorem
3. The classical LaSalle invariance and smooth center/stable-manifold theorems, used solely in their standard finite-dimensional forms as stated in the proof.
