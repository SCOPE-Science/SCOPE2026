# Sharp recurrence threshold and critical relaxation in a quadratic chaotic flow

## Finding
Consider the polynomial flow
\[
\dot x=a y,\qquad \dot y=x+z^2,\qquad \dot z=b+cx+dz,
\]
with \(a<0\), \(d<0\), \(c\ne 0\), and \(b\in\mathbb R\). Put \(\Delta=d^2+4bc\) and \(z_*=d/(2c)\). Then:

1. A nonempty compact invariant set exists **if and only if** \(\Delta\ge0\). For \(\Delta<0\), there is no bounded forward-complete trajectory; no claim of global existence for unbounded initial data is made.
2. At the sharp boundary \(\Delta=0\), the only compact invariant set is \(\{E_*\}\), where \(E_*=(-z_*^2,0,z_*)\). Every bounded forward-complete trajectory converges to \(E_*\).
3. For every compactly supported invariant probability measure \(\mu\),
\[
\int (z-z_*)^2\,d\mu=\frac{\Delta}{4c^2}.
\]
At \(\Delta=0\), the only such probability measure is the point mass at \(E_*\).
4. At \(\Delta=0\), there is a global strong-stable set \(W^{ss}(E_*)\), locally a smooth two-dimensional manifold, comprising precisely the initial states whose trajectories converge exponentially to \(E_*\). Every bounded forward-complete trajectory outside \(W^{ss}(E_*)\) satisfies
\[
\lim_{t\to\infty} t\bigl(z(t)-z_*\bigr)=\frac1c.
\]
Trajectories in the global \(W^{ss}(E_*)\) converge exponentially, and their corresponding limit is zero. The equilibrium itself has limit zero.

## Assumptions and scope
The vector field is exactly the Zhao–Lin–Dai three-dimensional modified Sprott N system, for real parameters satisfying \(a<0\), \(d<0\), \(c\ne0\). An invariant set here is compact, nonempty, and invariant under the complete flow restricted to it. Bounded forward-complete means that the solution exists for every \(t\ge0\) and has bounded forward image. No assertion is made that every solution of this polynomial vector field exists globally. The strong-stable manifold \(W^{ss}(E_*)\) means the **global** set of initial states with exponential convergence to \(E_*\), not merely its local portion. The asymptotic law is for each bounded forward-complete trajectory, not for arbitrary escaping or finite-time-blow-up trajectories. The comparison class for invariant measures is compactly supported Borel probability measures invariant under the flow.

## Proof
**Exact monotone observable.** Let \(Q=z-cy\). Direct substitution into the original equations gives the polynomial identity
\[
\dot Q=b+dz-cz^2=\frac{\Delta}{4c}-c(z-z_*)^2.\tag{1}
\]
In particular, if \(\Delta<0\), then, on the entire time interval of any solution,
\[
-\operatorname{sgn}(c)\bigl(Q(t)-Q(0)\bigr)
=\int_0^t \left(\frac{|\Delta|}{4|c|}+|c|(z(s)-z_*)^2\right)\,ds
\ge\frac{|\Delta|}{4|c|}t.\tag{2}
\]
Thus a forward-complete solution cannot be bounded. Conversely, for \(\Delta\ge0\), choose a root \(z_e=(d\pm\sqrt\Delta)/(2c)\) of \(b+dz-cz^2=0\). The corresponding \((-z_e^2,0,z_e)\) is an equilibrium and therefore forms a compact invariant set. This proves the exact threshold without assuming the existence of any global attractor.

**Critical rigidity.** At \(\Delta=0\), (1) becomes \(\dot Q=-c(z-z_*)^2\). If a forward-complete orbit is bounded, then \(Q(t)\) is monotone and bounded, and hence \(\int_0^\infty (z(t)-z_*)^2dt<\infty\). Along such an orbit, \(\dot z=b+cx+dz\) is bounded, so uniform continuity and the elementary integral lemma imply \(z(t)\to z_*\). More directly, the nonempty compact omega limit set is contained in the zero-derivative set \(\{z=z_*\}\) by LaSalle's invariance principle. On a trajectory that remains entirely in this set, \(\dot z=0\) forces \(x=-z_*^2\); then \(\dot x=0\) and \(a\ne0\) force \(y=0\). Therefore the maximal invariant subset is the singleton \(E_*\), proving convergence. If \(K\) is a nonempty compact **two-sided** invariant set, \(Q(t)\) is bounded and monotone on every orbit for all \(t\in\mathbb R\). Its limits at both ends exist; every alpha- or omega-limit orbit has constant \(Q\) and thus lies in \(z=z_*\), whose only invariant subset is \(E_*\). Hence every orbit in \(K\) has both ends at \(E_*\). But \(Q\) has the same limit \(Q(E_*)\) at both ends; hence \(Q\) must be constant, forcing \(z=z_*\), and thence the entire orbit to be \(E_*\). This proves the unique compact invariant set, including the exclusion of nonconstant complete homoclinic orbits.

**Invariant measures.** For a compactly supported invariant probability measure, integrate (1). Invariance and compact support give \(\int \dot Q\,d\mu=0\), hence the displayed second-moment identity. At the boundary its left side vanishes; positivity forces the support into \(z=z_*\), whose only invariant subset is \(E_*\). For \(\Delta<0\) the identity is impossible, consistently with the absence of compact invariant sets.

**Sharp boundary rate.** Translate to \(u=z-z_*\), \(v=x+z_*^2\), \(w=y\) and specialize \(\Delta=0\). The exact equations become
\[
\dot v=aw,\qquad \dot w=v+(d/c)u+u^2,\qquad \dot u=cv+du.\tag{3}
\]
The linear characteristic polynomial at \(E_*\) is \(\lambda(\lambda^2-d\lambda-a)\). Because \(a<0\), \(d<0\), the two nonzero roots have negative real parts. Standard smooth center-manifold and stable-foliation theory therefore gives a one-dimensional local center manifold together with a two-dimensional local strong-stable manifold. In the center coordinate \(u\), solving the quadratic invariance equations gives
\[
v=-\frac dc u-u^2+O(u^3),\qquad
w=\frac da u^2+O(u^3),\qquad
\dot u=-cu^2+O(u^3).\tag{4}
\]
For any nonconstant center-manifold trajectory converging to zero as \(t\to\infty\), necessarily \(cu>0\) eventually, and \(d(1/u)/dt=c+O(u)\). Since \(u\to0\), integration yields \((1/u(t))/t\to c\), or \(t u(t)\to 1/c\). Any sufficiently small forward trajectory converging to the equilibrium is exponentially tracked by a center-manifold trajectory; the tracked trajectory is identically the equilibrium precisely when the original trajectory eventually lies on the local strong-stable leaf (equivalently, its initial point lies in the global \(W^{ss}(E_*)\)), and otherwise has the same \(1/(ct)\) asymptotics. Every globally bounded forward-complete orbit eventually enters the relevant neighborhood by the preceding critical rigidity. This proves the global-on-bounded-orbits dichotomy. The scalar asymptotic does not assert a uniform-in-initial-data convergence time.

## Verification
The included executable `verify.py` recomputes (1), the equilibrium substitution, the critical characteristic polynomial, and all quadratic center-manifold invariance residuals with symbolic polynomial arithmetic. Run `python verify.py` with SymPy available; its assertions fail on any mismatch. The proof of global convergence uses a monotonicity/invariance argument, and the critical rate uses standard center-manifold/stable-foliation theory rather than finite simulation. No finite computation is used as an infinite-dimensional or all-time certificate.

## Relationship to prior work
Zhao, Lin, and Dai introduced this flow and established the equilibrium discriminant \(\Delta\), dissipativity, local equilibria, and a numerically observed Feigenbaum-like attractor (2014, Sections 2–4). Their text explicitly distinguishes numerical observations of boundedness from a proof. The present result uses a different invariant observable to promote the source's **equilibrium** boundary to an exact boundary for **every compact invariant dynamical set**, prove collapse and unique stationary statistics at equality, and quantify a universal critical approach rate. These claims do not follow from the source's equilibrium count alone: systems without equilibria can in general have compact periodic or chaotic attractors. General work on other chaotic flows with discriminant-based recurrence thresholds does not furnish an implication for these specific equations without the identity (1). Other papers and indexing gaps remain possible sources of overlapping results.

## Limitations
The result does not classify the periodic or chaotic invariant sets on the \(\Delta>0\) side or establish global existence for arbitrary initial conditions. The exact \(1/(ct)\) limit applies at \(\Delta=0\) only to bounded forward-complete trajectories off the global strong-stable manifold; it is not a uniform decay estimate. The literature comparison is not a proof that no unindexed equivalent statement exists. No independent review has been conducted.

## References
1. H. Zhao, Y. Lin, and Y. Dai, “A New Feigenbaum-Like Chaotic 3D System,” *Discrete Dynamics in Nature and Society* (2014), Article 328143, first published 13 March 2014, https://doi.org/10.1155/2014/328143. Full open-access source examined, Sections 2–5.
2. S. Wiggins, *Introduction to Applied Nonlinear Dynamical Systems and Chaos*, 2nd ed., Springer, 2003. Standard local center-manifold and stable-foliation theory (used only as a standard theorem, not as a claim about this particular system).
