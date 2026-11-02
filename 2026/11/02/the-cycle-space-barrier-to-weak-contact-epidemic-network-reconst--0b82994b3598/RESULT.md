# The cycle-space barrier to weak-contact epidemic network reconstruction

## Finding

For a finite susceptible–infected–susceptible (SIS) contact process with positive, known individual immigration and recovery rates, suppose the directed infection rates are jointly scaled by a known small contact multiplier. The derivative at zero contact intensity of the complete stationary joint infection law identifies all directional infection rates **if and only if the undirected contact graph is a forest**. In fact, the derivatives of individual prevalences and pairwise covariances already carry all information in the first derivative of the entire stationary law. The covariance slopes identify the undirected edges exactly. On a graph with \(n\) vertices, \(m\) undirected edges and \(c\) connected components, the local family of positive directed-rate assignments compatible with the complete first-order stationary law has precisely \(m-n+c\) free dimensions.

The restriction to *first-order response* matters: the statement neither asserts nor denies identifiability from a full nonzero-contact stationary law or from higher-order responses. It is an exact finite-population result, not a moment-closure approximation.

## Assumptions and scope

Let \(V=\{1,\ldots,n\}\) be finite, with \(n\ge 2\), and let \(X_i\in\{0,1\}\) indicate whether vertex \(i\) is infected. Fix known \(\alpha_i,\delta_i>0\). For distinct vertices, let \(\beta_{ji}\ge0\) be the rate of transmission from \(j\) to \(i\). Assume that for each unordered pair either both directions are strictly positive or both are zero. Let \(G=(V,E)\) be this (possibly unknown) undirected support graph. For a calibrated multiplier \(\varepsilon\ge0\), the continuous-time transitions at vertex \(i\) are

\[
0\longrightarrow1\quad\text{at rate}\quad \alpha_i+\varepsilon\sum_{j\ne i}\beta_{ji}X_j,
\qquad
1\longrightarrow0\quad\text{at rate}\quad\delta_i.
\]

All rates are otherwise constant and all local clocks are independent. Strictly positive immigration and recovery make the full \(2^n\)-state chain irreducible, so it has a unique stationary law \(\pi_\varepsilon\). Define

\[
s_i=\alpha_i+\delta_i,\qquad p_i=\alpha_i/s_i,\qquad
M_i=\left.\frac{d}{d\varepsilon}\mathbb E_{\pi_\varepsilon}X_i\right|_{\varepsilon=0},
\]
\[
C_{ij}=\left.\frac{d}{d\varepsilon}\operatorname{Cov}_{\pi_\varepsilon}(X_i,X_j)\right|_{\varepsilon=0}\qquad(i\ne j).
\]

These are exact population-level sensitivity quantities; the theorem does not assume that a finite sample determines them without error.

## Proof

**Step 1: exact response formula.** At zero contact, vertices are independent with probabilities \(p_i\). Let \(Y_i=X_i-p_i\). The unperturbed generator \(Q_0\) acts on \(Y_i\) as multiplication by \(-s_i\), and on \(Y_iY_j\), for distinct vertices, as multiplication by \(-(s_i+s_j)\). Write \(Q_\varepsilon=Q_0+\varepsilon Q_1\) and let \(\pi_0\) denote the product Bernoulli law. A direct incoming-minus-outgoing calculation for each binary configuration \(x\) gives

\[
\frac{(\pi_0Q_1)(x)}{\pi_0(x)}
=\sum_i\frac{x_i-p_i}{p_i}\sum_{j\ne i}\beta_{ji}x_j.
\]

With \(A_i=\sum_{j\ne i}p_j\beta_{ji}\), expansion into the independent, centered product basis yields

\[
\sum_i\frac{A_i}{p_i}Y_i
+\sum_{i<j}\left(\frac{\beta_{ji}}{p_i}+\frac{\beta_{ij}}{p_j}\right)Y_iY_j.
\]

The stationary distribution depends analytically on \(\varepsilon\) around zero because the finite irreducible generator has a simple stationary eigenvalue. The normalization and differentiated balance equation \(\pi'_0Q_0=-\pi_0Q_1\), together with reversibility of \(Q_0\), give the **entire first-order density**

\[
\boxed{\frac{\pi'_0(x)}{\pi_0(x)}=
\sum_i\frac{A_i}{p_i s_i}(x_i-p_i)
+\sum_{i<j}\frac{\beta_{ji}/p_i+\beta_{ij}/p_j}{s_i+s_j}
(x_i-p_i)(x_j-p_j).}
\]

Both sums have zero \(\pi_0\)-mean, and uniqueness follows because \(Q_0\) is invertible on mean-zero functions. Taking one- and two-site moments therefore gives the exact formulas

\[
\boxed{M_i=\frac{1-p_i}{s_i}\sum_{j\ne i}p_j\beta_{ji},}
\qquad
\boxed{C_{ij}=\frac{(1-p_i)(1-p_j)}{s_i+s_j}
\bigl(p_j\beta_{ji}+p_i\beta_{ij}\bigr).}
\]

In particular, \(C_{ij}>0\) exactly for \(\{i,j\}\in E\), and is zero for every nonedge. The displayed density formula shows that knowing all \(M_i\) and \(C_{ij}\) determines \(\pi'_0\) itself: no higher-order joint infection statistic supplies further *first-order* information.

**Step 2: a flow problem on the contact graph.** Define positive weighted directed contact strengths \(a_{j\to i}=p_j\beta_{ji}\), and compute from observed slopes

\[
U_i=\frac{s_iM_i}{1-p_i}=\sum_{j:\{i,j\}\in E}a_{j\to i},
\qquad
T_{ij}=\frac{(s_i+s_j)C_{ij}}{(1-p_i)(1-p_j)}
=a_{j\to i}+a_{i\to j}.
\]

Once the (already identified) undirected graph is fixed, each edge supplies one fixed sum \(T_{ij}\) of its two directional weights. The \(U_i\) are the incoming weighted sums at vertices. Choose any reference orientation of the \(m\) edges. Assigning one unknown directional strength to each edge, with the opposite strength set by \(T_{ij}\), transforms the vertex equations into a signed incidence-matrix system. Its rank is \(n-c\), since the incidence matrix of a graph with \(c\) connected components has rank \(n-c\). Therefore the affine solution fiber has dimension

\[
\boxed{m-(n-c)=m-n+c.}
\]

Since every supported directional rate is assumed strictly positive, the true solution is an interior point of the positive orthant. Small perturbations along the entire incidence kernel are still admissible, so the same number is the local dimension of the *positive* solution fiber, not merely an algebraic upper bound.

**Step 3: sharp identifiability dichotomy.** A forest has \(m=n-c\), so the fiber is a singleton. Alternatively, peel a leaf \(v\) whose neighbor is \(w\): \(U_v=a_{w\to v}\) and \(T_{vw}-U_v=a_{v\to w}\). Subtract the latter from \(U_w\), delete the leaf, and repeat. Dividing \(a_{j\to i}\) by the known positive \(p_j\) reconstructs every \(\beta_{ji}\). Isolated vertices carry no edges.

Conversely, if the graph has a cycle, add a small \(t\) to \(a_{j\to i}\) along each forward edge of an oriented cycle and subtract \(t\) on every reversed edge. The two directional weights on each cycle edge still sum to \(T_{ij}\), while each vertex gains one incoming \(+t\) and one incoming \(-t\), so every \(U_i\) remains unchanged. Small nonzero \(t\) preserves positivity but changes the directional transmission matrix. Independent cycles span the full \(m-n+c\)-dimensional ambiguity. By Step 1, the *complete stationary distribution derivative* is identical for all such assignments, finishing both directions of the theorem.

**Exact witness.** On a triangle with \(\alpha_i=\delta_i=1\) for every vertex, compare symmetric rates \(\beta_{ij}=2\) for all six directions with cyclic rates \(\beta_{12}=\beta_{23}=\beta_{31}=3\) and \(\beta_{21}=\beta_{32}=\beta_{13}=1\). Both have \(M_i=1/2\) for all three sites and \(C_{ij}=1/8\) for all three distinct pairs, and hence the same complete first-order stationary law, although their transmission matrices differ.

## Verification

The accompanying standalone standard-library script `verify.py` uses exact rational arithmetic, builds every finite-state generator explicitly, and checks the full differentiated stationary balance equation, all one- and two-site response identities, graph incidence ranks, constructive forest inversion, and the triangle alias. Running `python verify.py` returned `EXACT_CHECKS_OK 2505`. These are reproducibility tests of finite instances; the all-graph theorem is established by the preceding symbolic argument rather than finite enumeration.

## Relationship to prior work

Foxall (2014) introduces and analyzes a finite, directed contact process with spontaneous infection, including its exact generator and a reduced mean-field approximation; those model definitions and convergence results are prior work. The approximation explicitly discards pairwise dependence, so it does not imply the exact covariance response or its graph-cycle identifiability boundary. Sanders et al. (2013) derive a perturbative solution for a different deterministic, mobile-metapopulation SIS model, not the present stationary finite-state inverse problem. Cator and Van Mieghem (2014) establish nonnegative infection correlations, but not their zero-coupling coefficients or the directional reconstruction fiber. Rubido et al. (2014) study link detection from time-series correlations in coupled discrete-time maps, with different mechanisms and assumptions. Cai et al. (2016) develop approximate correlation-aware epidemic thresholds, not finite-state first-order inversion. Economou, Gómez-Corral and López-García (2015) develop exact finite-state SIS computational machinery, which is related but not known here to establish the constructive forest-versus-cycle theorem.

The intended distinction is therefore an exact first-order observation/identification result, **not** discovery of the contact process, generic Markov perturbation theory, nonnegative correlations, or the graph incidence-rank identity. The broad computational tools in prior work may facilitate independent derivations, and historical priority of the combined statement requires further verification.

## Limitations

The conclusion assumes calibrated contact scaling, known positive immigration and recovery rates, arbitrarily accurate response derivatives, and a fixed undirected support in which both transmission directions on each present edge are positive. Removing any of those assumptions creates additional inverse questions. First-order nonidentifiability on cycles does not establish nonidentifiability from nonlinear contact responses, interventions targeting individual edges, continuous-time trajectories, or unscaled stationary measurements. Statistical noise and finite-sample estimation error are not treated. No real-world transmission network or intervention effect is inferred from observational data.

## References

1. E. Foxall, *Convergence and monotonicity for a model of spontaneous infection and transmission*, Advances in Applied Probability 46 (2014), 560–584. https://doi.org/10.1239/aap/1401369707
2. L. P. Sanders, B. Söderberg, D. Brockmann, T. Ambjörnsson, *Perturbative solution to susceptible-infected-susceptible epidemics on networks*, Physical Review E 88 (2013), 032713. https://arxiv.org/abs/1304.3008
3. E. Cator, P. Van Mieghem, *Nodal infection in Markovian susceptible-infected-susceptible and susceptible-infected-removed epidemics on networks are non-negatively correlated*, Physical Review E 89 (2014), 052802. https://doi.org/10.1103/PhysRevE.89.052802
4. N. Rubido et al., *Exact detection of direct links in networks of interacting dynamical units*, New Journal of Physics 16 (2014), 093010. https://doi.org/10.1088/1367-2630/16/9/093010
5. A. Economou, A. Gómez-Corral, M. López-García, *A stochastic SIS epidemic model with heterogeneous contacts*, Physica A 421 (2015), 78–97. https://doi.org/10.1016/j.physa.2014.10.054
6. C.-R. Cai et al., *Solving the Dynamic Correlation Problem of the Susceptible-Infected-Susceptible Model on Networks*, Physical Review Letters 116 (2016), 258301. https://arxiv.org/abs/1606.02037
