# Sharp logarithmic sorting-error law for periodically reoriented Brownian colloids

## Finding

In a passive planar Brownian-colloid model with translation–rotation mobility coupling and deterministic orientation-only resets, the complete one-cycle displacement distribution factors into an angular endpoint term and an independent isotropic Gaussian. This factorization yields an exact large-deviation exponent for classifying two oppositely coupled colloid species by displacement sign. In the physically natural isotropic-Schur-complement family, the error exponent diverges **logarithmically**, rather than as an inverse diffusivity, as residual translation noise vanishes.

Write \(\vartheta=k_{\mathrm B}T\), and let \(c,\kappa,\tau,\vartheta>0\) and \(h\in\mathbb R^2\setminus\{0\}\). Suppose the body-frame mobility is
\[
\mu=\begin{pmatrix}\kappa I_2+hh^{\mathsf T}/c&h\\h^{\mathsf T}&c\end{pmatrix},
\quad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\quad u=-Jh/c,\quad a=\|u\|,\quad e=u/a.
\]
For angular resets to zero at every time \(j\tau\) without resetting position, put \(z=\vartheta c\tau\) and \(\epsilon=\vartheta\kappa\tau/a^2\). For every integer \(j\ge0\), the one-cycle displacements \(\Delta X_j=X_{(j+1)\tau}-X_{j\tau}\) are independent and identically distributed, with
\[
\Delta X_j\ \overset{d}=\ (R_{\Theta}-I_2)u+\sqrt{2\vartheta\kappa\tau}\,G,
\quad \Theta\sim N(0,2z),\quad G\sim N(0,I_2),\quad \Theta\perp G.
\tag{1}
\]
In particular, their longitudinal normalized projections obey
\[
Y_j=\frac{e\cdot\Delta X_j}{a}\ \overset{d}=\ \cos\Theta-1+\sqrt{2\epsilon}\,Z,
\qquad Z\sim N(0,1),\quad Z\perp\Theta.
\tag{2}
\]
Define the modified Bessel functions \(I_m\), and
\[
B_z(q)=I_0(q)+2\sum_{m=1}^{\infty}e^{-m^2z}I_m(q),
\qquad H_z=1+2\sum_{m=1}^{\infty}e^{-m^2z}.
\tag{3}
\]
For every fixed \(\epsilon,z>0\), the wrong-direction classification probability satisfies the **exact positive rate**
\[
\lim_{n\to\infty}-\frac{1}{n\tau}\log
\Pr\!\left(e\cdot(X_{n\tau}-X_0)\ge0\right)
=\mathcal L_\tau(\epsilon,z)
=\frac1\tau\sup_{q\ge0}\{q-\epsilon q^2-\log B_z(q)\}.
\tag{4}
\]
The supremum is attained at a unique \(q_*(\epsilon,z)>0\). For every fixed \(z>0\), as \(\epsilon\downarrow0\),
\[
q_*(\epsilon,z)\sqrt\epsilon\longrightarrow\frac12,
\qquad
\boxed{\displaystyle
\mathcal L_\tau(\epsilon,z)=\frac1{4\tau}\log\frac1\epsilon
-\frac1\tau\left[\frac14+\log\!\left(\frac{H_z}{\sqrt\pi}\right)\right]
+o_z(1)/\tau.}
\tag{5}
\]
This is an iterated limit: first \(n\to\infty\) at fixed positive \(\kappa\), and then \(\kappa\downarrow0\) with \(z,a,\tau\) fixed. Opposite couplings \(h\) and \(-h\), with identical \(c,\kappa,\vartheta,\tau\), have equal sign-misclassification rates when separated along \(e\).

## Assumptions and scope

The mobility is symmetric positive definite because its rotational entry \(c\) and translational Schur complement \(\kappa I_2\) are strictly positive. Between resets, the position \(X\in\mathbb R^2\) and unwrapped angle \(\phi\in\mathbb R\) follow the passive, force-free, **Stratonovich** mobility equation
\[
\begin{pmatrix}dX\\d\phi\end{pmatrix}
=\sqrt{2\vartheta}\,
\begin{pmatrix}R_\phi&0\\0&1\end{pmatrix}\mu^{1/2}\circ dW,
\quad R_\phi=\begin{pmatrix}\cos\phi&-\sin\phi\\\sin\phi&\cos\phi\end{pmatrix},
\tag{6}
\]
where \(W\) is standard three-dimensional Brownian motion; each reset changes only \(\phi\) to zero, instantaneously and without spatial displacement. The construction is mathematical for every indicated positive parameter and does not assert that all real colloid shapes have isotropic Schur complement. No external forces, excluded-volume interactions, or imperfect angle resetting are included. The initial spatial point \(X_0\) is arbitrary and deterministic; each cycle starts at angle zero.

## Proof

**1. Orthogonalize the mobility noise.** By Gaussian covariance factorization, equation (6) has exactly the same Stratonovich law as
\[
d\phi=\sqrt{2\vartheta c}\,dB_0,
\qquad dX=R_\phi\frac hc\circ d\phi
+\sqrt{2\vartheta\kappa}\,R_\phi\,dB_2,
\tag{7}
\]
where scalar \(B_0\) and planar \(B_2\) are independent Brownian motions. More precisely, the constant factor \(L=\begin{pmatrix}h/\sqrt c&\sqrt\kappa I_2\\\sqrt c&0_{1\times2}\end{pmatrix}\) satisfies \(LL^{\mathsf T}=\mu\), so \(L=\mu^{1/2}O\) for a **constant** orthogonal matrix \(O\). A constant rotation of the driving Wiener process therefore preserves the entire Stratonovich law, not just instantaneous covariance. Here \(dB_2\) is simultaneously an Itô and Stratonovich differential since the integrand depends only on independent \(B_0\).

**2. Integrate the angular coupling and identify the independent Gaussian.** The identity \(Ju=h/c\) gives the Stratonovich chain rule
\[
d(R_\phi u)=R_\phi Ju\circ d\phi=R_\phi h/c\circ d\phi.
\]
Thus over a cycle started at \(\phi=0\),
\[
\Delta X=(R_{\phi_\tau}-I_2)u
+\sqrt{2\vartheta\kappa}\int_0^\tau R_{\phi_s}\,dB_2(s).
\tag{8}
\]
Conditional on the *entire* angular path, the stochastic integral in (8) is a centered planar Gaussian with deterministic covariance \(\int_0^\tau R_{\phi_s}R_{\phi_s}^{\mathsf T}ds=\tau I_2\). Its conditional characteristic function is independent of that path, proving its independence from \(\phi_\tau\), not merely lack of covariance. Meanwhile \(\phi_\tau\sim N(0,2\vartheta c\tau)\), giving (1) and (2). Fresh Brownian increments and identical angular resets establish independence across cycles.

The joint one-cycle characteristic function, with no unproved Gaussianization assumption, is
\[
\mathbb E\bigl[e^{i k\cdot\Delta X}\bigr]
=e^{-\vartheta\kappa\tau\|k\|^2}\;
\mathbb E_{\Theta}\bigl[e^{i k\cdot(R_\Theta-I_2)u}\bigr]
\qquad (k\in\mathbb R^2).
\tag{9}
\]
For the orthogonal unit vector \(e_\perp=Je\), direct trigonometric integration also gives
\[
\mathbb E\Delta X=(e^{-z}-1)u,
\quad\operatorname{Var}(e\cdot\Delta X)
=\frac{a^2}{2}(1-e^{-2z})^2+2\vartheta\kappa\tau,
\quad\operatorname{Var}(e_\perp\cdot\Delta X)
=\frac{a^2}{2}(1-e^{-4z})+2\vartheta\kappa\tau,
\tag{10}
\]
with vanishing longitudinal–transverse covariance. These covariance formulas are auxiliary consequences, not a claim about every anisotropic mobility.

**3. Derive the large-deviation exponent.** For \(q\ge0\), the Fourier–Bessel series
\(e^{q\cos t}=I_0(q)+2\sum_{m\ge1}I_m(q)\cos(mt)\), together with \(\mathbb E\cos(m\Theta)=e^{-m^2z}\), gives
\[
\Lambda_{\epsilon,z}(q):=\log\mathbb E e^{qY}
=\epsilon q^2-q+\log B_z(q).
\tag{11}
\]
The series converges absolutely at every fixed \(q,z>0\). Since \(\Lambda'(0)=e^{-z}-1<0\), while \(\Lambda'(q)\to\infty\) as \(q\to\infty\) for \(\epsilon>0\), the minimizer of \(\Lambda\) is positive. Strict convexity follows from \(\Lambda''(q)=\operatorname{Var}_{q}(\cos\Theta-1)+2\epsilon>0\), proving uniqueness of \(q_*\).

Exponential Markov inequality yields the upper bound on the event in (4). For the matching bound, tilt each independent increment by \(e^{q_*Y-\Lambda(q_*)}\). Under the tilted law \(Y\) has mean zero and finite strictly positive variance. The central limit theorem shows that the event \(0\le n^{-1}\sum_{j<n}Y_j\le\delta\) has non-exponentially-small tilted probability for every \(\delta>0\). Undoing the tilt bounds the original probability below by \(\exp\{n\Lambda(q_*)-nq_*\delta\}\) times a subexponential factor. Letting \(\delta\downarrow0\) establishes (4) without assuming an unproved large-deviation lemma.

**4. Sharp weak-residual limit.** The wrapped Gaussian angle on \([-\pi,\pi]\) has strictly positive smooth density
\[
w_z(t)=\frac1{2\pi}\left(1+2\sum_{m\ge1}e^{-m^2z}\cos(mt)\right),
\qquad w_z(0)=\frac{H_z}{2\pi}>0.
\]
Set \(A_z(q)=e^{-q}B_z(q)=\int_{-\pi}^{\pi}e^{-q(1-\cos t)}w_z(t)\,dt\). The phase \(1-\cos t\) has its unique nondegenerate minimum at zero on this integration interval. The ordinary one-dimensional Laplace method, including differentiation under the integral and a Gaussian-dominated remainder, gives, for each fixed \(z>0\),
\[
A_z(q)=\frac{H_z}{\sqrt{2\pi q}}\bigl(1+O_z(q^{-1})\bigr),
\quad \frac{d}{dq}\log A_z(q)=-\frac1{2q}+O_z(q^{-2}).
\tag{12}
\]
Consequently \(\Lambda(q)=\epsilon q^2-\tfrac12\log q+\log(H_z/\sqrt{2\pi})+O_z(q^{-1})\). For every finite \(q\), \(d\log A_z(q)/dq<0\) since \(1-\cos\Theta>0\) almost surely; therefore the unique minimizer \(q_*(\epsilon,z)\to\infty\) as \(\epsilon\downarrow0\). Its critical equation and (12) imply
\[
2\epsilon q_*=\frac1{2q_*}+O_z(q_*^{-2}),
\qquad \epsilon q_*^2\to\frac14.
\]
Substitution into (11), using \(\log q_*=-\tfrac12\log\epsilon-\log2+o(1)\), yields (5), including its constant term. For \(\kappa=0\) exactly, every longitudinal cycle increment is nonpositive almost surely, so misclassification is impossible; this boundary case is not assumed positive definite.

**5. Opposite-coupling sorting.** Replacing \(h\) by \(-h\) changes \(u\) to \(-u\) and reverses the angular endpoint displacement, while retaining the isotropic Gaussian's law. Thus the complete displacement law is reflected through the origin. The separating line orthogonal to \(e\) has identical wrong-sign probabilities for either species, as asserted.

## Verification

The standalone `verify.py` uses independent Fourier–Bessel summation and angular quadrature (12 comparisons), numerically checks the asymptotic optimizer and rate (3 parameter tests), and directly Euler–Itô simulates the original correlated three-coordinate Brownian equation (longitudinal and transverse means/variances). All checks passed. The simulated paths do not use the endpoint-factorization formula to construct their increments. The exact infinite-particle-cycle rate and the singular-limit asymptotics are established analytically above; finite simulations alone do not prove either limit.

To rerun with Python 3, NumPy, and SciPy installed, execute `python verify.py` from the same directory; the script has no input datasets or network dependencies.

## Relationship to prior work

Cleuren and Eichhorn's *Sorting by Resetting* (arXiv:2603.19430v1, publicly posted 2026-03-19), Section (ii), supplies the parent translation–rotation-coupled Langevin mobility model, the deterministic angle-only reset protocol, and the average current (its Eq. (8)); the first moment of (10) agrees exactly with that equation. The inspected complete primary text and appendix do not state the independent Gaussian decomposition, the one-cycle full displacement law, an exact sign-error large-deviation variational formula, or the weak-Schur-complement logarithmic exponent and constant.

Chaki, Olsen and Löwen's *Anisotropic Brownian particles under resetting* (arXiv:2406.17550v2, Section II and V) studies anisotropic translation with **independent** rotational Brownian motion and Poissonian orientation resets. Its Gaussian late-time limit and effective diffusion tensor do not imply the nonzero mean or rare-event law induced here by **instantaneously cross-correlated translation–rotation noise**. General convex large-deviation and Laplace principles are proof tools, not the specific coupled-colloid statement. Searches of related published research records did not identify equivalent parameterized coverage; these negative results are not a proof of novelty.

## Limitations

The exact sharp rate is proved for an isotropic residual translational Schur complement \(\kappa I_2\), for independent thermal Brownian forcing, perfectly periodic resets to a fixed angle, and a fixed nonzero translation–rotation coupling. General anisotropic residual mobility, interactions, inertia, external forcing, finite-time optimal sorting thresholds, reset imprecision, and simultaneous limits in cycle number and residual noise are not classified. The limit \(\kappa\downarrow0\) approaches the boundary of positive definite mobility; no claim is made of a physically realizable singular hydrodynamic particle. Further undiscovered or implicit coverage by broad stochastic-flow or large-deviation literature remains possible.

## References

1. Bart Cleuren and Ralf Eichhorn, *Sorting by Resetting*, arXiv:2603.19430v1 (2026-03-19), especially Section (ii) and Appendix B: https://arxiv.org/html/2603.19430v1
2. Subhasish Chaki, Kristian Stølevik Olsen and Hartmut Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550v2 (2024), especially Sections II and V: https://arxiv.org/html/2406.17550v2
3. Standard mathematical tools used explicitly in the proof: the Fourier–Bessel expansion, the central limit theorem under exponential tilting, and the one-dimensional Laplace method. No result in these general tools is asserted as new.
