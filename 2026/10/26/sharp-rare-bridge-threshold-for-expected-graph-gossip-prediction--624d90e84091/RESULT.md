# Sharp rare-bridge threshold for expected-graph gossip predictions

## Finding
Fix integers \(L\ge1\) and \(H\ge2\). Take the unit-conductance path on vertices \(0,1,\ldots,2L+H\). Its endpoints are stubborn agents with fixed opinions \(0\) and \(1\), and all other vertices are regular agents. Independently add one shortcut edge between \(u=L\) and \(v=L+H\) with probability \(p\in(0,1)\), sampling this graph **once**, before gossip dynamics. The comparison *expected graph* retains the original path and assigns shortcut conductance \(p\). Let \(m^{(t)}\) be the limiting vector of **expected** opinions for a deterministic shortcut of conductance \(t\ge0\), let \(m^*=m^{(p)}\), and let \(\overline m=(1-p)m^{(0)}+p m^{(1)}\) be the graph-averaged conditional limiting expected opinion vector. Set
\[
\epsilon=\frac LH,\qquad a(t)=\frac{\epsilon+Lt}{1+2\epsilon+2Lt},\qquad C=1+2\epsilon.
\]
The shortcut endpoint and every vertex of the long central segment have the **exact** formulas
\[
m^{(t)}_L=a(t),\qquad
m^{(t)}_{L+k}=a(t)+\frac{k}{H}(1-2a(t))\quad (0\le k\le H).
\]
For every \(0<p<1\), the expected-graph shortcut endpoint strictly exceeds its graph-averaged counterpart by
\[
\Delta_{L,H,p}=a(p)-(1-p)a(0)-pa(1)
=\frac{2L^2p(1-p)}{C(C+2L)(C+2Lp)}>0.
\]
The exact population-averaged absolute discrepancy, with **all** \(H+2L+1\) vertices counted, is
\[
\frac{1}{H+2L+1}\sum_{j=0}^{H+2L}|m^*_j-\overline m_j|
=\Delta_{L,H,p}\frac{L-1+B_H}{H+2L+1},
\quad B_H=\frac H2+1+\frac{1-(-1)^H}{4H}.
\]

More importantly, let \(L\to\infty\), choose **any** integer sequence \(H_L\ge2\) with \(H_L/L\to\infty\), and choose \(p_L\in(0,1)\) with \(p_L\to0\) and \(Lp_L\to c\in[0,\infty]\). Define \(\phi(c)=c/(1+2c)\) for finite \(c\) and \(\phi(\infty)=1/2\). Then
\[
m^*_L\longrightarrow\phi(c),\qquad
\overline m_L\longrightarrow0,\qquad
\frac{1}{H_L+2L+1}\sum_j|m^*_j-\overline m_j|
\longrightarrow\frac{\phi(c)}2.
\]
If \(m^{(G)}\) denotes the conditional limiting expectation on the sampled **unweighted** graph, the same normalized absolute discrepancy between \(m^*\) and \(m^{(G)}\) converges **in probability** to \(\phi(c)/2\). Thus the critical shortcut probability scale is \(1/L\). In particular, when \(p_L\to0\) but \(Lp_L\to\infty\), the expected graph predicts opinion near \(1/2\) on asymptotically all vertices, while with probability tending to one the realized graph has a near-linear opinion gradient from \(0\) to \(1\). The population-averaged absolute prediction error then tends to the sharp value \(1/4\) **within this model family**.

## Assumptions and scope
The network is undirected, the base path edges have weight one, and the optional shortcut has weight one when present, otherwise zero. The two stubborn endpoints keep their opinions fixed. In one gossip update an edge is chosen with probability proportional to its conductance; two regular endpoints each replace their opinion by their pairwise arithmetic average, and a regular agent paired with a stubborn one moves halfway toward the stubborn value. Edge draws at successive updates are independent conditional on the graph. Initial regular opinions may be arbitrary bounded real numbers. Only the limiting **expectations** of the gossip opinions are asserted to exist; individual sample trajectories need not converge to constants. The expected-graph comparison is defined by first averaging **edge conductances**, not by resampling the graph at every update.

## Proof
**1. Harmonic characterization.** On a connected finite weighted graph with at least one stubborn endpoint reachable from every regular vertex, conditional expected opinion updates satisfy \(z(t+1)=Qz(t)+r\), where \(I-Q\) is a positive multiple of the grounded weighted Laplacian. The grounded Laplacian is positive definite. The expected-update matrix has spectral radius strictly below one on the regular coordinates, so the expected opinion has a unique limit; at each regular vertex the limit is the conductance-weighted average of neighbors. This is the grounded Dirichlet problem, not an assertion of pathwise opinion convergence.

**2. Series-parallel reduction.** For a deterministic shortcut conductance \(t\), the original central path between \(u\) and \(v\) has resistance \(H\), in parallel with the shortcut of conductance \(t\). Its effective resistance is \(R=H/(1+Ht)\), and the two outer arms each have resistance \(L\). The series current under boundary voltage difference one is \(J=1/(2L+R)\). Therefore \(a(t)=LJ=(L/H+Lt)/(1+2L/H+2Lt)\), and linear voltage drops give the stated central-segment formula. On the outer arms, the values are \(m^{(t)}_j=(j/L)a(t)\) for \(0\le j\le L\) and \(m^{(t)}_{L+H+j}=1-(1-j/L)a(t)\) for \(0\le j\le L\). These formulas directly verify every harmonic equation and both boundary conditions.

**3. Exact averaging bias.** Sampling the optional edge once gives precisely two possible graphs, with endpoint means \(a(0)\) and \(a(1)\). The function \(a(t)=\tfrac12-\{2(C+2Lt)\}^{-1}\) is strictly concave, and direct common-denominator subtraction yields \(\Delta_{L,H,p}=2L^2p(1-p)/[C(C+2L)(C+2Lp)]\). Every coordinate difference \(m^*-\overline m\) is \(\Delta_{L,H,p}\) times \(j/L\) on the left arm, \(1-2k/H\) on the central segment, and \(-(1-j/L)\) on the right arm. Summing absolute values on these three disjoint vertex sets gives \(L-1+B_H\), with \(B_H=\sum_{k=0}^H|1-2k/H|=H/2+1+[1-(-1)^H]/(4H)\). This proves the exact discrepancy formula, including endpoint and parity terms.

**4. Scale limit.** Write \(\epsilon_L=L/H_L\). By assumption \(\epsilon_L\to0\), and \(a(p_L)=(\epsilon_L+Lp_L)/(1+2\epsilon_L+2Lp_L)\to\phi(c)\), including \(c=\infty\). Moreover \(a(0)\to0\), \(0\le a(1)\le1/2\), and \(p_L\to0\), so \((1-p_L)a(0)+p_La(1)\to0\). Since \(B_{H_L}/H_L\to1/2\) and \(L/H_L\to0\), the normalized average discrepancy tends to \(\phi(c)/2\). The realized graph lacks the shortcut with probability \(1-p_L\to1\). On that event its expected limit is exactly \(m^{(0)}\), whose normalized discrepancy from \(m^*\) has the same limit. This proves convergence in probability. For central positions \(k/H_L\to\theta\), the expected-graph limiting profile is \(\phi(c)+(1-2\phi(c))\theta\); the no-shortcut profile tends to \(\theta\). For \(c=\infty\) these limits are \(1/2\) and \(\theta\), respectively, giving the limit \(1/4\) after absolute integration.

## Verification
Run the included standalone Python 3 standard-library script `verify.py`. It reconstructs grounded Laplacian systems in exact rational arithmetic for multiple integer arm/bridge lengths and conductances; it independently solves each linear system and compares the entire harmonic vector with the circuit formula. Further exact checks cover Jensen-gap algebra, strictness, antisymmetry, all-vertex discrepancy, parity, and concrete critical/supercritical finite instances. The script prints `VERIFY_OK exact_assertions=1124` on successful completion. All infinite-limit arguments appear in the analytic proof above and do not depend on finite computations.

For a five-vertex example with \(L=1\), \(H=2\), \(p=1/2\), the expected-graph opinion at the left shortcut endpoint is \(1/3\), whereas the graph-averaged conditional limiting expected opinion is \(5/16\), a strict difference of \(1/48\). This small example illustrates the bias; the macroscopic asymptotic theorem is a separate result.

## Relationship to prior work
Acemoğlu, Como, Fagnani, and Ozdaglar established the harmonic representation for expected gossip opinions with stubborn agents (2010 preprint, 2013 journal). Xing and Johansson studied approximations from random gossip graphs to their expected weighted graphs and proved concentration under substantial expected-degree/anchoring hypotheses (first arXiv submission 2023-01-13). The present low-degree path family does **not** satisfy their strong-degree assumptions; it is therefore not a counterexample to those theorems. The new statement is the exact rare-shortcut bias and its complete critical-scale, all-vertex limiting discrepancy in a connected graph family. Xing and Johansson's earlier community-structure paper concerns transient behavior on a weighted two-community model, while Wang, Xing, and Johansson study a different Friedkin–Johnsen model with partially stubborn agents. Standard electrical circuit reduction is used openly; neither the harmonic viewpoint nor the general fact that averaging nonlinear responses can create bias is claimed as new.

## Limitations
The proof concerns a single Bernoulli shortcut on a path with two fully stubborn endpoints and symmetric outer arms. The maximum \(1/4\) refers only to the normalized absolute discrepancy in this family and does not purport to be universal across networks. The sampled network is fixed throughout the gossip process. The result concerns conditional and graph-averaged **expected** long-time opinions, not the almost-sure limit of instantaneous gossip states or any general finite-time prediction guarantee. Publication priority for broader equivalent formulations remains uncertain; no independent audit has been performed.

## References
1. D. Acemoğlu, G. Como, F. Fagnani, A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, arXiv:1009.2653, first submitted 2010-09-14; Mathematics of Operations Research 38 (2013), 1–27. https://arxiv.org/abs/1009.2653
2. Y. Xing, K. H. Johansson, *Concentration in Gossip Opinion Dynamics over Random Graphs*, arXiv:2301.05352, first submitted 2023-01-13; SIAM Journal on Control and Optimization 62 (2024), 1521–1545. https://arxiv.org/abs/2301.05352
3. Y. Xing, K. H. Johansson, *Transient Behavior of Gossip Opinion Dynamics with Community Structure*, arXiv:2205.14784, first submitted 2022-05-29. https://arxiv.org/abs/2205.14784
4. L. Wang, Y. Xing, K. H. Johansson, *On final opinions of the Friedkin-Johnsen model over random graphs with partially stubborn community*, arXiv:2409.05063, first submitted 2024-09-08. https://arxiv.org/abs/2409.05063
