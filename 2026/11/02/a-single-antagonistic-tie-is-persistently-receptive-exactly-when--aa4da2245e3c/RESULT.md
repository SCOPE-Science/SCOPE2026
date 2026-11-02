# A single antagonistic tie is persistently receptive exactly when it lies on a cycle

## Finding

**Theorem (one-antagonistic-edge criterion).** Let \(G=(V,E)\) be any finite connected simple undirected graph with \(|V|\ge2\). Give exactly one edge \(e=\{u,v\}\) a negative sign and every other edge a positive sign. Run the synchronous, self-inclusive Kann–Feng repulsive bounded-confidence update with one common strict confidence radius \(c>0\), as specified below. A **fully receptive equilibrium** is a fixed opinion vector for which \(|x_i-x_j|<c\) on every original edge. Such an equilibrium exists **if and only if** \(e\) is not a bridge of \(G\), equivalently if \(e\) belongs to a cycle.

When \(e\) is not a bridge, for each value of the invariant degree-weighted mean, there are **exactly two** fully receptive equilibria, interchanged by reflection about that mean. They are locally exponentially attracting on the invariant mean hyperplane. If \(R_G(u,v)\) denotes effective resistance between \(u\) and \(v\) when **all edges, including the antagonistic one, have unit positive electrical conductance**, then their exact opinion separation and minimum edge-receptivity margin are
\[
|x_u^*-x_v^*|=cR_G(u,v),\qquad
\min_{\{i,j\}\in E}\bigl(c-|x_i^*-x_j^*|\bigr)=c\bigl(1-R_G(u,v)\bigr)>0.
\]
For a bridge, \(R_G(u,v)=1\) and the only formal stationary profiles for a fixed antagonistic orientation lie exactly on the **excluded** confidence boundary. The theorem does not claim those boundary profiles are actual fixed points or that general trajectories converge to them.

In particular, the triangle is the smallest connected graph admitting such persistent, fully receptive antagonism. For an antagonistic edge of a cycle \(C_n\), the separation is \(c(n-1)/n\), whereas for an antagonistic edge of the complete graph \(K_n\), it is \(2c/n\) (\(n\ge3\)). These are exact statements for this update rule, not generic predictions for other signed-opinion models.

## Assumptions and scope

Let \(A_{ii}=1\) for all vertices and \(A_{ij}=A_{ji}\in\{-1,0,1\}\) for \(i\ne j\), with \(A_{uv}=-1\), positive signs on the remaining edges, and zero on nonedges. At integer time \(t\), put
\[
M_{ij}(t)=\begin{cases}
x_j(t)-x_i(t),&A_{ij}\ge0,\\
\operatorname{sign}(x_j(t)-x_i(t))\bigl(c-|x_j(t)-x_i(t)|\bigr),&A_{ij}=-1,\ x_j(t)\ne x_i(t),\\
\operatorname{sign}(j-i)c,&A_{ij}=-1,\ x_j(t)=x_i(t),
\end{cases}
\]
and update all vertices simultaneously by
\[
x_i(t+1)=x_i(t)+\frac{\sum_j A_{ij}M_{ij}(t)\,\mathbf 1_{|x_j(t)-x_i(t)|<c}}{\sum_j |A_{ij}|\,\mathbf 1_{|x_j(t)-x_i(t)|<c}}.
\]
The self term guarantees that denominators are positive. The index-based tie rule is irrelevant in the strictly ordered neighborhoods of the equilibria established here. No restriction is placed on the initial opinions outside those neighborhoods, and no claim is made about global convergence.

Write \(d_i\) for the ordinary unsigned graph degree and \(D=\operatorname{diag}(d_i+1)\). Let \(L\) be the **ordinary unsigned** unit-conductance graph Laplacian. Within every fully receptive trajectory chamber, define the conserved quantity
\[
\bar x_D=\frac{\sum_i(d_i+1)x_i}{\sum_i(d_i+1)}.
\]
For the orientation \(x_u<x_v\), let \(\psi\) be the uniquely \(D\)-centered solution of
\[
L\psi=\mathbf e_v-\mathbf e_u,\qquad \sum_i(d_i+1)\psi_i=0.
\]
The two equilibria of the theorem are exactly \(x^\pm=\bar x_D\mathbf1\pm c\psi\). The sign \(+\) corresponds to \(x_u<x_v\); the sign \(-\) to the reversed orientation. Translation of every opinion by the same constant is a neutral symmetry, so attraction is stated within fixed-\(\bar x_D\) hyperplanes.

## Proof

**1. Reduction within one fully receptive orientation chamber.** Whenever every original edge is receptive and \(x_u<x_v\), the negative-edge term at \(u\) contributes
\[
-\bigl(c-(x_v-x_u)\bigr)=(x_v-x_u)-c,
\]
while at \(v\) it contributes \((x_u-x_v)+c\). All other incident edges give ordinary opinion differences. Thus the entire synchronous map becomes the affine update
\[
\boxed{\ x'=P x+cD^{-1}(\mathbf e_v-\mathbf e_u),\quad P=I-D^{-1}L.\ }
\]
The matrix \(P\) is the transition matrix of the random walk choosing uniformly among each vertex and its ordinary neighbors. Because \(G\) is connected and every vertex has a self-loop in \(P\), it is irreducible and aperiodic. Its reversible stationary probabilities are \(\pi_i=(d_i+1)/\sum_j(d_j+1)\). Consequently \(1\) is a simple eigenvalue, all remaining eigenvalues have absolute value strictly below \(1\), and \(\bar x_D\) is conserved. For the opposite orientation, the affine forcing changes sign.

**2. Necessary fixed profiles.** An all-edge-receptive fixed point cannot have \(x_u=x_v\): the prescribed tie convention assigns one of the two nonzero forcings, and then the stationary equation yields an endpoint gap of the opposite nonzero sign (see below). For either strict ordering, stationarity of the affine update requires
\[
Lx=\pm c(\mathbf e_v-\mathbf e_u).
\]
Connectedness and the degree-weighted mean condition give exactly \(x^+=\bar x_D\mathbf1+c\psi\) and \(x^-=\bar x_D\mathbf1-c\psi\), with no further possibilities.

**3. Electrical resistance, extrema, and sharp boundary.** For the unit-conductance electrical network with current injected at \(v\) and extracted at \(u\), \(\psi\) is the node-voltage vector. The discrete harmonic maximum principle away from \(u,v\) implies
\[
\min_i\psi_i=\psi_u,\qquad \max_i\psi_i=\psi_v.
\]
The effective resistance is
\[
R_G(u,v)=\psi_v-\psi_u=(\mathbf e_v-\mathbf e_u)^TL^+(\mathbf e_v-\mathbf e_u)>0.
\]
The direct edge \(uv\) has conductance \(1\). If it is a bridge, it alone carries the unit source-to-sink current, so \(R_G(u,v)=1\). If it is on a cycle, removing \(uv\) leaves an alternative \(u\)-to-\(v\) path of positive conductance; the direct unit-conductance edge in parallel with that path (and any remaining network) gives \(0<R_G(u,v)<1\). Conversely, \(R_G(u,v)<1\) implies the edge is not a bridge.

For nonbridges, every pair of vertex potentials differs by at most \(R_G(u,v)<1\). Therefore every original edge is strictly inside the confidence radius at \(x^+\) and \(x^-\); moreover, the hostile endpoint gap has its stipulated nonzero sign. Both formal solutions are genuine equilibria. Because \(uv\) itself attains the largest possible potential gap, the minimum receptivity margin over all edges is exactly \(c(1-R_G(u,v))\). For bridges, the only stationary candidates have the hostile gap \(c\), violating the strict confidence condition; no fully receptive equilibrium exists.

**4. Local exponential attraction.** In the nonbridge case both the edge-receptivity inequalities and the hostile pair's strict orientation have a positive margin at each equilibrium. Hence there is an open neighborhood in which the full nonlinear update equals the same affine map of step 1. On any invariant hyperplane of constant \(\bar x_D\), subtraction of its appropriate equilibrium yields \(z'=Pz\) with \(\sum_i(d_i+1)z_i=0\). Reversibility makes \(P\) self-adjoint for the weighted inner product \(\langle z,w\rangle_D=\sum_i(d_i+1)z_iw_i\). Its operator norm on that mean-zero hyperplane is some \(\rho(G)<1\); therefore \(\|z(t)\|_D\le\rho(G)^t\|z(0)\|_D\). A sufficiently small initial ball cannot leave the orientation/receptivity chamber. This proves local exponential attraction with fixed weighted mean, rather than unsupported global convergence.

**5. Exact graph families and minimality.** Unit resistors on \(C_n\) provide a length-one route in parallel with a length-\(n-1\) route, giving \(R=(n-1)/n\). Symmetry of the unit complete graph yields \(R_{K_n}=2/n\). No connected graph on fewer than three vertices has a cycle; \(C_3\) does. This completes all claims.

## Verification

The accompanying standalone script `verify.py` uses exact rational Gaussian elimination for the graph Poisson equation and exact rational application of the original simultaneous update rule. It enumerates all connected labeled simple graphs of orders \(2,3,4,5\) and every possible choice of the single antagonistic edge: **4,294** graph/edge instances, including **1,067** bridge instances and **3,227** nonbridge instances. It verifies \(R=1\) precisely for bridges, the voltage extreme bound, both fixed-point identities, strict receptivity when \(R<1\), and conservation of the degree-weighted mean. It also checks cycle and clique formulas for orders \(3\) through \(16\), and iterates a rational perturbation of a four-cycle equilibrium for 45 steps. All script assertions passed. The arbitrary-graph theorem follows from the proof, not from these bounded tests.

To reproduce, run `python3 verify.py` using the Python standard library. No external datasets or dependencies are required.

## Relationship to prior work

Kann and Feng introduce the precise synchronous signed bounded-confidence update and establish selected convergence and final-diameter results, especially for all-repulsive networks. Their article does not derive an exact effective-resistance law or a bridge-versus-cycle classification for a single antagonistic edge in an otherwise attractive arbitrary connected graph [1]. A prior complete-network calculation for the same rule yields a sharp hostile-degree condition guaranteeing receptivity of **every** fully receptive initial state; its object is different: complete graphs, universal initial-state retention, and a graph-independent denominator. The present result concerns existence and local stability of two interior equilibria on **arbitrary connected** graphs, and the role of a single edge's cycle membership. The complete-network case alone does not imply this general classification.

Altafini and Ceragioli's signed bounded-confidence models impose sign preservation in **continuous-time** formulations; they do not supply this discrete, self-inclusive model's electrical criterion [2]. He and coauthors study other discrete signed bounded-confidence rules, also built around opinion-sign preservation, rather than the particular distance-to-confidence antagonistic force used here [3]. Homs-Dones, Devriendt and Lambiotte give an extensive effective-resistance treatment of general **continuous-time nonlinear consensus** flows, supplying an important methodological analogy. Their continuously differentiable odd edge-force framework does not itself cover the strict-cutoff, tie-discontinuous, degree-normalized synchronous map or establish the present criterion and discrete-time attraction [4].

## Limitations

Only one original edge is antagonistic. All other edges are positively weighted with **unit** weight, all original edges share the same strict confidence radius, and every vertex self-includes with weight one. The claim is about fixed states in which **every original edge remains receptive**; fixed states with some inactive edges are not classified. The attracting property is local and is exponential only after quotienting the neutral common-translation direction, or equivalently at fixed degree-weighted mean. No uniform rate independent of graph size is asserted. Boundary states with exact opinion gap \(c\), global orbit convergence, switching-time claims, multiple antagonistic edges, and heterogeneous thresholds remain outside scope. Bibliographic equivalence with uninspected specialized formulations cannot be excluded absolutely.

## References

[1] C. Kann and M. Feng, *A Repulsive Bounded-Confidence Model of Opinion Dynamics in Polarized Communities*, arXiv:2301.02210v1, 5 January 2023, https://arxiv.org/html/2301.02210v1 .

[2] C. Altafini and F. Ceragioli, *Signed bounded confidence models for opinion dynamics*, Automatica 93 (2018), 114–125, DOI:10.1016/j.automatica.2018.03.064.

[3] G. He, J. Liu, H. Hu and J.-A. Fang, *Discrete-time signed bounded confidence model for opinion dynamics*, Neurocomputing 425 (2021), 53–61, DOI:10.1016/j.neucom.2019.12.061.

[4] M. Homs-Dones, K. Devriendt and R. Lambiotte, *Nonlinear consensus on networks: equilibria, effective resistance and trees of motifs*, SIAM Journal on Applied Dynamical Systems 20 (2021), 1544–1570, arXiv:2008.12022, https://arxiv.org/abs/2008.12022 .
