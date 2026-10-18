# Finite symmetric dispersal attains the logistic biomass bound exactly under directed-cut feasibility

## Finding

For any integer \(n\ge 2\), positive growth rates \(r_i\), positive carrying capacities \(k_i\), and any undirected allowed-corridor graph \(H\) on \(\{1,\ldots,n\}\), consider the logistic patch system
\[
 \dot x_i=r_i x_i\left(1-\frac{x_i}{k_i}\right)
 +\sum_{j:\{i,j\}\in E(H)}d_{ij}(x_j-x_i),\qquad
 d_{ij}=d_{ji}\ge0.
\]
Every finite choice of coefficients has exactly one strictly positive equilibrium \(p(d)\), which attracts every strictly positive initial state. The **known universal biomass bound** is
\[
 \sum_i p_i(d)\le B:=\frac12\left(\sum_i k_i+\sqrt{RS}\right),\qquad
 R=\sum_i r_i k_i,\quad S=\sum_i\frac{k_i}{r_i}.
\]
The **new characterization** determines precisely whether the known bound is actually attained by *finite symmetric migration on a prescribed graph*, and constructs all necessary migration coefficients.

Set
\[
 c=\sqrt{R/S},\qquad p_i^\star=\frac{k_i}{2}\left(1+\frac{c}{r_i}\right),\qquad
 g_i^\star=r_ip_i^\star\left(1-\frac{p_i^\star}{k_i}\right)=\frac{k_i}{4}\left(r_i-\frac{c^2}{r_i}\right).
\]
Orient each allowed edge with \(p_i^\star>p_j^\star\) from \(i\) to \(j\); discard edges joining equal target densities. Then the following statements are **equivalent**:

1. Some *finite* assignment of nonnegative symmetric edge conductances supported in \(H\) has equilibrium \(p^\star\), hence has total biomass \(B\).
2. For **every** vertex subset \(U\) with **no oriented edge leaving** \(U\), its net intrinsic production satisfies \(\sum_{i\in U}g_i^\star\le0\).

In particular, on a complete allowed graph with all target densities distinct and sorted \(p_1^\star<\cdots<p_n^\star\), the criterion is just \(\sum_{i=1}^m g_i^\star\le0\) for each \(1\le m<n\). For arbitrary graphs, the test is a standard finite network-flow feasibility problem with a constructive solution. Ties require the full subset formulation; the distinct-target prefix test does not apply at ties.

## Assumptions and scope

All \(r_i,k_i\) are strictly positive; \(n\) is finite. Each undirected edge is an *option*, not an obligation: its realized coefficient can be zero, and all realized coefficients must be finite and nonnegative, with no upper capacity imposed. There is no immigration from outside the landscape, no asymmetric transportation and no dispersal mortality. The allowable graph may be disconnected, and target densities may coincide. The equilibrium and convergence statements concern strictly positive initial data. The earlier upper bound \(B\) is not claimed as novel; the object of the characterization is the exact attainability of that *already established* bound under a prescribed finite symmetric corridor architecture.

## Proof

**1. Unique globally attracting positive equilibrium.** Choose constant lower and upper state vectors \(\varepsilon\mathbf1\) and \(M\mathbf1\), with \(0<\varepsilon<\min_i k_i\) and \(M>\max_i k_i\). Their vector fields are respectively strictly positive and strictly negative, because symmetric diffusion annihilates constant vectors. Cooperative comparison produces a positive equilibrium between them by monotone limiting trajectories, including when \(H\) is disconnected. For uniqueness, let \(p,q\) be positive equilibria and suppose \(\alpha=\max_i p_i/q_i>1\), attained at \(i\). In that coordinate, subtracting \(\alpha\) times the equilibrium equation for \(q\) from the equation for \(p\) gives
\[
 0=-\frac{r_i}{k_i}\alpha(\alpha-1)q_i^2
 +\sum_jd_{ij}(p_j-\alpha q_j)<0,
\]
a contradiction. Interchanging \(p,q\) excludes the remaining inequality. For convergence, suitable multiples \(ap\le x(0)\le bp\), where \(0<a<1<b\), are strict sub- and supersolutions since the diffusion term is linear and
\(F_i(ap)=a(1-a)r_ip_i^2/k_i>0\), \(F_i(bp)=b(1-b)r_ip_i^2/k_i<0\). Their monotone limits are the unique equilibrium, squeezing all positive trajectories.

**2. Sharp ellipsoid geometry.** Summing stationary equations cancels migration and gives \(\sum_i r_i p_i(1-p_i/k_i)=0\). Completing squares gives the ellipsoid
\[
 \sum_i\frac{r_i}{k_i}\left(p_i-\frac{k_i}{2}\right)^2=\frac R4.
\]
Cauchy–Schwarz yields \(\sum_i p_i\le B\), with equality at the **unique** ellipsoid maximizer \(p^\star\) displayed in the Finding. In fact, for every positive stationary state on the ellipsoid the stronger exact deficit identity holds:
\[
 B-\sum_i p_i=\frac1c\sum_i\frac{r_i}{k_i}(p_i-p_i^\star)^2.
\]
To verify this identity, expand the right side and use the two equal ellipsoid norms \(\sum_i(r_i/k_i)(p_i-k_i/2)^2=\sum_i(r_i/k_i)(p_i^\star-k_i/2)^2=R/4\), together with \((r_i/k_i)(p_i^\star-k_i/2)=c/2\). Hence *equality in the known bound requires exactly \(p=p^\star\).* This step uses standard ellipsoid geometry and is not separately asserted as original.

**3. A directed flow formulation.** Orient each edge with unequal target coordinates from the greater to the lesser target. If a finite symmetric conductance realizes \(p^\star\), define the nonnegative oriented flux \(f_{ij}=d_{ij}(p_i^\star-p_j^\star)\) on that oriented edge. The stationary equation at vertex \(i\) becomes
\[
 \sum_{i\to j}f_{ij}-\sum_{j\to i}f_{ji}=g_i^\star.
\]
The total \(\sum_i g_i^\star\) is zero by the ellipsoid equation. Summing over any \(U\) with no outgoing oriented edge gives \(\sum_{i\in U}g_i^\star=-\sum_{j\notin U,\,j\to i\in U}f_{ji}\le0\), proving necessity.

**4. Sufficiency and finite construction.** Suppose the stated inequalities hold. Let \(P=\sum_{i:g_i^\star>0}g_i^\star\), equal to the absolute total negative production. Build a directed flow network with a source linked to each positive-production vertex \(i\) with capacity \(g_i^\star\), each negative-production vertex \(j\) linked to a sink with capacity \(-g_j^\star\), and each original greater-to-lesser target edge with capacity \(P\). By the max-flow/min-cut theorem, a flow of value \(P\) exists exactly when every cut has capacity at least \(P\). A cut retaining a set \(U\) of original vertices on the source side either crosses one original edge (and automatically has capacity at least \(P\)), or crosses no original edge and has capacity
\[
 P-\sum_{i\in U}g_i^\star.
\]
Our condition makes every such capacity at least \(P\). An integral-of-flux (not necessarily integer-valued) maximum flow therefore realizes all net divergences \(g_i^\star\). Put
\[
 d_{ij}=\frac{f_{ij}}{p_i^\star-p_j^\star}
\]
on every oriented edge \(i\to j\), and set all remaining coefficients to zero. The denominator is strictly positive, so these coefficients are finite, nonnegative and symmetric when copied to their undirected counterparts. They make \(p^\star\) stationary. By Step 1 it is the unique positive equilibrium. The case \(P=0\) is immediate with all conductances zero. This proves the equivalence.

**5. Distinct-target complete graphs.** With \(p_1^\star<\cdots<p_n^\star\), an outgoing-edge-free subset in the complete directed comparison graph is exactly an initial segment \(\{1,\ldots,m\}\), including the empty and full sets. Equivalently, if all prefix conditions hold, the chain of conductances
\[
 d_{m,m+1}=-\frac{\sum_{i=1}^m g_i^\star}{p_{m+1}^\star-p_m^\star},\qquad 1\le m<n,
\]
and all other conductances zero realizes the optimizer. Both numerator and denominator have the claimed signs.

## Verification

**Exact feasible witness.** For \((r_1,r_2,r_3)=(1,2,3)\), \((k_1,k_2,k_3)=(1,2,90/11)\), and the chain of edges \(\{1,2\},\{2,3\}\), one has
\[
 R=325/11,\quad S=52/11,\quad c=5/2,\quad p^\star=(7/4,9/4,15/2),
 \quad g^\star=(-21/16,-9/16,15/8).
\]
The finite edge rates \(d_{12}=21/8\), \(d_{23}=5/14\) solve every stationary equation exactly; the equilibrium total is \(B=23/2\). The target is nonuniform and the interaction network is not complete, so this is a genuine finite-rate corridor realization rather than a perfect-mixing limit.

**Exact obstruction.** For \((r_1,r_2,r_3)=(1,2,3)\), \((k_1,k_2,k_3)=(3,1,2)\), even with **all** edges available, \(R=11\), \(S=25/6\), \(c=\sqrt{66}/5\), and the second patch is the unique lowest target-density vertex. Its intrinsic production is \(g_2^\star=17/100>0\); the singleton set \(\{2\}\) has no outgoing oriented edge. Thus no finite nonnegative symmetric dispersal rates, on *any* undirected network, can attain \(B\) for these rates and capacities.

The included standard-library script checks the two exact witnesses and independently tests the cut condition against exact rational maximum flow on deterministically generated small directed comparison graphs. Finite tests are not substitutes for the universal proof above.

## Relationship to prior work

Ruiz-Herrera and Torres (2020), especially Proposition 1.1, Eq. (14), and the supplementary discussion, **already establish the ellipsoid biomass upper bound** and study network architectures in low- and high-mobility regimes; they describe intermediate finite mobility largely numerically. Elbetch, Benzekri, Massart, and Sari (2021) develop the symmetric multi-patch logistic model and equilibrium-total comparisons, including its ellipsoid balance. Jorba-Cuscó and colleagues (2023 preprint; 2024 journal) analytically optimize a two-patch problem with a specified diffusion parameter. None of these inspected statements gives an all-graph if-and-only-if *finite symmetric rate-design* criterion with a cut certificate and explicit constructive rates at the ellipsoid maximizer. The max-flow/min-cut component is a classical theorem used here as a tool, not claimed as new.

## Limitations

The result is about **exactly reaching the known universal biomass bound**, not finding the optimal attainable total below it when a graph fails the cut test. Edge rates are unbounded above but each chosen rate is finite; strictly positive rates on every allowed edge, fixed budgets, prescribed common scaling of conductances, transport asymmetry, and dispersal loss are not covered. The necessary condition rules out equality but does not itself optimize submaximal configurations. 

## References

1. A. Ruiz-Herrera and P. J. Torres (2020), *Optimal Network Architectures for Spatially Structured Populations with Heterogeneous Diffusion*, The American Naturalist 196, 29–44, doi:10.1086/708806. Relevant manuscript and supplementary mathematical appendix: Proposition 1.1, Theorems 1.3–1.4.
2. B. Elbetch, T. Benzekri, D. Massart and T. Sari (2021), *The multi-patch logistic equation*, Discrete and Continuous Dynamical Systems B 26, 6405–6424, doi:10.3934/dcdsb.2021025; early online 2021-01-13.
3. M. Jorba-Cuscó, R. I. Oliva-Zúniga, J. Sardanyés and D. Pérez-Palau (2023), *Dispersal-enhanced resilience in two-patch metapopulations: origin's instability type matters*, arXiv:2308.01364v1 (2023-08-02); revised journal version doi:10.1007/s12064-023-00411-2.
4. Classical max-flow/min-cut theorem for finite directed capacitated networks.
