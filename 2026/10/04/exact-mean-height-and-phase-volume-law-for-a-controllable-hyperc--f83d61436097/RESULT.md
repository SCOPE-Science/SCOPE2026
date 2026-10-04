# Exact mean-height and phase-volume law for a controllable hyperchaotic hidden-attractor flow
## Finding
Consider the smooth four-dimensional system
\[
\dot x=-ay-xz-u,\qquad
\dot y=x(z-c),\qquad
\dot z=-b-mxy,\qquad
\dot u=kx-y.
\]
For \(b\ne0\), define
\[
R=m y^2+(z-c)^2.
\]
Then every classical solution satisfies the exact identity
\[
\dot R=-2b(z-c).
\]
Therefore, for every \(T>0\) for which the solution exists,
\[
\frac1T\int_0^T z(t)\,dt
=c-\frac{R(T)-R(0)}{2bT}.
\]
In particular, every bounded forward solution obeys
\[
\lim_{T\to\infty}\frac1T\int_0^T z(t)\,dt=c,
\]
and every compactly supported invariant probability measure \(\mu\) satisfies \(\int z\,d\mu=c\).

The divergence of the vector field is \(-z\). Thus Liouville's formula sharpens to
\[
\log |\det D\phi_T|
=-\int_0^T z(t)\,dt
=-cT+\frac{R(T)-R(0)}{2b}.
\]
Hence every bounded forward orbit has asymptotic phase-volume rate \(-c\). For every compactly supported ergodic invariant probability measure for which the Lyapunov spectrum is defined,
\[
\lambda_1+\lambda_2+\lambda_3+\lambda_4=-c.
\]
Every periodic orbit therefore has exact period mean \(c\) in the \(z\)-coordinate.

## Assumptions and scope
The identities hold for real parameters and classical solutions of the printed polynomial ODE, with \(b\ne0\). Bounded-forward conclusions require the trajectory to remain bounded; no claim is made that all initial data are globally bounded. The invariant-measure statement assumes compact support, which makes the polynomial observables integrable. The Lyapunov-sum conclusion is for invariant measures where the usual Oseledets spectrum is defined. The source's examples use positive \(b\) and \(m\), but positivity of \(m\) is not needed for the algebraic identity.

## Proof
Differentiate \(R\) along the vector field:
\[
\begin{aligned}
\dot R
&=2my\dot y+2(z-c)\dot z\\
&=2my\,x(z-c)+2(z-c)(-b-mxy)\\
&=-2b(z-c).
\end{aligned}
\]
Integrating from \(0\) to \(T\) gives
\[
R(T)-R(0)=-2b\int_0^T(z(t)-c)\,dt,
\]
which rearranges to the finite-time mean formula. If the forward orbit is bounded, then \(R(T)\) is bounded, so the boundary term divided by \(T\) vanishes.

For a compactly supported invariant probability measure, stationarity of the smooth observable \(R\) gives \(\int \dot R\,d\mu=0\). Since \(\dot R=-2b(z-c)\) and \(b\ne0\), this yields \(\int z\,d\mu=c\).

The Jacobian trace is \(-z\). Liouville's formula for the variational flow therefore gives \(\log|\det D\phi_T|=-\int_0^T z(t)\,dt\). Substitution of the finite-time mean identity gives the displayed exact determinant formula. Dividing by \(T\) on a bounded orbit yields the asymptotic rate \(-c\). For an ergodic compactly supported invariant measure, the standard determinant/Oseledets identity equates the Lyapunov-sum with the invariant mean of the divergence, hence with \(-c\).

## Verification
The source prints exactly the four equations above and computes their divergence as \(-z\). It reports Lyapunov exponents \((0.3606,0.1222,0,-1.4827)\) for \(c=1\), whose sum is \(-0.9999\), and \((0.2137,0.0623,0,-1.5761)\) for \(c=1.3\), whose sum is \(-1.3001\). These numerical sums agree with the exact law to the displayed numerical precision. The proof itself is symbolic and does not depend on those finite simulations.

## Relationship to prior work
Zhang, Li, Lei, Liu and Tao introduced the four-dimensional system and observed numerically that parameter \(c\) is “almost” positively correlated with the offset of \(z\); they also used the negative numerical average of the divergence to support dissipativity. The identity above shows that the long-time mean of \(z\) is exactly \(c\) on every bounded forward trajectory and every compact stationary state, and it fixes the asymptotic volume-contraction rate exactly at \(-c\).

The paper builds on the earlier three-dimensional Cang--Wang--Chen--Jia Lorenz-like system, which corresponds to a special fixed offset in the \(y,z\) subsystem. The accessible abstract and bibliographic material for that precursor do not state the parametric mean-height identity or the four-dimensional phase-volume consequence. A full-text copy of that precursor was not available in the inspected lawful sources, so possible special-case discussion there remains a residual literature risk.

## Limitations
The result does not prove existence of an attractor, hyperchaos, global boundedness, or uniqueness of an invariant measure. It does not assert individual Lyapunov exponents, only their sum when they exist. The exact law concerns the \(z\)-mean and phase-volume rate; the source's separate amplitude-control statements for other coordinates are not addressed.

## References
1. X. Zhang, C. Li, T. Lei, Z. Liu, C. Tao, “A Symmetric Controllable Hyperchaotic Hidden Attractor,” *Symmetry* 12 (2020), 550. DOI: 10.3390/sym12040550. Published 2020-04-04.
2. S. Cang, Z. Wang, Z. Chen, H. Jia, “Analytical and numerical investigation of a new Lorenz-like chaotic attractor with compound structures,” *Nonlinear Dynamics* 75 (2014), 745–760. DOI: 10.1007/s11071-013-1101-7.
