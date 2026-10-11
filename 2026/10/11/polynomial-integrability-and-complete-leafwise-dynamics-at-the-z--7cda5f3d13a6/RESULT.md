# Polynomial integrability and complete leafwise dynamics at the zero-coupling Pehlivan–Wei boundary

## Finding
Consider the Pehlivan–Wei polynomial differential equations
\[
\dot x=y(1-z),\qquad \dot y=y(1+z)-ax,\qquad \dot z=a-y(x+y).
\]
At the singular parameter \(a=0\), a globally invertible *polynomial* change of variables reduces the three-dimensional flow exactly to the scalar cubic family
\[
\dot u=P_{H,K}(u):=K+(1+H)u-\frac{u^3}{12},\qquad \dot H=\dot K=0.
\]
The labels \(H,K\) are two independent polynomial first integrals. Every trajectory is globally defined and bounded forward in time and converges to an equilibrium. In particular, every compactly supported invariant probability measure is concentrated on the equilibrium plane \(y=0\); no nonconstant periodic orbit or nonstationary recurrent orbit occurs.

The complete equilibrium and bounded-complete-orbit count on each invariant leaf is determined by
\[
q=1+H,\qquad \Delta=16q^3-9K^2.
\]
For \(q>0\) and \(\Delta>0\) there are exactly three distinct equilibria and exactly two nonconstant heteroclinic orbits modulo translation in time; for \(q>0\) and \(\Delta=0\) there are exactly two distinct equilibria and one such orbit; in every other case there is one equilibrium and no nonconstant bounded complete orbit. At the cusp leaf \((H,K)=(-1,0)\) every nonstationary solution has the asymptotic law \(u(t)\sim\operatorname{sgn}(u_0)\sqrt{6/t}\). At a fold with a nonzero double root \(r\), the approaching branch obeys \(\lim_{t\to\infty}t(u(t)-r)=4/r\).

## Assumptions and scope
The vector field and state variables are real; \(a\) is fixed to exactly zero throughout the theorem. We consider classical maximal solutions with arbitrary finite initial state in \(\mathbb R^3\). Invariant probability measures are Borel probability measures invariant under the forward-complete flow, with compact support. A complete orbit is defined for all real times and is bounded if its image is bounded; two heteroclinic orbits are identified if they differ by a time translation. The word cusp describes the algebraic discriminant of the invariant-leaf equilibrium equation in \((H,K)\), **not** a claimed parameter bifurcation of the full system as \(a\) varies.

## Proof
**1. Polynomial conjugacy.** Set \(u=x+y\) and introduce
\[
H=z+\frac{(x+y)^2}{4},\qquad K=2y-(1+H)(x+y)+\frac{(x+y)^3}{12}.
\]
Direct differentiation along the original vector field at \(a=0\) gives
\[
\dot u=2y,\qquad \dot H=-yu+\frac{u}{2}(2y)=0,
\]
and, using \(z=H-u^2/4\),
\[
\dot K=2y(1+z)-(1+H)(2y)+\frac{u^2}{4}(2y)=0.
\]
Solving the polynomial coordinate equations yields the inverse
\[
\begin{aligned}
 y&=\frac12\left(K+(1+H)u-\frac{u^3}{12}\right),\\
 x&=u-y,\\
 z&=H-\frac{u^2}{4}.
\end{aligned}
\]
Hence \(\dot u=2y=P_{H,K}(u)\). The original-to-new coordinate Jacobian determinant is the constant \(-2\), so this is a global polynomial diffeomorphism, not merely a local reduction. Every pair \((H,K)\in\mathbb R^2\) labels a nonempty invariant leaf.

**2. Forward completeness and recurrence rigidity.** For each fixed pair \((H,K)\), the polynomial \(P_{H,K}(u)\) is positive for sufficiently large negative \(u\) and negative for sufficiently large positive \(u\). Thus, a suitable closed interval is forward invariant and absorbs the scalar forward trajectory. Solutions are bounded and exist for all positive time. Between any adjacent real roots of \(P_{H,K}\) the sign is fixed, so every nonstationary scalar solution is strictly monotone and converges to an equilibrium root. The inverse transformation then proves bounded convergence in the original coordinates.

For the stronger invariant-measure statement, define the polynomial
\[
G(u,H,K)=Ku+\frac{(1+H)u^2}{2}-\frac{u^4}{48}.
\]
Since \(\partial_uG=P_{H,K}\), every trajectory has
\[
\frac{dG}{dt}=P_{H,K}(u)^2=4y^2\ge 0.
\]
If \(\mu\) is a compactly supported invariant probability measure, invariance and boundedness of the polynomial on its support imply \(0=\int \dot G\,d\mu=4\int y^2\,d\mu\). Consequently \(y=0\) almost surely, and every point of this plane is an equilibrium at \(a=0\). This rules out periodic and nonstationary recurrent dynamics without requiring ergodicity.

**3. Exact leafwise census.** The equilibrium equation is
\[
u^3-12(1+H)u-12K=0.
\]
Its cubic discriminant is \(432\Delta\). Since its derivative is \(3u^2-12q\), three distinct real roots occur exactly when \(q>0\) and \(\Delta>0\); the locus \(q>0,\Delta=0\) has precisely two distinct roots, one double; all remaining parameters have a unique distinct real root (the cusp triple root counts once). Nonstationary bounded complete solutions of a scalar autonomous ODE are precisely the monotone trajectories in bounded intervals between consecutive distinct equilibria: any such interval is traversed in infinite time at both endpoints by smooth uniqueness; any trajectory outside the extreme roots escapes to infinity in finite negative time. On each interval all trajectories differ only by time translation. This proves the asserted heteroclinic counts.

**4. Quantitative cusp and fold laws.** On the cusp leaf \(H=-1,K=0\), one has \(\dot u=-u^3/12\), which integrates exactly to
\[
u(t)=\frac{u_0}{\sqrt{1+u_0^2t/6}}\qquad(t\ge0).
\]
For \(u_0\ne0\) this yields the stated \(t^{-1/2}\) constant. At a nonzero double root \(r\), necessarily \(q=r^2/4\), \(K=-r^3/6\), and
\[
P_{H,K}(u)=-\frac{(u-r)^2(u+2r)}{12}.
\]
Writing \(w=u-r\), \(\dot w=-\tfrac r4w^2-\tfrac1{12}w^3\). On the approaching side \(rw_0>0\), \(w(t)\to0\), and \(\frac{d}{dt}(1/w)=\tfrac r4+\tfrac1{12}w\to\tfrac r4\). Cesàro averaging gives \(\frac1{tw(t)}\to\frac r4\), hence \(t(u(t)-r)\to4/r\).

## Verification
The standalone script `checks/verify_conjugacy.py` uses exact rational polynomial algebra to check the two Lie derivatives, polynomial inverse, constant Jacobian, discriminant, fold factorization, Lyapunov derivative, and explicit cusp solution. Run it with `python checks/verify_conjugacy.py` with SymPy installed. The symbolic identities are supporting reproducibility evidence; the global dynamical and invariant-measure arguments are the proofs above, not extrapolations from finite numerical trajectories.

## Relationship to prior work
Pehlivan and Wei introduced this quadratic family and investigated chaos and controlled Hopf behavior, with numerical examples centered on \(a=2\) [1]. Their model's displayed two-equilibrium formula applies generically but degenerates at \(a=0\), where the full equilibrium plane becomes visible. The separate 2021 application study [2] implements and numerically compares several chaotic systems, including the same Pehlivan–Wei equations, but does not give the zero-parameter polynomial reduction or complete leafwise dynamics. Classical one-dimensional gradient-flow theory explains the scalar consequences once the two integrals and global conjugacy are exhibited; by itself it does not identify this particular reduction. The accessible portions of [1] do not contain the stated polynomial conjugacy. The remainder of [1] was not fully accessible and is an explicit literature-priority limitation.

## Limitations
The theorem describes **only** \(a=0\) and neither claims global integrability for \(a\ne0\) nor stability of its equilibria against nonzero-parameter perturbations. Some nonstationary trajectories blow up in finite *negative* time, so forward completeness must not be confused with two-sided completeness. The cusp is leafwise, not a full-parameter codimension-two bifurcation claim. The original paper's remaining pages could contain relevant historical information not available for comparison; novelty beyond the inspected material is not independently established.

## References
[1] İ. Pehlivan and Z. Wei, “Analysis, nonlinear control, and chaos generator circuit of another strange chaotic system,” *Turkish Journal of Electrical Engineering and Computer Sciences* 20 (Suppl. 2) (2012), 1229–1239, DOI: https://doi.org/10.3906/elk-1103-14. Accessible extracted preview: https://paperity.org/p/150891673/analysis-nonlinear-control-and-chaos-generator-circuit-of-another-strange-chaotic-system .

[2] O. Kalayci et al., “A New Chaotic Mixer Design Based on the Delta Robot and Its Experimental Studies,” *Mathematical Problems in Engineering* (2021), article 6615856, DOI: https://doi.org/10.1155/2021/6615856; full text: https://onlinelibrary.wiley.com/doi/10.1155/2021/6615856 .
