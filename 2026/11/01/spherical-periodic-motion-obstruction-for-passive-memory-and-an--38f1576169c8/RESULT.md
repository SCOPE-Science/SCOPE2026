# Spherical periodic-motion obstruction for passive memory and an exact delayed-kernel circle

## Finding

A nontrivial positive mixture of exponential velocity-memory filters forbids every nonconstant periodic trajectory that remains on a fixed sphere in a translation-invariant self-generated radial-repulsion equation. The statement allows arbitrary periodic motion on the sphere, not only a uniformly rotating circle. This obstruction is specific to the filter shape: an explicit nonnegative, subunit-mass, delayed exponential velocity kernel admits a continuum of exact circular motions with the same type of smooth bounded, strictly decreasing radial imprint.

**Theorem (spherical rigidity).** Let \(d\ge2\), let \(w\in L^1(0,\infty)\) be nonnegative, let \(\kappa\ge0\), and let \(a:[0,\infty)\to[0,\infty)\) be continuous. Let \(\mu\) be a nonzero positive Borel measure on \((0,\infty)\) such that \(\int\beta^{-1}\,\mu(d\beta)<\infty\), and define
\[
m(s)=\int_{(0,\infty)}e^{-\beta s}\,\mu(d\beta),\qquad s>0.
\]
Then the hereditary differential equation
\[
\dot x(t)=\int_0^\infty m(s)\dot x(t-s)\,ds
+\kappa\int_0^\infty w(s)a(|x(t)-x(t-s)|)[x(t)-x(t-s)]\,ds
\tag{1}
\]
has no nonconstant \(C^1\), entire, periodic solution \(x:\mathbb R\to\mathbb R^d\) lying on a sphere \(|x(t)-c|=R\), for any \(c\in\mathbb R^d\) and \(R\ge0\).

**Explicit boundary witness.** In dimension two set
\[
\rho=\frac{\sqrt{10}}5,\quad \tau=\pi+\arctan3,\quad
m(s)=\rho e^{-(s-\tau)}\mathbf1_{[\tau,\infty)}(s),\quad
w(s)=e^{-2s},\quad\kappa=4.
\]
For \(r\ge0\), put
\[
a(r)=\begin{cases}1,&0\le r\le1,\\
\exp\!\left[-(r-1)^2e^{-1/(r-1)^2}\right],&r>1,\end{cases}
\qquad \Phi(z)=\int_{|z|}^\infty r a(r)\,dr.
\]
The radial function \(\Phi\) is bounded, smooth, and strictly decreasing with radius, and \(-\nabla\Phi(z)=a(|z|)z\). Although \(m\ge0\) and \(\int_0^\infty m(s)\,ds=\rho<1\), for **every** \(0<R\le\frac12\), the curve
\[
x_R(t)=R(\cos t,\sin t)
\]
is an exact entire period-\(2\pi\) solution of (1). In particular, positivity and subunit mass of the velocity kernel alone cannot replace the positive-exponential-mixture assumption in spherical rigidity.

## Assumptions and scope

Equation (1) uses fixed temporal weights \(m,w\), not state-dependent age weights. Complete trajectories have bounded position and bounded velocity because they are periodic, so all integrals converge absolutely. The sphere center and radius are arbitrary, and no hypothesis is made on the angular speed, planar orbit shape, or spatial dimension beyond \(d\ge2\). A mixture of exponentials is assumed with its explicit measure integrability; arbitrary positive or decreasing kernels are not covered by the prohibition. The repulsive imprint need only have nonnegative radial coefficient \(a\), not a strictly positive one, for the prohibition; the constructive witness has a strictly decreasing smooth potential. The witness's jump in the ordinary velocity-memory kernel is allowed because this kernel is integrable and nonnegative.

## Proof

**1. Positive identity for the passive velocity filters.** Translate the putative trajectory by its sphere center, \(u(t)=x(t)-c\), and write \(v=\dot u\). For each \(\beta>0\), introduce the periodic filtered position
\[
z_\beta(t)=\int_0^\infty e^{-\beta s}u(t-s)\,ds.
\]
Differentiation and integration by parts give
\[
\dot z_\beta(t)=\int_0^\infty e^{-\beta s}\dot u(t-s)\,ds
=u(t)-\beta z_\beta(t).
\]
Consequently, over one period \(T\),
\[
\int_0^T u(t)\cdot\dot z_\beta(t)\,dt
=\int_0^T|\dot z_\beta(t)|^2\,dt
+\frac\beta2[|z_\beta(T)|^2-|z_\beta(0)|^2]
=\int_0^T|\dot z_\beta(t)|^2\,dt.
\tag{2}
\]
This quantity is strictly positive for every \(\beta>0\) if \(u\) is nonconstant. Indeed \(\dot z_\beta\equiv0\) would force \(u=\beta z_\beta\) to be constant. The hypothesis \(\int\mu(d\beta)/\beta<\infty\) ensures that interchanging temporal and \(\beta\)-integrals is valid, because \(\int_0^\infty m(s)ds=\int\beta^{-1}\mu(d\beta)\).

**2. Geometric radial identity.** Since \(|u(t)|=|u(t-s)|=R\), direct polarization gives
\[
u(t)\cdot[u(t)-u(t-s)]=\frac12|u(t)-u(t-s)|^2.
\tag{3}
\]
Also \(\int_0^T u\cdot\dot u\,dt=0\). Dotting (1) with \(u(t)\), integrating over one period, and using (2) and (3), yields the **exact nonnegative sum**
\[
0=\int_{(0,\infty)}\!\left[\int_0^T|\dot z_\beta(t)|^2dt\right]\mu(d\beta)
+\frac\kappa2\int_0^\infty\!w(s)\int_0^T\! a(|u(t)-u(t-s)|)|u(t)-u(t-s)|^2\,dt\,ds.
\tag{4}
\]
The interchange is valid by the bounded periodic history and the boundedness of \(a\) on \([0,2R]\). The first summand is strictly positive for a nonconstant \(u\) because \(\mu\ne0\); the second is nonnegative. Equation (4) is impossible. This proves the first assertion.

**3. A delayed positive kernel defeats spherical rigidity.** For the specified \(m\), direct Fourier–Laplace evaluation at frequency one gives
\[
\widehat m(i)=\int_0^\infty m(s)e^{-is}ds
=\frac{\rho e^{-i\tau}}{1+i}=\frac{1+2i}{5}.
\]
For \(w(s)=e^{-2s}\), \(W_0=\int_0^\infty w(s)ds=\frac12\), and
\[
\widehat w(i)=\int_0^\infty w(s)e^{-is}ds=\frac1{2+i}=\frac{2-i}{5}.
\]
Each chord of \(x_R\) has length at most \(2R\le1\), so \(a\) equals one on every chord. Identifying the plane with \(\mathbb C\), substitute \(x_R(t)=Re^{it}\) into (1). Its right side is exactly
\[
\bigl[i\widehat m(i)+4(W_0-\widehat w(i))\bigr]x_R(t)
=\left[\frac{-2+i}{5}+\frac{2+4i}{5}\right]x_R(t)
=i x_R(t)=\dot x_R(t).
\]
The prescribed formula for \(a\) is \(C^\infty\), positive and constant on \([0,1]\), and decays rapidly for large \(r\). Hence the radial integral defining \(\Phi\) converges, \(\Phi\) is a smooth function of \(z\) (locally a constant minus \(|z|^2/2\) at the origin), and \(\Phi\) strictly decreases for each radius \(r>0\). Finally \(\int m=\rho=\sqrt{10}/5<1\). This establishes the boundary witness.

## Verification

Run `python checks/check.py` with Python 3 and SymPy installed. It checks the delayed-kernel Fourier transform, the positive mass bound, the exact angular balance, and the passive-frequency sign for one exponential filter. These exact symbolic checks complement, and do not substitute for, the general period-integrated analytic identity (4). The proof is self-contained under the stated regularity and integrability assumptions; no finite simulation asserts a general absence of orbits.

## Relationship to prior work

Vrabel, *Geometric Stability of Dynamical Systems with Self-Generated State-Space Memory*, arXiv:2610.24152v1 (first submitted 16 October 2026), introduces the nonlinear hereditary geometric force (its equations (3)–(4)), analyzes global velocity arrest and translating branches, and explicitly names geometric invariant-set stability for rotating or recurrent motions as an extension in Section 13. The present theorem treats a different invariant-set question within its fixed-weight radial subclass: a sharp qualitative contrast between positive mixtures of exponential velocity memories and a nonnegative delayed-exponential velocity memory.

Liu, Durey, and Bush, *Wave- and potential-driven instabilities in orbital pilot-wave dynamics*, Journal of Fluid Mechanics (2025), study circular motion with inertial dynamics and external confining or Coriolis forces. Their governing assumptions neither give nor contradict the pure first-order unconfined radial-memory theorem here. Sarkar, *Memory engine: Self-organized coherence from internal feedback*, Physical Review E **112** (2025), 054111, analyzes a Brownian particle with internal viscoelastic memory and presents simulations of coherent modes, not this deterministic spherical filter dichotomy. Classical passive Volterra methods motivate the positive convolution identity; originality is claimed for the fully specified geometric equation and the sharp delayed-kernel witness, not for filtering identities in isolation.

## Limitations

Only periodic trajectories lying on one fixed Euclidean sphere are excluded under the passive-mixture hypothesis. Non-spherical periodic orbits, quasiperiodic states, translating solutions, trajectories in a state-adaptive-weight model, and nonlinear stability of the delayed example are not classified. The delayed example establishes existence but not stability of any orbit. Historical priority beyond the inspected literature is not independently certified. The proof uses a nonzero positive mixture of exponential kernels; more general positive-definite kernels may also admit rigidity, but that enlargement is not claimed.

## References

1. R. Vrabel, *Geometric Stability of Dynamical Systems with Self-Generated State-Space Memory*, arXiv:2610.24152v1 (16 October 2026), https://arxiv.org/html/2610.24152v1.
2. Y. Liu, M. Durey, and J. W. M. Bush, *Wave- and potential-driven instabilities in orbital pilot-wave dynamics*, Journal of Fluid Mechanics (2025), https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/wave-and-potentialdriven-instabilities-in-orbital-pilotwave-dynamics/776B1233003763E3685990B9DE9CA22B.
3. A. Sarkar, *Memory engine: Self-organized coherence from internal feedback*, Physical Review E **112** (2025), 054111, https://doi.org/10.1103/t7nk-4p57.
4. G. Gripenberg, S.-O. Londen, and O. Staffans, *Volterra Integral and Functional Equations*, Cambridge University Press (1990), https://doi.org/10.1017/CBO9780511662805.
