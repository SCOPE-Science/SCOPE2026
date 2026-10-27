# An explicit periodic-orbit wedge in a triadic rock-paper-scissors replicator

## Finding
For the cyclic three-strategy replicator defined below, set
\[
a_*=\frac{1+4b+\beta-2\alpha}{3+2\alpha-\beta},\qquad
a_{\partial}=\frac{2b+1-\alpha}{1+\alpha}.
\]
For **every** parameter choice satisfying
\[
1<\alpha\le2,\quad 0<\beta<1,\quad b>\frac{\alpha-1}{2},\quad
 a\ge0,\quad a_*<a<a_{\partial},
\]
the equal-frequency equilibrium is locally asymptotically stable, the boundary heteroclinic three-cycle is locally attracting from the simplex interior, and **at least one periodic orbit lies in the interior and separates their attraction basins**. No uniqueness, hyperbolicity, or exact period of the orbit is asserted. The coexistence interval has the explicitly positive width
\[
a_{\partial}-a_*=
\frac{2(b+1)(1-\beta)}{(1+\alpha)(3+2\alpha-\beta)}.
\]
For example, \((a,b,\alpha,\beta)=(1/4,1,2,1/2)\) lies strictly in this interval: \(a_*=3/13<a=1/4<a_{\partial}=1/3\). This supplies a completely rational admissible parameter witness and a rigorous global interval of periodic-orbit existence, rather than an inference from numerical trajectories.

## Assumptions and scope
Consider proportions \((x,y,z)\) in the closed simplex \(\Delta=\{(x,y,z)\in[0,1]^3:x+y+z=1\}\). Put \(h=a+1\), \(k=b+1\) and define the fitness functions
\[
 f_1(x,y,z)=-k y(1+x+y)+h z(1+\beta x+\alpha z),
\]
\[
 f_2(x,y,z)=f_1(y,z,x),\qquad f_3(x,y,z)=f_1(z,x,y).
\]
These are exactly the pairwise payoff matrix and triadic payoff slices (equations (5)–(8)) in Griffin–Wu (2023): pairwise payoffs are \(0,-k,h\) in cyclic order and the quadratic correction consists of the indicated triadic terms. The evolutionary dynamics are
\[
\dot x=x(f_1-\bar f),\quad \dot y=y(f_2-\bar f),\quad
\dot z=z(f_3-\bar f),\qquad \bar f=xf_1+yf_2+zf_3.
\]
The simplex is forward invariant; its interior consists of initial conditions with all three populations present. Time is continuous. All parameters are dimensionless. The existence statement holds for every point in the stated **open interval in \(a\)** and for every other parameter choice in the displayed ranges.

## Proof
**1. Equilibria.** On \(z=0\), writing \(y=1-x\),
\[
 f_1-f_2=-2k(1-x)-hx\bigl(1+\beta(1-x)+\alpha x\bigr)<0\quad (0<x<1).
\]
Cyclic symmetry implies that each open edge has no equilibrium and carries a heteroclinic connection between vertices. The uniform point \(e=(1/3,1/3,1/3)\) is an interior equilibrium.

To exclude additional interior equilibria, let \(\omega=e^{2\pi i/3}\), \(U=x+\omega y+\omega^2z\), and \(F=f_1+\omega f_2+\omega^2f_3\). Direct expansion on \(x+y+z=1\) gives
\[
F=K U+L\overline U^{\,2},
\]
where
\[
\begin{aligned}
K={}&h\left(-\frac\alpha3+\frac\beta6-\frac12
+i\sqrt3\left(\frac\alpha3+\frac\beta6+\frac12\right)\right)
+k\left(\frac23+i\sqrt3\right),\\
L={}&h\left(-\frac{\alpha+\beta}{6}
+i\sqrt3\frac{\alpha-\beta}{6}\right)+\frac{k}{3}.
\end{aligned}
\]
Their squared-modulus difference simplifies to the strictly positive quantity
\[
|K|^2-|L|^2=\frac{h^2(\alpha^2+\alpha\beta+4\alpha+\beta+3)+hk(5\alpha+4\beta+7)+10k^2}{3}>0.
\]
At an interior equilibrium, all three fitnesses are equal, equivalently \(F=0\). Since \(|U|\le1\), \(KU+L\overline U^2=0\) and \(|K|>|L|\) force \(U=0\); hence \(x=y=z=1/3\). This also establishes uniqueness of the interior equilibrium independently of an assumption based only on cyclic symmetry.

**2. The interior sink.** The planar Jacobian at \(e\) has
\[
\operatorname{tr}J_e=\frac{1+4b+\beta-2\alpha-a(3+2\alpha-\beta)}{9},\qquad
\det J_e=\frac{|K|^2}{9}>0.
\]
Because \(3+2\alpha-\beta>0\), the trace is negative precisely for \(a>a_*\). The equilibrium is then a hyperbolic sink.

**3. The attracting heteroclinic boundary.** At each pure-strategy vertex, the eigenvalue along the outgoing edge is \(\lambda_u=h(1+\alpha)>0\), while the eigenvalue transverse to the incoming edge is \(-\lambda_s=-2k<0\). A local saddle transition maps an incoming transverse displacement \(r\) to a positive constant times \(r^{\lambda_s/\lambda_u}(1+o(1))\); the regular connecting-edge transitions have positive finite derivatives. The first-return map near the complete three-vertex boundary cycle consequently has the form
\[
 r\longmapsto C r^{\rho}(1+o(1)),\qquad
 \rho=\left(\frac{2k}{h(1+\alpha)}\right)^3,
\]
for some \(C>0\). Therefore the entire boundary cycle attracts an open interior collar when \(\rho>1\), equivalently \(a<a_{\partial}\). These local claims concern approach to the **cycle**, not convergence to an individual saddle.

**4. Periodic orbit.** In the displayed parameter interval both the sink and the heteroclinic boundary have nonempty, disjoint, open attraction basins in the connected open simplex. The basin boundary of the sink relative to the open simplex is nonempty and invariant. It is disjoint from a neighborhood of the sink and from a sufficiently thin boundary collar attracted to the heteroclinic cycle. Thus every orbit on that basin boundary has a nonempty compact omega-limit set in the **interior**, where Step 1 excludes all equilibria except the sink (which is not on the basin boundary). The Poincaré–Bendixson theorem implies that the omega-limit set is a periodic orbit. This periodic orbit belongs to the basin boundary and hence separates the two attraction regions. The argument proves existence, but not uniqueness or instability in the hyperbolic sense.

Finally, straightforward common-denominator subtraction gives the positive width displayed in the finding. The additional requirement \(b>(\alpha-1)/2\) ensures \(a_{\partial}>0\) and hence an admissible positive \(a\) interval.

## Verification
The accompanying `verify.py` independently reconstructs the three fitness polynomials from the published pairwise and triadic matrices and performs exact symbolic checks of the Fourier decomposition, the strictly positive squared-modulus identity, the planar Jacobian trace/determinant, the edge sign formula, the threshold gap and the rational example. Run using `python verify.py` with SymPy installed; the observed output was `EXACT_SYMBOLIC_IDENTITIES_OK`. The cycle existence itself is proved by the local saddle-return argument and Poincaré–Bendixson, **not** by a finite numerical search. The program does not certify the topological theorem or enumerate periodic orbits.

## Relationship to prior work
Griffin and Wu (2023) define this pairwise-plus-triadic rock-paper-scissors game, compute its interior linear stability threshold and numerically investigate unstable limit cycles and their persistence range. Those model definitions, the stability threshold and the general possibility of limit cycles are prior work. The contribution here is an explicit rigorous, all-parameter **global sufficient interval** in the original admissible regime that guarantees a periodic separatrix, proved from the simultaneous basin-attraction inequalities and a separate exact uniqueness-of-interior-equilibrium argument. In particular, it does not claim a new model or the first observation of a cycle.

Griffin, Feng and Wu (2023/2024) analyze spatial dynamics under **different** payoff matrices and a zero-mean-fitness specialization, with traveling waves and a related Hopf computation; that is not the same as the original aspatial fixed-\(b\) global wedge proved here. General planar coexistence and heteroclinic-boundary techniques are classical; the special-source calculations and explicit parameter interval are the model-specific content.

## Limitations
The theorem gives at least one periodic orbit but neither its exact period, number, stability type, nor basin area. The boundary \(a=a_{\partial}\), the Hopf threshold \(a=a_*\), and \(\beta=1\) are excluded because the strict attraction argument fails there; nothing is inferred about periodic orbits at those endpoints. This is an aspatial deterministic model, not a finite stochastic ecological population model. Literature priority beyond the inspected references, especially under equivalent planar-coordinate reductions, remains open to external confirmation. Self-review is not independent scientific validation.

## References
1. Christopher Griffin and Rongling Wu, *Higher Order Dynamics in the Replicator Equation Produce a Limit Cycle in Rock-Paper-Scissors*, arXiv:2301.02518 (first submitted 2023-01-06); *Europhysics Letters* 142 (2023), 33001, DOI:10.1209/0295-5075/accd93. Model and linear analysis in Sections II–III.
2. Christopher Griffin, Li Feng, and Rongling Wu, *Spatial Dynamics of Higher Order Rock-Paper-Scissors and Generalisations*, arXiv:2312.16722 (2023-12-27); *Journal of Physics A* 57 (2024), 185701. Sections II–IV and conclusion.
3. Steven M. Baer, Bingtuan Li, and Hal L. Smith, *Multiple limit cycles in the standard model of three species competition for three essential resources*, *Journal of Mathematical Biology* (2006), DOI:10.1007/s00285-005-0367-x. Different population model illustrating classical separatrix mechanisms.
4. Poincaré–Bendixson theorem and local saddle-transition estimates for planar hyperbolic heteroclinic cycles (standard planar dynamical-systems results).
