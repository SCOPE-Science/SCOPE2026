# Parabolic confinement of bounded complete trajectories in a Lorenz-like flow
## Finding
Consider the Lorenz-like flow
\[
\dot x=a(y-x),\qquad \dot y=-dx+cy-xz,\qquad \dot z=-bz+fx^2+gxy.
\]
Assume \(a>0\), \(b>0\), \(f,g\ge 0\), \(f+g>0\), and define
\[
\kappa=f+g-\frac{bg}{2a}.
\]
If \(\kappa>0\), every bounded complete trajectory is either the equilibrium origin or obeys
\[
z(t)>\frac{g}{2a}x(t)^2\qquad\text{for every }t\in\mathbb R.
\]
Equivalently, the transformed height
\[
W=z-\frac{g}{2a}x^2
\]
has the exact representation
\[
W(t)=\kappa\int_0^\infty e^{-bs}x(t-s)^2\,ds.
\]
Therefore every compact invariant set \(K\) satisfies
\[
K\subseteq\{0\}\cup\left\{(x,y,z):z>\frac{g}{2a}x^2\right\}.
\]

## Assumptions and scope
The statement concerns classical complete solutions of the printed autonomous system. The parameters \(c\) and \(d\) are arbitrary real numbers; the confinement depends only on the first and third equations. Bounded completeness is essential for removing the backward homogeneous term. The theorem does not assert existence, uniqueness, or chaos of a non-equilibrium compact invariant set.

## Proof
Set \(W=z-gx^2/(2a)\). Direct differentiation along the vector field gives
\[
\dot W
=-bz+fx^2+gxy-\frac{g}{a}x\,a(y-x)
=-bW+\left(f+g-\frac{bg}{2a}\right)x^2
=-bW+\kappa x^2.
\]
For a bounded complete trajectory and any \(T>0\), variation of constants yields
\[
W(t)=e^{-bT}W(t-T)+\kappa\int_0^T e^{-bs}x(t-s)^2\,ds.
\]
Because \(b>0\) and \(W\) is bounded, the first term tends to zero as \(T\to\infty\). Hence
\[
W(t)=\kappa\int_0^\infty e^{-bs}x(t-s)^2\,ds\ge0.
\]
If equality holds at some time, continuity and \(\kappa>0\) force \(x(t-s)=0\) for every \(s\ge0\). The first equation then gives \(y=0\) on the whole past half-orbit. The third equation reduces there to \(\dot z=-bz\); boundedness as time tends to \(-\infty\) forces \(z=0\). The trajectory therefore reaches the origin, and uniqueness makes it the equilibrium trajectory for all time. Every other bounded complete trajectory has \(W(t)>0\) for every \(t\), proving the strict parabolic confinement. Every point of a compact invariant set lies on a bounded complete trajectory, which gives the set inclusion.

## Verification
The standalone checker `verify.py` expands the defining polynomial identity after clearing the denominator \(2a\) and verifies exact equality of all multivariate coefficients. The memory formula and strictness are analytical consequences of variation of constants, positivity of \(e^{-bs}\), and uniqueness; no finite numerical experiment is used as a substitute for the proof.

## Relationship to prior work
Li, Zhao, and Geng introduce the displayed eight-term Lorenz-like system and analyze equilibria, local manifolds, Hopf bifurcations, dynamics at infinity, and infinite heteroclinic orbits. Their full text does not state the transformed-height memory identity or the resulting pointwise parabolic confinement.

The earlier Li–Ou system has the same first and third equations but a different second equation. Li and Ou prove, under \(a>d\) and \(bg>2a(f+g)\), a Lyapunov theorem forcing convergence to equilibria and excluding closed orbits. That condition is exactly the opposite strict sign, \(\kappa<0\), from the present theorem. A later Wang–Li follow-up highlights the boundary \(bg=2a(f+g)\), corresponding to \(\kappa=0\), for a heteroclinic-orbit result. Thus those same-family results do not imply the \(\kappa>0\) pointwise confinement proved here.

## Limitations
The result is conditional on \(b>0\) and \(\kappa>0\). It gives a necessary geometric condition for bounded complete recurrence, not a sufficient condition for any recurrent set to exist. It does not classify dynamics on the complementary parameter regimes \(\kappa\le0\), and it does not by itself validate numerical Lyapunov exponents or prove the existence of a chaotic attractor.

## References
1. Y. Li, M. Zhao, F. Geng, “Dynamical Analysis and Simulation of a New Lorenz-Like Chaotic System,” *Mathematical Problems in Engineering* (2021), Article 6669956, DOI 10.1155/2021/6669956. Published 16 March 2021.
2. X. Li, Q. Ou, “Dynamical properties and simulation of a new Lorenz-like chaotic system,” *Nonlinear Dynamics* 65 (2011), 255–270, DOI 10.1007/s11071-010-9887-z.
3. H. Wang, X. Li, “Hopf bifurcation and new singular orbits coined in a Lorenz-like system,” *Journal of Applied Analysis & Computation* 8 (2018), 1307–1325, DOI 10.11948/2018.1307.
