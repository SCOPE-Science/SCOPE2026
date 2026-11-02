# A sharp global relaxation boundary and a supercritical Hopf lattice for a sinusoidal jerk flow

## Finding

Consider the smooth flow
\[
\dot x=y,\qquad \dot y=az,\qquad \dot z=-y-bz+c\sin(dx),\qquad a,b,c,d>0.
\]
The following statements jointly give a sharp global-to-oscillatory transition.

**Global-convergence dichotomy.** Every solution from every initial condition in \(\mathbb R^3\) converges to one equilibrium of the form \(((k\pi)/d,0,0)\), \(k\in\mathbb Z\), **if and only if** \(cd\le b\). The equality endpoint is included. For \(cd\le b\), each compactly supported invariant probability is a finite convex combination of the equilibrium point masses.

**Oscillatory emergence.** Fix \(a,b,d>0\) and put \(\mu=cd-b\). For all sufficiently small \(\mu>0\), each odd equilibrium \(((2k+1)\pi/d,0,0)\) has a unique nearby (up to phase) orbitally asymptotically stable periodic orbit. The periodic orbits for different \(k\in\mathbb Z\) are distinct, and are translates of each other by \(2\pi/d\). If \(A_k(\mu)\) is the largest absolute displacement in the \(x\) coordinate from the corresponding odd equilibrium and \(T_k(\mu)\) is the least period, then
\[
A_k(\mu)=\sqrt{\frac{8\mu}{bd^2}}+O_{a,b,d}(\mu),\qquad
T_k(\mu)=\frac{2\pi}{\sqrt a}+O_{a,b,d}(\mu^2).
\]
In particular, the first-order period shift cancels exactly.

**Global period floor.** For all positive parameters, every nonconstant periodic solution of least period \(T\) satisfies the strict, universal bound
\[
T>\frac{2\pi}{\sqrt a}.
\]
The bound is optimal over this family because the small Hopf cycles approach it as \(cd\downarrow b\) from above. No claim is made that periodic orbits exist for every \(cd>b\).

## Assumptions and scope

The phase space is all of \(\mathbb R^3\), not just a numerical window or a compact absorbing set. All parameters \(a,b,c,d\) are strictly positive. The sine term and its derivative are bounded, so the vector field is globally Lipschitz and the flow exists for every real time. The translation \(x\mapsto x+2\pi/d\) is an exact symmetry. "Converges to an equilibrium" means ordinary Euclidean convergence to a single point, which may depend on the initial condition. A compactly supported invariant probability is an invariant Borel probability whose support is compact in \(\mathbb R^3\). The Hopf asymptotics hold at fixed \(a,b,d\), as \(\mu\downarrow0\), and not uniformly across arbitrary parameter degenerations.

## Proof

### 1. An exact strict Lyapunov identity

Set
\[
\begin{aligned}
\mathcal P(x,y,z)={}&-\frac12\left(1+\frac{b^2}{a}\right)y^2-byz-\frac a2z^2\\
&+cy\sin(dx)-\frac{bc}{d}\cos(dx).
\end{aligned}
\]
Direct differentiation along the displayed vector field gives the **exact identity**
\[
\boxed{\dot{\mathcal P}=(b+cd\cos(dx))y^2.}
\tag{1}
\]
For transparency, this can be reconstructed from the two simpler exact derivatives
\[
\begin{aligned}
\frac{d}{dt}\left(cy\sin(dx)-\frac12y^2-\frac a2z^2\right)
&=abz^2+cd\cos(dx)y^2,\\
\frac{d}{dt}\left(yz+\frac{b}{2a}y^2+\frac cd\cos(dx)\right)
&=az^2-y^2.
\end{aligned}
\]
Subtracting \(b\) times the second bracket from the first yields (1).

The symmetric quadratic form
\[
\begin{pmatrix}1+b^2/a&b\\ b&a\end{pmatrix}
\]
has positive first principal minor and determinant exactly \(a>0\). Consequently, \(\mathcal P\) is uniformly bounded above and tends to minus infinity when \(y^2+z^2\to\infty\), uniformly in \(x\). It is periodic in \(x\) with period \(2\pi/d\).

When \(cd\le b\), identity (1) says \(\dot{\mathcal P}\ge0\). Along each forward trajectory, \(\mathcal P\ge\mathcal P(x_0,y_0,z_0)\). Coercivity bounds \(y\) and \(z\) for all forward time. Passing to the quotient cylinder \((\mathbb R/(2\pi/d)\mathbb Z)\times\mathbb R^2\) makes the orbit precompact, and \(\mathcal P\) descends to a bounded, nondecreasing Lyapunov function there.

The largest invariant subset of \(\{\dot{\mathcal P}=0\}\) consists precisely of equilibria, **including at the critical endpoint**. Indeed, if \(cd<b\), equality forces \(y=0\). If \(cd=b\), equality says \((1+\cos(dx))y^2=0\). Along an orbit entirely in that equality set, \(y\ne0\) on an open time interval would force \(\cos(dx)=-1\) there, hence \(x\) constant there, contradicting \(\dot x=y\ne0\). Thus in either case \(y\equiv0\), then \(z\equiv0\) from \(\dot y=az\), and finally \(\sin(dx)=0\) from \(\dot z\). The equilibria on the quotient circle are just its even and odd classes.

LaSalle's invariance principle now confines every omega-limit set on the compactified cylinder to those two isolated equilibria. An omega-limit set of a precompact continuous-time forward orbit is connected, so it consists of one of them. Hence the quotient orbit converges to one equilibrium class. Once the periodic coordinate stays in a small neighborhood of one class for all sufficiently large times, its real lift cannot change winding number (doing so would leave that neighborhood). Therefore the original \(x\)-coordinate also converges to a single lift \(k\pi/d\), and \(y,z\to0\). This proves convergence **for every initial condition**, not merely for bounded starting neighborhoods.

If \(\nu\) is a compactly supported invariant probability, invariance and (1) imply \(\int(b+cd\cos(dx))y^2\,d\nu=0\). The preceding invariant-set argument forces its support onto equilibria. Compactness leaves only finitely many such points, proving the measure assertion.

### 2. Necessity of the closed boundary

At \(E_k=(k\pi/d,0,0)\), the Jacobian is
\[
J_k=\begin{pmatrix}0&1&0\\0&0&a\\(-1)^kcd&-1&-b\end{pmatrix}.
\]
Even equilibria have characteristic polynomial \(\lambda^3+b\lambda^2+a\lambda-acd\), so one eigenvalue is positive. Odd equilibria have polynomial \(\lambda^3+b\lambda^2+a\lambda+acd\), which by the cubic Routh–Hurwitz criterion has all eigenvalues in the open left half-plane exactly when \(cd<b\). At \(cd=b\), it factors as \((\lambda+b)(\lambda^2+a)\). For \(cd>b\), the odd equilibria have two eigenvalues with positive real part; neither type has eigenvalues on the imaginary axis. Thus **every equilibrium** is hyperbolically unstable when \(cd>b\).

The initial conditions converging to any particular hyperbolically unstable equilibrium lie in its global stable manifold, an immersed submanifold of dimension at most two, hence a set of three-dimensional Lebesgue measure zero. A countable union of these sets cannot cover \(\mathbb R^3\). Therefore not every solution converges to an equilibrium for \(cd>b\). This proves necessity without assuming the existence of a global attractor on that side.

### 3. Nondegenerate simultaneous supercritical Hopf bifurcations

At every odd equilibrium, translate \(u=x-(2k+1)\pi/d\) and use \(\mu=cd-b\). The third equation becomes
\[
\dot z=-y-bz-\frac{b+\mu}{d}\sin(du)
=-y-bz-(b+\mu)u+\frac{(b+\mu)d^2}{6}u^3+O(u^5).
\]
At \(\mu=0\), the eigenvalues are \(-b,\pm i\omega\), \(\omega=\sqrt a\). Choose the critical right eigenvector and normalized left spectral functional
\[
q=(1,i\omega,-1)^{\mathsf T},\qquad
\ell^{\mathsf T}q=1,\quad \ell^{\mathsf T}J=i\omega\ell^{\mathsf T},\quad
\ell_3=-\frac{a+ib\omega}{2(a+b^2)}.
\]
The linear eigenvalue crossing derivative and the complex resonant cubic coefficient in the coordinate \(u=w+\bar w+O(|w|^2)\) are respectively
\[
L=\left.\frac{d\lambda}{d\mu}\right|_0
=\frac{a+ib\omega}{2(a+b^2)},\qquad
\Gamma=\frac{bd^2}{2}\ell_3
=-\frac{bd^2(a+ib\omega)}{4(a+b^2)}.
\]
The cubic coefficient follows by projecting the \(3w^2\bar w\) harmonic of \((bd^2/6)(w+\bar w)^3\); there are no quadratic nonlinearities at this equilibrium, so there are no quadratic normal-form corrections. Both crucial signs are strict:
\[
\operatorname{Re}L=\frac{a}{2(a+b^2)}>0,
\qquad \operatorname{Re}\Gamma=-\frac{abd^2}{4(a+b^2)}<0.
\]
The ordinary nondegenerate Hopf theorem therefore supplies a unique nearby stable limit cycle for sufficiently small \(\mu>0\), and none on the opposite side near the equilibrium. The radial normal-form balance gives
\[
|w|^2=-\frac{\operatorname{Re}L}{\operatorname{Re}\Gamma}\mu+O(\mu^2)
=\frac{2\mu}{bd^2}+O(\mu^2).
\]
Because the physical \(u\) coordinate begins with \(w+\bar w\), the leading maximum displacement is twice \(|w|\), proving the stated amplitude with the conservative \(O(\mu)\) error.

The first frequency correction vanishes **exactly**:
\[
\operatorname{Im}L+
\frac{2}{bd^2}\operatorname{Im}\Gamma=0.
\]
Smooth Hopf expansions thus give angular frequency \(\omega+O(\mu^2)\) and period \(2\pi/\omega+O(\mu^2)\). Translation by \(2\pi/d\) reproduces the locally stable cycle about every odd equilibrium, yielding infinitely many distinct cycles.

### 4. A universal strict period lower bound

For any nonconstant periodic solution of least period \(T\), the exact derivative
\[
\frac{d}{dt}\left(yz+\frac{b}{2a}y^2+\frac cd\cos(dx)\right)=az^2-y^2
\]
implies \(\int_0^T y^2\,dt=a\int_0^T z^2\,dt\). Also \(\int_0^T y\,dt=x(T)-x(0)=0\) and \(y'=az\). Periodic Wirtinger's inequality therefore gives
\[
\left(\frac{2\pi}{T}\right)^2\int_0^T y^2\,dt
\le\int_0^T (y')^2\,dt
=a\int_0^T y^2\,dt.
\]
Nonconstancy makes the last integral positive, proving \(T\ge2\pi/\sqrt a\). If equality held, \(y\) would be a first harmonic and \(x(t)=x_*+R\sin(2\pi t/T+\theta)\) for \(R>0\). Then \(z=y'/a\) is a first harmonic, and the third differential equation forces \(\sin(dx(t))\) to be a first-harmonic trigonometric polynomial. Because \(\sin(d(x_*+Rv))\) would then be affine in \(v\in[-1,1]\), its second derivative in \(v\), namely \(-d^2R^2\sin(d(x_*+Rv))\), would have to vanish identically. That is impossible when \(d,R>0\). Thus equality cannot hold. The Hopf cycles show the strict lower bound is nevertheless the optimal family-wide infimum.

## Verification

The accompanying `verify.py` checks by exact symbolic differentiation the boxed Lyapunov identity, positive definiteness via its determinant, the normalized Hopf eigenvectors, the crossing and cubic coefficients, the amplitude constant, and the vanishing first-order frequency correction. Additional high-accuracy ODE integrations confirm the small-cycle amplitude and period for two sample positive values of \(\mu\) and subcritical relaxation for two parameter samples. Run with `python verify.py` using SymPy, NumPy and SciPy. These finite calculations support the algebra but do not replace the global LaSalle argument, the Hopf theorem, or the strict period proof.

## Relationship to prior work

Li and Zeng [1], Equation (1), introduce precisely this sine-jerk flow and investigate equilibria, numerical bifurcations, multiple coexisting scrolls, initial-value dependence, and circuit realization. The inspected original article gives the equilibrium Jacobian and selected numerical eigenvalues; it does not derive the global closed parameter threshold, its coercive Lyapunov identity, the all-site supercritical Hopf coefficient, the vanishing first-order period shift, or the universal sharp periodic-time bound. The approach uses standard invariant-set and Hopf tools [2,3], rather than claiming either general theorem as new. General third-order feedback and other jerk-system period constraints are methodologically related but involve different nonlinearities and do not directly provide the simultaneous exact conclusions for this sine-jerk family.

## Limitations

The boundary characterizes global convergence **to some equilibrium**, not uniform convergence to one common equilibrium. Above the boundary, the theorem proves lack of universal equilibrium convergence for every parameter but constructs stable periodic cycles only sufficiently close to it. It does not classify high-amplitude attractors, all periodic orbits, transient time scales, noise-perturbed circuits, or basin boundaries. The sharp period floor is a family-wide infimum, not achieved by any nonconstant orbit. The literature comparison is necessarily subject to unindexed or inaccessible prior work; independent mathematical validation has not been performed.

## References

[1] F. Li and J. Zeng, "Multi-Scroll Attractor and Multi-Stable Dynamics of a Three-Dimensional Jerk System," *Energies* **16** (2023), 2494; published 6 March 2023. DOI: `10.3390/en16052494`.

[2] J. K. Hale, *Ordinary Differential Equations*, 2nd edition, Robert E. Krieger, 1980 (invariant-set and stability principles).

[3] Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, 3rd edition, Springer, 2004 (nondegenerate Hopf bifurcation and normal forms).
