# Universal transient circulation response and sharp bath-switch reversal in a Brownian gyrator

## Finding
Let \(A=\left(\begin{smallmatrix}a&c\\c&b\end{smallmatrix}\right)\) be real symmetric positive definite with \(c\ne0\), and let the two baths of the overdamped harmonic gyrator have positive, locally bounded, measurable temperatures \(T_x(t)\) and \(T_y(t)\). For any initial probability distribution with finite second moments, define the signed integrated angular probability current
\[
Q(t)=\int_{\mathbb R^2}\bigl(xj_y(x,y,t)-yj_x(x,y,t)\bigr)\,dx\,dy.
\]
It obeys the **exact closed response law**
\[
\dot Q+(a+b)Q=2c\,[T_y(t)-T_x(t)]\quad\text{a.e.},\qquad
Q(t)=e^{-(a+b)t}Q(0)+2c\int_0^t e^{-(a+b)(t-s)}[T_y(s)-T_x(s)]\,ds.
\]
Thus the circulation observable has one relaxation rate, the trace of the stiffness matrix, even though the three individual quadratic moments generally relax at several rates. This law applies to every admissible bath protocol and all finite-second-moment initial laws, including non-Gaussian laws.

Suppose the system initially has its unique stationary state with positive temperature difference \(\Delta_0=T_y(0^-)-T_x(0^-)>0\), and future protocols obey the lower bound \(T_y(t)-T_x(t)\ge-B\) a.e., for some \(B>0\). After multiplying \(Q\) by the sign of \(c\), the earliest possible moment of zero circulation is
\[
\boxed{t_{\min}=\frac{1}{a+b}\log\left(1+\frac{\Delta_0}{B}\right).}
\]
A constant post-quench difference \(T_y-T_x=-B\), achievable with strictly positive temperatures, attains this bound and produces a unique change of sign. In particular, instantly swapping the original bath temperatures gives the universal reversal time \(\log2/(a+b)\). The optimality concerns the **first zero of the integrated angular current**, not the full-state relaxation time or the mean unweighted angular velocity.

## Assumptions and scope
Consider the overdamped Langevin equations, for \(t\ge0\),
\[
dZ_t=-AZ_t\,dt+\operatorname{diag}\bigl(\sqrt{2T_x(t)},\sqrt{2T_y(t)}\bigr)\,dW_t,
\quad Z_t=(X_t,Y_t)^\top,
\]
with independent standard Brownian coordinates, unit friction, and fixed symmetric stiffness matrix \(A\). Assume \(a,b>0\), \(ab>c^2\), \(c\ne0\). The initial state is independent of subsequent noise and has finite raw second moments. The piecewise or measurable bath temperatures are strictly positive almost everywhere and locally bounded. For \(t>0\) there is a smooth density \(p(z,t)\) and current \(j=-Azp-D(t)\nabla p\), with \(D=\operatorname{diag}(T_x,T_y)\). Define \(Q\) by the current moment, or equivalently by the generator formula below. In the quench result the initial state is the stationary distribution for a constant past bath pair with difference \(\Delta_0>0\). The control bound is on the **difference** only, not on individual heating power; positive constant bath pairs realizing \(-B\) exist for any finite \(B\).

## Proof
**1. Current observable.** Gaussian smoothing for positive times and Gaussian-tail bounds from the linear diffusion permit integration by parts. The diffusion contributions to \(\int(xj_y-yj_x)\) vanish because \(\partial_y x=\partial_x y=0\). With \(j=-Azp-D\nabla p\),
\[
Q=\mathbb E\bigl[X(-cX-bY)-Y(-aX-cY)\bigr]
=c(\mathbb EY^2-\mathbb EX^2)+(a-b)\mathbb E[XY].
\]
This also defines \(Q(0)\) without requiring an initial density.

**2. Exact closure without Gaussian initialization.** Write \(u=\mathbb EX^2\), \(v=\mathbb EXY\), \(w=\mathbb EY^2\). Itô's formula yields, almost everywhere,
\[
\dot u=-2au-2cv+2T_x,\quad
\dot v=-(a+b)v-c(u+w),\quad
\dot w=-2bw-2cv+2T_y.
\]
Substitute into \(Q=c(w-u)+(a-b)v\). The \(u,v,w\) coefficients cancel, giving \(\dot Q=-(a+b)Q+2c(T_y-T_x)\). Variation of constants proves the convolution for every \(t\ge0\). The scalar closure is not an approximation or a stationary limit. Its decay rate contains neither the off-diagonal coupling \(c\) nor the anisotropy \(a-b\).

**3. Initial stationary preparation.** Positive definiteness of \(A\) implies exponential stability, hence a unique stationary Gaussian state for each positive constant bath pair. Setting \(\dot Q=0\) gives \(Q(0)=2c\Delta_0/(a+b)\). This statement does not assert that the entire covariance relaxes with that one rate.

**4. Optimal first reversal.** Let \(s=a+b>0\) and \(\sigma=\operatorname{sgn}(c)\). For every admissible future difference \(\Delta(t)\ge-B\), positivity of the scalar convolution kernel yields
\[
\sigma Q(t)\ge\frac{2|c|}{s}\left[-B+(\Delta_0+B)e^{-st}\right].
\]
The right-hand side is strictly positive for \(0\le t<s^{-1}\log(1+\Delta_0/B)\), proving impossibility of an earlier zero. It equals zero at that time. A constant difference \(\Delta=-B\) makes the inequality an identity, crosses zero exactly once, and is realizable by selecting, for example, positive temperatures \(T_x=M+B/2\), \(T_y=M-B/2\) with \(M>B/2\). If \(B=\Delta_0\), the time becomes \(\log 2/s\). Equality at the first-zero time forces the bath difference to attain its lower bound almost everywhere before reversal, because the convolution kernel is strictly positive. This proves sharpness and essential uniqueness of the fastest difference protocol (while the common bath temperature may vary).

## Verification
Run `python checker.py` with NumPy and SciPy installed. The program integrates the complete three-moment equations independently of the closed scalar formula for 180 random stable stiffness matrices, arbitrary initial moment matrices and new bath pairs; it compares nine times per case. It also checks 120 stationary-start quench parameter sets, including the exact reversal crossing and a family of dominated future protocols. It reports 2,100 successful numerical comparisons. The algebraic cancellation in Proof 2 and the positivity comparison in Proof 4 establish the infinite-parameter claims; finite numerical testing alone would not.

## Relationship to prior work
Filliger and Reimann introduced the Brownian gyrator and computed its stationary torque and heat-engine interpretation [1]. The full text does not give the arbitrary-measurable-bath **transient scalar closure** or the sharp fastest-reversal time. Dotsenko, Maciołek, Vasilyev and Oshanin [2] derived steady-state spatial currents and the ordinary mean angular velocity; that angular velocity is a different observable from the integrated moment \(Q\). Baldassarri, Puglisi and Sesta [3] study engineered finite-time equilibration with **time-dependent trap stiffness** and fixed bath temperatures, while here the trap is fixed and bath temperatures are varied. Cerasoli and coauthors [4] analyze transient effective temperatures for a biased, cold-component model at fixed bath temperatures. Patrón, Plata and Prados [5] treat minimum-time connection between full nonequilibrium steady states using **potential parameters** as controls, rather than fastest first reversal of \(Q\) using a constrained bath difference. Source [5] could be compared only at abstract level in the available retrieval; its complete content is an explicit remaining priority risk. General Gaussian covariance evolution is established prior machinery, not a novelty claim. The proposed contribution is its nontrivial one-dimensional invariant circulation mode together with the exact difference-constrained reversal criterion.

## Limitations
The current moment \(Q\) is not the conventional mean angular velocity weighted by inverse radius, and the result does not imply a one-mode relaxation of all state observables. Temperature protocols must respect the declared positive-bath and bounded-difference assumptions, with fixed symmetric stable stiffness. The optimization concerns a first sign change, not minimum time to transform the full distribution into a new stationary distribution. Existing linear-diffusion theory supplies much of the machinery; historical priority of this exact combined statement is not independently certified, and a related later control paper was not fully inspected.

## References
[1] R. Filliger and P. Reimann, *The Brownian gyrator: a minimal heat engine on the nano-scale*, arXiv:0710.3735v1 (19 October 2007), https://arxiv.org/abs/0710.3735, DOI 10.1103/PhysRevLett.99.230602.

[2] V. Dotsenko, A. Maciołek, O. Vasilyev and G. Oshanin, *Two-temperature Langevin dynamics in a parabolic potential*, arXiv:1302.4056 (2013), https://arxiv.org/abs/1302.4056, DOI 10.1103/PhysRevE.87.062130.

[3] A. Baldassarri, A. Puglisi and L. Sesta, *Engineered swift equilibration of a Brownian gyrator*, arXiv:2009.06989 (2020), https://arxiv.org/abs/2009.06989, DOI 10.1103/PhysRevE.102.030105.

[4] S. Cerasoli, V. Dotsenko, G. Oshanin and L. Rondoni, *Time-dependence of the effective temperatures of a two-dimensional Brownian gyrator with cold and hot components*, arXiv:2011.03124 (2020), https://arxiv.org/abs/2011.03124, DOI 10.1088/1751-8121/abe0d6.

[5] A. Patrón, C. A. Plata and A. Prados, *Minimum time connection between non-equilibrium steady states: the Brownian gyrator*, arXiv:2407.21110v1 (2024), https://arxiv.org/abs/2407.21110, DOI 10.1088/1751-8121/ad909a.
