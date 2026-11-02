# Cyclic-cover rigidity of weighted-variation stability for isotonic regression

## Finding
For any finite partially ordered set \(P\) whose **undirected Hasse cover graph is precisely a simple cycle** \(C_n\), with \(n\ge4\), weighted least-squares isotonic regression is globally nonexpansive in edge total variation **exactly when the edge-variation weights are uniform**, regardless of the observation masses.

More precisely, give vertex \(v\) a positive observation mass \(a_v\) and undirected cover edge \(e\) a positive variation weight \(w_e\). Let \(\Pi_a\) denote the metric projection onto the order cone in the squared norm \(\sum_v a_v|y_v|^2\), and set
\[
V_w(f)=\sum_{uv\in E(P)}w_{uv}|f(u)-f(v)|.
\]
Then
\[
\left[\forall y,z\in\mathbb R^{P}:\quad V_w(\Pi_a y-\Pi_a z)\le V_w(y-z)\right]
\quad\Longleftrightarrow\quad
\left[\forall e,e'\in E(P):\ w_e=w_{e'}\right].
\]
For equal weights the sharp global two-input Lipschitz constant is \(1\). For unequal weights it exceeds \(1\), and strict amplification occurs for arbitrarily close real data pairs.

## Assumptions and scope
The order relation is a finite partial order (not a directed cycle); its Hasse diagram is acyclic, with underlying *simple undirected* graph \(C_n\), \(n\ge4\). This cover condition excludes a redundant shortcut edge. The data are arbitrary real vectors. Observation masses \(a_v\) and variation weights \(w_e\) are independent and strictly positive. Each edge is counted exactly once in \(V_w\). A positive constant rescaling of all variation weights leaves the property unchanged.

## Proof
**1. Local linear pieces of the isotonic map.** Weighted least-squares isotonic projection onto a polyhedral order cone is a continuous piecewise-affine map. On each full-dimensional active-set cell, the coordinates pooled by the active cover equalities form connected components of the active-edge subgraph, and its linear part \(E_{\mathcal B}\) replaces the data on each component \(B\) by its \(a\)-weighted mean \(\sum_{i\in B}a_i h_i/\sum_{i\in B}a_i\). One way to see this is to write the Lagrange optimality equations with the active cover equalities fixed: all coordinates in each active component have one common fitted value, which minimizes the sum of weighted squared residuals on that component. The remaining strict inequalities and positive active multipliers persist inside a full-dimensional cell. At cell boundaries, continuity and finite piecewise-affinity allow one to integrate derivatives along an arbitrary segment.

Every connected proper subset of a simple cycle is a cyclic interval. Hence \(\mathcal B\) consists of disjoint cyclic intervals, with the all-vertices block also allowed.

**2. Uniform-edge cyclic-interval averaging is contractive.** Consider any partition of the cycle into cyclicly consecutive blocks \(B_1,\ldots,B_k\), with arbitrary positive averaging masses. For each block independently select a vertex \(X_j\in B_j\), with probability \(a_i/\sum_{u\in B_j}a_u\) for vertex \(i\in B_j\). Form the random blockwise-constant signal \(g\) whose value on \(B_j\) is \(h(X_j)\). Then \(\mathbb E g=E_{\mathcal B}h\). The case \(k=1\) gives zero variation. Otherwise, since the chosen representatives occur in their block order around the cycle, the clockwise paths between successive representatives partition the original edges of the cycle into disjoint directed paths. Thus the triangle inequality gives, for every selection,
\[
V_{\mathbf1}(g)=\sum_{j=1}^{k}|h(X_{j+1})-h(X_j)|\le\sum_{e\in E(P)}|\nabla_eh|=V_{\mathbf1}(h),
\]
where \(X_{k+1}=X_1\). Convexity and Jensen's inequality imply \(V_{\mathbf1}(E_{\mathcal B}h)\le V_{\mathbf1}(h)\). Integrating the piecewise-constant Jacobian of \(\Pi_a\) along the line segment from \(z\) to \(y\) yields
\[
V_{\mathbf1}(\Pi_a y-\Pi_a z)\le V_{\mathbf1}(y-z).
\]
The order cone has a nonempty strict interior (choose any strictly order-preserving assignment), on which \(\Pi_a\) is the identity. Therefore the sharp modulus is exactly \(1\).

**3. Every cover-edge two-vertex pool occurs locally.** Fix any oriented cover relation, whose underlying edge is \(e_i=\{i,i+1\}\) in cyclic numbering. There exists an order-feasible \(z\) with equality only across this cover and with every other cover inequality strict. Indeed, identify the two adjacent comparable vertices; the quotient order constraints remain acyclic, since a contrary path would make this relation transitively redundant. Take any strict topological rank for the quotient and pull it back to the original poset. Perturb the corresponding input \(y\) slightly into violation of this one constraint in its positive weighted normal direction. The unique projection then pools exactly the pair \(\{i,i+1\}\), with strict inequalities elsewhere. On a full-dimensional input neighborhood the local derivative is therefore
\[
(E_i h)_i=(E_i h)_{i+1}=\frac{a_i h_i+a_{i+1}h_{i+1}}{a_i+a_{i+1}},
\]
and \((E_i h)_j=h_j\) at all other vertices.

**4. The local variations force uniform weights.** For each \(i\), choose a test difference \(h\) with \(h_{i-1}=h_i=1\) and \(h_{i+1}=h_{i+2}=0\); other coordinates are arbitrary. Four indicated vertices are distinct because \(n\ge4\). Since only the three edges touching the pooled pair can change their variation, direct subtraction yields
\[
V_w(E_i h)-V_w(h)=
\frac{a_{i+1}w_{i-1}+a_i w_{i+1}}{a_i+a_{i+1}}-w_i.
\]
If \(\Pi_a\) were globally nonexpansive, every such local derivative would be nonexpansive, so for every cyclic index \(i\),
\[
w_i\ge\frac{a_{i+1}w_{i-1}+a_i w_{i+1}}{a_i+a_{i+1}}.
\]
Choose an index at which \(w_i\) is minimal. Both neighboring weights are at least \(w_i\), and both convex-combination coefficients are strictly positive. The inequality forces both neighbors to equal \(w_i\). Repeating around the connected cycle shows all weights equal. Conversely, if the weights differ, one of these inequalities fails; the corresponding locally realized \(E_i\) has an explicit input direction with positive variation gain. Arbitrarily short perturbations inside its open active cell give pairs \(y,z\) witnessing strict amplification. Together with Step 2 this proves the equivalence.

## Verification
The independent, exact-arithmetic supplementary checker is `verify.py` and requires only Python's standard library. Run `python verify.py`. It enumerates all cyclic-interval set partitions for cycle sizes \(4\) through \(7\), tests three positive mass profiles and all nonconstant zero-one signals for uniform-edge contraction, and checks strictly positive anisotropic local witnesses for multiple mass and weight profiles. It also reproduces a four-vertex diamond example.

For a diamond cover orientation \(0\prec1\prec2\) and \(0\prec3\prec2\), with equal observation masses and consecutive edge weights \((1,1,1,2)\), the pooled Jacobian on \(\{0,1\}\) sends \(h=(1,0,0,1)\) to \((1/2,1/2,0,1)\); the edge variation changes from \(2\) to \(5/2\), giving a local ratio \(5/4\). This is a feasible active-set Jacobian: take the fitted vector \(z=(0,0,2,1)\) and a nearby input with \(y_0>y_1\) so that only the first cover relation pools.

The finite tests support the algebra; they are not an exhaustive argument for arbitrary cycle lengths, masses or weights. The general theorem is proved in the preceding four steps.

## Relationship to prior work
Order-cone metric projections and their coordinate-order isotonicity are studied by Németh and Németh (2012, 2015). Weighted and unweighted isotonic regression on totally ordered chains is structurally distinct: its underlying cover graph is a path, and its boundary variation coordinates do not close into a cycle. Yang and Barber (2017) establish norm-contraction criteria for univariate chain isotonic regression; their chain criterion does not state or directly entail the cyclic-cover anisotropic rigidity above. Guyader and collaborators (2012) analyze iterative univariate isotone regression and its bounded-variation context rather than the stated two-input graph-edge seminorm. The result here gives the exact **cycle-cover** rigidity criterion across all positive observation masses, not a claim of novelty for chain algorithms or general order-cone existence.

## Limitations
The result treats finite real scalar quadratic isotonic regression, positive observation masses, and cycle-shaped **Hasse cover graphs** of at least four vertices. It does not classify arbitrary graph-shaped posets, arbitrary nonlinear loss functions, or all anisotropic Lipschitz constants when the weights differ; it only establishes strict amplification and characterizes the sharp contraction boundary. Research-literature coverage can be incomplete, particularly for older order-restricted regression sources; an implicitly equivalent statement cannot be categorically excluded.

## References
- A. B. Németh and S. Z. Németh, *Isotonicity of the projection onto monotone cone*, arXiv:1201.4677 (public preprint January 23, 2012).
- A. Guyader and collaborators, *A Geometrical Approach to Iterative Isotone Regression*, arXiv:1211.3930 (public preprint November 16, 2012).
- A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458 (public preprint March 29, 2015).
- F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852 (2017; cited for mathematical comparison, not cohort eligibility).
