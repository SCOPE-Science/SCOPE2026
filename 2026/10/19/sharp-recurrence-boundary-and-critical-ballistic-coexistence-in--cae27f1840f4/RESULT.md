# Sharp recurrence boundary and critical ballistic coexistence in a three-dimensional sine map

## Finding
Consider the three-dimensional smooth map
\[
F(x,y,z)=\bigl(y,\sin z,\ z+\alpha+\beta x+\gamma y-\delta\sin z\bigr)
\]
with real parameters \(\alpha,\beta,\gamma,\delta\). This is the unit-self-feedback specialization of the sinusoidal map in Rajagopal–Kanagaraj–Volos–Karthikeyan (2023). Put \(\kappa=\beta+\gamma-\delta\), and define
\[
U(x,y,z)=z+\beta x+(\beta+\gamma)y.
\]
The exact identity
\[
U\circ F-U=\alpha+\kappa\sin z                                      \tag{1}
\]
gives the following complete compact-recurrence phase boundary:

1. A nonempty compact forward-invariant set (equivalently, a compactly supported invariant probability measure, or simply a fixed point) exists **if and only if** \(|\alpha|\le |\kappa|\). When \(\kappa\ne0\), every equilibrium has the form \((s,s,\zeta)\) where \(s=-\alpha/\kappa\) and \(\sin\zeta=s\); for strict inequality there are exactly two equilibrium classes modulo \(2\pi\), and at equality there is exactly one. When \(\alpha=\kappa=0\), every \((\sin\zeta,\sin\zeta,\zeta)\) is an equilibrium.
2. If \(|\alpha|>|\kappa|\), every real forward orbit escapes to \(\operatorname{sgn}(\alpha)\infty\) in its third coordinate, with
   \[
   \liminf_{n\to\infty}\frac{\operatorname{sgn}(\alpha)z_n}{n}
     \ge|\alpha|-|\kappa|>0.
   \]
   Therefore there are no bounded forward orbits and no nonempty compact invariant sets.
3. On the nondegenerate boundary \(|\alpha|=|\kappa|>0\), put \(s=-\alpha/\kappa\in\{-1,1\}\). **Every** real initial condition has exactly one of these outcomes: it escapes with \(z_n\to\operatorname{sgn}(\alpha)\infty\), or its complete state converges to one of the equilibria \((s,s,\zeta)\) with \(\sin\zeta=s\). Every compactly supported invariant probability measure on this boundary is a mixture of Dirac measures on that equilibrium lattice.
4. Every boundary equilibrium has a local one-dimensional smooth center manifold. Writing \(r=z-\zeta\) on such a manifold, the return law is
   \[
   r_{n+1}=r_n+\tfrac{\alpha}{2}r_n^2+O(r_n^3).
   \]
   All sufficiently close nonstationary points of its attracting-side branch \(\alpha r<0\) converge to the equilibrium with the **parameter-independent sharp law**
   \[
   \lim_{n\to\infty}n(z_n-\zeta)=-\frac{2}{\alpha}.                \tag{2}
   \]
   This rate is claimed for that center-manifold branch, not for every convergent initial condition.
5. Fixed states and escaping states can coexist even at the same boundary parameters with all positive coefficients: at \(\alpha=\beta=\gamma=\delta=\pi\), \((-1,-1,3\pi/2)\) is fixed, whereas \((1,1,\pi/2+2\pi n)\) is an exact orbit for every integer \(n\ge0\). Thus the boundary is a genuine stationary–ballistic coexistence regime.

## Assumptions and scope
All four parameters are arbitrary finite real numbers, and every initial state is in \(\mathbb R^3\). The self-feedback coefficient is exactly one. Iteration starts at \(n=0\). Compact invariant sets refer to nonempty subsets of \(\mathbb R^3\) invariant under the forward map; invariant probability measures are Borel probabilities. The claim is about the full real lift of the sine map, not only its quotient modulo \(2\pi\), and does not assert uniqueness of a basin or a limit velocity for all boundary escaping trajectories.

If \(\kappa=0\), identity (1) simplifies to \(U(F^n w)=U(w)+n\alpha\). Consequently \(z_n/n\to\alpha\) whenever \(\alpha\ne0\), while \(\alpha=0\) yields a first integral and a bounded third coordinate after two iterations. These identities explain the degenerate edge of the phase diagram.

## Proof
**Coboundary and bounded transverse coordinates.** Write \(F(x,y,z)=(x',y',z')\). Expanding the definition,
\[
\begin{aligned}
U(x',y',z')-U(x,y,z)
&=\alpha+(\beta+\gamma-\delta)\sin z, \\
&=\alpha+\kappa\sin z.
\end{aligned}
\]
For every initial condition, \(y_n=\sin z_{n-1}\) for \(n\ge1\), and \(x_n=\sin z_{n-2}\) for \(n\ge2\). Hence \(|x_n|,|y_n|\le1\) for \(n\ge2\), and
\[
|U(x_n,y_n,z_n)-z_n|\le|\beta|+|\beta+\gamma|.                 \tag{3}
\]
When \(|\alpha|>|\kappa|\), the increments of \(U\) have the sign of \(\alpha\), with signed magnitude at least \(|\alpha|-|\kappa|\). Summation and (3) prove the escape bound. No compact forward-invariant set can contain an orbit escaping this way.

**Existence and census of equilibria.** At a fixed point, the first two equations give \(x=y=\sin z=s\); the third then requires \(\alpha+\kappa s=0\). Since \(|s|\le1\), a solution exists precisely when \(|\alpha|\le|\kappa|\). This also includes the degenerate pair \(\alpha=\kappa=0\), for which every real \(z\) is allowed. The elementary solutions of the sine equation give the stated per-period census. Every equilibrium itself supports a compact invariant set and a Dirac invariant probability, establishing the sharp reverse implication.

**Boundary orbit dichotomy.** Suppose \(|\alpha|=|\kappa|>0\) and fix any \(\zeta\) with \(\sin\zeta=s=-\alpha/\kappa\). Because \(s=\pm1\),
\[
\sin z=s\cos(z-\zeta),\qquad
U(Fw)-U(w)=\alpha\bigl(1-\cos(z-\zeta)\bigr).                 \tag{4}
\]
Thus \(U_n\) is monotone, increasing for positive \(\alpha\) and decreasing for negative \(\alpha\). If its signed magnitude tends to infinity, (3) gives escape of \(z_n\) in that direction. Otherwise \(U_n\) has a finite limit. The nonnegative increments in (4) then form a convergent series and tend to zero, so \(\cos(z_n-\zeta)\to1\), hence \(\sin z_n\to s\). The shift identities imply \(y_n\to s\), \(x_n\to s\), and (3), together with the definition of \(U\), implies that \(z_n\) converges to a finite \(z_\infty\). Its sine is \(s\), and the complete state therefore converges to the asserted equilibrium. No intermediate bounded nonconvergent outcome is possible.

For a compactly supported invariant probability \(\nu\), the bounded continuous observable \(U\) on its compact support is integrable, and invariance gives \(\int(U\circ F-U)\,d\nu=0\). Equation (4) has a fixed sign, forcing \(\sin z=s\) almost surely. Invariance then forces \(y=s\) almost surely (as \(y'=\sin z\)), and one further push-forward gives \(x=s\) almost surely. Hence the measure is supported on the countable equilibrium lattice. Conversely, every probability mixture of those equilibrium atoms is invariant and compactly supported when its selected lattice subset is bounded; infinite-support mixtures remain invariant but are not necessarily compactly supported.

**Critical center-manifold coefficient and rate.** At the equilibrium \((s,s,\zeta)\), the Jacobian is
\[
DF(s,s,\zeta)=
\begin{pmatrix}0&1&0\\0&0&0\\\beta&\gamma&1\end{pmatrix},
\]
with one simple unit eigenvalue and two stable zero eigenvalues. The smooth center-manifold theorem for discrete maps supplies a local one-dimensional invariant graph \(x=s+h(r)\), \(y=s+j(r)\), with \(h(0)=j(0)=h'(0)=j'(0)=0\) and \(r=z-\zeta\). Since
\[
\sin(\zeta+r)-s=s(\cos r-1)=-\tfrac{s}{2}r^2+O(r^4),
\]
its two graph-invariance equations give
\[
h(r)=j(r)=-\tfrac{s}{2}r^2+O(r^3).
\]
Substitution into the third map coordinate yields
\[
\begin{aligned}
r'&=r+\beta h(r)+\gamma j(r)-\delta s(\cos r-1)\\
  &=r-\tfrac{s(\beta+\gamma-\delta)}2r^2+O(r^3)
   =r+\tfrac\alpha2r^2+O(r^3),
\end{aligned}
\]
because \(-s\kappa=\alpha\). On the attracting side \(\alpha r<0\), sufficiently small iterates remain on that side and approach zero: the quadratic correction has the opposite sign to \(r\) and the map is locally increasing. For \(a=\alpha/2\ne0\), put \(w_n=-1/(a r_n)>0\). The recurrence gives \(w_{n+1}-w_n=1+O(r_n)\to1\); the Cesàro mean then gives \(w_n/n\to1\), proving (2). The local expansion is independent of the choice of center manifold up to the required order.

**Exact coexistence.** With \(\alpha=\beta=\gamma=\delta=\pi\), one has \(\kappa=\pi\), so these parameters lie precisely on the boundary. Direct substitution shows the fixed orbit \((-1,-1,3\pi/2)\), and for every integer \(n\ge0\) the map sends \((1,1,\pi/2+2\pi n)\) to \((1,1,\pi/2+2\pi(n+1))\). This realizes both outcomes without relying on numerics.

## Verification
The supplementary standalone program `checks.py` uses SymPy to recompute (1), the quadratic center-graph conditions, the reduced quadratic coefficient under the critical relation, and the exact coexistence states. It additionally tests 400 independently sampled real-parameter identities and a 200,000-iterate approach trajectory. At package construction it passed 411 assertions/checks and the final numerical diagnostic was \(n(z_n-3\pi/2)\approx-1.99751834\) at \(n=200000\) with unit parameters. These finite checks are diagnostics only; the global assertions and limit law are consequences of the preceding analytical proof.

## Relationship to prior work
Rajagopal, Kanagaraj, Volos and Karthikeyan introduced and numerically investigated the self-feedback sinusoidal map, varying feedback and other parameters to display periodic, quasiperiodic and chaotic regimes. Their full 2023 study does not state an exact compact-recurrence threshold for unit feedback, a complete critical orbit dichotomy, or a critical stationary-measure support theorem. Existing general center-manifold theory supplies the local analytical method, but not this map's specific drift observable or parameter coefficient. Related recurrence thresholds for other dynamical systems do not imply the formula (1) or this map's equilibrium/ballistic coexistence.

## Limitations
The theorem is restricted to the **exact** unit-self-feedback parameter surface and addresses the uncoupled three-dimensional map, not the paper's network model or its numerical regimes at other feedback strengths. On the critical boundary, the algebraic asymptotic is proved for the attracting branch on a local center manifold and is not asserted for all convergent states. The result neither classifies all bounded dynamics for \(|\alpha|<|\kappa|\) nor assigns a common asymptotic velocity to boundary escape. Invariant measures with noncompact support are not globally classified. Although targeted published comparisons did not identify the same theorem, an older or differently formulated antecedent remains possible.

## References
1. K. Rajagopal, S. Kanagaraj, C. Volos, A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry **15** (2023), article 780. First public: 23 March 2023. DOI: 10.3390/sym15040780. Public text: https://www.mdpi.com/2073-8994/15/4/780.
2. J. B. van den Berg, W. Hetebrij and B. Rink, *The parameterization method for center manifolds*, Journal of Differential Equations **269** (2020), 2132–2184, DOI: 10.1016/j.jde.2020.01.033; open preprint https://arxiv.org/abs/1905.00264. This establishes a general center-manifold framework for discrete-time maps, not the map-specific theorem here.
