# Bounded-future rigidity and critical harmonic recurrence in a reflection-symmetric quadratic flow

## Finding
Consider the real polynomial differential equation
\[
\dot x=x(1-y),\qquad \dot y=z,\qquad \dot z=-y-a z+x^2,\quad a\in\mathbb R.
\]
For **every** parameter \(a\le0\), all forward-bounded trajectories are classified as follows.

1. If \(x(0)>0\), the trajectory is forward-complete and converges to \(E_+=(1,1,0)\). If \(x(0)<0\), it converges to \(E_-=(-1,1,0)\). The assertion is conditional on forward boundedness; it makes no assertion that every initial condition is bounded.
2. If \(x(0)=0\) and \(a<0\), the only forward-bounded trajectory is the origin \(E_0=(0,0,0)\).
3. If \(x(0)=0\) and \(a=0\), all solutions are the exact harmonic circles \(x=0\), \(y(t)=r\cos(t+\theta)\), \(z(t)=-r\sin(t+\theta)\), for \(r\ge0\) and arbitrary phase \(\theta\). Every nonzero circle has least period \(2\pi\).

Consequently, when \(a<0\) every compactly supported invariant Borel probability measure is a convex combination of the three equilibrium Dirac masses \(\delta_{E_0}\), \(\delta_{E_+}\), and \(\delta_{E_-}\). When \(a=0\), these measures are exactly the mixtures of \(\delta_{E_+}\), \(\delta_{E_-}\), and uniform rotation measures on the harmonic circles in \(x=0\) (including the zero-radius circle \(\delta_{E_0}\)). The mixing distribution over radii must have compact support. In particular, no nonconstant periodic orbit can occur away from \(x=0\) for \(a\le0\).

The mechanism is the globally polynomial observable
\[
L(x,y,z)=\frac{z^2+(1-y)^2}{2}+(x^2-1)(1-y),
\qquad
\boxed{\dot L=2x^2(1-y)^2-a z^2}.
\]
The critical value \(a=0\) separates the strictly gradient-like bounded-future regime on either open half-space from an exact invariant harmonic foliation on the symmetry plane. This statement is a characterization of bounded forward orbits and compact stationary statistics, **not** a claim of global boundedness.

## Assumptions and scope
The phase space is \(\mathbb R^3\), and \(a\) is real with \(a\le0\) for the classification. A forward-bounded solution means a maximal classical solution whose image is bounded on its forward existence interval. Because the polynomial vector field is locally Lipschitz, such a solution extends to every \(t\ge0\). The omega-limit set \(\omega(q)\) is the set of limits along sequences \(t_n\to\infty\). Invariant probability measures are understood for the complete dynamics on their compact invariant support. Reflection \(x\mapsto-x\) exchanges the two nonzero equilibria; \(x=0\) is an invariant plane, and nonzero \(x(t)\) retains its sign.

## Proof
**1. Exact monotone identity.** Direct differentiation along the stated vector field gives
\[
\begin{aligned}
\dot L
&=2x^2(1-y)^2+(y-x^2)z+z(-y-a z+x^2)\\
&=2x^2(1-y)^2-a z^2.
\end{aligned}
\]
For \(a\le0\), \(L\) is nondecreasing on every solution. Along a forward-bounded solution, \(L\) is bounded and converges to a finite limit \(\ell\). Its nonempty compact omega-limit set is connected, invariant and contained in the zero-derivative set \(Z=\{\dot L=0\}\): indeed \(L=\ell\) on this set and invariance forces its derivative to vanish there.

**2. Negative parameter.** If \(a<0\), then
\[
Z=\{z=0,\ x(1-y)=0\}.
\]
Any full orbit contained in \(Z\) must have \(\dot z=-y+x^2=0\) as well. If \(x=0\), these conditions force \(y=0\); if \(y=1\), they force \(x^2=1\). Thus the largest invariant subset of \(Z\) is precisely \(\{E_0,E_+,E_-\}\). The omega-limit set is connected and therefore a singleton, so the trajectory converges to one of these equilibria. For \(x(0)\ne0\), the exact formula
\[
 x(t)=x(0)\exp\left(\int_0^t(1-y(s))\,ds\right)
\]
precludes convergence to \(E_0\): if \(y(t)\to0\), its logarithmic growth rate tends to \(1\), contradicting boundedness. Sign preservation chooses \(E_+\) for positive \(x(0)\) and \(E_-\) for negative \(x(0)\). On \(x=0\), the equation reduces to \(\ddot y+a\dot y+y=0\). For \(a<0\) both characteristic roots have strictly positive real part, so only the zero solution is forward bounded.

**3. The critical parameter.** When \(a=0\), the zero-derivative set is
\[
 Z=\{x=0\}\cup\{y=1\}.
\]
The entire plane \(x=0\) is invariant and carries \(\ddot y+y=0\). To remain in the other branch \(y=1\), one needs \(z=0\), then \(x^2=1\). Hence the largest invariant subset is the disjoint union of \(x=0\) and the points \(E_+,E_-\). By connectedness, a bounded forward trajectory has omega-limit contained wholly in the plane or in one of the two isolated equilibria. If \(x(0)\ne0\) and its omega-limit were in the plane, then \(x(t)\to0\) and, since the orbit is bounded, integration of \(\dot z=x^2-y\) gives
\[
\frac1T\int_0^T y(t)\,dt
=\frac1T\int_0^T x(t)^2\,dt-\frac{z(T)-z(0)}{T}\longrightarrow0.
\]
But the exact logarithmic identity then yields
\[
\frac1T\log\frac{|x(T)|}{|x(0)|}
=1-\frac1T\int_0^T y(t)\,dt\longrightarrow1,
\]
contradicting boundedness. Thus the omega-limit is the equilibrium of the same sign. If \(x(0)=0\), the harmonic formula in the finding follows directly from the planar linear system.

**4. Compact stationary measures.** For any compactly supported invariant probability \(\mu\), invariance and differentiability imply \(\int\dot L\,d\mu=0\). For \(a\le0\), \(\dot L\ge0\), hence the invariant support of \(\mu\) lies in the largest invariant subset of \(Z\) established above. At \(a<0\), this forces an arbitrary convex combination of the three equilibrium masses. At \(a=0\), the plane is foliated by harmonic circles on which the only invariant probability is normalized angle measure; disintegration by radius and optional atoms at \(E_\pm\) yields exactly the described measures. Conversely, each listed measure is invariant.

## Verification
The standalone `check.py` uses exact SymPy arithmetic and asserts: the displayed \(\dot L\) identity; vanishing of the vector field at all three equilibria; the harmonic-circle solution formula; and the equilibrium characteristic polynomials. Run `python check.py` with SymPy available. The proof of omega-limit convergence and the complete measure classification is analytical, not inferred from finite experiments or numerical integration.

## Relationship to prior work
Sprott, *Simplest Chaotic Flows with Involutional Symmetries*, International Journal of Bifurcation and Chaos 24 (2014), article 1450009, Eq. (8), introduced this reflection-symmetric model. Its treatment gives equilibria, the local Hopf threshold \(a=2\), and numerical attractor-merging/bifurcation observations at positive parameters. It does not establish the polynomial monotonicity identity above or classify all bounded forward trajectories and compact stationary measures at \(a\le0\). Li et al., *Symmetric Strange Attractors: A Review of Symmetry and Conditional Symmetry* (2023), revisit exactly this equation to illustrate coexistence and symmetry breaking; their discussion in Section 2.2 concerns attractor geometry, not the negative/zero-parameter omega-limit classification. The negative-damping boundary is therefore a distinct global dynamical question, although other older or unindexed equivalent analyses cannot be excluded categorically.

## Limitations
No bound is established for arbitrary positive-time trajectories; some solutions may be unbounded or fail global continuation. The theorem does not describe general compact invariant sets containing nonrecurrent connecting trajectories, and the classification of invariant measures must not be misread as classification of all compact invariant sets. The statement does not establish existence, uniqueness, or nonexistence of recurrent attractors for \(a>0\), including the numerically observed chaotic regime. The polynomial identity alone does not prove a novel general theorem for unrelated jerk equations. Historical priority remains subject to unindexed or differently formulated earlier sources and independent review.

## References
1. J. C. Sprott, “Simplest Chaotic Flows with Involutional Symmetries,” *International Journal of Bifurcation and Chaos* **24** (2014), 1450009, DOI: 10.1142/S0218127414500096. Author-hosted full text: https://sprott.physics.wisc.edu/pubs/paper407.pdf (Eq. (8), pp. 8–9).
2. C. Li, Z. Li, Y. Jiang, T. Lei and X. Wang, “Symmetric Strange Attractors: A Review of Symmetry and Conditional Symmetry,” *Symmetry* **15** (2023), 1564, DOI: 10.3390/sym15081564. Lawful full-text preprint: https://www.preprints.org/manuscript/202307.0510 (Section 2.2, Eq. (3)).
