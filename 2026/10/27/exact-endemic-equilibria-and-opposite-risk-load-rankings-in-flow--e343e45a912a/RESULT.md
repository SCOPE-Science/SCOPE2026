# Exact endemic equilibria and opposite risk–load rankings in flow-regulated bipartite SIS networks

## Finding

A flow-regulated susceptible–infected–susceptible (SIS) model has an explicit, unique positive equilibrium on **every** complete bipartite graph, including unequal parts and stars. This gives a complete stationary-state classification in an irregular network family for which the source model generally offered approximations.

**Theorem.** Let \(m,n\ge1\) be integers, let \(\gamma>0\), and let \(B>0\) be the conserved sum of nodal infection-rate loads. Consider the dynamical system defined below on \(K_{m,n}\). Put

\[
B_c=\gamma\frac{m+n}{\sqrt{mn}}.
\]

For every \(B>0\), the only disease-free equilibrium has infection probabilities zero at all vertices and uniform nodal loads \(B/(m+n)\). If \(B\le B_c\), this is the **only equilibrium** in the biological state space. If \(B>B_c\), there is, in addition, exactly one equilibrium with positive infection at every vertex. Define

\[
\eta=\frac{(B/\gamma)\sqrt{mn}-(m+n)}{m\sqrt m+n\sqrt n}>0.
\]

At that equilibrium, each vertex in the part of size \(m\) has infection level and load

\[
x_L=\frac{\eta\sqrt n}{1+\eta\sqrt n},\qquad
\beta_L=\frac{\gamma}{\sqrt{mn}}(1+\eta\sqrt m),
\]

and each vertex in the part of size \(n\) has

\[
x_R=\frac{\eta\sqrt m}{1+\eta\sqrt m},\qquad
\beta_R=\frac{\gamma}{\sqrt{mn}}(1+\eta\sqrt n).
\]

For unequal part sizes, the two infection levels and the two infection-rate loads have *opposite* strict rankings: if \(m<n\), then \(x_L>x_R\) but \(\beta_L<\beta_R\); if \(m>n\), both inequalities reverse. The infection-rate loads are affine functions of the conserved total load \(B\) throughout the supercritical regime. The disease-free equilibrium is locally exponentially stable for \(B<B_c\) and linearly unstable for \(B>B_c\), relative to the fixed-total-load manifold.

## Assumptions and scope

The graph is a finite, unweighted, undirected simple complete bipartite graph \(K_{m,n}\), with no isolated vertices. For each vertex \(i\), let \(x_i(t)\in[0,1]\) be its infected fraction and \(\beta_i(t)\ge0\) its endogenous infection-rate load. With recovery rate \(\gamma>0\), the flow-regulated network SIS system is

\[
\dot x_i=\beta_i(1-x_i)\sum_{j\sim i}x_j-\gamma x_i,
\qquad
\dot\beta_i=\sum_{j\sim i}\bigl[\beta_j(1-x_i)-\beta_i(1-x_j)\bigr].
\]

These are equations (3) and (4) of Punzo's 2022 flow-driven SIS model, specialized to undirected networks. The sum \(B=\sum_i\beta_i\) is conserved. An equilibrium means both derivatives vanish, with infection fractions in \([0,1]\) and nonnegative loads adding to \(B\). The theorem classifies equilibria, not arbitrary trajectories, stochastic finite-population extinction probabilities, or time-varying graph structures.

## Proof

**1. Boundary alternatives and strict positivity.** At any equilibrium, \(x_i<1\), since \(\dot x_i=-\gamma\) when \(x_i=1\). Because \(B>0\) and the graph is connected, all loads are strictly positive at equilibrium: if \(\beta_i=0\), then the load equation, with \(1-x_i>0\), forces \(\beta_j=0\) for every neighbor; connectedness contradicts \(B>0\). If some \(x_i=0\) at equilibrium, its infection equation and \(\beta_i>0\) force all neighboring infection fractions to vanish. Connectedness then gives \(x=0\) everywhere. Thus any nonzero-infection equilibrium is strictly positive at every vertex.

**2. Detailed balance on any undirected connected graph.** Fix an equilibrium and write \(u_i=\beta_i/(1-x_i)\). The load equations become

\[
0=\sum_{j\sim i}(1-x_i)(1-x_j)(u_j-u_i).
\]

Multiplying the equation for vertex \(i\) by \(u_i\), summing over vertices, and grouping undirected edges yields

\[
0=-\sum_{\{i,j\}\in E}(1-x_i)(1-x_j)(u_i-u_j)^2.
\]

Every coefficient is positive, so \(u_i\) is constant across a connected graph. Therefore

\[
\beta_i=c(1-x_i),\qquad
c=\frac{B}{\sum_j(1-x_j)}>0.
\]

In particular, at \(x=0\), every \(\beta_i=B/(m+n)\). This proves uniqueness of the disease-free equilibrium.

**3. Bipartite class symmetry is forced, not assumed.** At a positive equilibrium, define the positive sum \(S_R=\sum_{j\in R}x_j\). For every vertex \(i\) in the part \(L\) of size \(m\), substitution of step 2 into the infection equation gives

\[
\frac{x_i}{(1-x_i)^2}=\frac{cS_R}{\gamma}.
\]

The function \(z\mapsto z/(1-z)^2\) is strictly increasing on \((0,1)\). Hence all \(m\) infection levels in \(L\) coincide. Repeating for \(R\) forces class-constant infection levels \(x_L,x_R\) and, by step 2, class-constant loads \(\beta_L,\beta_R\).

**4. Solve the two class equations.** The remaining equations are

\[
cn(1-x_L)^2x_R=\gamma x_L,\qquad
cm(1-x_R)^2x_L=\gamma x_R.
\]

Taking the positive square root after dividing these equations shows

\[
\sqrt m\,\frac{x_L}{1-x_L}
=\sqrt n\,\frac{x_R}{1-x_R}.
\]

There is thus a unique parameter \(\eta>0\) with

\[
\frac{x_L}{1-x_L}=\eta\sqrt n,\qquad
\frac{x_R}{1-x_R}=\eta\sqrt m.
\]

Substitution into either class equation gives

\[
c=\frac{\gamma}{\sqrt{mn}}(1+\eta\sqrt n)(1+\eta\sqrt m).
\]

Using \(\beta_L=c(1-x_L)\) and \(\beta_R=c(1-x_R)\) yields the loads in the theorem. The conserved-mass condition is

\[
B=m\beta_L+n\beta_R
=\frac{\gamma}{\sqrt{mn}}
\bigl[m+n+\eta(m\sqrt m+n\sqrt n)\bigr].
\]

It admits a positive \(\eta\) if and only if \(B>B_c\), and then \(\eta\) is exactly the unique value displayed in the theorem. Conversely, substituting these expressions directly into the original nodewise differential equations makes every derivative zero. Thus the positive equilibrium exists precisely above threshold and is unique. Steps 1–2 exclude any further boundary equilibria.

**5. Opposite rankings and threshold stability.** For \(\eta>0\), the odds of \(x_L\) and \(x_R\) are proportional to \(\sqrt n\) and \(\sqrt m\), while the loads \(\beta_L\) and \(\beta_R\) have increments proportional to \(\sqrt m\) and \(\sqrt n\). This proves strict opposite rankings for \(m\ne n\). The displayed mass relation makes \(\eta\), and hence each load, affine in \(B\). Finally, at the disease-free equilibrium the infection linearization is \((B/(m+n))A-\gamma I\), while the load-only linearization on the conserved-mass subspace is \(-L_G\); the full Jacobian is block triangular in that ordering. The adjacency spectral radius of \(K_{m,n}\) is \(\sqrt{mn}\), and the Laplacian is strictly positive away from its constant eigenvector. Therefore the disease-free equilibrium is locally exponentially stable for \(B<B_c\) and has a positive eigenvalue for \(B>B_c\). The equality case is nonhyperbolic and no rate claim is made there.

## Verification

The accompanying `verify_bipartite_flow_sis.py` implements the original vertexwise ODE independently of the closed-form class equations. Running `python3 verify_bipartite_flow_sis.py` with Python 3 and its standard library evaluates the claimed equilibrium on complete bipartite graphs, directly checks zero nodewise derivatives and exact conservation of total load, and tests the opposite-ordering boundary.

On the inspected package path, verification passed 128 **exact rational** supercritical cases (with square part sizes), 972 additional floating-point supercritical cases (maximum absolute nodewise residual \(4.885\times10^{-15}\)), and 363 disease-free cases. These finite tests are independent arithmetic corroboration of the formulas, not substitutes for the proof of infinitely many cases. No stochastic process was simulated or inferred from these ODE tests.

For example, with \((m,n)=(1,4)\), \(\gamma=1\) and \(B=3\), the formulas give \(\eta=1/9\), \((x_L,x_R)=(2/11,1/10)\) and \((\beta_L,\beta_R)=(5/9,11/18)\), with exact total load \(5/9+4(11/18)=3\). The threshold is \(5/2\).

## Relationship to prior work

Punzo, *An SIS network model with flow driven infection rates* (2022), defines precisely the coupled infection–load equations used here, proves conserved total load, and obtains a general spectral threshold (Sections 2–4). Sections 5.2–5.3 provide approximate endemic formulas on general strongly connected graphs and an exact expression for **balanced degree-regular** graphs. The source's conclusion expressly distinguishes the exact regular case from the general approximations. Balanced \(K_{m,m}\) belongs to that covered case; the present contribution is the complete exact classification for **unequal** \(K_{m,n}\), including stars, together with the forced symmetry and opposing infection–load rankings. The spectral threshold is inherited, not claimed as a novel generic threshold. Likewise, Punzo's weighted-Laplacian stationary-load Lemma 3 already implies the undirected proportionality \(\beta_i\propto 1-x_i\); the reversed infection–load ordering is presented as an explicit interpretation of the new unequal-biclique formulas, not as a separately original phenomenon.

Mei, Mohagheghi, Zampieri and Bullo (2017) analyze the standard deterministic network SIS system with a **fixed scalar** infection rate at each node; their equilibrium and uniqueness theorems therefore do not determine the coupled endogenous-load equilibria here. Meloni, Arenas and Moreno (2009) study packet-driven infection on scale-free networks, where the transmission mechanism and routing quantities differ from the present continuous-time, receiver-health-regulated load redistribution. These comparisons rely on material read from the cited primary texts; they are not statements of exhaustive literature coverage.

## Limitations

The results concern the deterministic flow-regulated mean-field ODE, not exact finite-population SIS probabilities. The theorem classifies stationary states and local stability of the disease-free state; it does **not** independently establish global convergence or local stability of the positive equilibrium. It assumes undirected, unweighted, fully cross-connected bipartite graphs, homogeneous positive recovery, conserved positive total load, and receiver-health-dependent flow. It does not cover directed bicliques, heterogeneously weighted edges, changing recovery rates, or arbitrary graph families. The result may have equivalent algebraic formulations in unindexed or later work; a search finding no such formulation is not a mathematical uniqueness guarantee.

## References

1. G. Punzo, “An SIS network model with flow driven infection rates,” *Automatica* **137** (2022), 110107. DOI: 10.1016/j.automatica.2021.110107. Open full text: https://eprints.whiterose.ac.uk/id/eprint/178189/13/1-s2.0-S0005109821006361-main.pdf . Online publication dated 10 January 2022 in the institutional repository record.
2. W. Mei, S. Mohagheghi, S. Zampieri and F. Bullo, “On the Dynamics of Deterministic Epidemic Propagation over Networks,” *Annual Reviews in Control* **44** (2017), 116–128. Preprint: https://arxiv.org/abs/1701.03137 .
3. S. Meloni, A. Arenas and Y. Moreno, “Traffic-driven epidemic spreading in finite-size scale-free networks,” *PNAS* **106** (2009), 16897–16902. DOI: 10.1073/pnas.0907121106. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2761312/ .
