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
gives the following compact-recurrence phase boundary:

1. A nonempty compact forward-invariant set exists if and only if \(|\alpha|\le |\kappa|\). For this map, this is equivalent both to existence of a compactly supported invariant probability measure and to existence of a fixed point. When \(\kappa\ne0\), every equilibrium has the form \((s,s,\zeta)\) where \(s=-\alpha/\kappa\) and \(\sin\zeta=s\); for strict inequality there are two equilibrium classes modulo \(2\pi\), and at equality there is one. When \(\alpha=\kappa=0\), every \((\sin\zeta,\sin\zeta,\zeta)\) is an equilibrium.
2. If \(|\alpha|>|\kappa|\), every real forward orbit escapes to \(\operatorname{sgn}(\alpha)\infty\) in its third coordinate, with
   \[
   \liminf_{n\to\infty}\frac{\operatorname{sgn}(\alpha)z_n}{n}
     \ge|\alpha|-|\kappa|>0.
   \]
   There are no bounded forward orbits and no nonempty compact forward-invariant sets.
3. On the nondegenerate boundary \(|\alpha|=|\kappa|>0\), put \(s=-\alpha/\kappa\in\{-1,1\}\). Every real initial condition either escapes with \(z_n\to\operatorname{sgn}(\alpha)\infty\) or converges in the full state to one of the equilibria \((s,s,\zeta)\) with \(\sin\zeta=s\). The compactly supported invariant probabilities on this boundary are exactly the finite mixtures of these equilibrium atoms.
4. For each fixed finite integer \(k\ge3\), every equilibrium on the nondegenerate boundary \(|\alpha|=|\kappa|>0\) has a local one-dimensional \(C^k\) center manifold. Writing \(r=z-\zeta\) on it, the return law is
   \[
   r_{n+1}=r_n+\tfrac{\alpha}{2}r_n^2+O(r_n^3).
   \]
   All sufficiently close nonstationary points on its attracting-side branch \(\alpha r<0\) converge to the equilibrium and satisfy the sharp law
   \[
   \lim_{n\to\infty}n(z_n-\zeta)=-\frac{2}{\alpha}.                \tag{2}
   \]
   The coefficient and limit depend only on \(\alpha\), not separately on \(\beta,\gamma,\delta\). The limit is claimed for the indicated branch, not for every convergent initial condition.
5. Fixed states and escaping states can coexist at the same boundary parameters with all positive coefficients: at \(\alpha=\beta=\gamma=\delta=\pi\), \((-1,-1,3\pi/2)\) is fixed, whereas \((1,1,\pi/2+2\pi n)\) is an exact orbit for all integers \(n\ge0\).

## Assumptions and scope
All four parameters are arbitrary finite real numbers, every initial state is in \(\mathbb R^3\), the self-feedback coefficient is exactly one, and iteration starts at \(n=0\). A forward-invariant set satisfies \(F(K)\subseteq K\). Invariant probability measures are Borel probabilities. The conclusions are for the full real lift, not only the quotient modulo \(2\pi\).

If \(\kappa=0\), (1) simplifies to \(U(F^n w)=U(w)+n\alpha\). Consequently \(z_n/n\to\alpha\) whenever \(\alpha\ne0\), while \(\alpha=0\) yields a first integral and a bounded third coordinate after two iterations.

## Proof
**Coboundary and bounded transverse coordinates.** Expanding \(U(F(x,y,z))\) cancels the affine terms in \(x,y\), leaving (1). Also \(y_n=\sin z_{n-1}\) for \(n\ge1\), and \(x_n=\sin z_{n-2}\) for \(n\ge2\). Thus
\[
|U(x_n,y_n,z_n)-z_n|\le |\beta|+|\beta+\gamma|\qquad(n\ge2).       \tag{3}
\]
When \(|\alpha|>|\kappa|\), the signed increments of \(U\) are bounded below by \(|\alpha|-|\kappa|\). Summation and (3) give the escape bound. A nonempty compact forward-invariant set would contain a bounded orbit. Also, the support of a compactly supported invariant probability for a continuous map is forward-invariant, so such a probability cannot exist in the strict escape regime.

**Existence and census of equilibria.** The first two fixed-point equations give \(x=y=\sin z=s\); the third requires \(\alpha+\kappa s=0\). This gives exactly the stated census and criterion, including the degenerate case \(\alpha=\kappa=0\). A fixed point itself supports both a compact invariant set and an invariant Dirac probability.

**Boundary orbit dichotomy.** Suppose \(|\alpha|=|\kappa|>0\), and fix one \(\zeta\) with \(\sin\zeta=s=-\alpha/\kappa\). Since \(s=\pm1\),
\[
\sin z=s\cos(z-\zeta),\qquad U(Fw)-U(w)=\alpha(1-\cos(z-\zeta)). \tag{4}
\]
The sequence \(\operatorname{sgn}(\alpha)U_n\) is nondecreasing. If it tends to infinity, (3) gives escape in the specified direction. Otherwise \(U_n\) has a finite limit, so (4) gives \(\cos(z_n-\zeta)\to1\) and \(\sin z_n\to s\). The two shift identities give \(y_n\to s\) and \(x_n\to s\). Now \(z_n=U_n-\beta x_n-(\beta+\gamma)y_n\) converges to a finite \(z_\infty\), which has sine \(s\). The full state converges to the corresponding equilibrium.

For a compactly supported invariant probability \(\nu\), invariance gives \(\int(U\circ F-U)\,d\nu=0\). The integrand in (4) has one sign, hence \(\sin z=s\) almost surely. Invariance of the two shift coordinates then gives \(y=s\) and \(x=s\) almost surely. Thus \(\nu\) is supported on the equilibrium lattice. A bounded subset of this lattice is finite; finite mixtures of the equilibrium atoms are compactly supported and invariant. An infinite-support probability mixture is also invariant but is not compactly supported.

**Center-manifold coefficient and rate.** At \((s,s,\zeta)\) the Jacobian is
\[
DF(s,s,\zeta)=\begin{pmatrix}0&1&0\\0&0&0\\\beta&\gamma&1\end{pmatrix}.
\]
It has a simple unit eigenvalue with eigendirection the \(z\)-axis, and two stable zero eigenvalues. For each finite \(k\ge3\), the discrete-map \(C^k\) center-manifold theorem applies after a local cutoff of the smooth nonlinear part. In coordinates adapted to the splitting the stable block is nilpotent, of operator norm smaller than one in an equivalent norm, and the center block is the identity. No inverse for the stable block is required. The manifold is a local graph \(x=s+h(r),\ y=s+j(r)\) by the inverse function theorem, with \(h(0)=j(0)=h'(0)=j'(0)=0\) and \(r=z-\zeta\). The assertion does not require that one graph be \(C^\infty\), or that the graph be unique.

The third-coordinate law has \(r'=r+O(r^2)\) by tangency and \(\sin(\zeta+r)-s=-s r^2/2+O(r^4)\). The invariance identities \(h(r')=j(r)\), \(j(r')=\sin(\zeta+r)-s\) then give \(h(r)=j(r)=-s r^2/2+O(r^3)\). Substitution yields
\[
r'=r+\beta h(r)+\gamma j(r)-\delta s(\cos r-1)
  =r-\tfrac{s(\beta+\gamma-\delta)}{2}r^2+O(r^3)
  =r+\tfrac{\alpha}{2}r^2+O(r^3).
\]
For sufficiently small \(|r|>0\) with \(\alpha r<0\), the quadratic correction makes the magnitude strictly smaller without changing sign. The magnitude tends to zero since the return map has no other fixed point in a sufficiently small interval. With \(a=\alpha/2\), put \(w_n=-1/(a r_n)\); then \(w_{n+1}-w_n=1+O(r_n)\to1\). The Cesàro mean gives \(w_n/n\to1\), proving (2). The quadratic coefficient is forced by invariance, independently of the choice of center manifold.

**Exact coexistence.** For \(\alpha=\beta=\gamma=\delta=\pi\) we have \(\kappa=\pi\). At \(x=y=\sin z=-1\) the increment in \(z\) is zero. At \(x=y=\sin z=1\) it is \(2\pi\); this preserves the sine and yields the specified ballistic orbit by induction.

## Verification
The supplementary standalone program `checks.py` uses SymPy to recompute (1), the quadratic center-graph conditions, the quadratic coefficient under the critical relation, and the coexistence states. It also tests 400 sampled pointwise drift identities and a 200,000-iterate trajectory. The original package recorded 411 checks and a diagnostic \(n(z_n-3\pi/2)\approx-1.99751834\) at \(n=200000\) with unit parameters. These finite checks do not prove the global assertions, center-manifold existence, or the limit law.

## Relationship to prior work
Rajagopal, Kanagaraj, Volos and Karthikeyan introduced the map and examined bifurcation, Lyapunov and network behavior. Their map is the starting point; the contribution here is the exact real-lift compact existence threshold, nondegenerate critical orbit dichotomy and stationary-measure classification, and the center-branch rate and explicit coexistence. The general center-manifold theorem supplies a local method, not the map-specific drift or coefficient.

## Limitations
The result is restricted to the exact unit-self-feedback surface of the uncoupled map. It neither classifies all bounded dynamics for \(|\alpha|<|\kappa|\) nor assigns a common asymptotic velocity to boundary escape. The center-branch law is not a statement about all convergent starts. The theorem describes compactly supported invariant probabilities; it does not classify noncompact invariant measures globally. A differently formulated antecedent remains possible.

## References
1. K. Rajagopal, S. Kanagaraj, C. Volos, A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry **15** (2023), article 780, DOI: 10.3390/sym15040780, https://www.mdpi.com/2073-8994/15/4/780.
2. J. B. van den Berg, W. Hetebrij and B. Rink, *The parameterization method for center manifolds*, Journal of Differential Equations **269** (2020), 2132–2184, DOI: 10.1016/j.jde.2020.01.033, https://arxiv.org/abs/1905.00264. See Theorem 2.1 and the preceding cutoff discussion in the preprint.
